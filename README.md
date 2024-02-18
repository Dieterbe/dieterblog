## Dieterblog

public directory = live on https://dieter.plaetinck.be

Lots of legacy html content (originally migrated from drupal, pyblosxom). It used to have manually declared summaries, but I took those out (from the html) because:

* https://github.com/gohugoio/hugo/issues/6686: html content does not include summary, whereas md content does
* https://github.com/gohugoio/hugo/issues/6513: syntax highlighting, video embeds break when using summary dividers in html content
* https://github.com/gohugoio/hugo/issues/8910: other summary rendering issues. not sure if this affects us

This version of the blog doesn't use summaries anyway.

release checklist:
* web and rss only new posts / confirm GUID's. try on planet grep with 1.

before advertising twitter:
* favicon
* push new blog post
* posthog integration
* comma integration

post release checklist:
* 404 links
* advertise RSS in the source code // something like old site ?     <link href="http://dieter.plaetinck.be/index.xml" rel="alternate" type="application/rss+xml" title="Dieter&#39;s blog" />
* check pagespeed errors https://github.com/hugo-sid/hugo-blog-awesome
* CDATA rendering


note: i have 2 (identical?) rss feeds (just title/url different)
http://localhost:1313/posts/index.xml
http://localhost:1313/index.xml

Later:
re-organize static files, maybe

old site used these URL's:
1. http://dieter.plaetinck.be/rss.xml # planet grep
2. http://dieter.plaetinck.be/post/index.xml # rss icon on page
3. http://dieter.plaetinck.be/index.xml # alternate link in html source

1 and 2 were identical. the 3rd one practically identical, just advertised a different alternate url, and had different title.