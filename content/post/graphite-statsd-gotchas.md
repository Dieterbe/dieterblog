+++
title = "Graphite and statsd gotchas"
date = "2016-01-04T16:22:03-04:00"
tags = ["monitoring"]
draft = true
+++

For several years now, I've worked with Graphite and statsd on a daily basis.
Over the years, I ran into many subtle issues and today I want to share some 
gotchas and insights I've gathered over the years.

First of all, whenever you're trying to debug what's going on with your metrics 
going in or out of either of these tools,
don't be afraid to dive into the network or the whisper files.
They are often invaluable in understanding what's up.

For network sniffing, I almost always use these commands:
<code>
ngrep -d any -W byline port 2003
ngrep -d any -W byline port 8125
</code>
Getting the json output from Graphite (just append `&format=json`) can be very 
helpful as well.
Many dashboards, including <a href="http://www.grafana.org">Grafana</a> already 
do this, so you can use the browser network tab to inspect requests.
For the whisper files, graphite comes with various useful utilities such as 
whisper-info, whisper-dump, whisper-fetch, etc.


here we go:

1) omg! did all our traffic just drop?
probably the most common gotcha, and one i run into periodically.
Graphite will return data up until the current time, according to your data 
schema.
E.g. if your data is stored at 10s resolution, then at say 10:02:35 it will show 
data up until 10:02:30, but once the clock hits 10:02:40, it will also include 
that point,
but it typically takes some time for your services to send data for that 
timestamp, and for it to be processed by graphite, so graphite will typically 
return a null here for that timestamp
and depending on how you visualize (see for example the "null as null/zero" 
option in grafana) it may look like a drop in your graph, and cause panic.
You can work around this with "null as null" in Grafana, transformNull() in 
graphite, or plotting until a few seconds ago instead of now.
See below for some other related issues.

2) graphite functions don't exactly follow the rules of logic (by design)
When you request something like `sumSeries(diskspace.server_*.bytes_free)` 
graphite returns the sum of all bytes_free's for all your servers, at each point 
in time.
If all of the servers have a null for a given timestamp, the result will be null 
as well for that time.
However, if only some - but not all - of the terms are null, they are counted as 
0.
For example: 100 + 150 + null + null = 250.  So when some of the series have the 
occasional null, it may look like a drop in the summed series.
This especially commonly happens for the last point at each point in time, when 
your servers don't submit their metrics at the exact same time.

Now let's say you work for a major video sharing website that runs many upload 
&amp; transcoding clusters around the world.
And let's say you build this really cool traffic routing system that sends user 
video uploads to the most appropriate cluster, by taking into account network 
speeds, transcoding queue wait times, storage cluster capacity (summed over all 
servers), infrastructure cost and so forth.  Building this on top of graphite 
would make a lot of sense, and in all testing everything works fine, but in 
production the decisions made by the algorithm seem nonsensical, because the 
storage capacity seems to fluctuate all over the place.   Let's just say that's 
how a certain Belgian engineer became intimately familiar with Graphite's 
implementation of functions such as sumSeries.  Lesson learned.  No videos were 
hurt.

Graphite could be changed to strictly follow the rules of logic, meaning as soon 
as there's a null in an equation, emit a null as output.
But a low number of nulls in a large sum is usually not a big deal and having a 
result with the nulls counted as 0 can be more useful than no result at all.
Especially when averaging, since those points can typically be safely excluded 
without impact on the output.
When Graphite performs storage aggregation (rollups), it allows allowing a 
certain fraction of null values, configured through xFilesFactor,
It would be nice if these on-demand math requests would take an xFilesFactor 
argument to do the same thing.
But for now, just be aware of it, not using the last point is usually all you 
need if you're only looking at the most recent data.
Or get the timing of your agents tighter and only request data from graphite 
until now=-5s or so.


3) nulls consolidation logic

Just like above, when Graphite performs runtime consolidation (for example when 
there's more points than pixels, or than maxDataPoints), it simply takes out 
null values.
Imagine a series that measures throughput with points 10, 12, 11, null, null, 
10, 11, 12, 10.
Let's say it needs to aggregate every 3 points with sum. this would return 33, 
10, 33.
This will visually look like a drop in throughput, and if you have alerting that 
looks for throughput drops, it would trigger here.

For some functions like avg, a missing value amongst several valid values is 
usually not a big deal, but the likeliness of it becoming a big deal increases 
with the amount of nulls,
so I think here we should also implement an xFilesFactor.


4) consolidation &amp; aggregation confusion

The storage-aggregation.conf configuration is only used for storage-level 
aggregation (aka rollups), not any runtime consolidation.
<ul>
<li>if you submit multiple values into graphite for the same interval, the last 
one overwrites any previous values, no consolidation/aggregation happens in this 
scenario.
(note that carbon-aggregator and carbon-relay-ng can aggregate multiple series 
together, as well as multiple points per series into a single point, so you can 
use that)</li>
<li>if graphite performs any runtime consolidation (e.g. there are more points 
than pixels for your graph, or more points than your maxDataPoints option), it 
will always use
average unless told otherwise through consolidateBy.  This means it's easy to 
run into cases where data is rolled up (in whisper) using, say, max or count, 
but then
accidentally with average while creating your visualization, resulting in 
incorrect information.  It's easy to make mistakes and applying the wrong 
function for rollups or
runtime consolidation.  It would be nice if the roll-up configuration would also 
apply here (the function choice as well as xFilesFactor, see above), but for 
now, just be careful :)</li>
</ul>

(side note: only having 1 option to consolidate data can be restricting.  Many 
systems consolidate <a href="http://blog.librato.com/posts/time-series-data"> 
data into a few summary stats</a> so that you can later get the flavor you 
want.)

5) aggregating percentiles.
The pet peeve of many, it has been written about a lot: if you have percentiles, 
such as those collected by statsd, - e.g. 95th percentile response time for each 
server - there is in theory
no proper way to aggregate those numbers.  This issue appears when rolling up 
the data in the storage layer, as well when doing runtime consolidation, or when 
trying to combine the data for all servers (multiple series) together.
There is real math behind this, and I'm not going into it because in practice it 
actually doesn't seem to matter much.
If you're trying to spot issues, alert on outliers, you get quite far with 
averaging the data together or taking the max value seen, especially when the 
amount of requests represented by each latency measurement is in the same order 
of magnitude,  e.g. your averaging per-server latency percentiles and your 
servers get a similar load or multiple points in time for one server, but there 
was a similar load at each point then you'll be fine.  And you can always set up 
a separate alerting rule for unbalanced servers or drops in throughput.  As 
we'll see in some of these other points, sometimes taking sensible shortcuts 
instead of obsessing over math is the better way to get your work done operating 
your infrastructure or software.

6) deriving &amp; integration in graphite.

The graphite documentation for derivative() hints at it already ("This function 
does not normalize for periods of time, as a true derivative would."), but to be 
entirely clear:
<ul>
<li>graphite's derivative is not a derivative. (a <a 
href="https://en.wikipedia.org/wiki/Derivative">derivative</a> divides 
difference in value by difference in time.  Graphite's derivative just returns 
the value delta's. Similar for nonNegativeDerivative).  If you want an actual 
derivative, use the somewhat awkwardly named perSecond() function.</li>
<li>graphite's integral is not an integral either. (an <a 
href="https://en.wikipedia.org/wiki/Integral">integral adds the multiplications 
of the value difference with the time span</a>.  Graphite's integral just adds 
up the value differences).  To my knowledge there's no proper way to do an 
actual integral, but luckily this is an uncommon operation anyway.
 Note also that graphite's integral just skips null values, so a value at each 
 point in time can be lower than it should, due to nulls that preceded it.</li>
 </ul>

Maybe for a future stable graphite release this can be reworked.  for now, just 
something to be aware of.

7) graphite quantization
We already saw in the consolidation paragraph that for multiple points per 
interval, last write wins.
But you should also know that any data point submitted gets the timestamp 
rounded down.
Let's say you record points every 10 seconds but submit a point with timestamp 
at 10:02:59, in graphite this will be stored at 10:02:50.
So it's important that you make sure to submit points at consistent intervals, 
aligned to your graphite retention intervals (e.g. every 10s, submit on 
timestamps divisible by 10)

8) statsd flush offset depends on when statsd was started
Statsd lets you configure a flushInterval, i.e. how often it should compute the 
output stats and submit them to your backend.
However, the exact timing is pretty arbitrary and depends on when statsd is 
started.
For example, if you start statsd at 10:02:00 with a flushInterval of 10, then it 
will emit values with timestamps at 10:02:10, 10:02:20, etc (this is what you 
want), but if you happened
to start it at 10:02:09 then it will submit values with timestamps 10:02:19, 
10:02:29, etc. So typically, the values sent by statsd are subject to graphite's 
quantization and are moved into the past.  In the latter example, by 9 seconds. 
This can make troubleshooting harder, especially when comparing statsd metrics 
to metrics from a different service.

Note: <a href="https://github.com/vimeo/statsdaemon">vimeo/statsdaemon</a> (and 
possibly other servers as well) will always submit values at quantized intervals 
so that it's guaranteed to map exactly to graphite's timestamps as long as the 
interval is correct.

9) improperly time-attributed metrics.
You don't tell statsd timestamps of when things happened.  Statsd applies its 
own timestamp when it flushes the data.
So this is prone to various (mostly network) delays.
This could result in a metric being generated in a certain interval only 
arriving in statsd after the next interval has started.
But it can get worse.  Let's say you measure how long it takes to connect to a 
database server.
Typically it takes 100ms but maybe now it takes 60s. Note that the metric 
message is only sent after the full request has completed.
So during the full minute where requests were slow and busy, there are no 
metrics, and only after a minute do you get the stats that reflect requests 
spawned a minute ago, and issues that were live several intervals before being 
reported.
Not a major issue, just something to be aware of. The higher a timing value, the 
more into the past the values it represents. Note that many instrumentation 
libraries have similar issues.

10) the relation between timestamps and the intervals they describe.
When I look at a point at a graph that represents a spike in latency, a drop in 
throughput, or anything interesting really, I always wonder whether it describes 
the timeframe before, or after it.
For example, with points every minute, and a spike at 10:17:00, does it mean the 
spike happened in the timeframe between 10:16 and 10:17, or between 10:17 and 
10:18 ?
I don't know if a terminology for this exists already, but I'm going to call the 
former premarking (data described by a timestamp that precedes the observation 
period) and the latter postmarking (data described by a timestamp at the end).  
As we already saw statsd postmarks, and many tools seem to do this, but some, 
including graphite, premark.

We saw above that any data received by graphite for a point in between an 
interval is adjusted to get the timestamp at the beginning of the interval.
Furthermore, during aggregation (say, aggregating 10 minutely points into 10min 
points), each 10 minutes taken together get assigned the timestamp that precedes 
those 10 intervals.
So essentially, graphite likes to show metric values before they actually 
happened, especially after aggregation, whereas other tools rather use a 
timestamp that is too late rather than too soon.  As a monitoring community, we 
should probably standardize on an approach.

10) the statsd timing type is only for timings.
The naming is a bit confusing, but anything you want to compute summary 
statistics (min, max, mean, percentiles, etc) for
(for example message sizes) can be submitted as a timing metric. You'll get your 
summary stats just fine.
The type is just named "timing" because that was the original (and still most 
common) use case.
Note that if you want to time an operation that happens at consistent intervals, 
you may just as well simply use a statsd gauge for it.

11) the choice of metric keys you can use depends on how you deployed your 
statsd's
It's common to deploy a statsd server per machine or per cluster.
This is a convenient way to assure you have a lot of processing capacity.
However, if multiple statsd servers receive the same metric, they will do their 
own,
independent computations, and emit the same output metric, overwriting each 
other.
So if you run a statsd server per host, you should include the host in your 
keys.

Takeaway: don't send the same key to multiple statsd servers

12) statsd is "fire and forget" &amp; udp sends "have no overhead".

This probably stems from this snippet in the <a 
href="https://codeascraft.com/2011/02/15/measure-anything-measure-everything/">original 
statsd announcement</a>.
<quote>
[UDP is] fast — you don’t want to slow your application down in order to track 
its performance — but also sending a UDP packet is fire-and-forget.
</quote>
UDP sends do have an overhead that can slow your application down. I think a 
more accurate description would be that the overhead can be considered 
insignificant, depending on a few factors:

<ul>
<li>other code running, and its performance.  If you have a PHP code base with 
some statsd calls amongst slow / data-intensive code to generate complex pages, 
there won't be much difference.
This is a common, and the original setting, for statsd instrumentation calls.  
But I have done quite some cpu profiling of high-performance Golang 
applications,
both at Vimeo and raintank, and when statsd was used the apps were often 
spending most of their time in UDP writes caused by statsd invocations.
Typically they were using a simple statsd client where each statsd call 
corresponds to a udp write.
Using a statsd client library that batches sends into buffered messages, and/or 
offloads some of the computation client side, can help a lot in such cases.
You can also use sampling to lower the volume. This does come with some problems 
however, see below.
</li>
<li>Your network stack.  The sends are not asynchronous, which is a common 
assumption.
Udp write calls from userspace will block until the kernel has moved the data 
through the networking stack, firewall rules, through the network driver, onto 
the network.
I found this out the hard way once when an application I was testing on my 
laptop ran much slower than expected, due to my consumer grade WiFi adapter, 
holding back my program which was hanging on statsd calls.
Using this simple go program http://play.golang.org/p/1YOZ1oxB-d I found that I 
could do 115 k/s udp sends to localhost (where the kernel can bypass some of the 
network stack), but only 2k/s to a remote host (where it needs to go through all 
layers, including your NIC).
</li>
<li>Finally, it should be noted that sending to non-listening destinations may 
make your application slower.
This is because destination hosts receiving udp traffic for a closed socket, 
will return ICMP rejects to the sender, which the sender then has to process.
I've not seen this with my own eyes, but the people on the #go-nuts channel who 
were helping me out definitely seemed to know what they're talking about.
Sometimes "disabling" statsd sends is implemented by pointing to a random host 
or port that's not listening (been there done that) and is hence not the best 
idea.
</li>
</ul>

Takeaway: If you use statsd in high-performance situations, use client libraries 
that buffer udp writes and optionally offload preliminary calculations to the 
client side.
Or use client libraries such as go-metrics, but be prepared to pay a processing 
tax on all of your servers.
Be aware that slow NICs and sending to non-listening destinations will slow your 
app down.


13) statsd sampling.
The sampling feature was part of the original statsd, so it can be seen in 
pretty much every client and server alternative.  The idea sounds simple enough:
If a certain statsd invocation causes too much statsd network traffic or 
overloads the server, sample down the messages.
However, there's several gotchas with this.  A common invocation with a typical 
statsd client looks something like:
```
statsd.Increment("requests.$backend.$http_response")
```
In this code, we have 1 statement, and it increments a counter to track http 
response codes for different backends.  It works for different values of backend 
and http_response, tracking the counts for each.
However, let's say the backend "default" and http_response 200 are causing too 
much statsd traffic.
It's easy to just sample down and change the line to:
```
statsd.Increment("requests.$backend.$http_response", 0.1)
```

There's 3 problems here though:

1) How do you select a good sampling ratio? It's usually a gut feel or some very 
quick math at best to come up with a reasonable number, without
any attention to the impact on statistical significance, so you may be hurting 
the quality of your data.
2) While you mainly wanted to target the highest volume metric (something like 
"requests.default.200"), your sampling setting affects the metrics for all 
values of backend and http_response.  Those variable combinations that are less 
frequent (for a backend that's rarely used or a response code not commonly seen) 
will be too drastically sampled down,
resulting in an inaccurate view of those cases, and worst case, not seeing any 
data over the course over a longer time period, even though there were points at 
every interval.
You can add some code to use different invocations based with different sample 
rates on the values of the variables, but that can get kludgy.
3) volumes of metric calls tend to constantly evolve over time.  It's simply not 
feasible to be constantly manually adjusting sample rates.  And given the above, 
it's not a good solution anyway.

<p>
one of the ideas I wanted to implement in https://github.com/vimeo/statsdaemon 
was a feedback mechanism where the server would maintain counts
of received messages for each key, and based on preferences and standard 
deviation measurements, would periodically update "recommended sampling rates"
for every single key, which then could be fed back into the clients (by 
compiling into a php config file for example, or over a tcp connection).  
Ultimately I decided it was just too complicated and deployed a statsdaemon 
server
on every single machine so I could sample as gently as possible.

Takeaway: sampling can be used to lower load, but be aware of the trade offs.

14) as long as my network doesn't saturate, statsd graphs should be accurate.
we all know that graphs from statsd are not guaranteed to be accurate, because 
it uses UDP,
so is prone to data loss and inaccurate graphs. And we're OK with that trade 
off, because the convenience is worth the loss in accuracy.
However, it's commonly believed that the only, or main reason of inaccurate 
graphs is udp data loss on the network.
In my experience, I've seen a lot more message loss due to the udp buffer 
overflowing on the statsd server.

A typical statsd server is constantly receiving a flood of metrics at all times.
For a network socket, the Linux kernel maintains a buffer in which it stores 
newly received network packets, while the listening application (statsd) reads 
them out of the buffer.
But a statsd server will flush and compute all summary statistics, each 
configured flushInterval.
Typically this operation takes between 50ms and a few seconds, depending mostly 
on how many timing metrics were received, cause those are the most 
computationally expensive.
Usually statsd's cpu is maxed out during this operation, but you won't see it on 
your cpu graphs because your cpu measurements are averages taken at intervals 
that typically
don't exactly coincide with the statsd flush-induced spikes.
During this time, it temporarily cannot read from the UDP buffer, and it is very 
common for the UDP buffer to rapidly fill up with new packets, at which point
the Linux kernel is forced to drop incoming network packets for the UDP socket.
In my experience this is very common and often even goes undetected, because 
only a portion of the metrics are lost, the graphs are not obviously wrong.

There's two things to be done here:
<ol>
<li>
Luckily we can tune the size of the incoming udp buffer with the
net.core.rmem_max and net.core.rmem_default sysctl's.
I recommend setting it to the <a 
href="http://stackoverflow.com/questions/2090850/specifying-udp-receive-buffer-size-at-runtime-in-linux">max 
values</a>
</li>
<li>the kernel increments a counter every time it drops a udp packet.
You can see udp packet drops with <code>netstat -s --udp</code> on the command 
line.
I highly encourage you to monitor this with something like collectd, visualize 
it over time, and make sure to set an alert on it.
</li>
</ol>

Note also that the larger of a buffer you need, the more delay between receiving 
a metric and including it in the output data, possibly skewing data into the 
future.

intermezzo: there's a lot of good statsd servers out there with various feature 
sets.
Most of them provide improved performance (upstream statsd is single threaded 
JavaScript), but some come with additional interesting features.
My favorites include <a href="https://github.com/armon/statsite">statsite</a>, 
<a href="http://githubengineering.com/brubeck/">brubeck</a> and of course
<a href="https://github.com/vimeo/statsdaemon">vimeo's statsdaemon version</a>


15) you can't graph what you haven't seen
Taking the earlier example again:
```
statsd.Increment("requests.$backend.$http_response")
```

The metrics will only be created after the values have been sent. Sounds 
obvious, but this can get surprisingly annoying. Let's say you want to make a 
graph of http 500's,
but they haven't happened yet, then the metrics won't exist and with many 
dashboards, you won't be able to create the graph yet, or at least need extra 
work.
I see this very commonly with all kinds of error metrics.  I think with Grafana 
it will become easier to deal with this over time,  but for now I write code to 
just send each metric
once at startup.  For counts you can just send a 0, for gauges and timers it's 
of course harder/weirder to come up with a fake value but it's still a 
reasonable approach.


16) don't let the data fool you: nulls and deleteIdleStats options.

statsd has the deleteIdleStats, deleteGauges, and similar options. By default 
they are disabled, meaning statsd will keep sending data for metrics it's no 
longer seeing.
So for example, it'll keep sending the last gauge value even if it didn't get an 
update. I have three issues with this:
<ul>
<li>your graphs are misleading. Your service may be dead but you can't tell from 
the gauge graphs cause they will still "look good". If you have something like 
counters for requests handled, you can't tell the difference between your 
service being dead or it being up but not getting incoming requests.  I rather 
have no data show up if there is none, combined with something else (alerting, 
different graph) to deduce whether the service is up or not</li>
<li>any alerting rules defined on the metrics have the same fate as humans and 
can't reliably do their work</li>
<li>it makes it harder to phase out metrics.  If you decommission servers or 
services, it's nice that the metrics stop updating so you can clean them up 
later</li>
</ul>
So my recommendation is, enable deleteIdleStats.  I went as far as hard coding 
that behavior into <a 
href="https://github.com/vimeo/statsdaemon">vimeo/statsdaemon</a> and not making 
it configurable.

To visualize it, make sure in Grafana to set the "null as null" option, though 
"null as zero" can make sense for counters.
You can also the transformNull or drawNullAsZero options in graphite for those 
cases where you want to explicitly get 0's instead of nulls, which I typically 
do in some of my bosun alerting rules, so I can treat null counts as no traffic 
received, while having a separate alerting rule to make sure my service is up 
and running, based on a different metric.
while using null as null for visualization. 


Closing thoughts:
Graphite and statsd are great tools, but there's some things to watch out for.
When setting them up, make sure you configure graphite and statsd to play well 
together.
Make sure to set your roll-up functions and data retentions properly, and 
whichever statsd version you decide to use, make sure it flushes at the same 
interval as your graphite schema's.
see <a 
href="https://github.com/etsy/statsd/blob/master/docs/graphite.md">this</a> for 
more details.

