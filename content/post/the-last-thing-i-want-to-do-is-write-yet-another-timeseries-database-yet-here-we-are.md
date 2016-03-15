+++
title = "The last thing i want to do is write yet another timeseries database. Yet here we are"
date = "2016-03-15T10:25:02+02:00"
tags = ["golang", "monitoring"]
+++

There's a lot of TSDB's (timeseries databases) out there.
From the more commonly known ones such as [Graphite's whisper](http://graphite.readthedocs.org/en/latest/whisper.html), [OpenTSDB](http://opentsdb.net/), [Elasticsearch](https://www.elastic.co/products/elasticsearch), [KairosDB](http://kairosdb.github.io/), [InfluxDB](https://influxdata.com/time-series-platform/influxdb/), [cyanite](http://cyanite.io/), [prometheus](http://prometheus.io/) to the more obscure ones such as
[riak-ts](http://basho.com/products/riak-ts/),[druid](http://druid.io), [blueflood](http://blueflood.io/), [dalmatiner](http://dalmatiner.io), [akumuli](http://akumuli.org/) and [openNMS' newTS](https://github.com/OpenNMS/newts ).
I'm sure I've seen about another dozen, ranging from 1-person pet projects to systems supporting the production monitoring of various large companies.

Graphite, despite its limited storage system and its lack of support for tags (and party because of it) has a tremendously powerful yet simple data processing api.
Despite its age, its query api is mostly unrivaled.
API-wise, two other interesting options come to my mind:

* Elasticsearch is no longer just for log searching. It's getting [quite good for timeseries metrics](https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store).
(did you know that [CERN](http://http://home.cern/) - the scientists who run the Large Hydron Collider - [use it to monitor their LHC jobs](http://cds.cern.ch/record/2011172/files/LHCb-TALK-2015-060.pdf) ?)
* druid also has [quite extensive query options](http://druid.io/docs/0.8.3/querying/querying.html)

Neither of these two sufficiently solve our needs though.

Also note that both the Graphite and Graphite-api projects support plugging in 3rd party databases through a plugin api. (docs for [Graphite](http://graphite.readthedocs.org/en/latest/storage-backends.html) and [Graphite-api](http://graphite-api.readthedocs.org/en/latest/finders.html)).
This is a great way to bolt Graphite's powerful API on top of a more limited database.
I've used this in the past to write a [graphite-influxdb plugin](https://github.com/vimeo/graphite-influxdb) and at Raintank we made one [for kairosdb](https://github.com/raintank/graphite-kairosdb).


Some key properties I look for in a TSDB are resource efficiency, performance, a powerful / flexible API and operational simplicity.
I also want the system to be free / open source, and scale from running some local metrics on my laptop to serving thousands of customer in the datacenter.

Spoiler alert: I haven't seen a system that checks all the boxes.  Most can get about 4 out of 6.  
There's also no way that I (or we, at raintank) have the resources to build a better general purpose TSDB.  
Nor do we want to.  There's already a rich ecosystem of good open source monitoring software.
We want to build a great monitoring system and reuse existing technology where possible.  We don't want to reinvent what already exists and introduce yet another system that scatters the ecosystem and confuses things.
integrate, paying off for grafana and raintank openSaaS
 We want to build a great OpenSaaS platform, and stand on the shoulders of open source giants where possible. If it already exists, we should use it.

# So we didn't want to build yet another TSDB, than why did we?

While with Grafana, we have the interests of a broad group of people at heart, for the hosted metrics platform specifically our requirements are actually fairly narrow:

1. the main concern was resource efficiency, in particular data store required: we needed good data compression.  Kairosdb+cassandra needed too many resources, in particular disk space.
2. Since we run a multi-tenant SaaS platform, we only need to worry about medium to large scale.  But we needed solid clustering.  Luckily there is proven technology to build upon (like cassandra)
3. Whatever we use must be fully free/open source (a must for our business model)

We're also not trying to sell you a product, so ego, branding or business interests don't get in the way.  We can be pragmatic:
1. graphite-api already has a great api and alleviates the API concern mostly
2. we need performant storage and solid clustering.  Cassandra has this pretty well covered.
3. Elasticsearch does text/tags searching very well.  Using it as metadata store can take us far
4. When I read Facebook's float compression paper www.vldb.org/pvldb/vol8/p1816-teller.pdf I got very excited. Especially because Damian Gryski implemented it in Go
https://github.com/dgryski/go-tsz  Data compression was very important to us and I felt this could be the key to a good solution. (in retrospect this turned out true.  About a dozen projects are based on this library, including the new InfluxDB TSM storage engine)


So we could solve our problem by building a solution that is uses Graphite (and Grafana) as frontend and uses ElasticSearch for metadata indexing, 
It needs to ingest data, compresses it using go-tsz and store the chunks in Cassandra.  And it would be nice if it could keep a configurable amount of data in RAM for fast retrievals.
we also wanted to run several versions for redundancy and loadbalancing and to do hot upgrades.


**So that's what we built**: A simple system that solves our need for a scalable, performant timeseries storage system, by standing on the shoulders of giants.

Later we also added:

* runtime consolidation (to offload graphite)
* support for rollup bands (while loading raw data from cassandra and runtime consolidation is fast enough, decoding the points was a bottleneck)

In particular, we store several bands per metric, so you can choose your view (min/max/avg etc) 
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#limited.aggregation
and so that the data is correct in all circumstances
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#runtime.consolidation
and so that Grafana can show more accurate data
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#grafana.consolidation


we switched from kairosdb to metric-tank in production in early january.  We were able to lower our disk usage by about 10x and significantly shrink our cassandra cluster.
Cassandra has actually proven the most reliable piece of the stack (we've done some tests with killing instances etc), which feels pretty reassuring



# Limitations & future plans:

* only deals with float64 and uint32 unix timestamps in second resolution. No ints, bools, text, etc. Some type optimisations may come, but it's all numeric for now.
* No tags support for querying yet. The metrics are tagged but we still need to update the query language to make use of it. 
* no sharding/partitioning. Our instances currently take about 15GB of RAM, with just over 500k active metrics and 400 million points. We have to work on a solution to split data across instances or we'll run in trouble once we hit the RAM ceiling on a server.
* around 400k metrics/s CPU starts maxing out (8 core Xeon 2.3 GHz). We're also seeing ES blocking due to the metadata indexing.  Both can and will be optimized more.
* Unknown future:  If something better comes along that meets all our criteria, we may jump ship.
We make no commitments to the future of this project currently. We may jump or join ship if something better comes along. It is currently powering the raintank hosted TSDB early access, but if that changes the commitment to this project will likely change.
* no computation locality: we pull in all the raw data first from cassandra, then process/consolidate it. Further processing/aggregation happens in Graphite.  At a certain scale you need to move the computation to the data, but we don't have that problem yet, though we do plan to move more of the graphite logic into metric-tank
* no data locality: we don't have anything that puts related series together.  Cassandra has been stellar so far though.
* tied to the rest of the raintank stack (for now). We had to make some changes to https://github.com/raintank/graphite-api and use a message format that is almost metrics2.0 compatible, but not quite yet. http://metrics20.org/
* we use NSQ as our transport, and that's the only ingest method for now.  A carbon listener would be easy to add.  We want to transition to kafka because it has strong ordering guarantees, NSQ does not. And we need orderderd ingest for compression & rollups.
* We lose about 100ms each request to retrieve the metadata from ES.

# Bottom line
Remember: we want you to use the TSDB that works best for you (and in fact, many of you run multiple) as we do ourselves.
While we are pretty happy with our current stack and probably will be for the foreseeable future, and will keep investing in metric-tank; as the landscape evolves, our preference will evolve as well.  If a solid, well-run tsdb project comes along that clearly is a better choice, then we will switch. 
In other words: we need to scratch our itch, if you're having the same itch: feel free to use our scratcher. But be aware that if a better scratcher comes along (or our itch changes in nature) we may switch scratchers.

# Get it here

* [Finder plugin for graphite](https://github.com/raintank/graphite-raintank)
* [Custom graphite-api server](https://github.com/raintank/graphite-api)
* [Metric-tank](https://github.com/raintank/raintank-metric/tree/master/metric_tank)
* [Grafana dashboard for metric-tank](https://github.com/raintank/raintank-docker/blob/master/grafana-dev/dashboards/metric-tank.json)



<!--
Experiences so far:
So far it has been an interesting learning experience, so I'ld like to share a few things:
*) When dealing with large requests / no rollups, i thought data i/o would be slowest. nope
profiling, performance. allocations.

-->



