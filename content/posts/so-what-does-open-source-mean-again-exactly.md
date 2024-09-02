+++
title = 'So what does Open Source mean again, exactly?'
date = 2024-08-29T09:57:53+02:00
summary= 'world view shattered'
draft = true
+++
# Alternative titles

* 'Could we all be so wrong about the open source definition?'
* 'How could we all be so wrong about the open source definition?'
* 'Here's why you can ignore the OSD when talking about open source'

<br>
<br>

> Computer science, too, must exist in an uneasy alliance with industry

From the book [Open Sources: Voices from the Open Source Revolution](https://www.oreilly.com/openbook/opensources/book/)

GitHub - founded in 2008 - is by far the largest Open Source code platform with more than 100 million developers globally.
The term "Open Source" has been in wide (and formalized) use for decades before that, so when Scott Chacon, cofounder of GitHub remarked earlier this year that most developers understand "open source" to mean "public on GitHub" and suggested [redefining "open source"](https://x.com/chacon/status/1754883687668232334) as such; I couldn't believe what I was reading.  I couldn't comprehend how someone could propose something so obviously ludicrous.  I thought, "maybe the success of GitHub got to his head?".  I've been active in Open Source for about 20 years myself; and could use another refresher on its origins.  The plan was simple:  write a blog post about why the [Open Source Definition](https://opensource.org/osd) is authorative, collect evidence in its support (e.g. widespread acceptance, confirmation that they invinted the term), and confirm that there has been very few contestations.  In particular, confirm that there hasn't been all that many commercial vendors who've used, or wanted, to use the term "open source" to mean "you can view/modify/use the source, but there are commercial restrictions"

However, the further I looked, the more I found evidence of the opposite. As I've spent about a week full time digging, some of my long standing beliefs were shattered.  I honestly still quite can't believe some of the things I found out.  Clearly I was too emotionally invested in my old standing beliefs, and I suspect many of us may be.

Note: Open Source represents many things in many different contexts, but in this article I want to dig into what "Open Source" means in wrt. software licensing and corporate communications specifically.

My goal for this post is:
* bring back to light some relevant historical facts, that despite their age, are still relevant
* provide a nuanced perspective, highlighting facts over interpretations and without taking any particular "side".
* provide my practical recommendations

Without further ado, let me share what I found.

## The "official" OSI story.

Let's first get the official story out the way, the one you see repeated over and over on [websites](https://www.redhat.com/en/topics/open-source/what-is-open-source), [on WikiPedia](https://en.wikipedia.org/wiki/Open-source-software_movement) and probably in most computing history books.

Back in 1998, there was a [small group of folks who felt that the verbiage at the time (Free Software) had become too politicized](https://web.archive.org/web/20021001164015/http://www.opensource.org/docs/history.php). (note: the Free Software Foundation was founded 13 years prior, in 1985, and informal use of "free software" had around since the 1970's).  They felt they needed a new word "to market the free software concept to people who wore ties". ([source](https://www.oreilly.com/openbook/opensources/book/perens.html))  (somewhat ironic since today many of us like to say "Open Source is not a business model")

Bruce Perens - an early Debian project leader and hacker on free software projects such as [busybox](https://www.busybox.net/) - had authored the first [Debian Free Software Free Guidelines](https://en.wikipedia.org/wiki/Debian_Free_Software_Guidelines) in 1997 which was turned into the first [Open Source Definition](https://en.wikipedia.org/wiki/The_Open_Source_Definition) when he founded the [OSI](https://opensource.org) (Open Source Initiative) with Eric Raymond in 1998.

Eric Raymond is of course known for his seminal 1999 essay on development models ["The cathedral and the bazaar"](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar), but he also worked on [fetchmail](https://en.wikipedia.org/wiki/Fetchmail) among others.

According to Bruce Perens, there was some criticism at the time, but only to the term "Open" in general and to "Open Source" only in a completely different industry.

> At the time of its conception there was much criticism for the Open Source campaign, even among the Linux contingent who had already bought-in to the free software concept. Many pointed to the existing use of the term "Open Source" in the political intelligence industry. Others felt the term "Open" was already overused. Many simply preferred the established name Free Software. I contended that the overuse of "Open" could never be as bad as the dual meaning of "Free" in the English language--either liberty or price, with price being the most oft-used meaning in the commercial world of computers and software

From [Open Sources: Voices from the Open Source Revolution: The Open Source Definition](https://www.oreilly.com/openbook/opensources/book/perens.html)

Furthermore, from Bruce Perens' own account:

> I wrote an announcement of Open Source which was published on February 9 [1998], and that’s when the world first heard about Open Source.

source: [On Usage of The Phrase “Open Source”](http://perens.com/2017/09/26/on-usage-of-the-phrase-open-source/)

One caveat that comes up occasionally: it may have been Christine Peterson, [who coined the term first](https://opensource.com/article/18/2/coining-term-open-source-software) but didn't give it a precise meaning, that was left to Eric whom she was meeting with, he and and Bruce gave it a precise definition in the next few days.

Even when you're the first to use or define a term, you can't legally control how others use it.  However, if you have a trademark, you can seek legal repercussions, which is a strong incentive for others not to misuse your mark.  Luckily for OSI, US trademark law recognizes the first user when you file an application, so they filed for a trademark right away. But what happened? It was rejected!  [The OSI's official explanation reads:](https://opensource.org/pressreleases/certified-open-source.php)

> We have discovered that there is virtually no chance
that the U.S. Patent and Trademark Office would register the mark
“open source”; the mark is too descriptive. Ironically, we were
partly a victim of our own success in bringing the “open source”
concept into the mainstream

This looks a bit like a 🚩 to me.  Maybe it makes sense, but I think some of the things I found (see further below) are a more clear reason why it wasn't granted.
(tip: I found this handy [TradeMark search](https://tmsearch.uspto.gov/) website in the process)

Since then, adoption of the term "Open Source" has taken over the world, across software projects, from hobby projects to large industry players.  OSI's scope of influence has grown to cover [goverment in the US, the UK, some of the EU, Asia and Australia](https://opensource.org/authority), is sponsored by [a small selection of the world's largest tech companies](https://opensource.org/sponsors) - including GitHub, tied to non-profit/foundation [affiliates](https://opensource.org/affiliates/list) and [organizations who've vouched for OSI's authority](https://opensource.org/blog/osd_affirmation).
As I was checking out these lists, I actually found som of them rather... surprisingly short.  But I assume there are a multitude more organizations who vouch for OSI, yet haven't initiated any official relation.  E.g. Grafana Labs [bets its entire business on OSI compliance](https://grafana.com/blog/2021/04/20/qa-with-our-ceo-on-relicensing/), yet is nowhere to be found in these lists.

The [Open Source Definition](https://opensource.org/osd) has been on the OSI website for 25 years.  Here is [version 1.9 from 2002](https://web.archive.org/web/20020621160209/https://opensource.org/docs/definition.php). Since then it has received some minor tweaks, and addition of a clause of technology-neutrality.

This clause is particularly important:

> Free Redistribution: The license shall not restrict any party from selling (...)

Because most contention over the Open Source definition is usually commercial limitations (non-competes) where receivers of the code are forbidden to resell it.

## Prior uses of the term "Open Source", especially with commercial restrictions

Many publications simply repeat the idea that OSI came up with the term, has the authority (if not legal, at least in practice) and call it a day.
I, however, had nothing better to do, so I decided to spend a few days and see if I could dig up any references to "Open Source" predating OSI's definition in 1998, especially ones with different meanings or definitions.

**Of course, it's totally possible that multiple people come up with the same term independently and I don't actually care so much about "who was first", I'm more interested in figuring out what different meanings have been assigned to the term and how widespread those are.**

Turns out, the "Open Source" term had been used already for years, prior to the OSI founding.

### Caldera announces Open Source OpenDOS

In 1996, a company called Caldera had "open sourced" a DOS operating system called OpenDos. Their announcement (accessible on [google groups](https://groups.google.com/g/no.linux/c/1UZo-3iv0tM) and [a mailing list archive](https://web.archive.org/web/20020910071813/http://www.xent.com/FoRK-archive/fall96/0269.html)) reads:

> Caldera Announces Open Source for DOS.  
> (...)  
> Caldera plans to openly distribute the source code for all of the DOS
> technologies it acquired from Novell., Inc  
> (...)  
> Caldera believes an open source code model benefits the industry in many ways.  
> (...)  
> Individuals can use OpenDOS source for personal use at no cost.   
> Individuals and organizations desiring to commercially redistribute   
> Caldera OpenDOS must acquire a license with an associated small fee.

Today we would refer to it as dual-licensing, using Source Available due to the non-compete clause. But in 1996, actual practitioners referred to it as "Open Source" and OSI couldn't contest it because it didn't exist!

You can download the OpenDos package from [ArchiveOS](https://archiveos.org/drdos/) and have a look at the license file, which includes even more restrictions such as "single computer". (like I said, I had nothing better to do).

### investigations by Martin Espinoza re: Caldera

On his blog, Martin has an article [making a similar observation about Caldera's prior use of "open source"](https://web.archive.org/web/20180205140347/http://hyperlogos.org/article/Who-Invented-Term-Open-Source), following up with another [article](https://web.archive.org/web/20180315075903/http://hyperlogos.org/blog/drink/term-Open-Source) which includes a response from Lyle Ball, who headed the PR department of Caldera 

Quoting martin:

> As a member of the OSI, he [Bruce] frequently championed that organization's prerogative to define what "Open Source" means, on the basis that they invented the term. But I [Martin] knew from personal experience that they did not. I was personally using the term with people I knew before then, and it had a meaning — you can get the source code. It didn't imply anything at all about redistribution.

The response from Caldera includes such gems as:

> I joined Caldera in November of 1995, and we certainly used "open source" broadly at that time. We were building software. I can't imagine a world where we did not use the specific phrase "open source software". And we were not alone. The term "Open Source" was used broadly by Linus Torvalds (who at the time was a student (...), John "Mad Dog" Hall who was a major voice in the community (he worked at COMPAQ at the time), and many, many others.

> Our mission was first to promote "open source", Linus Torvalds, Linux, and the open source community at large. (...) we flew around the world to promote open source, Linus and the Linux community....we specifically taught the analysts houses (i.e. Gartner, Forrester) and media outlets (in all major markets and languages in North America, Europe and Asia.) (...) My team and I also created the first unified gatherings of vendors attempting to monetize open source

So according to Caldera, "open source" was a phenomenon in the industry already and Linus himself had used the term.
For anyone who wants to contribute their own research, he mentions plenty of avenues.

### Linux Kernel discussions

Mr. Ball's mentions of Linus and Linux pique'd my interest, so I started digging.

I couldn't find a mention of "open source" in the Linux Kernel Mailing List archives prior to the OSD day (Feb 1998), though the archives [only start as of March 1996](https://lkml.org/lkml/1996).
I asked ChatGPT where people used to discuss Linux kernel development prior to that, and it suggested 5 usenet groups:

* alt.os.linux ([no hits](https://groups.google.com/g/alt.os.linux/search?q=%22open%20source%22%20after%3A1960-01-01%20before%3A1998-03-01))
* comp.os.minix ([no hits](https://groups.google.com/g/comp.os.minix/search?q=%22open%20source%22%20after%3A1960-01-01%20before%3A1998-03-01))
* comp.os.linux ([one hit!](https://groups.google.com/g/comp.os.linux/search?q=%22open%20source%22%20after%3A1960-01-01%20before%3A1998-03-01))
* comp.os.linux.development ([no hits](https://groups.google.com/g/comp.os.linux.development/search?q=%22open%20source%22%20after%3A1960-01-01%20before%3A1998-03-01))
* comp.os.linux.announce ([two hits!](https://groups.google.com/access-error?continue=https://groups.google.com/g/comp.os.announce/search?q%3D%2522open%2Bsource%2522%2Bafter:1960-01-01%2Bbefore:1998-03-01))

What were the hits? Glad you asked!

#### comp.os.linux: a 1993 discussion about supporting binary-only software on Linux

[source](https://groups.google.com/g/comp.os.linux/c/06y4cr6wr7o/m/fZPOOaIMCCYJ)

> The GPL and
the open source code have made Linux the success that it is.
Cygnus and other commercial interests are quite comfortable
with this open paradigm, and in fact prosper. One need only
pull the source code to GCC and read the list of many
commercial contributors to realize this.

#### comp.os.linux.announce: 1996 announcement of Caldera's open-source environment

In November 1996 Caldera [shows up again](https://groups.google.com/g/comp.os.linux.announce/c/9iyffmTxjxU/m/N1jX-Jclx6UJ),
this time with a Linux based "open-source" environment:

> Channel Partners can utilize Caldera's Linux-based, open-source
environment to remotely manage Windows 3.1 applications at home, in
the office or on the road. By using Caldera's OpenLinux (COL) and Wabi
solution, resellers can increase sales and service revenues by leveraging
the rapidly expanding telecommuter/home office market. Channel Partners
who create customized turn-key solutions based on environments like SCO
OpenServer 5 or Windows NT,

#### comp.os.linux.announce: 1996 announcement of a trade show

On 17 Oct 1996 we find [this announcement](https://groups.google.com/g/comp.os.linux.announce/c/tthtKrsFT24/m/7r8kLqxDy5gJ)

> There will be a Open Systems World/FedUnix conference/trade show in
Washington DC on November 4-8. It is a traditional event devoted to
open computing (read: Unix), attended mostly by government and
commercial Information Systems types.

In particular, this talk stands out to me:

> ** Schedule of Linux talks, OSW/FedUnix'96, Thursday, November 7, 1996 ***  
> (...)  
> 11:45 Alexander O. Yuriev, "Security in an open source system: Linux study"

### 1990: Tony Patti on "software developed from open source material"

in 1990, a magazine editor by name of Tony Patti not only refers to Open Source software [but mentions that NSA in 1987 referred to "software was developed from open source material"](https://groups.google.com/g/sci.crypt/c/_696x9zT8MI#0243ee9294bdc300)

### 1995: open-source changes emails on OpenBSD-misc email list

I could find one mention of "Open-source" on an OpenBSD email list, seems there was a directory "open-source-changes" which had incoming patches, distributed over email.  ([source](http://web.archive.org/web/19970508053404/http://www.sigmasoft.com/~openbsd/misc/msg00069.html)).  Though perhaps the way to interpret is, to say it concerns "source-changes" to OpenBSD, paraphrased to "open".

(I did not look at other BSD's)

### Bryan Lunduke's research

Seems an individual by the name of Bryan Lunduke has done similar research and found several more USENET posts about "open source", clearly in the context of of source software, predating OSI by many years. He breaks it down [on his substack](https://lunduke.substack.com/p/who-really-coined-the-term-open-source) and concludes, that without doing further digging, we can conclude that the first usages of the term "Open Source" go back at least as early as as:

* commercially, by Caldera in 1996.
* by an invidiual, May of 1990 by Tony Patti.
* potentially by a government agency, the NSA in 1987.

In particular, he highlights a use of the term "Open Source" in 1993 that I find worth pointing out because he talks about "disclosing" and "releasing stuff with source".

## Uses of the word "open"

We're specifically talking about "open source" in this article. But we should probably also consider how the term "open" was used in software, as that may have played a role in the rejection of the trademark as well.

https://en.wikipedia.org/wiki/Open_Software_Foundation 1988

The word "open" was also used in software, e.g. [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS) since 1977, [OpenStep](https://en.wikipedia.org/wiki/OpenStep) since 1994 and of course in 1996, the OpenBSD project started.  They have this to say [about their name:](https://web.archive.org/web/20220818022950/https://en.wikipedia.org/wiki/OpenBSD) (while OpenBSD started in 1996, this quote is from 2006):

> The word "open" in the name OpenBSD refers to the **availability of the operating system source code on the Internet**, although the word "open" in the name OpenSSH means "OpenBSD". It also refers to the wide range of hardware platforms the system supports.


## Does it run DOOM?

The proof of any hardware platform is always whether it can run Doom.  Since the DOOM source code was published in December 1997, it may serve as the ultimate proof of whether the term "Open Source" was in use, at least by ID Software at that time.  There are some FTP mirrors where you can still see the files with the original December 1997 timestamps (e.g. [this one](https://ftp.gwdg.de/pub/misc/ftp.idsoftware.com/idstuff/source/)).  However, after sifting through the README and other documentation files, I only found references to the "Doom source code".  No mention of Open Source.


## The origins of the famous "Open Source" trademark

Apparently in June 1997 the [SPI ("Software In the Public Interest")](https://en.wikipedia.org/wiki/Software_in_the_Public_Interest) organization was born to support the Debian project, and funded by the Debian community.  It started proceedings for the "Open Source" trademark, which Bruce then tried to migrate over into OSI, which [didn't seem like a good idea to the Debian leader](https://disguised.work/debian/bruce-perens-debian-swiping-the-open-source-trademark/) and https://techrights.org/n/2024/04/23/Ean_Schuessler_Debian_SPI_OSI_trademark_disputes.shtml Ean Schuessler

In August (or October, I'm not sure) 1998 Bruce published the following:

> Thus, the board of Software in the
Public Interest decided to spin off a new organization for Open Source
early last week. Three of the four SPI directors elected to move to
the new organization, because they are no longer involved in Debian.
This left Ian Jackson, who is the current Debian Project Leader, on the
SPI board to appoint new directors from the ranks of the Debian
developers.  
> (...)  
> The Open Source trademark attribution will now change to:  
>    "Open Source is a Certification Mark of The Open Source Initiative".


In December 1998 the [SPI made its position clear](https://www.spi-inc.org/corporate/resolutions/1998/1998-12-01.iwj.1/):

> Bruce Perens, Ian Murdock and Timothy Sailer ('the Former Board Members') have not been authorised, and remain not authorised, to carry out any assignment of the 'Open Source' trademark.

According to [this article](https://www.techmonitor.ai/technology/open_source_initiative_gives_up_on_trademark/) it was Bruce who himself paid for, and carried out the registration of the mark (while he was at SPI) which led him to believe he could transfer it to a different organization (the OSI).

I'm sure a lot more can be found out about this, but I think I'll leave it at that.  Some interesting (unanswered) questions are: did the majority of SPI leave and move on to OSI?  Which side of the story represents the majority?  FWIW, [here's](https://techrights.org/n/2024/04/23/Ean_Schuessler_Debian_SPI_OSI_trademark_disputes.shtml) the perspective of Debian developer Ean Schuessler's at the time.

a few years later, wounds were healing - https://www.theregister.com/2003/02/06/perens_throws_hat_into_spi/


## Contention post-OSI founding

OK, so we found evidence of the term "Open Source" being in use in the industry in the decade before the OSI was founded.  And sometimes the term was used referring to software that came with commercial restrictions.  Can we find examples of contention against OSI's definition after OSI was founded?

### OpenSource.com

Here's something I found slightly amusing.  Apparently in 1998, there was a business in Texas called ["OpenSource, Inc"](https://web.archive.org/web/19981212031620/http://www.opensource.com/).  Their website launched in April 1998, so I would guess the business probably incorporated after the OSI launched.  Not sure what happened, did the OSI send a cease & desist?  Did they fail to commercialize OSS? Or did they do it so successfully that they retired or exited? [Sometime during the year 2000](https://web.archive.org/web/20000601000000*/opensource.com), the website became a RedHat property.

Today, that website looks like some sort of community website ran by RedHat.  For some reason they published a lot of rather vague and confusing prose about ["What is Open Source"](https://opensource.com/resources/what-open-source) and [The Open Source Way](https://opensource.com/open-source-way). These articles contain over 1900 words combined, and yet there's only a single reference to the [Open Source Definition](https://opensource.org/osd), not even in the text.  You have to mouse-over all the hyperlinks to find it.

Here are some quotes from the "What Is Open Source?" article:

> Open source software is software with source code that anyone can inspect, modify, and enhance.

(nothing here about redistribution, or copying even)

> Open source software is different [from proprietary and "closed source" software]. Its authors make its source code available to others who would like to view that code, copy it, learn from it, alter it, or share it.

(nothing here about redistribution)

This website confirms a couple of interesting things:
* anyone person or entity is permitted to declare "their truth" on what Open Source means
* your "truth" doesn't need to match OSI.
* you don't need to offer a precise, consistent explanation.

## Linux Distributions

Do popular linux distributions abide by OSI?

* Debian, while affiliated with OSI, maintains its own license review process, though it is similar to OSI's ([source](https://www.debian.org/News/2012/20120330.en.html))
* Red Hat [stands with OSI](https://www.redhat.com/en/topics/open-source/what-is-open-source) 
* [so does Ubuntu](https://ubuntu.com/community/ethos/mission). (though both seem to present an inaccurate view on how the term came to be)
* BSD's only allow permisse BSD licenes, no GPLs. See [FreeBSD](https://www.freebsd.org/internal/software-license/) and https://www.openbsd.org/policy.html 


### 2007's "OSI crackdown"

https://slashdot.org/story/07/06/21/1146259/osi-to-crack-down-on-open-source-abusers%E2%8B%85same
backlash
OSI approved

## TODO

trust take years to build, seconds to break, and forever to repair?

* i guess OSI probably did spread awareness
* but i also guess most people are indeed not quite familiar


* yes it was in use, but not super widespread, OSI may have helped to spread wide
* uneasy feeling due to the claims of invention. undermines credibility
* find more instances of OSI being challenged by vendors who don't agree

TODO slashdot search for "open source"

https://news.slashdot.org/story/99/06/17/0213251/esr-on-the-open-source-trademark comments osi approval
https://news.slashdot.org/comments.pl?sid=91&cid=1851204 generic term



But we have more good datapoints:
* the multitude of voluntary "OSI defense" happening on platforms such as [X](https://x.com/chacon/status/1754820325022294393), reddit, etc.  It's a deep rooted part of the industry, even if not formalized.



During this time, it has regularly been contested.


In about 2019 when MongoDB sought OSI approval for its SSPL license (and failed to secure it).
Since then, several companies have followed suit and adopted various new licenses with similar commercial non-compete clauses. The non-OSI compliance has led to new terms such as [Source Available](https://en.wikipedia.org/wiki/Source-available_software), [Open Core](https://en.wikipedia.org/wiki/Open-core_model), [Fair Code](https://faircode.io/), [Commons Clause](https://commonsclause.com/) and [Fair Source](https://fair.io/).  Note, [I have written an analysis of Fair Source](/posts/fair-source).  It seems the community at large has come to the conclusion that the easiest solution in these cases is to just coin new terms and start initatives.

GitHub - founded in 2008 - is by far the largest code platform with more than 100 million developers globally. Its reach eclipses that of the affiliates and sponsors lists combined.
Most recently, Scott Chacon, cofounder of GitHub remarked that most developers understand "open source" to mean "public on GitHub" and suggested [redefining "open source"](https://x.com/chacon/status/1754883687668232334) as such.  The gravity of this observation is not to be underestimated.  GitHub has indeed brought in tens of millions of developers who may not be up to speed on the whole "Open Source" definition.  And it *is* tempting to just redefine a term to accommodate them all at once. But what would this actually solve?  If we don't disagree with the OSD, then everyone agrees, and there are no ambiguities whatsoever that could be resolved by redefining.  In fact, redefining would create ambiguities (at the global scale) and this wouldn't really solve the need to educate people either.  At the end of the day, they still need to know if they're allowed to commercially redistribute, for example.

I think redefining "Open Source" today would be tremendously impractical.  It is, in fact, a tremendous achievement that most of the whole world can agree on what a term means.  It is truly exceptional that all over the world, goverment offices, startups, students, academia, and so on, are either already perfectly aligned, or can align, with a minimum of self-education.  To try to change that, after 25 years would create so much friction that far outweighs any perceived benefits.

It's much easier to just coin a new term and promote that instead, which is this case is what happened with Fair Source.


But the fact of the matter is, they were not the first to coin the term, they don't have a trademark, and it has been consistly contested despite their garguantuan efforts to get the whole world aligned (with good results in the programming community, in goverments, and the industry)

### In conclusion
alt headline: 'Foolish to assume open source means OSD, double foolish to try to make it so'

It seems as if every single year, the same pot gets stirred: a vendor publicizes source code under a license that allows viewing, modifying and reuse (but with a commercial restriction) and makes an announcement about "open source", and the community is up in arms because "that's not what open source means".  So what does "open source" mean, exactly?

When communities form and evolve along with the world around them, inevetably incompatible viewpoints emerge and can cause fractures. This was as true in the 1990's as it is in the 2020's.

The gravity of this observation is not to be underestimated.  GitHub has indeed brought in tens of millions of developers who may not be up to speed on the whole "Open Source" definition.  And it *is* tempting to just redefine a term to accommodate them all at once. But what would this actually solve?  If we don't disagree with the OSD, then everyone agrees, and there are no ambiguities whatsoever that could be resolved by redefining.  In fact, redefining would create ambiguities (at the global scale) and this wouldn't really solve the need to educate people either.  At the end of the day, they still need to know if they're allowed to commercially redistribute, for example.


Who gets to say exactly what a term means, or doesn't mean?  Today, the word "literally" means its opposite, and what is DevOps anyway?

In a world that can't agree on anything, the amount of alignment that OSI has been able to create is remarkable.
But there is plenty of evidence that the word "open source" has been used in ways incompatible with the OSD, both before, and after OSI's creation. 
One meaning of open source comes up over and over again: publishing source code for anyone to use, except to compete with the author.
OSI's attempts to control usage of the term - for which they have no legal grounds - have been proven mostly pointless, and I don't see this conflict ever being truly resolved.

My suggestion therefore, is a pragmatic one:
* as a vendor, communicate in more detail (but not too verbosely) what your terms are.  Customers and prospects appreciate clarity and dislike being misguided.
* as a consumer/customer, always look beyond the buzz-words and build a good understanding of the licensing terms you are about to use.
* if as a vendor, you find it important to use a OSI compliant license, simply mention "OSI certified", which is trademarked, and has a precise meaning.
* as a consumer/customer, look beyond the "OSI certified" (or "Open Source") label.  It may only cover a part of the whole offering (e.g. any Open core product), you may need to sign a customer agreement undermining the OSI license (e.g. RedHat), and something non-OSI compliant may actually serve you better (e.g. Source-Available or [Fair Source](/posts/fair-source)).

As far as "Open Source" terminology goes, arguing about whether that means OSI compliant or not, is pretty useless.  I would try to sidestep it al together. Except if you're a company who believes "any press is good press", than use the term "open source" as you wish, especially for non-OSI compliant licenses.  You're free to do so, and you'll have guaranteed buzz.


Source Available or [Fair Source](/posts/fair-source).  And if those don't fit your need, you can always create a new one.   Even Bruce Perens himself is working [on an "Open Source" reimagined](https://www.theregister.com/2023/12/27/bruce_perens_post_open/) which will be a distinct initiative as well.


could OSI really be so unaware of these prior uses of open source? somebody should let them know.


$$$$ IGNORE THIS DRAFT TEXT BELOW

https://lists.nongnu.org/archive/html/discuss-gnustep/2013-09/msg00113.html another example of commercial clause making non-osi compliant

There is something to be said about the work of taking a word that is colloquially used, and formally defining it.

TODO: simon phipps open source definition hot debate. 5-10 years ago

You can meet the OSI definition, not be OSD compliant

swiss government datapoint https://www.fedlex.admin.ch/eli/cc/2023/682/de

If I can find formal uses from 4 decades ago, when the world communication was much less digitized then without a doubt there were more formal and informal uses



- https://www.gnu.org/philosophy/open-source-misses-the-point.html uses Osd. Though the rift is out of scope
- He points out misunderstanding. Also state of Kansas

in a world that can't agree on anything..


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


https://web.archive.org/web/20070627154037/https://opensource.org/node/163 2007 enforcing by OSI with huge backlash and some good quotes re TMp
https://slashdot.org/story/07/06/21/1146259/osi-to-crack-down-on-open-source-abusers same


https://www.reddit.com/r/mongodb/comments/1ao3yan/has_sspllicensed_mongodb_been_accepted/ mostly rejected

https://news.ycombinator.com/item?id=35544600 sspl discussion. many find open source = can download



https://slashdot.org/~drinkypoo/journal/175327 this is the same guy as before, martin, i think


https://www.theregister.com/2007/09/27/open_season_episode_3/ rumours that google would make own license?



TODO: contact asay?


TODO: caldera location, bruce ESR location?
