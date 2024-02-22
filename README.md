## Dieterblog

This is live on https://dieter.plaetinck.be

Lots of legacy html content (originally migrated from drupal, pyblosxom). It used to have manually declared summaries, but I took those out (from the html) because:

* https://github.com/gohugoio/hugo/issues/6686: html content does not include summary, whereas md content does
* https://github.com/gohugoio/hugo/issues/6513: syntax highlighting, video embeds break when using summary dividers in html content
* https://github.com/gohugoio/hugo/issues/8910: other summary rendering issues. not sure if this affects us

This version of the blog doesn't use summaries anyway.

before advertising twitter:
* favicon

post release checklist:
* 404 links
* 404 monitoring?
* check pagespeed errors https://github.com/hugo-sid/hugo-blog-awesome
* re-introduce tags showing on individual posts, maybe on titles too. and better showing on /tags ?
* re-add link to website on social profiles


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
improve loading time: fix DNS and CDN TTL.
https://pagespeed.web.dev/analysis/https-dieter-plaetinck-be/w8rtxmnjst?form_factor=mobile


fix intermezzo style.
with previous theme, it was this:
/* from previous twentyfourteen theme. not used anymore */
.intermezzo {
	background-color:#e6f7ff;
	color:#00344d;
	padding:20px;
	border-radius:8px;
}
