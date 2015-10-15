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
* http://dieter.plaetinck.be/tags/monitoring/

# quixotic

looked it up:
idealistic without regard to practicality - cool word. has typo

# raintank <3 grafana
Wanted to focus my efforts and find a team to work on open source monitoring fulltime.
Spoke to tens of companies over the course of about 2 years.
Raintank was by far the most interesting company.  wanted open source monitoring and wanted to work from anywhere, strong resonance and good fit with team.
Joined in early 2015.

# alerting number 1 requested feature
<survey wordcloud>

alerting is not just a little feature, it's an entire domain to be solved, just like viz
we have the chance to start from scratch.

tiers: viz | alerting

# who?
at raintank, people with technical, product and UX background
<community faces github>
we try to involve community and everyone is welcome to participate
we're always curious to hear concerns, requirements, goals, etc

though it does prove to be very hard, as the scope is extremely large
and we try to find an elegant solution that addresses the common problems
but not necessarily the edge cases


# idealized design
http://www.ida.liu.se/~steho87/und/htdd01/AckoffGuidetoIdealizedRedesign.pdf
don't improve parts, do system as a whole
http://knowledge.wharton.upenn.edu/article/idealized-design-how-bell-labs-imagined-and-created-the-telephone-system-of-the-future/
from old dial pad to touch tone, conference calls, mobile phones,  etc
sparked a chain of inventions
~ brainstorming

if we can do half as good as at&t did, i'm going to be thrilled.


# ux-driven
<img here>

# saying no
second system syndrome
quixotic
80/20
we learned we had to start saying no

# learning from Grafana
torkel: grafana rapidly powerful, but shoot yourself in the foot

#if you prevent people from doing stupid things, you also prevent them from doing smart things


#really really really hard
finding a balance between the approaches, under time pressure. startup not r&d lab

# going forward
prototype and iterate.
evolvable design



## i think this can be removed. but mention CCI later
# Why alerting in grafana?
# fear of the monolith
good integration
i.e. why not a dedicated alerting tool? a lot of people advocate "let each tool do what it does best", i.e. a dashboarding program and an alerting program.
i just think that model is too simplistic

# composable compatible integration

many people advocate *composability* and end up implementing all kinds of tools that are not very *compatible*: Different paradigms, concepts, poor API's.
I prefer stronger integration. can still be decoupled, on an ops level, but strongly aligned concepts and API's.

# Grafana: alert configuration & viz, *: alert execution, notifications, ...

- manage viz and alerting in one place -> streamlined experience
- leverage existing grafana capabilities for viz data when defining rules, annotations for events, markers for timeranges, etc


# Why Grafana?
I have written and worked on graphite dashboards (GE), alerting systems (GE alerting, bosun) and yet think Grafana is the best base to build an alerting feature on.
Here is why.

# Integration
 - access to most databases, even things that aren't really designed as TSDB, but still commonly used as one (ES, mysql, postgresql)
 - [note: i'm deliberately not mentioning here that grafana's tsdb support is currently all in js,
    and for alerting execution you need something like Go. but still it's good for viz, settings, ... which we are focusing on]
# Power through Ux
 - tens of graphite dashboards. Giraffe, Graph-Explorer, Gdash, descartes. grafana most powerful and best UX. reason it took off so well.
 - lot of groupndwork already in place. annotations, markings, tabs, ...
# 100% active open source
 - actively maintained
 - at raintank we try to support and improve grafana as much as we can, committed to keeping open source, has no copyright or ownership of grafana, it's an independent project
 - community input: github ticket activity and surveys

# Alerting workflow
 - most common workflow: once data is visualized, we want to set alerts. it's a natural extension of the flow
 - focus on alerting *configuration* from inside panels: streamlined workflow. instant feedback
 - maintain viz and alerting in same place
 - 2nd: viz of alerting state over time. many pieces already there (annotations) and flot features like markings. TODO: add mockup here.

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

