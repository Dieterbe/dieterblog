+++
title = "Histograms in statsd, and graphing them over time with graphite."
date = "2012-11-07T18:45:11-04:00"
tags = ["devops", "monitoring", "perf"]
+++
<p>

I submitted a pull request to statsd which adds <a href="https://github.com/etsy/statsd/pull/162">histogram support</a>.

<img style="float:left;margin:0 5px 0 0;" src="/files/Black_cherry_tree_histogram.svg.png" alt="Example histogram, from Wikipedia"/>

<br/>(refresher: a histogram is [a visualization of] a frequency distribution of data,

paraphrasing your data by keeping frequencies for entire classes (ranges of data).

<a href="http://en.wikipedia.org/wiki/Histogram">histograms - Wikipedia</a>)

<br/>It's commonly documented how to plot single histograms, that is a 2D diagram consisting of rectangles whose

<ul>

<li>area is proportional to the frequency of a variable</li>

<li>whose width is equal to the class interval</li>

</ul>

Class intervals go on x-axis, frequencies on y-axis.

<br/>

<br/>

Note: histogram class intervals are supposed to have the same width.

<br/>My implementation allows arbitrary class intervals with potentially different widths,

as well as an upper boundary of infinite.

</p>

<h4>Plotting histograms.. over time</h4>

<!--more-->

<p>

We want to plot histograms over time, and not just for a few select points in time (in which case you can just make several histograms),

but a contiguous range of time, preferably through graphite's 2D graphs cause graphite is neat and common enough.

<br/>Time goes on x-axis, that's pretty much a given.  So I'm trying to explore ways to visualize both class intervals as well as frequencies on the y-axis.

</p>

<p>The example I'll use are page rendering timings, condensed into classes with upper boundaries of 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50 and infinite seconds</p>

<p>

Tips and notes:

<ul>

<li>

the histogram implementation stores absolute frequencies, but it's easy to get relative frequencies in percent, like so:

{{< highlight "javascript" "style=default" >}}<![CDATA[

target=scale(divideSeries(stats.timers.<your_metric>.bin_*,stats.timers.render_time.count),100)

]]>{{< /highlight >}}

</li>

<li>I'll be using relative frequencies here because it normalizes the scale of the y-axis</li>

<li>In this use case each class has a notion of desirability (<i>low render time good, high render time bad</i>),

<br/>I think it makes sense to use color to represent this.  This extends to a lot of operational metrics which one would be using histograms for.

<br/>(unlike non-software histograms that represent demographics or tree heights, where classes usually have nothing to do with desirability or quality).

<br/>As it turns out, it's fairly easy to programmatically compute colors between green and red in order to have mathematically correct "steps" of color.

<br/>However, <a href="http://stackoverflow.com/questions/340209/generate-colors-between-red-and-green-for-a-power-meter">Looks like HSV values are more suited

than RGB</a> but <a href="https://github.com/graphite-project/graphite-web/issues/93">

graphite doesn't support HSV (yet)</a> (although one could convert HSV to RGB).

Also <a href="http://vis4.net/blog/posts/goodbye-redgreen-scales/">it looks like

green-purple would be a better choice for people with color blindness</a>.  I haven't gone too far in this topic.

</li>

<li>Since I choose to go with color gradients, it means I better use stacked graphs, otherwise it would be too hard to distinguish which graph is what</li>

<li>None of this is restricted to timing data.  The metric type under which histograms are (and should be) implemented is called "timing", which is

a misleading name but <a href="https://github.com/etsy/statsd/issues/98">we're working on renaming it</a>.</li>

</ul>





<h4>First version</h4>

{{< highlight "javascript" "style=default" >}}<![CDATA[

http://localhost:9000/render/?height=300&

width=740&from=-24h&title=Render time histogram&

vtitle=relative frequency in %&yMax=100&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_01,stats.timers.render_time.count),100),'2FFF00'),'0.01')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_05,stats.timers.render_time.count),100),'64DD0E'),'0.05')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_1,stats.timers.render_time.count),100),'9CDD0E'),'0.1')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_5,stats.timers.render_time.count),100),'DDCC0E'),'0.5')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_1,stats.timers.render_time.count),100),'DDB70E'),'1')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_5,stats.timers.render_time.count),100),'FF6200'),'5')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_10,stats.timers.render_time.count),100),'FF3C00'),'10')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_50,stats.timers.render_time.count),100),'FF1E00'),'50')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_inf,stats.timers.render_time.count),100),'FF0000'),'inf')&

lineMode=slope&areaMode=stacked&drawNullAsZero=false&hideLegend=false

]]>{{< /highlight >}}

<img src="/files/rendertime-histogram.png" width="740" height="300" alt="rendertime histogram" />

<br/>Turns out we mainly see the vast majority that performs well, simply because with this way of rendering,

the higher the frequency of a class, the more prominent.  Bad values are hard to see because there's not many of them,

despite being more interesting.

A thought I had at this point was to make all "class bands" equally wide and use a green-to-red gradient to denote the frequency values,

or even just keep the current color assignments but rely on something like opacity to express frequencies. Alas, none of this is currently

possible with graphite, as far as I can tell.  Though I would like to explore this further.  Especially because I think it wouldn't be hard to implement

in graphite.

<br/>

<br/>

So, let's see what <i>can</i> be done right now.



<h4>Leaving out the smallest class</h4>

This adaption is basically the same as before, but leaves out the smallest class (which took most space), this way

the other bands are a bit more visible but the effect isn't as clear as we want.

{{< highlight "javascript" "style=default" >}}<![CDATA[

http://localhost:9000/render/?height=300&

width=740&from=-24h&title=Render time histogram&

vtitle=relative frequency in %, leaving out first class&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_05,stats.timers.render_time.count),100),'64DD0E'),'0.05')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_1,stats.timers.render_time.count),100),'9CDD0E'),'0.1')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_5,stats.timers.render_time.count),100),'DDCC0E'),'0.5')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_1,stats.timers.render_time.count),100),'DDB70E'),'1')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_5,stats.timers.render_time.count),100),'FF6200'),'5')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_10,stats.timers.render_time.count),100),'FF3C00'),'10')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_50,stats.timers.render_time.count),100),'FF1E00'),'50')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_inf,stats.timers.render_time.count),100),'FF0000'),'inf')&

lineMode=slope&areaMode=stacked&drawNullAsZero=false&hideLegend=false

]]>{{< /highlight >}}

<img src="/files/rendertime-histogram-leaving-out-first-class.png" width="740" height="300" alt="rendertime histogram leaving out first class" />



<h4>Per-band scaling</h4>

Finally, the bigger the values represented by each class the more we inflate the band,

so the more problematic cases become more visible, despite having a lower frequency.

{{< highlight "javascript" "style=default" >}}<![CDATA[

http://localhost:9000/render/?height=300&

width=740&from=-24h&title=Render time histogram&

vtitle=rel. freq with scale adjustment per band&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_01,stats.timers.render_time.count),0.01),'2FFF00'),'0.01')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_05,stats.timers.render_time.count),0.04),'64DD0E'),'0.05')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_1,stats.timers.render_time.count),0.05),'9CDD0E'),'0.1')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_0_5,stats.timers.render_time.count),0.4),'DDCC0E'),'0.5')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_1,stats.timers.render_time.count),0.5),'DDB70E'),'1')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_5,stats.timers.render_time.count),4),'FF6200'),'5')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_10,stats.timers.render_time.count),5),'FF3C00'),'10')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_50,stats.timers.render_time.count),40),'FF1E00'),'50')&

target=alias(color(scale(divideSeries(stats.timers.render_time.bin_inf,stats.timers.render_time.count),60),'FF0000'),'inf')&

lineMode=slope&areaMode=stacked&drawNullAsZero=false&hideLegend=false

]]>{{< /highlight >}}

<img src="/files/rendertime-histogram-higher-focus-for-higher-class-interval.png" width="740" height="300" alt="rendertime histogram with higher focus for higher class interval" />

<br/>I started off by scaling each band by the width of the class interval.  This is actually more arbitrary than it may seem.

<br/>The point is that now it's easier to spot acute as well as long-standing problems, but note you can't really read statistics from this graph because of the per-band scaling.

<br/>Note also that outliers contribute to the outer band(s) and are given as much focus as non-outliers in the same bands.

In a system over which you have no complete control (i.e. if you were graphing histograms of time until first byte or page loaded at client,

where you rely on the internet as a transport) it makes sense to give less attention to outliers and focus on optimizing for as many users as possible,

I think it there's no reliable way to subtract outliers from the upper bands and you should also graph averages and percentiles and understand what each

graph does.

But anyway here I want to include outliers, because they represent latencies we can fix.



<h4>Final notes</h4>

While the tools we have are by no means perfect, I'm seeing gradual improvement in the monitoring space.  This work is only a small piece

of the puzzle. The rendering of histograms can be improved but at this point I think they are good enough to be usable. The real challenge is

putting in place automated trending, anomaly detection and alerting.  If we can figure that out, there's less need to be looking at graphs in the first place.
