+++
title = "Interview with Matt Reiferson, creator of NSQ"
date = "2015-10-02T10:25:02+02:00"
tags = ["golang", "programming"]
+++

I'm a fan of the [NSQ](http://nsq.io/) message processing system written in golang.
I've studied the code, [transplanted its diskqueue code](/post/transplanting-go-packages-for-fun-and-profit/) into another project, and have used NSQ by itself.
The code is well thought out, organized and written.


Inspired by the book [coders at work](http://codersatwork.com/) and the [systems live](http://systemslive.org/) podcast,
I wanted to try something I've never done before: spend an hour talking to [Matt Reiferson](https://github.com/mreiferson) - the main author of NSQ - about software design and Go programming patterns,
and post the video online for whomever might be interested.

We talked about Matt's background, starting the NSQ project at Bitly as his first (!) Go project,
(code) design patterns in NSQ and the nsqd diskqueue in particular and the new [WAL](https://github.com/nsqio/nsq/pull/625) (write-ahead-log) approach in terms of design and functionality.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-X73gfrt8Qk" frameborder="0" allowfullscreen></iframe>
You can watch it [on youtube](https://www.youtube.com/watch?v=-X73gfrt8Qk)

Unfortunately, the video got cut a bit short.
But basically in the cut off part i asked about the new go internals convention that prevents importing packages that are in an internals subdirectory.
Matt wants to make it very clear that certain implementation details are not supported (by the NSQ team) and may change, whereas my take was that it's annoying
when i want to reuse code some I find in a project.
We ultimately both agreed that while a bit clunky, it gets the job done, and is probably a bit crude because there is also no proper package management yet.

I'ld like to occasionally interview other programmers in a similar way and post on my site later.

