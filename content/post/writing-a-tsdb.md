+++
title = "The last thing i want to do is write yet another timeseries database. Yet here we are"
date = "2015-10-02T10:25:02+02:00"
tags = ["golang", "monitoring"]
draft = true
+++

There's a lot of TSDB's (timeseries databases) out there.
From the more commonly known ones such as Graphite's whisper, OpenTSDB, Elasticsearch, KairosDB, InfluxDB, [cyanite](http://cyanite.io/), prometheus to the more obscure ones such as
[riak-ts](http://basho.com/products/riak-ts/),[druid](druid.io), blueflood, [dalmatiner](dalmatiner.io), [akumuli](http://akumuli.org/) and [openNMS' newTS](https://github.com/OpenNMS/newts ).
I'm sure I've seen about another dozen, ranging from 1-person pet projects to systems supporting the production monitoring of various large companies.

Graphite, despite its limited storage system and its lack of support for tags (and party because of it) has a tremendously powerful yet simple data processing api.
Despite its age, it's api is mostly unrivaled.
though two others spring to my mind:
Elasticsearch is no longer just for log searching. It's getting quite good for timeseries metrics https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store
(CERN, the guys who run the Large Hydron Collider, use it to monitor their jobs! http://cds.cern.ch/record/2011172/files/LHCb-TALK-2015-060.pdf)
and I find druid also quite interesting http://druid.io/docs/0.8.3/querying/querying.html
Neither of these two sufficiently solve our needs though.

For those who don't know, in both http://graphite.readthedocs.org/en/latest/storage-backends.html and http://graphite-api.readthedocs.org/en/latest/finders.html you can plug
in custom data storage system and still enjoy the great api.

we were actually running on graphite+kairosdb for a while. But that only took us so far.


Some key properties I look for in a TSDB are resource efficiency, performance, a powerful / flexible API and operational simplicity.
I also want the system to be free / open source, and scale from running some local metrics on my laptop to serving thousands of customer in the datacenter.

Spoiler alert: I haven't seen a system that checks all the boxes.  Most can get about 4 out of 6.
There's also no way that I (or we, at raintank) have the resources to build a better general purpose TSDB.  Nor do we want to. We want to build a great monitoring system and reuse existing technology where possible.  We don't want to reinvent what already exists and introduce yet another system that scatters the ecosystem and confuses things.

So we didn't want to build yet another TSDB, than why did we?

While with Grafana, we have the interests of a broad group of people at heart, for the hosted metrics platform specifically our requirements are actually fairly narrow:

1. the main concern was resource efficiency, in particular data store required: we needed good data compression.  Kairosdb+cassandra needed too many resources, in particular disk space.
2. Since we run a multi-tenant SaaS platform, we only need to worry about medium to large scale.  But we needed solid clustering.  Luckily there is proven technology to build upon (like cassandra)
3. Whatever we use must be fully free/open source (a must for our business model)

We're also not trying to sell you a product, so ego, branding or business interests don't get in the way.  We can be pragmatic:
1. graphite-api already has a great api and alleviates the API concern mostly
2. we need performant storage and solid clustering.  Cassandra has this pretty well covered.
3. Elasticsearch does text/tags searching very well.  Using it as metadata store can take us far
4. When I read Facebook's float compression paper www.vldb.org/pvldb/vol8/p1816-teller.pdf I got very excited. Especially because somebody implemented it in Go
https://github.com/dgryski/go-tsz  Data compression was very important to us and I felt this could be the key to a good solution. (in retrospect this turned out true.  About a dozen projects are based on this library, including the new InfluxDB TSM storage engine)


So we could solve our problem by building a solution that is uses Graphite (and Grafana) as frontend and uses ElasticSearch for metadata indexing, 
It needs to ingest data, compresses it using go-tsz and store the chunks in Cassandra.  And it would be nice if it could keep a configurable amount of data in RAM for fast retrievals.
we also wanted to run several versions for redundancy and loadbalancing and to do hot upgrades.


So that's what we built.
A simple system that solves our need for a scalable, performant timeseries storage system. Nothing more, nothing less.

Later we also added:
*) runtime consolidation (to offload graphite)
*) support for rollup bands (while loading raw data from cassandra and runtime consolidation is fast enough, decoding the points was a bottleneck)

In particular, we store several bands per metric, so you can choose your view (min/max/avg etc) 
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#limited.aggregation
and so that the data is correct in all circumstances
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#runtime.consolidation
and so that Grafana can show more accurate data
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#grafana.consolidation


we switched from kairosdb to metric-tank in production in early january.  We were able to lower our disk usage by about 10x and significantly shrink our cassandra cluster.
Cassandra has actually proven the most reliable piece of the stack (we've done some tests with killing instances etc), which feels pretty reassuring



Limitations & future plans:
* only deals with float64 and uint32 unix timestamps in second resolution. No ints, bools, text, etc. Some type optimisations may come, but it's all numeric for now.
* Doesn't use tags for querying or searching. This may come.
* no sharding/partitioning. Our instances currently take about 15GB of RAM, withjust over 500k active metrics and 400 million points. We have to work on a solution to split data across instances or we'll run in trouble once we hit the RAM ceiling on a server.
* each instance can ingest up to about 100~150k metrics/s, after that CPU starts maxing out (8 core Xeon 2.3 GHz)
* no long term support / endorsement.  If something better comes along that meets all our criteria, we may jump ship.
* no computation locality: we pull in all the raw data first from cassandra, then consolidate it. Series are only aggregated together in graphite.  At a certain scale you need to move the computation to the data, but we don't have that problem yet.
* no data locality: we don't have anything that puts related series together.  Cassandra has been stellar so far though.
* tied to the rest of the raintank stack (for now). We had to make some changes to https://github.com/raintank/graphite-api and use a message format that is almost metrics2.0 compatible, but not quite yet. http://metrics20.org/
* we use NSQ as our transport, and that's the only ingest method for now.  A carbon listener would be easy to add.  We want to transition to kafka because it has strong ordering guarantees, NSQ does not. And we need orderderd ingest for compression & rollups.
* We lose about 100ms each request to retrieve the metadata from ES.


scratch our itch, if you're having the same itch: feel free to use our scratcher. But be aware that if a better scratcher comes along, we may start using and recommending that.
Remember: we want you to use the TSDB that works best for you (and in fact, many of you run multiple) as we do ourselves.
While we are pretty happy with our current stack and will be for the foreseeable future; as the landscape evolves, our preference will evolve as well

<!--
Experiences so far:
So far it has been an interesting learning experience, so I'ld like to share a few things:
*) When dealing with large requests / no rollups, i thought data i/o would be slowest. nope
profiling, performance. allocations.

-->


https://github.com/raintank/graphite-raintank
https://github.com/raintank/raintank-metric/tree/master/metric_tank
https://github.com/raintank/raintank-docker/blob/master/grafana-dev/dashboards/metric-tank.json Grafana dashboard to monitor it


