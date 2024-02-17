## Dieterblog

public directory = live on https://dieter.plaetinck.be

Lots of legacy html content (originally migrated from drupal, pyblosxom). It used to have manually declared summaries, but I took those out (from the html) because:

* https://github.com/gohugoio/hugo/issues/6686: html content does not include summary, whereas md content does
* https://github.com/gohugoio/hugo/issues/6513: syntax highlighting, video embeds break when using summary dividers in html content
* https://github.com/gohugoio/hugo/issues/8910: other summary rendering issues. not sure if this affects us

This version of the blog doesn't use summaries anyway.

TODO: static files were introduced in bulk, may want to optimize this..
 
 blog checklist:
	web and rss only new posts
	rss works, shows full articles, and we advertise in the source code
	comments still load
	post -> posts redirect
	make profiles work like in lekh
	check pagespeed errors https://github.com/hugo-sid/hugo-blog-awesome
	for now, just copied all files to static dir.. think about this
	update talks
new bio
lucky enough that i was able to hire many smart engineers that could take on or rewrite my code before i got too burnt-out

grep dietertest
posthog integration