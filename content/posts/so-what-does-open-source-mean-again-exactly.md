+++
title = 'So what does Open Source mean again, exactly?'
date = 2024-08-18T09:57:53+02:00
draft = true
+++

> Computer science, too, must exist in an uneasy alliance with industry

From the book [Open Sources: Voices from the Open Source Revolution](https://www.oreilly.com/openbook/opensources/book/)

Who gets to say exactly what a term means, or doesn't mean?  Today, the word "literally" means its opposite, and what is DevOps anyway?

Open Source is both a development model and a licensing model, says Heather Meeker in her book [Open Source For Business](https://www.amazon.com/Open-Source-Business-Practical-Licensing/dp/1544737645).
In Bryan Cantrill's [talk on Corporate Open Source Anti-Patterns](https://youtu.be/um5bC20NTQ0?si=BLIfobkPDWtTN3Do) he describes Open Source as an incredible catalyst of human innovation and highlights its aspect of being a social contract.

Open Source indeed represents many things in many different contexts, but in this article I want to dig into what "Open Source" means in terms of software licensing and corporate communications specifically.It seems as if every single year, the same pot gets stirred: a vendor publicizes source code under a license that allows viewing, modifying and reuse (but with a commercial restriction) and makes an announcement about "open source", and the community is up in arms because "that's not what open source means".  So what does "open source" mean, exactly?

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

(According to Christine Peterson, [she coined the term a few days prior](https://opensource.com/article/18/2/coining-term-open-source-software) but for the purpose of this article, this isn't very relevant, as there was no particular meaning to the term, that was handed over to Eric whom she was meeting with - and Bruce)

So they were the first to introduce the term "Open Source" to the world and published the [Open Source Definition](https://opensource.org/osd) online. But hold on, does that mean anyone who wants to use the term "Open Source" needs to abide by this?   You cannot legally stop someone from using or misusing a word.  However, if you have a trademark, you can seek legal repercussions, which is a strong incentive for others not to misuse your mark.  Luckily for OSI, US trademark law recognizes the first user when you file an application, so they filed for a trademark right away! But what happened? [It was rejected!?](https://opensource.org/pressreleases/certified-open-source.php)

🚩 However, the OSI was unable to claim ownership. 🚩  
🚩 Nobody has since been able to file the trademark [tip: TM search](https://tmsearch.uspto.gov/). 🚩  
Could it be that the term predates OSI and/or had been used with a different meaning? 🤔

Many articles simply repeat the idea that OSI coined the term and call it a day.   I, however, had nothing better to do, so I decided to spend a few days and see if I could dig up any references to "Open Source" predating OSI's definition in 1998, especially ones with different meanings or definitions.

**Of course, it's totally possible that multiple people come up with the same term independently and I don't actually care so much about "who was first", I'm more interested in figuring out what different meanings have been assigned to the term and how widespread those are.**

Turns out, the "Open Source" term had been used already for years, prior to the OSI founding.
For example a company called Caldera had "open sourced" a DOS operating system called OpenDos, and their announcement is accessible on [google groups](https://groups.google.com/g/no.linux/c/1UZo-3iv0tM) and [a mailing list archive](https://web.archive.org/web/20020910071813/http://www.xent.com/FoRK-archive/fall96/0269.html).

Their announcement mentions:

> Individuals can use OpenDOS source for personal use at no cost.  
> Individuals and organizations desiring to commercially redistribute  
> Caldera OpenDOS must acquire a license with an associated small fee.

Today we would refer to it as dual-licensing, using Source Available due to the non-compete clause. But in 1996, actual practitioners referred to it as "Open Source"!

You can download the OpenDos package from [ArchiveOS](https://archiveos.org/drdos/) and have a look at the license file, which includes even more restrictions such as "single computer". (like I said, I had nothing better to do).

Martin Espinoza
  https://web.archive.org/web/20180205140347/http://hyperlogos.org/article/Who-Invented-Term-Open-Source similar breakdown to me
  https://web.archive.org/web/20180315075903/http://hyperlogos.org/blog/drink/term-Open-Source followup with Caldera response, "open source" was widespread!
couldn't find a mention in the Linux Kernel Mailing List archives prior to the OSD day, though they only start March 1996 https://lkml.org/lkml/1996

I couldn't quite figure out where people used to discuss Linux kernel development prior to that, so I asked ChatGPT.
It suggested I check out the following 5 usenet groups:

but no https://groups.google.com/g/comp.os.minix/search?q=%22open%20source%22
and not on https://groups.google.com/g/alt.os.linux/search?q=%22open%20source%22%20after%3A1964-07-02%20before%3A1999-08-01


comp.os.linux
discussion about supporting binary-only software on Linux
https://groups.google.com/g/comp.os.linux/c/06y4cr6wr7o/m/fZPOOaIMCCYJ
> The GPL and
the open source code have made Linux the success that it is.
Cygnus and other commercial interests are quite comfortable
with this open paradigm, and in fact prosper. One need only
pull the source code to GCC and read the list of many
commercial contributors to realize this.


https://groups.google.com/g/comp.os.linux.announce/c/9iyffmTxjxU/m/N1jX-Jclx6UJ
nov 1996 Caldera again
Channel Partners can utilize Caldera's Linux-based, open-source
environment to remotely manage Windows 3.1 applications at home, in
the office or on the road. By using Caldera's OpenLinux (COL) and Wabi
solution, resellers can increase sales and service revenues by leveraging
the rapidly expanding telecommuter/home office market. Channel Partners
who create customized turn-key solutions based on environments like SCO
OpenServer 5 or Windows NT,


17 Oct 1996
https://groups.google.com/g/comp.os.linux.announce/c/tthtKrsFT24/m/7r8kLqxDy5gJ

> There will be a Open Systems World/FedUnix conference/trade show in
Washington DC on November 4-8. It is a traditional event devoted to
open computing (read: Unix), attended mostly by government and
commercial Information Systems types.

** Schedule of Linux talks, OSW/FedUnix'96, Thursday, November 7, 1996 ***
> 11:45 Alexander O. Yuriev, "Security in an open source system: Linux study"



REDO everything with open-source
https://groups.google.com/g/comp.os.linux.development/search?q=%22open-source%22&sortBy=DATE no hits



in 1990, a magazine editor by name of Tony Patti not only refers to Open Source software [but mentions that NSA in 1987 referred to "software was developed from open source material"](https://groups.google.com/g/sci.crypt/c/_696x9zT8MI#0243ee9294bdc300)



Seems an individual by the name of Bryan Lunduke has done similar research and found several more USENET posts about "open source", clearly in the context of opet source software, predating OSI by many years. He breaks it down [on his substack](https://lunduke.substack.com/p/who-really-coined-the-term-open-source) and concludes, that without doing further digging, we can conclude that the first usages of the term "Open Source" go back at least as early as as:

* commercially, by Caldera in 1996.
* by an invidiual, May of 1990 by Tony Patti.
* potentially by a government agency, the NSA in 1987.

Sidenote, the word "open" was also used in software, e.g. [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS) since 1977, [OpenStep](https://en.wikipedia.org/wiki/OpenStep) since 1994 and of course in 1996, the OpenBSD project started.  [about their name:](https://web.archive.org/web/20220818022950/https://en.wikipedia.org/wiki/OpenBSD):

> The word "open" in the name OpenBSD refers to the **availability of the operating system source code on the Internet**, although the word "open" in the name OpenSSH means "OpenBSD". It also refers to the wide range of hardware platforms the system supports.




Since then, adoption of the term "Open Source" has taken off like wildfire across software projects, from hobby projects to large industry players.  OSI's scope of influence has grown to cover [goverment in the US, the UK, some of the EU, Asia and Australia](https://opensource.org/authority), is sponsored by [a small selection of the world's largest tech companies](https://opensource.org/sponsors) - including GitHub, tied to non-profit/foundation [affiliates](https://opensource.org/affiliates/list) and [organizations who've vouched for OSI's authority](https://opensource.org/blog/osd_affirmation).
As I was checking out these lists, I actually found them rather... surprisingly short? But I assume there are a multitude more organizations who vouch for OSI, yet haven't initiated any official relation.  E.g. Grafana Labs [bets its entire business on OSI compliance](https://grafana.com/blog/2021/04/20/qa-with-our-ceo-on-relicensing/), yet is nowhere to be found in these lists. (I've reached out to my connections there to see if we can change that).

But we have more good datapoints:
* the multitude of voluntary "OSI defense" happening on platforms such as [X](https://x.com/chacon/status/1754820325022294393), reddit, etc.  It's a deep rooted part of the industry, even if not formalized.
* Linux Distributions: Debian, while affiliated with OSI, maintains its own license review process, though it is similar to OSI's ([source](https://www.debian.org/News/2012/20120330.en.html), Red Hat [stands with OSI](https://www.redhat.com/en/topics/open-source/what-is-open-source) and [so does Ubuntu](https://ubuntu.com/community/ethos/mission). (though both seem to present an inaccurate view on how the term came to be)


  1998 https://web.archive.org/web/19981212031620/http://www.opensource.com/ "OpenSource, Inc"
  [Sometime during the year 2000](https://web.archive.org/web/20000601000000*/opensource.com), it became a RedHat property.

The [Open Source Definition](https://opensource.org/osd) has been on the OSI website for 25 years.
During this time, it has regularly been contested.


In about 2019 when MongoDB sought OSI approval for its SSPL license (and failed to secure it).
Since then, several companies have followed suit and adopted various new licenses with similar commercial non-compete clauses. The non-OSI compliance has led to new terms such as [Source Available](https://en.wikipedia.org/wiki/Source-available_software), [Open Core](https://en.wikipedia.org/wiki/Open-core_model), [Fair Code](https://faircode.io/), [Commons Clause](https://commonsclause.com/) and [Fair Source](https://fair.io/).  Note, [I have written an analysis of Fair Source](/posts/fair-source).  It seems the community at large has come to the conclusion that the easiest solution in these cases is to just coin new terms and start initatives.

GitHub - founded in 2008 - is by far the largest code platform with more than 100 million developers globally. Its reach eclipses that of the affiliates and sponsors lists combined.
Most recently, Scott Chacon, cofounder of GitHub remarked that most developers understand "open source" to mean "public on GitHub" and suggested [redefining "open source"](https://x.com/chacon/status/1754883687668232334) as such.  The gravity of this observation is not to be underestimated.  GitHub has indeed brought in tens of millions of developers who may not be up to speed on the whole "Open Source" definition.  And it *is* tempting to just redefine a term to accommodate them all at once. But what would this actually solve?  If we don't disagree with the OSD, then everyone agrees, and there are no ambiguities whatsoever that could be resolved by redefining.  In fact, redefining would create ambiguities (at the global scale) and this wouldn't really solve the need to educate people either.  At the end of the day, they still need to know if they're allowed to commercially redistribute, for example.

I think redefining "Open Source" today would be tremendously impractical.  It is, in fact, a tremendous achievement that most of the whole world can agree on what a term means.  It is truly exceptional that all over the world, goverment offices, startups, students, academia, and so on, are either already perfectly aligned, or can align, with a minimum of self-education.  To try to change that, after 25 years would create so much friction that far outweighs any perceived benefits.

It's much easier to just coin a new term and promote that instead, which is this case is what happened with Fair Source.


But the fact of the matter is, they were not the first to coin the term, they don't have a trademark, and it has been consistly contested despite their garguantuan efforts to get the whole world aligned (with good results in the programming community, in goverments, and the industry)

### In conclusion

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
