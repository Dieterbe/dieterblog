## reviving the blog.

have not been able to update it for years.

here's what we know:
* the last real website update was december 10, 2016 (commit 0d728c8854608d2f426e9db176b2d7f86023b270) so it must have used a hugo version from december 2016 or older
  (i probably had not updated hugo for a while)
  - I think it was v0.16 from june 2016 but I'm not sure. (https://github.com/gohugoio/hugo/releases/tag/v0.16)
  - Could also have been https://github.com/gohugoio/hugo/releases/tag/v0.17 from october 2016, or anything pre 0.16
  - Probably nothing later, as v0.18 was only on december 19 (though it's possible i published that last post a few weeks after writing/committing it, but unlikely)

* public-real contains the website that is live right now (last updated in december 2016)
* I'm quite sure that public-real was generated with this command:
  ```
  hugo --config config-prod.toml -d public-real
  ```
  It is possible that 3 years ago i may have made manual tweaks inside public-real after generating it with hugo, though it seems unlikely
* Today, I want to revive my blog and be able to add new content to it.
  To be able to do this, i should first be able to regenerate public-real from the current content (not meaningfully updated since 2016 as can be seen in git history), using a recent version of hugo.

  **So this is our main objective: regenerating the site with a recent hugo (but possibly tweaked config file) should not meaningfully change "public-real"**
  I'm especially concerned about the RSS feed. I've had issues in the past (not with hugo) where subtle changes to the generated feed caused all content to re-appear fresh for all users. Want to avoid this from happening again. (I don't fully understand/remember how it happened. perhaps the post id's changed).


## attempts to revive
### using latest hugo master on 30/12/2019
Compiled from 5509954c7e8b0ce8d5ea903b0ab639ea14b69acb

```
$ hugo version
Hugo Static Site Generator v0.63.0-DEV linux/amd64 BuildDate: unknown
$ hugo --config config-prod.toml -d public-prodcfg-master
Building sites … WARN 2019/12/30 11:47:21 Page.RSSLink is deprecated and will be removed in a future release. Use the Output Format's link, e.g. something like: 
    {{ with .OutputFormats.Get "RSS" }}{{ .RelPermalink }}{{ end }}
WARN 2019/12/30 11:47:21 Page.BaseFileName is deprecated and will be removed in a future release. Use .File.BaseFileName
WARN 2019/12/30 11:47:21 Page.URL is deprecated and will be removed in a future release. Use .Permalink or .RelPermalink. If what you want is the front matter URL value, use .Params.url

                   | EN   
+------------------+-----+
  Pages            | 218  
  Paginator pages  |   0  
  Non-page files   |   0  
  Static files     |  23  
  Processed images |   0  
  Aliases          |   0  
  Sitemaps         |   1  
  Cleaned          |   0  

Total in 159 ms

$ diff -r public-real public-prodcfg-master | wc -l
17744
```
The diff is huge. There's some benign looking changes (whitespace) and more problematic ones.
Tip: `git diff` is easier to work with then `diff -r` so for analyzing I run `rm -rf public-real && mv public-prodcfg-master public-real` and then use the git tools.

* these files getting removed:
```
404.html
post/emulating_two-dimensional_(or_even_multi-dimensional)_arrays_in_bash/index.html
post/practical-fault-detection-redux-next-generation-alerting/index.html 
```
* a bunch of content missing in index.html
* lots of changes in markup and content
* tags now lower case in html titles and page titles (harmless)


I'm pretty sure in the past i've noticed problems around the "more" content divider

### 0.15
Probably too old of a hugo version
```
mkdir hugo-0.15 && cd hugo-0.15
wget https://github.com/gohugoio/hugo/releases/download/v0.15/hugo_0.15_linux_amd64.tar.gz
tar xzf hugo_0.15_linux_amd64.tar.gz
cd ..
./hugo-0.15/hugo_0.15_linux_amd64/hugo_0.15_linux_amd64 --config config-prod.toml -d public-prodcfg-v015
```
```
$ diff -r public-real public-prodcfg-v015 | wc -l
1856
```

### 0.16
With hugo 0.16 I get quite close to public-real, but there is still a bunch of differences in the generated output.
```
mkdir hugo-0.16 && cd hugo-0.16
wget https://github.com/gohugoio/hugo/releases/download/v0.16/hugo_0.16_linux-64bit.tgz
tar xzf hugo_0.16_linux-64bit.tgz
cd ..
./hugo-0.16/hugo --config config-prod.toml -d public-prodcfg-v016
```
```
$ diff -r public-real public-prodcfg-v016 | wc -l
193
```

### 0.17
Bigger diff again. so this confirms we probably used 0.16 3 years ago.
```
mkdir hugo-0.17 && cd hugo-0.17
wget https://github.com/gohugoio/hugo/releases/download/v0.17/hugo_0.17_Linux-64bit.tar.gz
tar xzf hugo_0.17_Linux-64bit.tar.gz
cd ..
./hugo-0.17/hugo_0.17_linux_amd64/hugo_0.17_linux_amd64 --config config-prod.toml -d public-prodcfg-v017
```
```
$ diff -r public-real public-prodcfg-v017 | wc -l
2072
```
