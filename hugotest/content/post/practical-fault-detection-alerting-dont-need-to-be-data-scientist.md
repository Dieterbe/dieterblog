+++
title = "Practical fault detection & alerting.  You don't need to be a data scientist"
date = "2015-01-29T09:08:02-04:00"
tags = ["devops", "monitoring"]
+++
As we try to retain visibility into our increasingly complicated applications and infrastructure, we're building out more advanced monitoring systems.

Specifically, a lot of work is being done on alerting via fault and anomaly detection.

This post covers some common notions around these new approaches, debunks some of the myths that ask for over-complicated solutions, and provides some practical pointers that any programmer or sysadmin can implement that don't require becoming a data scientist.

<!--more-->

<br/>

<br/>



<h2>It's not all about math</h2>

<p>

I've seen smart people who are good programmers decide to tackle anomaly detection on their timeseries metrics.

(anomaly detection is about building algorithms which spot "unusual" values in data, via statistical frameworks).  This is a good reason to brush up on statistics, so you can apply some of those concepts.

But ironically, in doing so, they often seem to think that they are now only allowed to implement algebraic mathematical formulas. No more if/else, only standard deviations of numbers.  No more for loops, only moving averages. And so on.

<br/>When going from thresholds to something (<i>anything</i>) more advanced, suddenly people only want to work with mathematical formula's.  Meanwhile we have entire Turing-complete programming languages available, which allow us to execute any logic, as simple or as rich as we can imagine.  Using only math massively reduces our options in implementing an algorithm. 

<br/>

<br/>For example I've seen several presentations in which authors demonstrate how they try to fine-tune moving average algorithms and try to get a robust base signal to check against but which is also not affected too much by previous outliers, which raise the moving average and might mask subsequent spikes).  

<br/>

<img src="http://dieter.plaetinck.be/files/fault-detection-moving-average.png">

from <a href="https://speakerdeck.com/astanway/a-deep-dive-into-monitoring-with-skyline">A Deep Dive into Monitoring with Skyline</a>

<br/>

<br/>

But you can't optimize both, because a mathematical formula at any given point can't make the distinction between past data that represents "good times" versus "faulty times".

<br/>However: we wrap the output of any such algorithm with some code that decides what is a fault (or "anomaly" as labeled here) and alerts against it, so why would we hold ourselves back in feeding this useful information back into the algorithm?

<br/>I.e. <b>assist the math with logic</b> by writing some code to make it work better for us:  In this example, we could modify the code to just retain the old moving average from before the time-frame we consider to be faulty.  That way, when the anomaly passes, we resume "where we left off".  For timeseries that exhibit seasonality and a trend, we need to do a bit more, but the idea stays the same.   Restricting ourselves to only math and statistics cripples our ability to detect actual <b>faults</b> (problems).

</p>

<p>

Another example: During his <a href="https://coderanger.net/talks/echo/">Monitorama talk</a>, Noah Kantrowitz made the interesting and thought provoking observation that Nagios flap detection is basically a low-pass filter.  A few people suggested re-implementing flap detection as a low-pass filter.  This seems backwards to me because reducing the problem to a pure mathematical formula loses information.  The current code has the high-resolution view of above/below threshold and can visualize as such.  Why throw that away and limit your visibility?

</p>



<h2>Unsupervised machine learning... let's not get ahead of ourselves.</h2>

<a href="https://codeascraft.com/2013/06/11/introducing-kale/">Etsy's Kale</a> has ambitious goals: you configure a set of algorithms, and those algorithms get applied to <b>all</b> of your timeseries.  Out of that should come insights into what's going wrong.  The premise is that the found anomalies are relevant and indicative of faults that require our attention.

<br/>I have quite a variety amongst my metrics.  For example diskspace metrics exhibit a sawtooth pattern (due to constant growth and periodic cleanup),

crontabs cause (by definition) periodic spikes in activity, user activity causes a fairly smooth graph which is characterized by its daily pattern and often some seasonality and a long-term trend.

<br/>

<br/>

<img width="70%" src="http://dieter.plaetinck.be//files/anomaly-detection-cases.png">

<br/>

<br/>Because they look differently, anomalies and faults look different too.  In fact, within each category there are multiple problematic scenarios. (e.g. user activity based timeseries should not suddenly drop, but also not be significantly lower than other days, even if the signal stays smooth and follows the daily rhythm)

<br/>

<br/>I have a hard time believing that running the same algorithms on all of that data, and doing minimal configuration on them, will produce meaningful results. At least I expect a very low signal/noise ratio.  Unfortunately, of the people who I've asked about their experiences with Kale/Skyline, the only cases where it's been useful is where skyline input has been restricted to a certain category of metrics - it's up to you do this filtering (perhaps via carbon-relay rules), potentially running multiple skyline instances - and sufficient time is required hand-selecting the appropriate algorithms to match the data.  This reduces the utility.

<br/>"Minimal configuration" sounds great but this doesn't seem to work.

<br/>

Instead, something like <a href="http://bosun.org/">Bosun</a> (see further down) where you can visualize your series, experiment with algorithms and see the results in place on current and historical data, to manage alerting rules seems more practical.

<br/>

<br/>Some companies (all proprietary) take it a step further and pay tens of engineers to work on algorithms that inspect all of your series, classify them into categories, "learn" them and automatically configure algorithms that will do anomaly detection, so it can alert anytime something looks unusual (though not necessarily faulty). 

This probably works fairly well, but has a high cost, still can't know everything there is to know about your timeseries, is of no help of your timeseries is behaving faulty from the start and still alerts on anomalous, but irrelevant outliers.

<br/>

<br/>



I'm <b>suggesting we don't need to make it that fancy</b> and we can do much better by <b>injecting some domain knowledge</b> into our monitoring system:

<ul>

<li>using minimal work of classifying metrics via metric meta-data or rules that parse metric id's, we can automatically infer knowledge of how the series is supposed to behave (e.g. assume that disk_mb_used looks like sawtooth, frontend_requests_per_s daily seasonal, etc) and apply fitting processing accordingly.

<br/>Any sysadmin or programmer can do this, it's a bit of work but should make a hands-off automatic system such as Kale more accurate.

<br/>Of course, adopting <a href="http://metrics20.org/">metrics 2.0</a> will help with this as well. Another problem with machine learning is they would have to infer how metrics relate against each other, whereas with metric metadata this can easily be inferred (e.g.: what are the metrics for different machines in the same cluster, etc)</li>

<li>hooking into service/configuration management: you probably already have a service, tool, or file that knows how your infrastructure looks like and which services run where.  We know where user-facing apps run, where crontabs run, where we store log files, where and when we run cleanup jobs.  We know in what ratios traffic is balanced across which nodes, and so on.  Alerting systems can leverage this information to apply better suited fault detection rules.  And you don't need a large machine learning infrastructure for it. (as an aside: I have a lot more ideas on cloud-monitoring integration)</li>

<li>Many scientists are working on algorithms that find cause and effect when different series exhibit anomalies, so they can send more useful alerts.  But again here, a simple model of the infrastructure gives you service dependencies in a much easier way.</li>

<li>hook into your event tracking. If you have something like <a href="https://github.com/Dieterbe/anthracite/">anthracite</a> that lists upcoming press releases, then your monitoring system knows not to alert if suddenly traffic is a bit higher.  In fact, you might want to alert if your announcement did not create a sudden increase in traffic.  If you have a large scale infrastructure, you might go as far as tagging upcoming maintenance windows with metadata so the monitoring knows which services or hosts will be affected (and which shouldn't).

</ul>

<br/>

Anomaly detection is useful if you don't know what you're looking for, or providing an extra watching eye on your log data.  Which is why it's commonly used for detecting fraud in security logs and such.

For operational metrics of which admins know what they mean, should and should not look like, and how they relate to each other, we can build more simple and more effective solutions.





<h2>The trap of complex event processing... no need to abandon familiar tools</h2>

On your quest into better alerting, you soon read and hear about real-time stream processing, and CEP (complex event processing) systems.

It's not hard to be convinced on their merits:  who wouldn't want real-time as-soon-as-the-data-arrives-you-can-execute-logic-and-fire-alerts?

<br/>They also come with a fairly extensive and flexible language that lets you program or compose monitoring rules using your domain knowledge.

I believe I've heard of <a href="https://storm.apache.org/">storm</a> for monitoring, but <a href="http://riemann.io/">Riemann</a> is the best known of these tools that focus on open source monitoring.

It is a nice, powerful tool and probably the easiest of the CEP tools to adopt.  It can also produce very useful dashboards.

However, these tools come with their own API or language, and programming against real-time streams is quite a paradigm shift which can be hard to justify.  And while their architecture and domain specificity works well for large scale situations, these benefits aren't worth it for most (medium and small) shops I know:  it's a lot easier (albeit less efficient) to just query a datastore over and over and program in the language you're used to.  With a decent timeseries store (or one written to hold the most recent data in memory such as <a href="https://github.com/dgryski/carbonmem">carbonmem</a>) this is not an issue, and the difference in timeliness of alerts becomes negligible!





<h2>An example: finding spikes</h2>

Like many places, we were stuck with static thresholds, which don't cover some common failure scenarios.

So I started asking myself some questions:

<br>

<br>

<center>

    <i>which behavioral categories of timeseries do we have, what kind of issues can arise in each category,

        <br/>how does that look like in the data, and what's the simplest way I can detect each scenario?</i>

</center>

<br/>

Our most important data falls within the user-driven category from above where various timeseries from across the stack are driven by, and reflect user activity.  And within this category, the most common problem (at least in my experience) is spikes in the data.  I.e. a sudden drop in requests/s or a sudden spike in response time.  As it turned out, this is much easier to detect than one might think:

<br/>

<img style="float:left; margin:15px;" src="http://dieter.plaetinck.be/files/poor-mans-fault-detection.png">

<br/>

In this example I just track the standard deviation of a moving window of 10 points.  <a href="http://en.wikipedia.org/wiki/Standard_deviation">Standard deviation</a> is simply a measure of how much numerical values differ from each other.  Any sudden spike bumps the standard deviation.   We can then simply set a threshold on the deviation.  Fairly trivial to set up, but has been highly effective for us.

<br/>

<br/>You do need to manually declare what is an acceptable standard deviation value to be compared against, which you will typically deduce from previous data.  This can be annoying until you build an interface to speed up, or a tool to automate this step.

<br/>In fact, it's trivial to collect previous deviation data (e.g. from the same time of the day, yesterday, or the same time of the week, last week) and automatically use that to guide a threshold.  (<a href="http://bosun.org/">Bosun</a> - see the following section - has "band" and "graphiteBand" functions to assist with this).  This is susceptible to previous outliers, but you can easily select multiple previous timeframes to minimize this issue in practice.

<br/>

<a href="https://groups.google.com/forum/#!topic/it-telemetry/Zb2H4DP6qtk">it-telemetry thread</a>

<br>

<br>

So without requiring fancy anomaly detection, machine learning, advanced math, or event processing, we are able to reliably detect faults using simple, familiar tools.  Some basic statistical concepts (standard deviation, moving average, etc) are a must, but nothing that requires getting a PhD.  In this case I've been using <a href="http://graphite.readthedocs.org/en/0.9.10/functions.html#graphite.render.functions.stdev">Graphite's stdev function</a> and <a href="http://vimeo.github.io/graph-explorer/">Graph-Explorer's</a> alerting feature to manage these kinds of rules, but it doesn't allow for a very practical iterative workflow, so the non-trivial rules will be going into <a href="http://bosun.org/">Bosun</a>.

<br/>BTW, you can also <a href="http://obfuscurity.com/2012/05/Polling-Graphite-with-Nagios">use a script to query Graphite from a Nagios check and do your logic</a>

<br/>

<br/>

<br/>

  

<!--

divideSeries(stdev(avg(keepLastValue(collectd.dfvimeopweb*.cpu.*.cpu.idle)),10),avg(keepLastValue(collectd.dfvimeopweb*.cpu.*.cpu.idle)))



why keepLastValue?

* sumSeries -> none counts as 0, so you can experience big drops which would trigger anomaly detection or failover

* averageSeries -> effectively ignores none values, so your accuracy can drop a lot in light of none values.



of course this masks when your monitoring breaks, so you still need something else to detect anomalies in the "out-of-date-ness" of your points.

-->



<h2>Workflow is key.  A closer look at bosun</h2>

One of the reasons we've been chasing self-learning algorithms is that we have lost faith in the feasibility of a more direct approach.  We can no longer imagine building and maintaining alerting rules because we have no system that provides powerful alerting, helps us keep oversight and streamlines the process of maintaining and iteratively developing alerting.

<br/>I recently discovered <a href="http://bosun.org/">bosun</a>, an alerting frontend ("IDE") by Stack Exchange, <a href="https://www.usenix.org/conference/lisa14/conference-program/presentation/brandt">presented at Lisa14</a>.  I highly recommend watching the video.  They have identified various issues that made alerting a pain, and built a solution that makes human-controlled alerting much more doable.  We've been using it for a month now with good results (I also gave it support for Graphite).



I'll explain its merits, and it'll also become apparent how this ties into some of the things I brought up above:

<img style="float:left; margin:35px;" src="http://bosun.org/public/ss_rule_timeline.png" width="15%">

<ul>

<li>in each rule you can query any data you need from any of your datasources (currently graphite, openTSDB, and elasticsearch).  You can call various <a href="http://bosun.org/configuration.html">functions, boolean logic, and math</a>.  Although it doesn't expose you a full programming language, the bosun language as it stands is fairly complete, and can be extended to cover

new needs.  You choose your own alerting granularity (it can automatically instantiate alerts for every host/service/$your_dimension/... it finds within your metrics, but you can also trivially aggregate across dimensions, or both).  This makes it easy to create advanced alerts that cover a lot of ground, making sure you don't get overloaded by multiple smaller alerts.  And you can incorporate data of other entities within the system, to simply make better alerting decisions.</li>

<li>you can define your own templates for alert emails, which can contain any html code.  You can trivially plot graphs, build tables, use colors and so on.  Clear, context-rich alerts which contain all information you need!</li>

<li>As alluded to, the bosun authors spent a lot of time <a href="https://www.usenix.org/conference/lisa14/conference-program/presentation/brandt">thinking about, and solving</a> the workflow of alerting.  As you work on advanced fault detection and alerting rules you need to be able to see the value of all data (including intermediate computations) and visualize it.  Over time, you will iteratively adjust the rules to become better and more precise.  Bosun supports all of this.  You can execute your rules on historical data and see exactly how the rule performs over time, by displaying the status in a timeline view and providing intermediate values.  And finally, you can see how the alert emails will be rendered <i>as you work on the rule and the templates</i></li>

</ul>



The <a href="http://bosun.org/examples.html">examples</a> section gives you an idea of the things you can do.

<br/>I haven't seen anything solve a pragmatic alerting workflow like bosun (hence their name "alerting IDE"), and its ability to not hold you back as you work on your alerts is refreshing. Furthermore, the built-in processing functions are very <b>complimentary to graphite</b>:

Graphite has a decent API which works well at aggregating and transforming one or more series into one new series; the bosun language is great at reducing series to single numbers, providing boolean logic, and so on, which you need to declare alerting expressions.  This makes them a great combination.

<br/>Of course Bosun isn't perfect either.  Plenty of things can be done to make it (and alerting in general) better.  But it does exemplify many of my points, and it's a nice leap forward in our monitoring toolkit.



<h2>Conclusion</h2>

Many of us aren't ready for some of the new technologies, and some of the technology isn't - and perhaps never will be - ready for us.

As an end-user investigating your options, it's easy to get lured in a direction that promotes over-complication and stimulates your inner scientist but just isn't realistic.

<br/>Taking a step back, it becomes apparent we <b>can</b> setup automated fault detection.  But instead of using machine learning, use metadata, instead of trying to come up with all-encompassing holy grail of math, use several rules of code that you prototype and iterate over, then reuse for similar cases.  Instead of requiring a paradigm shift, use a language you're familiar with.  Especially by polishing up the workflow, we can make many "manual" tasks much easier and quicker.  I believe we can keep polishing up the workflow, distilling common patterns into macros or functions that can be reused, leveraging metric metadata and other sources of truth to configure fault detection, and perhaps even introducing "metrics coverage", akin to "code coverage": verify how much, and which of the metrics are adequately represented in alerting rules, so we can easily spot which metrics have yet to be included in alerting rules.  I think there's a lot of things we can do to make fault detection work better for us, but we have to look in the right direction.



<h2>PS: leveraging metrics 2.0 for anomaly detection</h2>

In my last <a href="https://www.usenix.org/conference/lisa14/conference-program/presentation/plaetinck">metrics 2.0 talk, at LISA14</a> I explored a few ideas on leveraging metrics 2.0 metadata for alerting and fault detection, such as automatically discovering error metrics across the stack, getting high level insights via tags, correlation, etc. If you're interested, it's in the video from 24:55 until 29:40

<br/>

<br/>

<center>

<img src="http://dieter.plaetinck.be/files/metrics20-alerting.png" width="50%">

</center>



<!--

It's not about alerts anyway.



alerts are an immensely crude approach to raising operator awareness.

They are basically boolean: either they interrupt your workflow or they don't.  There's no in between.

Yes, you can just check your alert emails "once in a while", but then realize that after an email or text is sent,

there is no way to update them with new information.  Which is really limiting once you start thinking about it.

Updates have to be provided via new "alerts", or they are available in the monitoring interface but there's no way to tell

by just glancing at your alert overview.  You might be looking at very out of date information.

-> only sent alerts for critical things.

-->
