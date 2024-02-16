+++
title = "Practical fault detection: redux. Next-generation alerting now as presentation"
date = "2016-12-10T19:13:03+00:00"
tags = ["monitoring", "devops"]
+++

This summer I had the opportunity to present my [practical fault detection](/post/practical-fault-detection-alerting-dont-need-to-be-data-scientist/) concepts and [hands-on approach](http://dieter.plaetinck.be/post/practical-fault-detection-on-timeseries-part-2/) as conference presentations.

First at [Velocity](http://conferences.oreilly.com/velocity/vl-ca-2016/public/schedule/detail/49335) and then at [SRECon16 Europe](https://www.usenix.org/conference/srecon16europe/program/presentation/plaetinck).  The latter page also contains the recorded video. 

![image](http://dieter.plaetinck.be/files/poor-mans-fault-detection.png)

If you're interested at all in tackling non-trivial timeseries alerting use cases (e.g. working with seasonal or trending data) this video should be useful to you.

It's basically me trying to convey in a concrete way why I think the big-data and math-centered algorithmic approaches come with a variety of problems making them unrealistic and unfit, 
whereas the real breakthroughs happen when tools recognize the symbiotic relationship between operators and software, and focus on supporting a collaborative, iterative process to managing alerting over time. There should be a harmonious relationship between operator and monitoring tool, leveraging the strengths of both sides, with minimal factors harming the interaction.
From what I can tell, [bosun](http://bosun.org/) is pioneering this concept of a modern alerting IDE and is far ahead of other alerting tools in terms of providing high alignment between alerting configuration, the infrastructure being monitored, and individual team members, which are all moving targets, often even fast moving.  In my experience this results in high signal/noise alerts and a happy team.
(according to Kyle, the bosun project leader, my take [is a useful one](https://twitter.com/kylembrandt/status/804409406846746624))

That said, figuring out the tool and using it properly has been, and remains, rather hard.  I know many who rather not fight the learning curve.  Recently the bosun team has been making strides at making it easier for newcomers -
e.g. [reloadable configuration](https://github.com/bosun-monitor/bosun/pull/1817) and [Grafana integration](https://grafana.net/plugins/bosun-app) - but there is lots more to do.
Part of the reason is that some of the UI tabs aren't implemented for non-opentsdb databases and integrating Graphite for example into the tag-focused system that is bosun, is bound to be a bit weird.  (that's on me)

For an interesting juxtaposition, we released [Grafana v4 with alerting functionality](http://docs.grafana.org/guides/whats-new-in-v4/) which approaches the problem from the complete other side: simplicity and a unified dashboard/alerting workflow first, more advanced alerting methods later.  I'm doing what I can to make the ideas of both projects converge, or at least make the projects take inspiration from each other and combine the good parts. (just as I hope to bring the ideas behind [graph-explorer](http://vimeo.github.io/graph-explorer/) into Grafana, eventually...)

Note:
One thing that somebody correctly pointed out to me, is that I've been inaccurate with my terminology.
Basically, machine learning and anomaly detection can be as simple or complex as you want to make it. In particular, what we're doing with our alerting software (e.g. bosun) can rightfully also be considered machine learning, since we construct models that learn from data and make predictions.  It may not be what we think of at first, and indeed, even a simple linear regression is a machine learning model.  So most of my critique was more about the big data approach to machine learning, rather than machine learning itself.  As it turns out then the key to applying machine learning successfully is tooling that assists the human operator in every possible way, which is what IDE's like bosun do and how I should have phrased it, rather than presenting it as an alternative to machine learning.

