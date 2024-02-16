+++
title = "25 Graphite, Grafana and statsd gotchas"
date = "2016-03-15T16:22:03+10:00"
tags = ["monitoring"]
toc = true
tocOpen = true
+++
### Introduction
This is a crosspost of [an article I wrote on the raintank.io blog](https://blog.raintank.io/25-graphite-grafana-and-statsd-gotchas/)  
For several years I've worked with Graphite, Grafana and statsd on a daily basis and have been participating in the community.  All three are fantastic tools and solve very real problems.  Hence my continued use and recommendation.  However, between colleagues, random folks on irc, and personal experience, I've seen a plethora of often subtle issues, gotchas and insights, which today I'd like to share.

I hope this will prove useful to users while we, open source monitoring developers, work on ironing out these kinks.  At raintank we're addressing a bunch of these as well but we have a long road ahead of us.
<br>
Before we begin, when trying to debug what's going on with your metrics (whether they're going in or out of these tools), don't be afraid to dive into the network or the whisper files. They can often be invaluable in understanding what's up.

For network sniffing, I almost always use these commands:  
{{<highlight bash>}}
ngrep -d any -W byline port 2003 # carbon traffic
ngrep -d any -W byline port 8125 # statsd traffic
{{</highlight>}}

Getting the json output from Graphite (just append `&format=json`) can be very helpful as well. Many dashboards, including <a href="http://www.grafana.org">Grafana</a> already do this, so you can use the browser network inspector to analyze requests. For the whisper files, Graphite comes with various useful utilities such as whisper-info, whisper-dump, whisper-fetch, etc.

*here we go:*

### 1. OMG! Did all our traffic just drop?
Probably the most common gotcha, and one i run into periodically. Graphite will return data up until the current time, according to your data schema.

>**Example:** if your data is stored at 10s resolution, then at 10:02:35, it will show 
data up until 10:02:30. Once the clock hits 10:02:40, it will also include that point (10:02:40) in its response.

> It typically takes some time for your services to send data for that timestamp, and for it to be processed by Graphite, so Graphite will typically return a null here for that timestamp. Depending on how you visualize (see for example the "null as null/zero" option in grafana), or if you use a function such as sumSeries (see below) it may look like a drop in your graph, and cause panic.

You can work around this with "null as null" in Grafana, transformNull() or keepLastValue() in Graphite, or plotting until a few seconds ago instead of now. See below for some other related issues.

### 2. Null handling in math functions
Graphite functions don't exactly follow the rules of logic (by design). When you request something like `sumSeries(diskspace.server_*.bytes_free)` Graphite returns the sum of all bytes_free's for all your servers, at each point in time. If all of the servers have a null for a given timestamp, the result will be null as well for that time. However, if only some - but not all - of the terms are null, they are counted as 0.

>**Example:** The sum for a given point in time, 100 + 150 + null + null = 250.  

>So when some of the series have the 
occasional null, it may look like a drop in the summed series. This especially commonly happens for the last point at each point in time, when your servers don't submit their metrics at the exact same time.

Now let's say you work for a major video sharing website that runs many upload and transcoding clusters around the world. And let's also say you build this really cool traffic routing system that sends user video uploads to the most appropriate cluster, by taking into account network speeds, transcoding queue wait times, storage cluster capacity (summed over all servers), infrastructure cost and so forth.  Building this on top of Graphite would make a lot of sense, and in all testing everything works fine, but in production the decisions made by the algorithm seem nonsensical, because the storage capacity seems to fluctuate all over the place.   Let's just say that's  how a certain Belgian engineer became intimately familiar with Graphite's implementation of functions such as sumSeries.  Lesson learned.  No videos were hurt.

Graphite could be changed to strictly follow the rules of logic, meaning as soon as there's a null in an equation, emit a null as output. But a low number of nulls in a large sum is usually not a big deal and having a  result with the nulls counted as 0 can be more useful than no result at all. Especially when averaging, since those points can typically be safely excluded  without impact on the output. Graphite has the xFilesFactor option in storage-aggregation.conf, which lets you configure the minimum fraction of non-null values, which it uses during storage aggregation (rollups) to determine whether the input is sufficiently known for output to be known, otherwise the output value will be null.

It would be nice if these on-demand math requests would take an xFilesFactor argument to do the same thing. But for now, just be aware of it, not using the last point is usually all you need if you're only looking at the most recent data. Or get the timing of your agents tighter and only request data from Graphite until now=-5s or so.

<div class="chroma">
<strong>INTERMEZZO:</strong>
At this point we should describe the many forms of consolidation; a good understanding of this is required for the next points.
<br/><br/>
<ul>
<li><strong>storage consolidation aka aggregation, aka rollups</strong>: data aggregated to optimize the cost of historical archives and make it faster to return large timeframes of data. Driven by storage-aggregation.conf</li>
<br/>
<li><strong>runtime consolidation</strong>: when you want to render a graph but there are more datapoints than pixels for the graph, or more than the maxDataPoints setting. Graphite will reduce the data in the http response. Averages by default, but can be overridden through consolidateBy()</li>
<br/>
<li><strong>Grafana consolidation</strong>: Grafana can visualize stats such as min/max/avg which it computes on the data returned by your timeseries system.</li>
<br/>
<li><strong>statsd consolidation</strong>: statsd is also commonly used to consolidate usually very high rates of irregular incoming data in properly spaced timeframes, before it goes into Graphite.</li>
<br/>
<li>Unlike all above mechanisms which work per series,
the <a href="http://graphite.readthedocs.org/en/1.0/functions.html#graphite.render.functions.sumSeries">sumSeries()</a>, <a href="http://graphite.readthedocs.org/en/1.0/functions.html#graphite.render.functions.averageSeries">saverageSeries()</a>, <a href="http://graphite.readthedocs.org/en/1.0/functions.html#graphite.render.functions.groupByNode">groupByNode()</a> Graphite functions work
across series. They merge multiple series into a single or fewer series by aggregating  
points from different series at each point in time.</li>
<br/>
<li>And then there's <a href="http://graphite.readthedocs.org/en/latest/carbon-daemons.html#carbon-aggregator-py">carbon-aggregator</a> and <a href="https://github.com/graphite-ng/carbon-relay-ng">carbon-relay-ng</a> which operate on your metrics stream and can aggregate on per-series level, as well as across series, as well as a combination thereof.</li>

</ul>
</div>

### 3. Null handling during runtime consolidation  
Similar to above, when Graphite performs runtime consolidation it simply ignores null values. Imagine a series that measures throughput with points 10, 12, 11, null, null, 10, 11, 12, 10. Let's say it needs to aggregate every 3 points with sum. this would return 33, 10, 33. This will visually look like a drop in throughput, even though there probably was none.



For some functions like avg, a missing value amongst several valid values is usually not a big deal, but the likeliness of it becoming a big deal increases with the amount of nulls, especially with sums. For runtime consolidation, Graphite needs something similar to the xFilesFactor setting for rollups.

### 4. No consolidation or aggregation for incoming data  
If you submit multiple values into Graphite for the same interval, the last one overwrites any previous values, no consolidation/aggregation happens in this scenario.


Never send multiple values for the same interval. However, carbon-aggregator or carbon-relay-ng may be of help (see above)

### 5. Limited storage aggregation options  
In storage-aggregation.conf you configure which function to use for historical rollups. It can be limiting that you can only choose one. Often you may want to retain both the max values as well as the averages for example.(very useful for throughput). This feature exists in <a href="http://oss.oetiker.ch/rrdtool/">RRDtool</a>.

Another issue with this is that often these functions will be misconfigured. Make sure to think about all the possible metrics you'll be sending (e.g. min and max values through statsd) and set up the right configuration for them.


<a href="http://blog.librato.com/posts/time-series-data">Proprietary systems tend to be more flexible</a> and I'm sure it will make a come back in the Graphite stack as well. (more on that later)

### 6. Runtime consolidation is detached from storage aggregation  
The function chosen in storage-aggregation.conf is only used for rollups.

If Graphite performs any runtime consolidation it will always use average unless told otherwise through consolidateBy.  This means it's easy to run into cases where data is rolled up (in whisper) using, say, max or count,  but then accidentally with average while creating your visualization, resulting in incorrect information and nonsensical charts. Beware!

It would be nice if the configured roll-up function would also apply here (and also the xFilesFactor, as above),
For now, just be careful :)

### 7. Grafana consolidation is detached from storage aggregation and runtime consolidation  
Like mentioned earlier, Grafana can provide min/max/avg/... values from the received data. For now, it just computes these from the received data, which may already have been consolidated (twice: in storage and in runtime) using different functions, so these results may not be always representative. (<a href="http://play.grafana.org/dashboard/db/ultimate-graphite-query-guide">more info</a>) We will make this mechanism more powerful and accurate.

### 8. Aggregating percentiles  
The pet peeve of many, it has been written about a lot: If you have percentiles, such as those collected by statsd, (e.g. 95th percentile response time for each server) there is in theory no proper way to aggregate those numbers.  

This issue appears when rolling up the data in the storage layer, as well when doing runtime consolidation, or when  trying to combine the data for all servers (multiple series) together. There is real math behind this, and I'm not going into it because in practice it actually doesn't seem to matter much. If you're trying to spot issues or alert on outliers you'll get quite far with averaging the data together or taking the max value seen. This is especially true when the amount of requests, represented by each latency measurement, is in the same order of magnitude.  E.g. You're averaging per-server latency percentiles and your servers get a similar load or you're averaging multiple points in time for one server, but there was a similar load at each point.  You can always set up a separate alerting rule for unbalanced servers or drops in throughput.  As we'll see in some of the other points, taking sensible shortcuts instead of obsessing over math is often the better way to accomplish your job of operating your infrastructure or software.

### 9. Deriving and integration in Graphite  
The Graphite documentation for <a href="http://graphite.readthedocs.org/en/0.9.15/functions.html#graphite.render.functions.derivative">derivative()</a> hints at this already ("This function does not normalize for periods of time, as a true derivative would."), but to be  entirely clear:
<ul>
<li>Graphite's <a href="http://graphite.readthedocs.org/en/0.9.15/functions.html#graphite.render.functions.derivative">derivative</a> is not a derivative. A <a href="https://en.wikipedia.org/wiki/Derivative">derivative</a> divides difference in value by difference in time.  Graphite's derivative just returns the value deltas. Similar for <a href="http://graphite.readthedocs.org/en/0.9.15/functions.html#graphite.render.functions.nonNegativeDerivative">nonNegativeDerivative()</a>.  If you want an actual derivative, use the somewhat awkwardly named <a href="http://graphite.readthedocs.org/en/0.9.15/functions.html#graphite.render.functions.perSecond">perSecond()</a> function.</li>
<li>Graphite's integral is not an integral either. An <a href="https://en.wikipedia.org/wiki/Integral">integral sums the multiplications of the value difference with the time span</a>.  <a href="http://graphite.readthedocs.org/en/0.9.15/functions.html#graphite.render.functions.integral">Graphite's integral</a> just adds up the value differences.  To my knowledge there's no proper way to do an actual integral, but luckily this is an uncommon operation anyway. Note also that Graphite's integral just skips null values, so a value at each  point in time can be lower than it should, due to nulls that preceded it.</li>
</ul>
Maybe for a future stable Graphite release this can be reworked.  for now, just something to be aware of.  

### 10. Graphite quantization  
We already saw in the consolidation paragraph that for multiple points per interval, last write wins. But you should also know that any data point submitted gets the timestamp rounded down. 

>**Example**: You record points every 10 seconds but submit a point with timestamp at 10:02:59, in Graphite this will be stored at 10:02:50. To be more precise if you submit points at 10:02:52, 10:02:55 and 10:02:59, and have 10s resolution, Graphite will pick the point from 10:02:59 but store it at 10:02:50. So it's important that you make sure to submit points at consistent intervals, aligned to your Graphite retention intervals (e.g. if every 10s, submit on timestamps divisible by 10)

### 11. Statsd flush offset depends on when statsd was started  
Statsd lets you configure a flushInterval, i.e. how often it should compute the output stats and submit them to your backend. However, the exact timing is pretty arbitrary and depends on when statsd is  started.

>**Example**: If you start statsd at 10:02:00 with a flushInterval of 10, then it 
will emit values with timestamps at 10:02:10, 10:02:20, etc (this is what you want), but if you happened to start it at 10:02:09 then it will submit values with timestamps 10:02:19, 10:02:29, etc. So typically, the values sent by statsd are subject to Graphite's quantization and are moved into the past.  In the latter example, by 9 seconds.  This can make troubleshooting harder, especially when comparing statsd metrics to metrics from a different service.

*Note: <a href="https://github.com/vimeo/statsdaemon">vimeo/statsdaemon</a> (and possibly other servers as well) will always submit values at quantized intervals  so that it's guaranteed to map exactly to Graphite's timestamps as long as the interval is correct.*

### 12. Improperly time-attributed metrics  
You don't tell statsd the timestamps of when things happened.  Statsd applies its own timestamp when it flushes the data. So this is prone to various (mostly network) delays. This could result in a metric being generated in a certain interval only arriving in statsd after the next interval has started. But it can get worse.  Let's say you measure how long it takes to execute a query on a database server. Typically it takes 100ms but let's say now many queries are taking 60s, and you have a flushInterval of 10s. Note that the metric is only sent after the full query has completed. So during the full minute where queries were slow, there are no  metrics (or only some metrics that look good, they came through cause they were part of a group of queries that managed to execute timely), and only after a minute do you get the stats that reflect queries  spawned a minute ago. The higher a timing value, the higher the attribution error, the more into the past the values it represents and the longer the issue will go undetected or invisible. 

Keep in mind that other things, such as garbage collection cycles or paused goroutines under cpu saturation may also delay your metrics reporting. Also watch out for the queries aborting all together, causing the metrics never to be sent and these faults to be invisble! Make sure you properly monitor throughput and the functioning (timeouts, errors, etc) of the service from the client perspective, to get a more accurate picture.

*Note that many instrumentation libraries have similar issues.*

### 13. The relation between timestamps and the intervals they describe  
When I look at a point at a graph that represents a spike in latency, a drop in throughput, or anything interesting really, I always wonder whether it describes the timeframe before, or after it.

>**Example**: With points every minute, and a spike at 10:17:00, does it mean the spike happened in the timeframe between 10:16 and 10:17, or between 10:17 and 10:18?

I don't know if a terminology for this exists already, but I'm going to call the former ***premarking*** (data described by a timestamp that precedes the observation period) and the latter ***postmarking*** (data described by a timestamp at the end). As we already saw statsd postmarks, and many tools seem to do this, but some, including Graphite, premark.

We saw above that any data received by Graphite for a point in between an interval is adjusted to get the timestamp at the beginning of the interval. Furthermore, during aggregation (say, aggregating sets of 10 minutely points into 10min points), each 10 minutes taken together get assigned the timestamp that precedes those 10 intervals. (i.e. the timestamp of the first point)



So essentially, Graphite likes to show metric values before they actually happened, especially after aggregation, whereas other tools rather use a timestamp in the future of the event than in the past. As a monitoring community, we should probably standardize on an approach. I personally favor postmarking because measurements being late is fairly intuitive, predicting the future not so much.

### 14. The statsd timing type is not only for timings  
The naming is a bit confusing, but anything you want to compute summary statistics (min, max, mean, percentiles, etc) for (for example message or packet sizes) can be submitted as a timing metric. You'll get your  summary stats just fine. The type is just named "timing" because that was the original (and still most  common) use case. Note that if you want to time an operation that happens at consistent intervals,  you may just as well simply use a statsd gauge for it. (or write directly to Graphite)

### 15. The choice of metric keys depends on how you deployed statsd  
It's common to deploy a statsd server per machine or per cluster. This is a convenient way to assure you have a lot of processing capacity. However, if multiple statsd servers receive the same metric, they will do their own independent computations and emit the same output metric, overwriting each other. So if you run a statsd server per host, you should include the host in the metrics you're sending into statsd, or into the prefixStats (or similar option) for your statsd server, so that statsd itself differentiates the metrics.

*Note: there's some other statsd options to diversify metrics but the global
prefix is the most simple and common one used.*

### 16. statsd is "fire and forget", "non-blocking" &amp; UDP sends "have no overhead"  

This probably stems from this snippet in the <a href="https://codeascraft.com/2011/02/15/measure-anything-measure-everything/">original statsd announcement</a>.

<q class="cite">"[UDP is] fast — you don’t want to slow your application down in order to track its performance — but also sending a UDP packet is fire-and-forget."</q>

UDP sends do have an overhead that can slow your application down. I think a more accurate description is that the overhead is insignificant either if you're lucky, or if you've spent a lot of attention to the details. In specific, it depends on the following factors:

* **Your network stack.**  UDP sends are not asynchronous, which is a common assumption.  (i.e. they are not "non-blocking") Udp write calls from userspace will block until the kernel has moved the data  through the networking stack, firewall rules, through the network driver, onto the network.
I found this out the hard way once when an application I was testing on my laptop ran much slower than expected due to my consumer grade WiFi adapter, which was holding back my program by hanging on statsd calls. Using this <a href"http://play.golang.org/p/1YOZ1oxB-d">simple go program</a> I found that I could do 115 k/s UDP sends to localhost (where the kernel can bypass some of the network stack), but only 2k/s to a remote host (where it needs to go through all layers, including your NIC).

* **other code running, and its performance.**  If you have a PHP code base with some statsd calls amongst slow / data-intensive code to generate complex pages, there won't be much difference. This is a common, and the original setting, for statsd instrumentation calls. But I have conducted cpu profiling of high-performance Golang 
applications, both at Vimeo and raintank, and when statsd was used, the apps were often spending most of their time in UDP writes caused by statsd invocations. Typically they were using a simple statsd client, where each statsd call  corresponds to a UDP write.  There are some statsd clients that buffer messages and send batches of data to statsd, reducing the UDP writes, which is a lot more efficient. (see below). You can also use sampling to lower the volume.  This does come with some problems however, see the gotcha below.

* **The performance of client code itself can wildly vary as well.** Besides how it maps metric updates to UDP writes (see above) the invocations themselves can carry an overhead, which as you can see through <a href="https://github.com/Dieterbe/statsdbench">these benchmarks</a> of  all Go statsd clients I'm aware of, vary anywhere between 15 microseconds to 0.4 microseconds. <br /><br/>
When I saw this, <a href="https://github.com/alexcesaro/statsd"> Alex Cesaro's statsd client</a> promptly became my favorite statsd library for Go.  It has zero-allocation logic and various performance tweaks, such as the much needed client side buffering. Another interesting one is <a href="https://github.com/quipo/statsd">quipo's</a>, which offloads some of the computations into the client to reduce traffic and workload for the server.

* **Finally, it should be noted that sending to non-listening destinations may 
make your application slower.**
This is because destination hosts receiving UDP traffic for a closed socket, will return ICMP rejects to the sender, which the sender then has to process. I've not seen this with my own eyes, but the people on the #go-nuts channel who  were helping me out definitely seemed to know what they're talking about. Sometimes "disabling" statsd sends is implemented by pointing to a random host or port that's not listening (been there done that) and is hence not the best idea!


*Takeaway: If you use statsd in high-performance situations, use optimized client libraries . Or use client libraries such as go-metrics, but be prepared to pay a processing tax on all of your servers. Be aware that slow NICs and sending to non-listening destinations will slow your app down.*

### 17. statsd sampling  
The sampling feature was part of the original statsd, so it can be seen in pretty much every client and server alternative.  The idea sounds simple enough: If a certain statsd invocation causes too much statsd network traffic or  overloads the server, sample down the messages. However, there's several gotchas with this.  A common invocation with a typical  statsd client looks something like:
```
statsd.Increment("requests.$backend.$http_response")
```
In this code, we have 1 statement, and it increments a counter to track http response codes for different backends.  It works for different values of backend and http\_response, tracking the counts for each. However, let's say the backend "default" and http\_response 200 are causing too much statsd traffic. It's easy to just sample down and change the line to:
```
statsd.Increment("requests.$backend.$http_response", 0.1)
```

There's 3 problems here though:

1. How do you select a good sampling ratio? It's usually based on a gut feeling or some very quick math at best to come up with a reasonable number, without any attention to the impact on statistical significance, so you may be hurting the quality of your data.

2. While you mainly wanted to target the highest volume metric (something like "requests.default.200"), your sampling setting affects the metrics for all values of backend and http_response.  Those variable combinations that are less  frequent (for a backend that's rarely used or a response code not commonly seen)  will be too drastically sampled down, resulting in an inaccurate view of those cases. Worst case, you won't see any data over the course over a longer time period, even though there were points at every interval. You can add some code to use different invocations with different sample rates based on the values of the variables, but that can get kludgy.

3. Volumes of metric calls tend to constantly evolve over time.  It's simply not feasible to be constantly manually adjusting sample rates.  And given the above, it's not a good solution anyway.

One of the ideas I wanted to implement in https://github.com/vimeo/statsdaemon was a feedback mechanism where the server would maintain counts of received messages for each key. Based on performance criteria and standard deviation measurements, it would periodically update "recommended sampling rates" for every single key, which then could be fed back to the clients (by compiling into a PHP config file for example, or over a TCP connection).   Ultimately I decided it was just too complicated and deployed a statsdaemon server on every single machine so I could sample as gently as possible.

*Takeaway: Sampling can be used to lower load, but be aware of the trade offs.*

### 18. As long as my network doesn't saturate, statsd graphs should be accurate  
We all know that graphs from statsd are not guaranteed to be accurate, because it uses UDP, so is prone to data loss and inaccurate graphs. And we're OK with that trade  off, because the convenience is worth the loss in accuracy. However, it's commonly believed that the only, or main reason of inaccurate  graphs is UDP data loss on the network. In my experience, I've seen a lot more message loss due to the UDP buffer overflowing on the statsd server.

A typical statsd server is constantly receiving a flood of metrics. For a network socket, the Linux kernel maintains a buffer in which it stores newly received network packets, while the listening application (statsd) reads  them out of the buffer.  But if for any reason the application can't read from the buffer fast enough and it fills up, the kernel has to drop incoming traffic. The most common case are the statsd flushes, which compute all summary statistics and submit them each flushInterval. Typically this operation takes between 50ms and a few seconds, depending mostly on how many timing metrics were received, because those are the most computationally expensive.  Usually statsd's cpu is maxed out during this operation, but you won't see it on  your cpu graphs because your cpu measurements are averages taken at intervals that typically don't exactly coincide with the statsd flush-induced spikes. During this time, it temporarily cannot read from the UDP buffer, and it is very  common for the UDP buffer to rapidly fill up with new packets, at which point the Linux kernel is forced to drop incoming network packets for the UDP socket. In my experience this is very common and often even goes undetected, because  only a portion of the metrics are lost, and the graphs are not obviously wrong. Needless to say, there's also plenty of other scenarios for the buffer to fill up and cause traffic drops other than statsd flushing.

There's two things to be done here:

1. Luckily we can tune the size of the incoming UDP buffer with the net.core.rmem\_max and net.core.rmem\_default sysctl's. I recommend setting it to the <a href="http://stackoverflow.com/questions/2090850/specifying-udp-receive-buffer-size-at-runtime-in-linux">max values</a>

2. The kernel increments a counter every time it drops a UDP packet. You can see UDP packet drops with `netstat -s --udp` on the command  line. I highly encourage you to monitor this with something like collectd, visualize  it over time, and make sure to set an alert on it.


*Note also that the larger of a buffer you need, the more delay between receiving a metric and including it in the output data, possibly skewing data into the future.*

<div class="chroma">
<strong>INTERMEZZO:</strong>
There's a lot of good statsd servers out there with various feature  sets. Most of them provide improved performance (upstream statsd is single threaded JavaScript), but some come with additional interesting features. My favorites include <a href="https://github.com/armon/statsite">statsite</a>, <a href="http://githubengineering.com/brubeck/">brubeck</a> and of course <a href="https://github.com/vimeo/statsdaemon">vimeo's statsdaemon version</a>
</div>

### 19. Incrementing/decrementing gauges 
Statsd supports a syntax to <a href="https://github.com/etsy/statsd/blob/master/docs/metric_types.md#gauges"> increment and decrement gauges</a>. However, as we've seen, any message can be lost. If you do this and a message gets dropped, your gauge value will be incorrect forever (or until you set it explicitly again). Also by sending increment/decrement values you can confuse a statsd server if it was just started. For this reason, I highly recommend not using this particular feature, and always setting gauge values explicitly.  In fact, some statsd servers don't support this syntax for this reason.

### 20. You can't graph what you haven't seen  
Taking the earlier example again:
```
statsd.Increment("requests.$backend.$http_response")
```

The metrics will only be created after the values have been sent. Sounds obvious, but this can get surprisingly annoying. Let's say you want to make a graph of http 500's, but they haven't happened yet. The metrics won't exist and with many  dashboarding tools, you won't be able to create the graph yet, or at least need extra  work.

I see this very commonly with all kinds of error metrics.  I think with Grafana it will become easier to deal with this over time,  but for now I write code to just send each metric once at startup.  For counts you can just send a 0, for gauges and timers it's of course harder/weirder to come up with a fake value but it's still a  reasonable approach.

### 21. Don't let the data fool you: nulls and deleteIdleStats options  
statsd has the deleteIdleStats, deleteGauges, and similar options. By default they are disabled, meaning statsd will keep sending data for metrics it's no longer seeing. So for example, it'll keep sending the last gauge value even if it didn't get an update. I have three issues with this:

* **Your graphs are misleading.** Your service may be dead but you can't tell from 
the gauge graphs cause they will still "look good". If you have something like  counters for requests handled, you can't tell the difference between your  service being dead or it being up but not getting incoming requests.  I rather have no data show up if there is none, combined with something else (alerting, different graph) to deduce whether the service is up or not

* **Any alerting rules defined on the metrics have the same fate as humans and 
can't reliably do their work**

* **Tougher to phase out metrics.**  If you decommission servers or services, it's nice that the metrics stop updating so you can clean them up later</li>

My recommendation is, enable deleteIdleStats.  I went as far as hard coding that behavior into <a  href="https://github.com/vimeo/statsdaemon">vimeo/statsdaemon</a> and not making it configurable.

To visualize it, make sure in Grafana to set the "null as null" option, though "null as zero" can make sense for counters. You can also use the <a href="http://graphite.readthedocs.org/en/0.9.15/functions.html#graphite.render.functions.transformNull">transformNull()</a> or <a href="http://graphite.readthedocs.org/en/0.9.15/render_api.html#drawnullaszero">drawNullAsZero</a> options in Graphite for those  cases where you want to explicitly get 0's instead of nulls, which I typically  do in some of my bosun alerting rules, so I can treat null counts as no traffic received, while having a separate alerting rule to make sure my service is up  and running, based on a different metric, while using null as null for visualization. 


### 22. keepLastValue works... almost always
Another Graphite function to change the semantics of nulls is <a href="http://graphite.readthedocs.org/en/latest/functions.html#graphite.render.functions.keepLastValue"> keepLastValue</a>, which causes null values to be represented by the last known value that precedes them. However, that known value must be included in the requested time range.  This is probably a rare case that you may never encounter, but if you have scripts that infrequently update a metric and you use this function, it may result in a graph sometimes showing no data at all if the last known value becomes too old.  Especially confusing to newcomers, if the graph does "work" at other times.

### 23. statsd counters are not counters in the traditional sense  
You may know counters such as switch traffic/packet counters, that just keep increasing over time. You can see their rates per second by deriving the data. Statsd counters however, are typically either stored as the number of hits per flushInterval, or per second, or both (perhaps because of Graphite's derivative issue?). This in itself is not a huge problem, however this is more vulnerable to loss of data.  If your statsd server has trouble flushing some data to Graphite and some data gets lost.  If it were using a traditional counter, you could still derive the data and average out the gap across the nulls. In this case however this is not possible and you have no idea what the numbers were.  In practice this doesn't happen often though.  Many statsd implementations can buffer a writequeue or use something like <a href="https://github.com/graphite-ng/carbon-relay-ng"> carbon-relay-ng</a> as a write queue. 
Other disadvantages of this approach is that you need to know the flushInterval
value to make sense of the count values, and the rounding that happens when
computing the rates per second, which is also slightly lossy.

### 24. What can I send as input?  
Neither <a href="http://graphite.readthedocs.org/en/latest/feeding-carbon.html">Graphite</a>, nor <a href="https://github.com/etsy/statsd/blob/master/docs/metric_types.md">statsd</a> does a great job specifying exactly what they allow as input, which can be frustrating.  Graphite timestamps are 32bit unix timestamp integers, while values for both Graphite and statsd can be integers or floats, up to float 64bit precision. For statsd, see the <a href"https://github.com/b/statsd_spec">statsd_spec</a> project for more details.

As for what characters can be included in the metric keys. Generally, Graphite is somewhat forgiving and may alter your metric keys: it converts slashes to dots (which can be confusing), subsequent dots become single dots, prefix dots get removed, postfix dots will get it confused a bit though and create an extra hierarchy with an empty node at the end if you're using whisper. Non-alphanumeric characters such as <a href="https://github.com/graphite-project/graphite-web/issues/242">parenthesis</a>, <a href="https://github.com/graphite-project/graphite web/issues/604">colons</a>, or <a href="https://github.com/brutasse/graphite-api/issues/57"> equals signs</a> often don't work well or at all.

Graphite as a policy does not go far in validating incoming data, citing performance in large-throughput systems as the major reason. It's up to the senders to send data in proper form, with non-empty nodes (words between dots) separated by single dots.  You can use alphanumeric characters, hyphens and underscores, but straying from that will probably not work well. You may want to use <a href="https://github.com/graphite-ng/carbon-relay-ng"> carbon-relay-ng</a> which provides metric validation. See also <a href="https://github.com/graphite-project/carbon/issues/417">this issue</a> which aims to formalize what is, and isn't allowed.

### 25. Hostnames and ip addresses in metric keys  
The last gotcha relates to the previous one but is so common it deserves its own spot. Hostnames, especially FQDN's, and IP addresses (due to their dots), when included in metric keys, will be interpreted by Graphite as separate pieces. Typically, people replace all dots in hostnames and IP addresses with hyphens or underscores to combat this.

### Closing thoughts
Graphite, Grafana and statsd are great tools, but there's some things to watch out for. When setting them up, make sure you configure Graphite and statsd to play well together. Make sure to set your roll-up functions and data retentions properly, and  whichever statsd version you decide to use, make sure it flushes at the same  interval as your Graphite schema configuration. <a  href="https://github.com/etsy/statsd/blob/master/docs/graphite.md">More tips if you use the nodejs version</a>. Furthermore, I hope this is an extensive list of gotchas and will serve to improve our practices at first, and our tools themselves, down to road. We are definitely working on making things better and have some announcements coming up...
