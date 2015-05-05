+++
title = "Practical fault detection on timeseries part 2: first macros and templates"
date = "2015-04-27T09:05:02-04:00"
tags = ["devops", "monitoring"]
+++
It had an example of a simple but effective approach to find sudden spikes (peaks and drops) within fluctuating time series.

This post explains the continuation of that work and provides you the means to implement this yourself with minimal effort.

I'm sharing with you:

<ul>

<li><a href="http://bosun.org">Bosun</a> macros which detect our most common not-trivially-detectable symptoms of problems</li>

<li>Bosun notification template which provides a decent amount of information</li>

<li><a href="http://www.grafana.org">Grafana</a> and <a href="http://vimeo.github.io/graph-explorer/">Graph-Explorer</a> dashboards and integration for further troubleshooting</li>

</ul>

We reuse this stuff for a variety of cases where the data behaves similarly and I suspect that you will be able to apply this to a bunch of your monitoring targets as well.

<!--more-->

<h2>Target use case</h2>

As in the previous article, we focus on the specific category of timeseries metrics driven by user activity.

Those series are expected to fluctuate in at least some kind of (usually daily) pattern, but is expected to have a certain smoothness to it. Think web requests per second or uploads per minute.   There are a few characteristics that are considered faulty or at least worth our attention:



<table>

<tr>

  <td><img src="/files/practical-alerting-timeseries-good.png"/></td>

  <td><img src="/files/practical-alerting-timeseries-bad-spikes.png"/></td>

  <td><img src="/files/practical-alerting-timeseries-bad-erratic.png"/></td>

  <td><img src="/files/practical-alerting-timeseries-bad-timeseries-median-drop.png"/></td>

</tr>

<tr>

  <td><b style="color: green;">looks good</b><br/>consistent pattern<br/>consistent smoothness</td>

  <td><b style="color: red;">sudden deviation (spike)</b><br/>Almost always something broke or choked.<br/>could also be pointing up. ~ peaks and valleys</td>

  <td><b style="color: red;">increased erraticness</b><br/>Sometimes natural<br/>often result of performance issues</td>

  <td><b style="color: red;">lower values than usual</b> (in the third cycle)<br/>Often caused by changes in code or config, sometimes innocent.  But best to alert operator in any case [*]</td>

</tr>

</table>



<br/>

[*] Note that some regular patterns can look like this as well. For example weekend traffic lower than weekdays, etc.  We see this a lot.

<br/>The illustrations don't portray this for simplicity.   But the alerting logic below supports this just fine by comparing to same day last week instead of yesterday, etc.





<h2>Introducing the new approach</h2>



The <a href="/practical-fault-detection-alerting-dont-need-to-be-data-scientist.html">previous article</a> demonstrated using graphite to compute standard deviation.

This let us alert on the erraticness of the series in general and as a particularly interesting side-effect, on spikes up and down.

The new approach is more refined and concrete by leveraging some of bosun's and Grafana's strengths.  We can't always detect the last case above via erraticness checking (a lower amount may be introduced gradually, not via a sudden drop) so now we monitor for that as well, covering all cases above.



We use 

<ul>

<li>Bosun macros which encapsulate all the querying and processing</li>

<li>Bosun template for notifications</li>

<li>A generic Grafana dashboard which aids in troubleshooting</li>

</ul>

We can then leverage this for various use cases, as long as the expectations of the data are as outlined above.

We use this for web traffic, volume of log messages, uploads, telemetry traffic, etc.

For each case we simply define the graphite queries and some parameters and leverage the existing mentioned Bosun and Grafana configuration.

<br/>

<p>

The best way to introduce this is probably by showing how a notification looks like:

<br/>

<center>

<a href="/files/practical-alerting-dm-notification.png"><img height="600px" src="/files/practical-alerting-dm-notification.png"/></a>

<br/>

(image redacted to hide confidential information

<br/>the numbers are not accurate and for demonstration purposes only)

</center>

<p>

As you can tell by the sections, we look at some global data (for example "all web traffic", "all log messages", etc), and also

by data segregated by a particular dimension (for example web traffic by country, log messages by key, etc)

<br/>

To cover all problematic cases outlined above, we do 3 different checks:

(note, everything is parametrized so you can tune it, see further down)

<ul>

<li>Global volume: comparing the median value of the last 60 minutes or so against the corresponding 60 minutes last week and expressing it as a "strength ratio".  Anything below a given threshold such as 0.8 is alerted on</li>

<li>Global erraticness. To find all forms of erraticness (increased deviation), we use a refined formula.  See details below.  A graph of the input data is included so you can visually verify the series</li>

<li>On the segregated data: compare current (hour or so) median against median derived from the corresponding hours during the past few weeks, and only allow a certain amount of standard deviations difference</li>

</ul>



If any, or multiple of these conditions are in warning or critical state, we get 1 alert that gives us all the information we need.

<br/>

Note the various links to GE (Graph-Explorer) and Grafana for timeshifts.

The Graph-Explorer links are just standard GEQL queries, I usually use this if i want to be easily manage what I'm viewing (compare against other countries, adjust time interval, etc) because that's what GE is really good at.

The timeshift view is a Grafana dashboard that takes in a Graphite expression as a template variable, and can hence be set via a GET parameter by using the url  <pre>http://grafana/#/dashboard/db/templatetimeshift?var-patt=expression</pre>

It shows the current past week as red dots, and the past weeks before that as timeshifts in various shades of blue representing the age of the data. (darker is older).

<br/>

<br/>



<a href="/files/practical-alerting-screenshot-template-timeshift.png"><img width="50%" src="/files/practical-alerting-screenshot-template-timeshift.png" /></a>

<br/>

This allows us to easily spot when traffic becomes too low, overly erratic, etc as this example shows:

<br/>

<br/>



<a href="/files/practical-alerting-timeshift-use.png"><img width="50%" src="/files/practical-alerting-timeshift-use.png" /></a>

<br/>



<h2>Getting started</h2>



Note: I Won't explain the details of the bosun configuration.  Familiarity with bosun is assumed.  The <a href="http://bosun.org/">bosun documentation</a> is pretty complete.

<br/>

<br/>

<a href="https://gist.github.com/Dieterbe/d1892fa0b4454b892216">Gist with bosun macro, template, example use, and Grafana dashboard definition</a>.  Load the bosun stuff in your bosun.conf and import the dashboard in Grafana.

<br/>

<br/>

The pieces fit together like so:



<ul>

<li>The alert is where we define the graphite queries, the name of the dimension segregated by (used in template), how long the periods are, what the various thresholds are and the expressions to be fed into Grafana and Graph-Explorer.

<br/>

It also lets you set an importance which controls the sorting of the segregated entries in the notification (see screenshot).  By default it is based on the historical median of the values but you could override this.  For example for a particular alert we maintain a lookup table with custom importance values.</li>

<li>The macros are split in two:

<ol>

<li>dm-load loads all the initial data based on your queries and computes a bunch of the numbers.</li>

<li>dm-logic does some final computations and evaluates the warning and critical state expressions.</li>

</ol>

They are split so that your alerting rule can leverage the returned tags from the queries in dm-load to use a lookup table to set the importance variable or other thresholds, such as s_min_med_diff on a case-by-case basis, before calling dm-logic.

<br/>

We warn if one or more segregated items didn't meet their median requirements, and if erraticness exceeds its threshold (note that the latter can be disabled).

<br>Critical is when more than the specified number of segregated items didn't meet their median requirements, the global volume didn't meet the strength ratio, or if erraticness is enabled and above the critical threshold.

</li>

<li>The template is evaluated and generates the notification like shown above</li>

<li>Links to Grafana (timeshift) and GE are generated in the notification to make it easy to start troubleshooting</li>

</ul>



<h2>Erraticness formula refinements</h2>

<img style="float: right; margin: 45px;" width="30%" src="/files/practical-alerting-notes-cleaned-small.jpg" />

You may notice that the formula has changed to

<pre>

(deviation-now * median-historical) / ( (deviation-historical * median-now) + 0.01)

</pre>

<ul>

<li>Current deviation is compared to an automatically chosen historical deviation value (so no more need to manually set this)</li>

<li>Accounts for difference in volume: for example if traffic at any point is much higher, we can also expect the deviation to be higher.  With the previous formula we would have cases where in the past the numbers were very low, and naturally the deviation then was low and not a reasonable standard to be held against when traffic is higher, resulting in trigger happy alerting with false positives.

<br/>Now we give a fair weight to the deviation ratio by making it inversely proportional to the median ratio</li>

<li>The + 0.01 is to avoid division by zero</li>

</ul>



<!--

streak covers cases where values are very low so that stdev is in the same order (like low volume logs) and we can't properly use the erraticness or x-deviations. for example logs with very little traffic, datapoints representing healthy traffic can look like (1, 2, 0, 3, 1, ..)

although i think the ratio of medians (median_now/median_then) should work just as well as streak



<img src="/files/practical-alerting-low-values-zeroes.png" />

<img src="/files/practical-alerting-low-values-low.png" />

-->



<h2>Still far from perfect</h2>

While this has been very helpful to us, I want to highlight a few things that could be improved.

<ul>

<li>With these alerts, you'll find yourself wanting to iteratively fine tune the various parameters and validate the result of your changes by comparing the status-over-time timeline before and after the change.  While Bosun already makes iterative development easier and lets you <a href="http://bosun.org/public/ss_rule_timeline.png">run test rules against old data and look at a the status over time</a>, the interface could be improved by

<ol>

<li><a href="https://github.com/bosun-monitor/bosun/issues/636">showing timeseries (with event markers where relevant) alongside the status visualization</a>, so you have context to interpret the status timeline</li>

<li>routinely building <a href="https://github.com/grafana/grafana/pull/1569">a knowledge base of time ranges annotated with a given state for a given alerting concern, which would help in validating the generated status timeline, both visually and in code.  We could compute percentage of issues found, missed, etc</a>. "unit tests for alerting" my boss called it.</li>

</ol>

</li>

<li>Template could be prettier.  In particular the plots often don't render very well.  We're looking into closer Grafana-Bosun integration so I think that will be resolved at some point.</li>

<li><a href="https://github.com/bosun-monitor/bosun/issues/719">Current logic doesn't take past outages into account. "just taking enough periods in graphiteBand()" helps alleviate it mostly, but it's not very robust</a></li>

<li>See that drop in the screenshot a bit higher up? That one was preceded by a code deploy event in anthracite which made some changes where a drop in traffic was actually expected.  Would love to be able to mark stuff like this in deploys (like putting in the commit message something like "expect 20-50 drop" and have the monitoring system leverage that.</li>

</ul>



<h2>In conclusion</h2>

I know many people are struggling with poor alerting rules (static thresholds?)

<br/>As I explained in the previous article I fondly believe that the commonly cited solutions (anomaly detection via machine learning) are a very difficult endeavor and results can be achieved much quicker and more simpler.

<br/>While this only focuses on one class of timeseries (it won't work on diskspace metrics for example) I found this class to be in the most dire need of better fault detection.  Hopefully this is useful to you. Good luck and let me know how it goes!


