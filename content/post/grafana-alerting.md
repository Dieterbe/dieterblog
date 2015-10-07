+++
title = "Alerting in Grafana"
date = "2015-09-02T19:25:02+03:00"
tags = ["golang", "monitoring"]
draft = true
+++

# Who am I ?

Done a lot of ops and data processing, but at Vimeo, got really into monitoring where I could combine my love for both

* Graph-Explorer, metrics 2.0
* graphite-ng, carbon-relay-ng
* anthracite
* graphite-influxdb, influx-cli, whisper-to-influxdb
* bosun graphite

Wanted to focus my efforts and find a team to work on open source monitoring fulltime.
Spoke to tens of companies over the course of about 2 years.
Raintank was by far the most interesting company.  wanted open source monitoring and wanted to work from anywhere, strong resonance and good fit with team.
Joined in early 2015.


# Why alerting inside of grafana?
i.e. why not a dedicated alerting tool? a lot of people advocate "let each tool do what it does best", i.e. a dashboarding program and an alerting program
[ note: as i will show later we don't re-invent the wheel, grafana focus on alert configuration and viz, existing tools can take care of execution]
- manage viz and alerting in one place -> streamlined experience
- leverage existing grafana capabilities for viz data when defining rules, annotations for events, markers for timeranges, etc

many people advocate *composability* and end up implementing all kinds of tools that are not very *compatible*: Different paradigms, concepts, poor API's.
I prefer stronger integration. can still be decoupled, on an ops level, but strongly aligned concepts and API's.


# What makes grafana great?
I have written and worked on graphite dashboards (GE), alerting systems (GE alerting, bosun) and yet think Grafana is the best base to build an alerting feature on.
Here is why.

* Integration
 - access to most tsdb's, even things that aren't really designed as TSDB, but still commonly used as one (ES, mysql, postgresql)
 - [note: i'm deliberately not mentioning here that grafana's tsdb support is currently all in js,
    and for alerting execution you need something like Go. but still it's good for viz, settings, ... which we are focusing on]
* Power
 - most advanced dashboard. <add some features/screenshots here>
* Ux
 - tens of graphite dashboards. Giraffe, Graph-Explorer, Gdash, descartes.
 - some of those are pretty powerful but Grafana's user experience is one of a kind
 - the reason it took off so well. TODO: add some take-off charts here
* Openness
 - raintank contributes heavily, but has no control over the project or its roadmap. TODO: copyright? assigned to contributor? grafana project? raintank? would be nice to mention
 - development in the open
 - community input: voting in tickets (note: do we encourage this?) and surveys

# our approach
 - most common workflow: once data is visualized, we want to set alerts. it's a natural extension of the flow
 - focus on alerting *configuration* from inside panels: streamlined workflow. instant feedback
 - 2nd: viz of alerting state over time. many pieces already there (annotations) and flot features like markings. TODO: add mockup here.
 - really excited about the attention to UX we can give. Torkel has always done well and Matt is our dedicated UX person who can give this all he's got.

# integration:

 - export configuration data via our API to your execution software of choice.
   - https://github.com/arachnys/cabot
   - https://github.com/scobal/seyren
   - http://bosun.org/
   - ...
  - all of these essentially just execute expressions and deal with their outcomes

# batteries!
  - "batteries included, but removable"
  - hassle free, simple handler based on bosun libraries.


# conclusion
  - reiterate from before: strong integration. power of your alerting app of choice, while having a great viz driven work flow, workflow is what grafana excels at.
  - composability requires compatibility -> strong API for consuming alert defs, let's build a community around it.
  - prototype in grafana 2.x ?


# note: some thoughts / musings i have not included in this talk. not sure if i should / if it's a good fit:

* specifics of how it'll look like
* how an integration of an anomaly detection based system could look like (grafana as frontend for kale?)
* how bosun workflows could look like (much better), once there is better integration with grafana.
* pro's and con's of stream processing
* why i think bosun is great (iterative development, data querying, rich language, ...), and a great complement to grafana.
* many subtle issues
  * how do rules work when series are rendered with stacking
  * graphite broken sum with nulls behavior (sum(12+null+null) = 12 -> dangerously inaccurate results at the last timestamp)
* prior work at http://dieter.plaetinck.be/post/practical-fault-detection-alerting-dont-need-to-be-data-scientist/ and
  http://dieter.plaetinck.be/post/practical-fault-detection-on-timeseries-part-2/
  which has some interesting points:
  * restricting to pure math cripples our ability to detect faults. there is a place for code in alerting logic
  * machine learning has a place, but it's a very hard mechanism, and will never work right. there are much more obvious and easy tactics to be employed.
  * next-gen approaches that could be tremendously powerful, but we are not tackling because we're trying to get the basics right:
    classification via metrics metadata. leveraging data from config management, cluster awareness/load balancers, event management, etc.

* much power from thresholds on graphite api, not so much power from non-graphite systems. (grafana's own summary functions? graphite-ng?)
* gradually exposing more power of systems like bosun, through an easy grafana UX. (but also means losing "generic plugging interface" advantage)
* a few ways in which grafana alerting will be better than competition
  - viz and alerting same interface (<> datadog)
  - manual threshold sliders as main interface element, it's not about changing threshold numbers.
