## Dieterblog

public directory = live on https://dieter.plaetinck.be

Lots of legacy html content (originally migrated from drupal, pyblosxom). It used to have manually declared summaries, but I took those out (from the html) because:

* https://github.com/gohugoio/hugo/issues/6686: html content does not include summary, whereas md content does
* https://github.com/gohugoio/hugo/issues/6513: syntax highlighting, video embeds break when using summary dividers in html content
* https://github.com/gohugoio/hugo/issues/8910: other summary rendering issues. not sure if this affects us

This version of the blog doesn't use summaries anyway.

release checklist:
* static files were introduced in bulk, may want to optimize this..
* web and rss only new posts / confirm GUID's. try on planet grep with 1.
* rss works, shows full articles
* post -> posts redirect

before advertising twitter and pushing new blog post:
* posthog integration
* comma integration

post release checklist:
* 404 links
* advertise RSS in the source code
* check pagespeed errors https://github.com/hugo-sid/hugo-blog-awesome
* CDATA rendering


note: i have 2 (identical?) rss feeds (just title/url different)
http://localhost:1313/posts/index.xml
http://localhost:1313/index.xml

