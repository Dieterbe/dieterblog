+++
title = "The last thing i want to do is write yet another timeseries database. Yet here we are"
date = "2015-10-02T10:25:02+02:00"
tags = ["golang", "monitoring"]
draft = true
+++

There's a lot of TSDB's (timeseries databases) out there.

Grafana started out with [Graphite](http://graphite.readthedocs.org/en/latest/), but has grown to support mainy popuar TSDBs such as [OpenTSDB](http://www.opentsdb.net), [Prometheus](http://www.prometheus.io) and [InfluxDB](www.influxdb.com). There is also support for lesser known projects such as  [KairosDB](https://kairosdb.github.io/), [Cyanite](http://cyanite.io/), [Druid](druid.io),  [Newt](https://github.com/OpenNMS/newts), [Dalmatiner](dalmatiner.io), [Akumuli](http://akumuli.org/).

We're also talking with [Basho re: Riak-TS](http://basho.com/products/riak-ts/) and [Rackspace re: Blueflood](http://blueflood.io) about adding support for their offerings.

Plus, I'm sure I've seen about another dozen, ranging from 1-person pet projects to systems supporting the production monitoring of various large companies.

It seems the last thing the world needs is another TSDB.

Graphite, despite some well understood limitation and its age, has a tremendously powerful yet simple data processing API. In many ways, its unrivaled. It's the complete package, and it just works. At raintank, we're big fans of Graphite, and it offers a great experience when coupled with Grafana. 

Elasticsearch also deseves a spot on the list now. It's no longer just for log searching and events: it's getting [quite good for timeseries metrics](https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store). CERN, the guys who run the Large Hydron Collider, use it to [monitor their jobs!](http://cds.cern.ch/record/2011172/files/LHCb-TALK-2015-060.pdf)

SPOILER ALERT: Nothing we've mentioned here meets our needs for a hosted TSDB. We want something that (1) is performant and resource efficient (2) completely open source (3) have a powerful API, ideally similar to Graphite (4) extremely stable (5) didn't have a lot of dependencies we weren't comfortable with. No system we've found can check all the boxes. 

We were running KairosDB for a while. We even wrote a [Graphite Finder](http://www.github.com/raintank/) for it. There is now full support for KairosDB in Grafana. At our scale though, it only got us so far. We liked what we saw in Cassandra.

There's no way that we have the resources or the interest to build a better general purpose TSDB from the ground up. Nor do we want to. We want to build a great OpenSaaS platform, and stand on the shoulders of open source giants where possible. If it already exists, we should use it.

# So we didn't want to build yet another TSDB, than why did we?

As with most things, it starts as a prototype.

When I read Facebook's float compression paper www.vldb.org/pvldb/vol8/p1816-teller.pdf I got very excited. Especially because our friend Damian Gryskisomebody implemented the [algorithm in Go](https://github.com/dgryski/go-tsz). Data compression was very important to us, and I felt that this could be a game changer. 

Being able to swap out [Backends](http://graphite.readthedocs.org/en/latest/storage-backends.html) and [Finders](http://graphite-api.readthedocs.org/en/latest/finders.html) in the Graphite API code turns out to be pretty useful. The idea and power of Graphite can easily transcend a particular implementation.

We decided to prototype a small project: metrictank. Implementing the Facebook algorithm, it would things we were pretty comfortable with: Cassandra, Elasticsearch, and the Graphite API. 

It's job was simple: to ingest data, compress it, and store the chunks into Cassandra for long term storage. We also decided that it'd be nice if it could keep recent data in RAM, and do double duty as a cache and retrieval layer. The value of this became even more evident as we prototyped alerting features in Grafana.

The Facebook paper was indeed quite a big deal. Several projects ended up being based on this library, including the new InfluxDB TSM storage engine. 

**So that's what we built**: A simple system that solves our need for a scalable, performant timeseries storage system. Standing on the shoulders of giants.

Later we also added:

* runtime consolidation (to offload graphite)
* support for rollup bands (while loading raw data from cassandra and runtime consolidation is fast enough, decoding the points was a bottleneck)

In particular, we store several bands per metric, so you can choose your view (min/max/avg etc) 
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#limited.aggregation
and so that the data is correct in all circumstances
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#runtime.consolidation
and so that Grafana can show more accurate data
https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#grafana.consolidation

We cut over to metric-tank just a few months ago. So far the results are very promising. We've seen compression improvements in the order of 10x. Data storage requirements were on the order of 2bytes. 


# There are many limitations:

* Unknown future: We make no commitments to the future of this project currently. We may jump or join ship if something better comes along. It is currently powering the raintank hosted TSDB early access, but if that changes the commitment to this project will likely change.
* Limited data types: raintank-metric only supports float64 and uint32 unix timestamps in second resolution. No ints, bools, text, etc. Some type optimisations may come, but it's all numeric for now.
* Performance: Testing has shown that we can cache almost 1Billion datapoints, and ingest well over 100,000 data points per second, on a single commodity server with 8 physical cores and 32GB of RAM. These could be optimized, but represent an order of magnitude improvement for us.
* Redundancy: There is no redundancy with metric-tank, and sharding is "manual". We do get full redundancy for long term storage thanks to Cassandra. The only data at risk is what has not been flushed to Cassandra from metrictank. 
* No computatational locality: We pull in all the raw data first from cassandra, then consolidate it. Series are only aggregated together in gGraphite.  At a certain scale you need to move the computation to the data, but we don't have that problem yet.
* No data locality: We don't have anything that puts related series together.  Cassandra has been stellar so far though.
* Tied to the rest of the raintank stack (for now). We had to make some changes to https://github.com/raintank/graphite-api and use a message format that is almost metrics2.0 compatible, but not quite yet. http://metrics20.org/
* We use NSQ as our transport, and that's the only ingest method for now.  A carbon listener would be easy to add.  We want to transition to kafka because it has strong ordering guarantees, NSQ does not. And we need orderderd ingest for compression & rollups.
* Useless metadata: We lose time in each request to retrieve the metadata from ES, but currently provide no way to query or search on that metadata currently (our goal was Graphite compatability).

# Bottom line

At raintank, we want you to use the TSDB that works best for you. Grafana is all about bringing your data together, no matter where it lives or what format it is. 

But, for our hosted TSDB, we're pretty happy with where the prototype has taken us. 

In other words: we need to scratch our itch, if you're having the same itch: feel free to use our scratcher.

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



