+++
title = "The last thing i want to do is write yet another timeseries database. Yet here we are"
date = "2016-03-15T10:25:02+02:00"
tags = ["golang", "monitoring"]
+++

There's a lot of TSDB's (timeseries databases) out there.
[Graphite's whisper](http://graphite.readthedocs.org/en/latest/whisper.html), [OpenTSDB](http://opentsdb.net/), [Elasticsearch](https://www.elastic.co/products/elasticsearch), [KairosDB](http://kairosdb.github.io/), [InfluxDB](https://influxdata.com/time-series-platform/influxdb/), [cyanite](http://cyanite.io/), [prometheus](http://prometheus.io/), [riak-ts](http://basho.com/products/riak-ts/), [druid](http://druid.io), [blueflood](http://blueflood.io/), [dalmatiner](http://dalmatiner.io), [akumuli](http://akumuli.org/) and [openNMS' newTS](https://github.com/OpenNMS/newts ), just to name "a few".
I'm sure I've seen about another dozen, ranging from 1-person pet projects to systems supporting the production monitoring of various large companies.

Graphite, despite its limited storage system and its lack of support for tags (and party because of it) has a tremendously powerful yet simple data processing api.
Despite its age, its query api is mostly unrivaled except maybe for these two:

* Elasticsearch is no longer just for log searching. It's getting [quite good for timeseries metrics](https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store).  
(did you know that [CERN](http://http://home.cern/) - the scientists who run the Large Hydron Collider - [use it to monitor their LHC jobs](http://cds.cern.ch/record/2011172/files/LHCb-TALK-2015-060.pdf) ?)
* druid also has [quite extensive query options](http://druid.io/docs/0.8.3/querying/querying.html)

It's an interesting exercise to study all these projects and uncovering their varying pro's and cons.

At raintank (Grafana OpenSaaS), and with Grafana, we try to build a stellar open source monitoring stack (and also offer it hosted). The open source ecosystem is already very rich.  There's many projects out there and some them are very good.  So it makes a lot of sense to us to work with the existing communities and projects, and integrate with them where possible.  That's why we integrate with [several TSDB's](http://docs.grafana.org/datasources/overview/) and soon will do something similar for [alerting](https://github.com/grafana/grafana/issues/2209) (I also did a [talk](http://dieter.plaetinck.be/talks/) on this)
In fact there's so many [TSDB] projects, the last thing we want to do is write another.

# So we didn't want to build yet another TSDB, than why did we?

Driven by different contexts and requirements, people use different datasources in Grafana (and often combine several).  Likewise, our requirements are also fairly unique.
Until recently were were running on Kairosdb but our main problem with Kairosdb was how it works with cassandra: it used too many resources, in particular disk space and cpu. So it was too expensive to run.  
Here are our main requirements:

1. resource efficiency, in particular disk space: we needed good data compression to reduce cost
2. support growth from small to medium-scale multi-tenant SaaS.  We needed solid clustering for availability and load balancing.
3. whatever we use must be fully free/open source (a must for our business model)
4. operational simplicity
5. a powerful / flexible querying API, preferrably graphite compatible

Unfortunately, none of the projects we've found so far adresses this particular combination of needs.  

There's no way that I (or we, at raintank) have the resources to build a better general purpose TSDB.
However, we can be very pragmatic!
We're not trying to sell you a product so ego, branding or business interests don't get in the way.  We can stand on the shoulders of giants:

1. graphite already has a great api and alleviates the API concern mostly.
2. we need performant storage and solid clustering.  Cassandra has this pretty well covered.
3. Elasticsearch does text/tags searching quite well.  Using it as metadata store can take us far
4. When I read [Facebook's "Gorilla" float compression paper](www.vldb.org/pvldb/vol8/p1816-teller.pdf) I got very excited. These data compression numbers were looking great.  Then [Damian Gryski implemented it in Go](
https://github.com/dgryski/go-tsz).  Data compression was very important to us and I felt this could be the key to a good solution. In retrospect this was confirmed: about a dozen projects are based on this library, including the new InfluxDB TSM storage engine. <a href="https://raw.githubusercontent.com/dgryski/go-tsz/master/eval/eval-results.png">We're seeing space usage of a few bytes per point</a>, which is easily 10x less than uncompressed storage such as whisper or Kairosdb.

<div class="intermezzo"><strong>Intermezzo:</strong> Both the Graphite and its alternative Graphite-api projects support plugging in 3rd party databases through a plugin api.  
(docs for <a href="http://graphite.readthedocs.org/en/latest/storage-backends.html">Graphite</a> and <a href="http://graphite-api.readthedocs.org/en/latest/finders.html">Graphite-api</a>).  
This is a great way to bolt Graphite's powerful API on top of a more api-limited database.
I've used this in the past to write a <a href="https://github.com/vimeo/graphite-influxdb">graphite-influxdb plugin</a> and at Raintank we made one <a href="https://github.com/raintank/graphite-kairosdb">for kairosdb</a>.
<br/>
<br/>

There's also projects that aim to make running a Graphite compatible stack simpler and more performant by rewriting it in Go:  <a href="https://github.com/graphite-ng">Graphite-NG</a> and 
<a href="https://github.com/dgryski/carbonapi">carbonapi</a>.  We have started to invest in these but don't have anything to show yet</div>
<br/>

So we could solve our problem by building a solution that uses Graphite (and Grafana) as frontend and uses ElasticSearch for metadata indexing.
It needs to ingest data, compress it using go-tsz (the go implementation of the data compression) and store the chunks in Cassandra.  And it would be nice if it could keep a configurable amount of data in RAM for fast retrievals of hot data (for alerting queries).


**So that's exactly what we built**: A simple system that solves our current need for a scalable, performant timeseries storage system, by standing on the shoulders of giants.  
The current code name is **metric-tank** but this may change.

Later we also added:

* basic clustering so we can run several instances for redundancy and loadbalancing and to do hot upgrades.
* runtime consolidation (to offload graphite)
* support for rollup bands (while loading raw data from cassandra and runtime consolidation is fast enough, decoding the points was a bottleneck)

While we're at it, we can also fix some of <a href="/25-graphite-grafana-statsd-gotchas/">Graphite's shortcomings</a>.
In particular we store several rollup bands per metric (min/max/avg, etc) so that:

* you can choose your view instead of [being limited to a single aggregation function](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#limited.aggregation)
* runtime consolidation works in concert with the rollup so that [the data is correct in all circumstances](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#runtime.consolidation)
* and so that Grafana [can show accurate data in its own statistical summaries](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#grafana.consolidation)

We switched from Kairosdb to metric-tank in production in early january.  We were able to lower our disk usage by about 10x and significantly shrink our cassandra cluster.
we've done tests where we kill cassandra instances and everything just seems to work and recover fine.



# Limitations & future plans:

* Unknown future:  while currently metric-tank powers our hosted TSDB, if something better comes along that meets all our criteria, we may jump or join ship.
So we can't make commitments to the future of this project at this time. 
* only deals with float64 values. No ints, bools, text, etc. Some type optimisations may come, though using the float type for ints and bools works quite well.
In fact compression works best if the number has no decimals anyway.  But for the forseeable future it only supports numeric data.
* only uint32 unix timestamps in second resolution. Higher-resolution will probably be added later.
* No tags support for querying yet. The metrics are tagged but we still need to update the query language to make use of it. 
* no sharding/partitioning. Our instances currently take about 15GB of RAM, with just over 500k active metrics and 400 million points in RAM. We have to work on a solution to split data across instances or we'll run in trouble once we hit the RAM ceiling on a server.
* around 400k metrics/s CPU starts maxing out (8 core Xeon 2.3 GHz). We're also seeing ES blocking due to the metadata indexing around the 100k/s mark.  Both can and will be optimized more.
* no computation locality: we pull in all the raw data first from cassandra, then process/consolidate it in metric-tank. Further processing/aggregation happens in Graphite.  At a certain scale you need to move the computation to the data, but we don't have that problem yet, though we do plan to move more of the graphite logic into metric-tank and further develop graphite-ng.
* no data locality: we don't have anything that puts related series together.  Often this helps with read performance but we haven't needed to look into this yet.
* tied to the rest of the raintank stack (for now). We run a <a href="https://github.com/raintank/graphite-api">custom version of graphite-api</a> and use a message format that is almost <a href="http://metrics20.org">metrics2.0</a> compatible, but not quite yet.
* we use <a href="http://nsq.io">NSQ</a> as our transport, and that's the only ingest method for now.  A carbon listener would be easy to add.  We want to transition to kafka because it has strong ordering guarantees, NSQ does not. And we need orderderd ingest for compression & rollups.
* We lose about 100ms each request to retrieve the metadata from ES.
* While it does block off requests for too much data / too large time frames, there is no resource isolation between tenants  (other than what's needed for security).  Rate limiting still has to be implemented.

# Bottom line
We want you to use the TSDB that works best for you, as we do ourselves.
It's important to keep an eye on the evolving landscape and changing needs.
If a solid, well-run open source TSDB project comes along that clearly is a better choice, then we will probably switch.
However, we are happy with our current metric-tank stack and for the forseeable future we will keep investing in metric-tank.  

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



