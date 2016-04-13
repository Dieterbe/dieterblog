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

At raintank we're building a stellar open source monitoring stack with Grafana at the center.
The open source ecosystem is already very rich.  There's many projects out there and some them are very good.  So it makes a lot of sense to us to work with the existing communities and projects, and integrate with them where possible.  That's why we integrate with [several TSDB's](http://docs.grafana.org/datasources/overview/) (the upcoming Grafana 3 will take this concept to all kinds of integrations such as
[alerting](https://github.com/grafana/grafana/issues/2209) and online services)

The other side of raintank is providing said open source monitoring stack as a hosted platform, on [Grafana.net](http://www.grafana.net)
Luckily for us, there are a plethora of [TSDB] projects available, surely we could just try some and pick the one that suits the best, and maybe modify it a bit.
The last thing we thought we needed to do, is spend our time writing yet another TSDB.

# Than why are we doing just that?

Driven by different goals and requirements, people use different datasources in Grafana (and often combine several).  Likewise, the requirements for our hosted offering are also fairly unique:

1. resource efficiency, in particular disk space: we need good data compression to reduce cost
2. support growth from small to medium-scale multi-tenant SaaS.  We need solid clustering for availability and load balancing.
3. whatever we use must be fully free/open source (a must for our business model. Everyone must be able to run the stack)
4. operational simplicity
5. a powerful / flexible querying API, preferrably graphite compatible because it has a great data processing / querying API that a lot of people already know and love.

<div class="intermezzo"><strong>Intermezzo:</strong> Both the Graphite and its alternative Graphite-api projects support plugging in 3rd party databases through a plugin api.  
(docs for <a href="http://graphite.readthedocs.org/en/latest/storage-backends.html">Graphite</a> and <a href="http://graphite-api.readthedocs.org/en/latest/finders.html">Graphite-api</a>).  
This is a great way to bolt Graphite's powerful API on top of a more api-limited database.
I've used this in the past to write a <a href="https://github.com/vimeo/graphite-influxdb">graphite-influxdb plugin</a> and at raintank we made one <a href="https://github.com/raintank/graphite-kairosdb">for Kairosdb</a> since we ran on that for a while.
<br/>
<br/>
This largely removes the 5th concern.
</div>
<br/>

Unfortunately for us, while some of the mentioned TSDB's have absolutely great properties, none of them were able to check off all of our particular requirements.

We at raintank also don't have the resources to build a general purpose TSDB that solves everything for everyone (nor the desire); 
however, we can be very pragmatic and stand on the shoulders of giants:

1. Graphite already has a great api and alleviates the API concern mostly.
2. We need performant storage and solid clustering.  Cassandra has this pretty well covered.
3. Elasticsearch does text/tags searching quite well.  Using it as metadata store can take us pretty far.
4. When I read [Facebook's "Gorilla" float compression paper](www.vldb.org/pvldb/vol8/p1816-teller.pdf) I got very excited. These data compression numbers were looking great.  Then Damian Gryski implemented it in Go with the [go-tsz library](
https://github.com/dgryski/go-tsz).  Data compression was very important to us and I felt this could be the key to a good solution. In retrospect this was confirmed: about a dozen projects are based on this library, including the new InfluxDB TSM storage engine. <a href="https://raw.githubusercontent.com/dgryski/go-tsz/master/eval/eval-results.png">We're seeing space usage of a few bytes per point</a>, which is easily 10x less than uncompressed storage which most of the other TSDB's use.
<br/>

# Meet Metric-tank

We built a service that ingests timeseries streams, compresses them using go-tsz and stores the chunks in Cassandra.
It also keeps a configurable amount of data in RAM for fast retrievals of hot data (for alerting queries and some dashboards), in addition to querying from Cassandra.


Later we also added:

* basic clustering so we can run several instances for redundancy and load balancing and to do hot upgrades.
* runtime consolidation (to offload graphite)
* support for rollup bands (while loading raw data from cassandra and runtime consolidation is fast enough, decoding the points was a bottleneck)

While we're at it, we can also fix some of <a href="/25-graphite-grafana-statsd-gotchas/">Graphite's shortcomings</a>.
In particular we store several rollup bands per metric (min/max/avg, etc) so that:

* you can choose your view instead of [being limited to a single aggregation function](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#limited.aggregation)
* runtime consolidation works in concert with the rollup so that [the data is correct in all circumstances](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#runtime.consolidation)
* and so that Grafana [can show accurate data in its own statistical summaries](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/#grafana.consolidation)

 We were able to lower our disk usage by about 10x and significantly shrink our cassandra cluster.
we've done tests where we kill cassandra instances and everything just seems to work and recover fine.


# If you want to try it out

The current code name is **metric-tank** which may change.
It is currently not for the faint of heart.  If you want to run it, you'll need:

* [Finder plugin for graphite](https://github.com/raintank/graphite-raintank)
* [Patched graphite-api server](https://github.com/raintank/graphite-api)
* [Metric-tank](https://github.com/raintank/raintank-metric/tree/master/metric_tank)
* [Grafana dashboard to monitor metric-tank](https://github.com/raintank/raintank-docker/blob/master/grafana-dev/dashboards/metric-tank.json)

It takes in messagepack encoded [metrics2.0 style data](https://github.com/raintank/raintank-metric/blob/master/schema/metric.go#L15) via [NSQ](http://nsq.io/)

An easy way to see how the pieces fit together and get everything up and running is the <a href="https://github.com/raintank/raintank-docker">raintank-docker</a> stack.
It spins up our entire stack, including Grafana 3 beta and [worldping](https://grafana.net/plugins/raintank-worldping-app), so an easy way to test data ingest is just adding some worldping
endpoints or use <a href="https://github.com/raintank/raintank-metric/tree/master/fake_metrics_to_nsq">fake_metrics_to_nsq</a> which uses the right format to ingest metrics into NSQ.

If you need any help <a href="http://slack.raintank.io/">join our public slack</a>

We plan to make installation easier, support consuming from kafka and of course a carbon input listener.
Over time I'ld also like to take out more python code and replace it by Go, which is faster and much easier to install.

