+++
title = 'Why does the OSI get to police what Open Source means?'
date = 2024-08-18T09:57:53+02:00
draft = true
+++

> Computer science, too, must exist in an uneasy alliance with industry

From the book [Open Sources: Voices from the Open Source Revolution](https://www.oreilly.com/openbook/opensources/book/)

Who gets to say exactly what a term means, or doesn't mean?  Today, the word "literally" means its opposite, and what is DevOps anyway?

When communities form and evolve along with the world around them, inevetably incompatible viewpoints emerge and can cause fractures. This was as true in the 1990's as it is in the 2020's.

Back in 1998, there was a [small group of folks who felt that the verbiage at the time (Free Software) had become too much of a philosophical movement](https://web.archive.org/web/20021001164015/http://www.opensource.org/docs/history.php). (note: the Free Software Foundation was founded 13 years prior, in 1985, and informal use of "free software" had around since the 1970's)
They felt they needed a new word "to market the free software concept to people who wore ties". ([source](https://www.oreilly.com/openbook/opensources/book/perens.html))  
(somewhat ironic since today many of us like to say "Open Source is not a business model")

Bruce Perens - an early Debian project leader and hacker on free software projects such as [busybox](https://www.busybox.net/) - had authored the first [Debian Free Software Free Guidelines](https://en.wikipedia.org/wiki/Debian_Free_Software_Guidelines) in 1997 which was turned into the first [Open Source Definition](https://en.wikipedia.org/wiki/The_Open_Source_Definition) when he founded the [OSI](https://opensource.org) (Open Source Initiative) with Eric Raymond in 1998.

Eric Raymond is of course known for his seminal 1999 essay on development models ["The cathedral and the bazaar"](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar), but he also worked on [fetchmail](https://en.wikipedia.org/wiki/Fetchmail) among others.

> At the time of its conception there was much criticism for the Open Source campaign, even among the Linux contingent who had already bought-in to the free software concept. Many pointed to the existing use of the term "Open Source" in the political intelligence industry. Others felt the term "Open" was already overused. Many simply preferred the established name Free Software. I contended that the overuse of "Open" could never be as bad as the dual meaning of "Free" in the English language--either liberty or price, with price being the most oft-used meaning in the commercial world of computers and software

From [Open Sources: Voices from the Open Source Revolution: The Open Source Definition](https://www.oreilly.com/openbook/opensources/book/perens.html)

It seems that even at the time, there was criticism, but only to the term "Open" in general and to "Open Source" only in a completely different industry.

Were there other voices who opposed OSI's definition of "Open Source"? Hard to know for sure, but I'm not aware of any.  
Was the term already being used in the software industry for other purposes?  Hard to know for sure, but seems unlikely.

From Bruce Perens' own account:

> I wrote an announcement of Open Source which was published on February 9 [1998], and that’s when the world first heard about Open Source.

source: [On Usage of The Phrase “Open Source”](http://perens.com/2017/09/26/on-usage-of-the-phrase-open-source/)


With the evidence we have today, it seems fair to say the OSI was the leading, if not singularly authorative, voice within the new "Open Source" community.

Since then, adoption of the term "Open Source" has taken off like wildfire across software projects, from hobby projects to large industry players.  OSI's scope of influence has grown to cover [goverment in the US, the UK, some of the EU, Asia and Australia](https://opensource.org/authority), is sponsored by [a small selection of the world's largest tech companies](https://opensource.org/sponsors) - including GitHub, tied to non-profit/foundation [affiliates](https://opensource.org/affiliates/list) and [organizations who've vouched for OSI's authority](https://opensource.org/blog/osd_affirmation).
As I was checking out these lists, I actually found them rather... surprisingly short? But I assume there are a multitude more organizations who vouch for OSI, yet haven't initiated any official relation.  E.g. Grafana Labs [bets its entire business on OSI compliance](https://grafana.com/blog/2021/04/20/qa-with-our-ceo-on-relicensing/), yet is nowhere to be found in these lists. (I've reached out to my connections there to see if we can change that).

But we have more good datapoints:
* the multitude of voluntary "OSI defense" happening on platforms such as [X](https://x.com/chacon/status/1754820325022294393), reddit, etc.  It's a deep rooted part of the industry, even if not formalized.
* Linux Distributions: Debian, while affiliated with OSI, maintains its own license review process, though it is similar to OSI's ([source](https://www.debian.org/News/2012/20120330.en.html), Red Hat [stands with OSI](https://www.redhat.com/en/topics/open-source/what-is-open-source) and [so does Ubuntu](https://ubuntu.com/community/ethos/mission).

Does all this mean the OSI can police the term "Open Source"? It doesn't.

You cannot legally stop someone from using or misusing a word.  However, if you have a trademark, you can seek legal repercussions, which is a strong incentive for others not to misuse your mark.  Unfortunately, the OSI never succeeded in obtaining the trademark.  [As they explain](https://opensource.org/pressreleases/certified-open-source.php) the term was too widely adopted even already in 1999, rendering OSI (or anyone else) unable to claim ownership of it. 🤔


The [Open Source Definition](https://opensource.org/osd) has been on the OSI website for 25 years, to my knowledge largely uncontested.
But that changed in about 2019 when MongoDB sought OSI approval for its SSPL license (and failed to secure it).
Since then, several companies have followed suit and adopted various new licenses with similar commercial non-compete clauses. The non-OSI compliance has led to new terms such as [Source Available](https://en.wikipedia.org/wiki/Source-available_software), [Open Core](https://en.wikipedia.org/wiki/Open-core_model), [Fair Code](https://faircode.io/), [Commons Clause](https://commonsclause.com/) and [Fair Source](https://fair.io/).  Note, [I have written an analysis of Fair Source](/posts/fair-source).  It seems the community at large has come to the conclusion that the easiest solution in these cases is to just coin new terms and start initatives.

GitHub - founded in 2008 - is by far the largest code platform with more than 100 million developers globally. Its reach eclipses that of the affiliates and sponsors lists combined.
Most recently, Scott Chacon, cofounder of GitHub remarked that most developers understand "open source" to mean "public on GitHub" and suggested [redefining "open source"](https://x.com/chacon/status/1754883687668232334) as such.  The gravity of this observation is not to be underestimated.  GitHub has indeed brought in tens of millions of developers who may not be up to speed on the whole "Open Source" definition.  And it *is* tempting to just redefine a term to accommodate them all at once. But what would this actually solve?  If we don't disagree with the OSD, then everyone agrees, and there are no ambiguities whatsoever that could be resolved by redefining.  In fact, redefining would create ambiguities (at the global scale) and this wouldn't really solve the need to educate people either.  At the end of the day, they still need to know if they're allowed to commercially redistribute, for example.

I think redefining "Open Source" today would be tremendously impractical.  It is, in fact, a tremendous achievement that the whole world can agree on what a term means.  It is truly exceptional that all over the world, goverment offices, startups, students, academia, and so on, are either already perfectly aligned, or can align, with a minimum of self-education.  To try to change that, after 25 years would create so much friction that far outweighs any perceived benefits.

It's much easier to just coin a new term and promote that instead, which is this case is what happened with Fair Source.

In conclusion, the OSI is as authentic and credible as it gets, the open source definition has been widely accepted in the global community, industry, and many governments, which it collaborates with.  However, they cannot legally police the term "Open Source", and technically you *can* use it with a different meaning.  But that seems incredibly impractical and pointless.  It's also a fast way to antagonize most of the developer community.  What the OSI has achieved is a unique and remakable feat, and I believe the only sensible course of action is to keep them as the official un-official shepherds of "Open Source".  Of course, Open Source is not the only model, there are plenty of others to choose from, such as Source Available or [Fair Source](/posts/fair-source).  And if those don't fit your need, you can always create a new one.   Even Bruce Perens himself is working [on an "Open Source" reimagined](https://www.theregister.com/2023/12/27/bruce_perens_post_open/) which will be a distinct initiative as well.
