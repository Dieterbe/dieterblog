+++
title = "Moved blog to hugo, fastly and comma"
date = "2015-07-02T16:35:02-07:00"
tags = ["golang"]
+++
* I noticed what a disservice I was doing my readers when I started monitoring my site using [litmus](http://www.raintank.io/litmus/).
  A dynamic website in python on a cheap linode... What do you expect?  So I now serve through [fastly](https://www.fastly.com/) and use a static site generator.
* [pyblosxom](http://pyblosxom.github.io/) was decent while it lasted.
  It can generate sites statically, but the project never got a lot of traction and is slowly fading out.  There were a bit too many moving parts, so ...
* I now use the [hugo](http://gohugo.io/) static site generator, which is powerful, quite complete and gaining momentum.
  Fast and simple to use.
* Should also keep an eye on the [caddy](https://caddyserver.com/) webserver since it has some nice things such as [git integration](https://caddyserver.com/docs/git) which should work well with hugo.
* Trying to get disqus going was frustrating.
  Self hosted options like [talkatv](https://github.com/talkatv/talkatv) and [isso](https://github.com/posativ/isso) were too complex, and [kaiju](https://github.com/spf13/kaiju) is just not there yet and also pretty complex.
  I wrote [comma](https://github.com/Dieterbe/comma) which is a simple comment server in Go.
  Everything I need in 100 lines of Go and 50 lines of javascript! Let me know if you see anything funky.
* [pyblosxom-to-hugo.py](https://github.com/Dieterbe/dieterblog/blob/master/pyblosxom-to-hugo.py) migrated all content.

