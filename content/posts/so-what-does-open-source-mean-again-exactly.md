+++
title = 'So what does Open Source mean again, exactly?'
date = 2024-08-18T09:57:53+02:00
draft = true
+++

TODO integrate these

* https://opensource.com/article/18/2/coining-term-open-source-software
* https://web.archive.org/web/20180205140347/http://hyperlogos.org/article/Who-Invented-Term-Open-Source
* https://web.archive.org/web/20220810223503/https://slashdot.org/comments.pl?sid=239319&cid=19593809

> Computer science, too, must exist in an uneasy alliance with industry

From the book [Open Sources: Voices from the Open Source Revolution](https://www.oreilly.com/openbook/opensources/book/)

Who gets to say exactly what a term means, or doesn't mean?  Today, the word "literally" means its opposite, and what is DevOps anyway?
This was originally supposed to be a post confirming OSI's authority, but as I did my homework, I developed a more nuanced view...

Cantrill says it's a social contract
Heather says it's development model AND ...
Those are all true, but for the purpose of this post, let's drill down and figure out what the essential legal meaning is.

When communities form and evolve along with the world around them, inevetably incompatible viewpoints emerge and can cause fractures. This was as true in the 1990's as it is in the 2020's.

Back in 1998, there was a [small group of folks who felt that the verbiage at the time (Free Software) had become too politicized](https://web.archive.org/web/20021001164015/http://www.opensource.org/docs/history.php). (note: the Free Software Foundation was founded 13 years prior, in 1985, and informal use of "free software" had around since the 1970's)
They felt they needed a new word "to market the free software concept to people who wore ties". ([source](https://www.oreilly.com/openbook/opensources/book/perens.html))  
(somewhat ironic since today many of us like to say "Open Source is not a business model")

Bruce Perens - an early Debian project leader and hacker on free software projects such as [busybox](https://www.busybox.net/) - had authored the first [Debian Free Software Free Guidelines](https://en.wikipedia.org/wiki/Debian_Free_Software_Guidelines) in 1997 which was turned into the first [Open Source Definition](https://en.wikipedia.org/wiki/The_Open_Source_Definition) when he founded the [OSI](https://opensource.org) (Open Source Initiative) with Eric Raymond in 1998.

Eric Raymond is of course known for his seminal 1999 essay on development models ["The cathedral and the bazaar"](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar), but he also worked on [fetchmail](https://en.wikipedia.org/wiki/Fetchmail) among others.

According to Bruce Perens, there was some criticism at the time, but only to the term "Open" in general and to "Open Source" only in a completely different industry.

> At the time of its conception there was much criticism for the Open Source campaign, even among the Linux contingent who had already bought-in to the free software concept. Many pointed to the existing use of the term "Open Source" in the political intelligence industry. Others felt the term "Open" was already overused. Many simply preferred the established name Free Software. I contended that the overuse of "Open" could never be as bad as the dual meaning of "Free" in the English language--either liberty or price, with price being the most oft-used meaning in the commercial world of computers and software

From [Open Sources: Voices from the Open Source Revolution: The Open Source Definition](https://www.oreilly.com/openbook/opensources/book/perens.html)

Furthermore, from Bruce Perens' own account:

> I wrote an announcement of Open Source which was published on February 9 [1998], and that’s when the world first heard about Open Source.

source: [On Usage of The Phrase “Open Source”](http://perens.com/2017/09/26/on-usage-of-the-phrase-open-source/)

So they were the first to introduce the term "Open Source" to the world and published the [Open Source Definition](https://opensource.org/osd) online. But hold on, does that mean anyone who wants to use the term "Open Source" needs to abide by this?   You cannot legally stop someone from using or misusing a word.  However, if you have a trademark, you can seek legal repercussions, which is a strong incentive for others not to misuse your mark.  US trademark law recognizes the first user when you file an application.  
Luckily, the OSI filed for a trademark right away! But what happened? [It was rejected](https://opensource.org/pressreleases/certified-open-source.php) the term was too widely adopted even already in 1999, rendering OSI (or anyone else) unable to claim ownership of it. 🤔🤔🤔

# 🤔

Most online articles simply repeat the idea that OSI cointed and defined the term, but I had nothing better to do, so I decided to spend a few days and see if I could dig up any references to "Open Source" predating OSI's definition in 1998.

Turns out, the "Open Source" term had been used already for years.
For example a company called Caldera had "open sourced" a DOS operating system called OpenDos, and their announcement is accessible on [google groups](https://groups.google.com/g/no.linux/c/1UZo-3iv0tM) and [a mailing list archive](https://web.archive.org/web/20020910071813/http://www.xent.com/FoRK-archive/fall96/0269.html).

Their announcement mentions:

> Individuals can use OpenDOS source for personal use at no cost.  
> Individuals and organizations desiring to commercially redistribute  
> Caldera OpenDOS must acquire a license with an associated small fee.

Today we would refer to it as dual-licensing, using Source Available due to the non-compete clause. But in 1996, actual practiotioners referred to it as "Open Source"!

You can download the OpenDos package from [ArchiveOS](https://archiveos.org/drdos/) and have a look at the license file, which includes even more restrictions such as "single computer". (like I said, I had nothing better to do).

in 1990, a magazine editor by name of Tony Patti not only refers to Open Source software [but mentions that this was an Open Source policy at NSA in 1987](https://groups.google.com/g/sci.crypt/c/_696x9zT8MI#0243ee9294bdc300)

Also in 1996, the OpenBSD project [had this to say](https://web.archive.org/web/20220818022950/https://en.wikipedia.org/wiki/OpenBSD):

> The word "open" in the name OpenBSD refers to the availability of the operating system source code on the Internet, although the word "open" in the name OpenSSH means "OpenBSD". It also refers to the wide range of hardware platforms the system supports.

There's also [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS), and [OpenStep](https://en.wikipedia.org/wiki/OpenStep) where "open" was used in ways other than open source.

Seems an individual by the name of Bryan Lunduke has done similar research and found a couple more USENET posts. He breaks it down [on his substack](https://lunduke.substack.com/p/who-really-coined-the-term-open-source) and concludes, that without doing further digging, we can conclude that the first usages of the term "Open Source" go back at least as early as as:

* commercially, by Caldera in 1996.
* by an invidiual, May of 1990 by Tony Patti.
* potentially by a government agency, the NSA in 1987.





Since then, adoption of the term "Open Source" has taken off like wildfire across software projects, from hobby projects to large industry players.  OSI's scope of influence has grown to cover [goverment in the US, the UK, some of the EU, Asia and Australia](https://opensource.org/authority), is sponsored by [a small selection of the world's largest tech companies](https://opensource.org/sponsors) - including GitHub, tied to non-profit/foundation [affiliates](https://opensource.org/affiliates/list) and [organizations who've vouched for OSI's authority](https://opensource.org/blog/osd_affirmation).
As I was checking out these lists, I actually found them rather... surprisingly short? But I assume there are a multitude more organizations who vouch for OSI, yet haven't initiated any official relation.  E.g. Grafana Labs [bets its entire business on OSI compliance](https://grafana.com/blog/2021/04/20/qa-with-our-ceo-on-relicensing/), yet is nowhere to be found in these lists. (I've reached out to my connections there to see if we can change that).

But we have more good datapoints:
* the multitude of voluntary "OSI defense" happening on platforms such as [X](https://x.com/chacon/status/1754820325022294393), reddit, etc.  It's a deep rooted part of the industry, even if not formalized.
* Linux Distributions: Debian, while affiliated with OSI, maintains its own license review process, though it is similar to OSI's ([source](https://www.debian.org/News/2012/20120330.en.html), Red Hat [stands with OSI](https://www.redhat.com/en/topics/open-source/what-is-open-source) and [so does Ubuntu](https://ubuntu.com/community/ethos/mission). (though both seem to present an inaccurate view on how the term came to be)



The [Open Source Definition](https://opensource.org/osd) has been on the OSI website for 25 years.
During this time, it has regularly been contested.


In about 2019 when MongoDB sought OSI approval for its SSPL license (and failed to secure it).
Since then, several companies have followed suit and adopted various new licenses with similar commercial non-compete clauses. The non-OSI compliance has led to new terms such as [Source Available](https://en.wikipedia.org/wiki/Source-available_software), [Open Core](https://en.wikipedia.org/wiki/Open-core_model), [Fair Code](https://faircode.io/), [Commons Clause](https://commonsclause.com/) and [Fair Source](https://fair.io/).  Note, [I have written an analysis of Fair Source](/posts/fair-source).  It seems the community at large has come to the conclusion that the easiest solution in these cases is to just coin new terms and start initatives.

GitHub - founded in 2008 - is by far the largest code platform with more than 100 million developers globally. Its reach eclipses that of the affiliates and sponsors lists combined.
Most recently, Scott Chacon, cofounder of GitHub remarked that most developers understand "open source" to mean "public on GitHub" and suggested [redefining "open source"](https://x.com/chacon/status/1754883687668232334) as such.  The gravity of this observation is not to be underestimated.  GitHub has indeed brought in tens of millions of developers who may not be up to speed on the whole "Open Source" definition.  And it *is* tempting to just redefine a term to accommodate them all at once. But what would this actually solve?  If we don't disagree with the OSD, then everyone agrees, and there are no ambiguities whatsoever that could be resolved by redefining.  In fact, redefining would create ambiguities (at the global scale) and this wouldn't really solve the need to educate people either.  At the end of the day, they still need to know if they're allowed to commercially redistribute, for example.

I think redefining "Open Source" today would be tremendously impractical.  It is, in fact, a tremendous achievement that most of the whole world can agree on what a term means.  It is truly exceptional that all over the world, goverment offices, startups, students, academia, and so on, are either already perfectly aligned, or can align, with a minimum of self-education.  To try to change that, after 25 years would create so much friction that far outweighs any perceived benefits.

It's much easier to just coin a new term and promote that instead, which is this case is what happened with Fair Source.


I wish I could have concluded by confirming OSI's authority and confirming we should all just go with that. But the fact of the matter is, they were not the first to coin the term, they don't have a trademark, and it has been consistly contested despite their garguantuan efforts to get the whole world aligned (with good results in the programming community, in goverments, and the industry)

Open Source is not the only model, there are plenty of others to choose from, such as Source Available or [Fair Source](/posts/fair-source).  And if those don't fit your need, you can always create a new one.   Even Bruce Perens himself is working [on an "Open Source" reimagined](https://www.theregister.com/2023/12/27/bruce_perens_post_open/) which will be a distinct initiative as well.


my suggestion therefore, is a pragmatic one:
- the term "Open Source" is irreconsibly ambiguous. Always clarify beyond it, and seek the truth behind it

- Be pragmatic just say OSI values. see grafana announcement. No holy war. Just try to avoid saying open source when clearly not osi. But OSI not end all be all. Fair source makes sense. Red hat tricks. Open core despite agpl. Just be clear
-
- Don't try to actively mislead


* if you are proud to be OSI compliant, advertise as such
* if you have OSD-incompatible restrictions and want to do the honorable thing, try to pick a more appropriate term such as Source Available.  Simple clarity will be appreciated by your customers and prospects.
* if you have OSD-incompatible restrictions such as non-compete, but believe "any press is good press", claim you are open source, make vague statements and let the internet go nuts.




$$$$ IGNORE THIS DRAFT TEXT BELOW

Cygnus software used sourceware / free software, prior to 1998, I believe

> the more development we did on GNU software, the less we got back from the Net, until we were doing over 50% of all GNU toolchain development



> In fact, GNUPro has become so dominant that several of our competitors have announced their intention to sell commercial support for GNU software to compete with us! Fortunately, the Open Source model comes to the rescue again. Unless and until a competitor can match the 100+ engineers we have on staff today, most of whom are primary authors or maintainers of the software we support, they cannot displace us from our position as the "true GNU" source (we supply over 80% of all changes made to GCC, GDB, and related utilities). The best they can hope to do is add incremental features that their customers might pay them to add. But because the software is Open Source, whatever value they add comes back to Cygnus as open-source software, for us to integrate if it's good, or ignore if it's not. Unlike proprietary software in which competitors fight in a two-sided win/lose contest, with Open Source it's more like fighting on a Moebius strip, and everything flows to the side of the primary maintainer. So, while our competitors may get some tactical advantage in the "me-too" GNU space, Cygnus benefits in the long run. Founded in 1989, our first-mover advantage is ten years ahead of the competition.


https://dl.acm.org/doi/10.1145/164399.164402 lynx used 'free software' term


https://lists.nongnu.org/archive/html/discuss-gnustep/2013-09/msg00113.html another example of commercial clause making non-osi compliant


There is something to be said about the work of taking a word that is colloquially used, and formally defining it.


TODO: simon phipps open source definition hot debate. 5-10 years ago


You can meet the OSI definition, not be OSD compliant

swiss government datapoint https://www.fedlex.admin.ch/eli/cc/2023/682/de

If I can find formal uses from 4 decades ago, when the world communication was much less digitized then without a doubt there were more formal and informal uses



- https://www.gnu.org/philosophy/open-source-misses-the-point.html uses Osd. Though the rift is out of scope
- He points out misunderstanding. Also state of Kansas

in a world that can't agree on anything..




-
- https://opensource.org/licenses/review-process new developments. "Software freedom"
- https://opensource.org/licenses/review-process
-
- Heather says :
-
- The addition of 
  the requirement to “guarantee software freedom” introduced a   
  significant level of discretion into the approval process. That   
  discretionary element probably existed de facto prior to the SSPL   
  controversy but was made especially public as a result of it



  TODO: comparison to 4 freedoms? 4F is easier. why need to make own OSD?



  https://www.youtube.com/watch?v=um5bC20NTQ0
  5:20 -> power oss. enable further innovation, 8:20 kindof equating oss to making source available, but also incorporating into larger project and driving further innovation
