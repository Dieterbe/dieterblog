+++
title = 'Software Values'
date = 2025-02-15T16:28:19+02:00
draft = true
+++

**DRAFT**

If you've been involved with Open Source in any way, you're aware of the prevalence of the OSI "open source definition", which itself is based on the free software foundation's "4 freedoms".
Open Source fans (myself included) tend to put those front and center when it comes to procuring software, but do they still accurately represent what really matters?

In this article, I explore the idea that no, they actually don't correspond well to what most people really need from software, I propose some criteria that I believe are more representative of what really matters, and how those ultimately relate to Open Source (and similar concepts such as Open Core, Source Available, Fair Source, etc).

Note, when I say user, I mean anyone who procures or uses software and has certain expectations of it. This can be an individual, a small or large business, or government.

Before we get into it, I need to touch on on the "Open Source as an insurance" idea.

# The (Open Source as an) insurance fallacy

Open Source software is sometimes viewed as an insurance: if your SaaS vendor goes bankrupt (or for on-prem software, the licensor), then - so the reasoning goes - the source code will save you.  You can build & run the code yourself or another vendor will appear and offer a similar service.  There are various shortcomings with this reasoning:

* software can be extremely complicated to maintain and operate when it was designed and built by others, and especially when it's SaaS.  
* it is unlikely that a vendor will attempt a business model that has demonstrably failed, or create a new business on software they don't understand as well.
* Offering indemnification and standards compliance is also risky if you don't know the software well. So for enterprise software, this doesn't really happen.
* for SaaS, this requires a data migration, which is usually a painful process requiring lots of ad-hoc improvisation to compensate for missing support, if it's even possible to access your data to begin with.
* you might be able to run it yourself.  This can work well, sometimes for years. Sometimes this strains your own resources and therefore doesn't last long.  The primary factor is how "fit for use" the software is for your needs.  Open vs closed source by itself is usually not a big factor (though in some cases, it correlates to software quality).  The ability to inspect code (as allowed in open source, source available, fair source, etc paradigms) provides some assurance in theory (e.g. to build trust that you're executing something more likely to be "safe"), but in practice what I've seen is: you're either a serious enterprise who needs more than just being able to read the code before running it (you need a trusted partner, indemnification, SLA's, standards compliance guarantees, etc), or you're not, in which case code access is not practically beneficial (too time consuming to really go through it.  Although perhaps AI tools may help here soon?)

TODO clarify here: inspect code for security vs ability to patch for your own needs

All the above boils down to: source code access is rarely a meaningful form of "insurance". Certainly not for SaaS and enterprise use cases. But possibly for SME's and individuals.

# the 4 essential free software freedoms

according to https://www.gnu.org/philosophy/free-sw.en.html#four-freedoms software is free if it meets these 4 freedoms:

> The freedom to run the program as you wish, for any purpose (freedom 0).  
> The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.  
> The freedom to redistribute copies so you can help others (freedom 2).  
> The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.


(OSI's OSD is basically equivalent, just phrased differently)

Let's dig into all of these separately

> The freedom to run the program as you wish...

In practice, people and organisations have certain desires (e.g. cloud based, self-hosting, available on mobile, etc), which can be met regardless of any source code access.
Typically the "run as you wish" is constrained within the boundaries of what is made possible through ardent effort.  you can't easily take a cloud based tool and turn it into a mobile app, for example. it would mean rewriting the whole thing and basically ending up with a different product.
Therefore:
- it is a function of the software, not a "freedom" you can slap on top of it.
- the "desires" to e.g. run in a certain way or on a certain place is simply a desire for the software to have that specific functionality, just like any other functionalities you may require.

> ...for any purpose

First of all: the "run for any purpose" receives a lot of scrutiny in the OSS community, where ethical concerns lead to folks advocating for the exact opposite (essentially "do not use this software for 'evil'").  But that would land us in dictatorial/non-free waters, and has not been included as a concept in either free software, or OSI's definition.

software users indeed don't want to be at the mercy of a single vendor as far as when and what for they can use the software. Especially not when this gets tightened up down the road.
Unfortunately, Open source as an insurance policy, as we saw above, is mostly a theoretical idea, and not very practical, except maybe for SME's/individuals.

> The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.  

Freedom to study how the program works, purely for the sake of it, is for curious geeks who want to learn specific programming techniques and when the software implements something novel which isn't easily learned through more appropriate learning resources (courses, tutorials, etc), this is an edge case IMHO. Personally I've learned a lot from studying various OSS projects such as NSQ and Prometheus, but this has little to do with procuring software.

The most important value here is that you want software that does what you need it to.   But if any time software didn't do what we need, we'd have to study the project, make our own changes and rebuild it, (and sometimes host it yourself if upstream doesn't like your changes) our lives and economy would slow to a halt.   It's extremely impractical.   It reeks more of an anti-pattern.


> The freedom to redistribute copies so you can help others (freedom 2).  

The more practical way of phrasing this would be "software should be available to those who need it".  Has nothing to do with source code access.

> The freedom to distribute copies of your modified versions to others (freedom 3).  By doing this you can give the whole  
> community a chance to benefit from your changes.  Access to the source code is a precondition for this.  

This falls back again to people need software that meets their needs.  I don't think anyone sees it as a benefit when functionality you need was written by a 3rd party or volunteer rather than by the main author or than the vendor you're working with.  In fact, if it was the main vendor that did it, you can reasonably expect it to be better understood by the vendor and therefore better supported.  Although, sometimes innovations come from 3rd parties.  (I've seen this firsthand, where some of the best aspects of the database I worked on were contributed by a customer)

In summary, the most appealing aspect of of open/free software is that it may function somewhat as an insurance policy if you're an SME or individual.
Sometimes OSS leads to better quality software, but it's also common for OSS to undermine the economical feasability of software and completely undermine the projects development or even cause premature death.


# Actually relevant software values

What do users **really** care about?
In my experience, the free software values don't correspond well to what users actually want.  I think what people actually want is this:

1) Software should be fit for use
2) Longevity: software should either stay around (and receive improvements), or it should be relatively seamless to migrate to alternatives.
3) Secure, stable. Supported. For enterprise usage, you need certain compliance and certification marks.
4) Limitations on "bad-actor vendor" lockin.
5) Cost effective to produce and consume
6) Compensation for those who do the work

and then I think there's 2 which are perhaps a bit more fringe:

7) Generativity
8) Optional charitability.

Let's explore them in more detail.

The first three values are closely related and can be covered at once:

> Fit for use.  
> Longevity: software should either stay around (and receive improvements), or it should be relatively seamless to migrate to alternatives.  
> Secure, stable. Supported. For enterprise usage, you need certain compliance and certification marks.

There is a certain irony that open source licenses usually explicitly disavow fitness for any particular use, even if that's the most important factor when procuring software, and despite the software fitting the intended purpose well, clauses around this are often left for commercial agreements, for commercial open source software anyway)

* For applications with a specific, common, non-critical need (e.g. media players) community/voluntary OSS projects are a great solution to achieve these goals (e.g. VLC media player). There is so much drive among volunteers to build a high quality, secure and lasting piece of software that it wouldn't even make sense to compete with commercially directly and pay to do the work, unless it can be done better (e.g. streaming services).
* foundation/platform stuff by nature often makes sense to be open source because this is a case where source code access is actually highly relevant.  Sometimes commercial players are involved, and when they're not, it's usually at the peril of some voluntary developers. (see compensation below)
* For more niche (e.g. enterprise), critical (e.g. medical/military) and/or large, complicated applications (e.g. operating systems), the best way to achieve this is with one or more profitable business pushing the software forward.  (e.g. Grafana, Sentry, Android).  They may or may not include open source, open core, fair source, etc in their strategy.  I'm not so familiar with military/medical equipment but pretty sure that's closed off.
Expecting random strangers to meaningfully push such complicated projects forward at a high level is delusional - although sidenote: for commercial open source software projects, the community contributions can be significant, which allows for both more value creation and capture and in the end, everyone is usually better off - so the main point is you need a commercial entity driving it, even if that entity may employ an open source (or similar) concept as part of their business strategy.
Sometimes multiple vendors collaborate and jointly drive projects forward (see all the companies around Linux, and Cloudera/Hortonworks around hadoop), which necessitates some sort of open source licensing.  Whereas open source works well to gain reliability/security for software that is not overly complex and is inspected by many, it becomes less relevant for large scale projects with fewer eyeballs on them.  For those, you need to incentivize, e.g. Hacker bounty programs work great (open source or not).

If it's closed source *and* run by a single company there is a risk of the vendor mistreating clients and/or going bankrupt.  We've already seen that OSS is not a good insurance policy (for enterprises).
Having a reasonable migration path to an alternative vendor that offers a similar product can be a good solution here. Let's explore this more in the vendor lock-in section below.

What I see all too commonly is that Open Source software gets created, and sure, it may be OSI compliant, but it's missing various needed features, runs out of steam because it's not funded well, or misses the oh-so important marketing to actually make you aware that it even exists in the first place.  Yes, open source can be a great mechanism, but it shouldn't be the primary consideration. It should be part of a larger set of tradeoffs within a strategy. Which in a case like this, should be a business strategy.  Vendors will spring up to address your needs.

To summarize:
* OSS is best for specific, common, non-critical needs and foundational platform code. Commercialization is optional.
* Commercialization is needed for enterprise/critical/large needs. OSS is optional. (though it can be a good part of a business strategy)

> Limitations on "bad-actor vendor" lockin.

Being locked in to a vendor is not a problem as long as they treat customers right.  But many vendors will treat customers poorly if they can get away with it.
We already covered why OSS is not a good insurance policy (for enterprises), and conversely just because an enterprise vendor has open source as part of their strategy, that should give little confidence  that they will treat their customers well.  I furthermore believe it's naive to jump to a conclusion such as "Users need open standards and data freedom", "there always needs to be a migration path" etc.
When you let vendors compete in the market and let users (customers) be responsible for their own vendor selection criteria they will tend to (in my experience) make wise enough choices, not necessarily maximizing their "freedoms" as such, but making an informed choice of a particular vendor where the overall package (quality of the service, promise of longevity, risk of future disruptions due to having to migrate off of the vendor, cost, etc) comes out best. 

You can also get yourself "locked in" with open source code that is *not* driven by any vendor.  What if issues or incompatibilities arise and there is no one to support it?  Getting out of it usually means paying own staff or contractors to fix the mess, if it's even realistically possible.

I believe that the market can handle these concerns by itself, without trying to interfere with procurement selection criteria or "certifying" vendors via OSI compliant licenses (which in practice lose some significance in the context of open core, additional contracts, etc).  Open Source, migration tools, open standards, etc are all tools that change the dynamics, but none of them is a necessity.  Finally, the market works such that when a vendor starts showing abusive tendencies towards its clients, competitors will spring up to do it better.  As a user, this is just as good as an insurance policy as "open source" is.

Of course, vendor lock-in is sometimes unavoidable, especially for mission-critical, entrenched and heavily regulated systems (e.g. finance, military, medical). But especially here, open source won't save you, since the product is not the code (the "insurance policy" idea definitely doesn't work here).  And as we've seen, disruption is always possible (e.g. spaceX)

In summary: ultimately, competitive forces in the market will result in an equilibrium where users are ultimately treated with whatever freedoms they deserve.

> Cost effective to produce and consume

More value for less cost.  This fuels a growing economy and thriving society.
There's a few ways to achieve this:
* innovation driven by competition and by reinvesting profits: this requires a healthy, lean business which can capture some of the value.
* leveraging work done by others. 
This is why COSS (Commercial Open Source Software) can work well: but you need to find a sweet spot: getting enough contributions so that everyone (users and vendor) benefits, but not so much that the business is no longer the main innovator and becomes unviable. When there is less cash flow, there is less to reinvest in innovation.  and always such that people who put in the work, do either out of self-interest or get compensated. (see section below)

To summarize: cost effectiveness is sometimes enabled by OSS, and sometimes undermined by it. It depends on context and business model.

> Compensation for those who do the work

Regardless of which company they work for, if any.  If you do something valuable, it deserves compensation.
This can be achieved by having code be written by software vendors and them monetizing it (what a concept!), by users contributing to a shared OSS project in their own best interest, or of course, the various compensation schemes that are starting to spring up (sponsoring, tip jars, bounties, etc) but need to mature.

Situations where a developer's hobby projects gets commercially adopted, and then said developer is burdended with the support load and responsibilities without compensation, is a situation to avoid. But there are various solutions to this.

To summarize: Proprietary software has a more predictable compensation (for now).  Currently, OSS has a "lack of compensation" problem for some cases/projects, but I think we'll overcome that.

> Fringe: Generativity

Technology that is generative, fuels more further technology and accelerates more overall progress.
Good examples are transistors, the internet, and mobile phones.
Generally speaking, if technology is more generative, it is objectively better. For software I think of components such as libc, BSD, Linux, bash, TCP/IP, etc.  Often Open Source foundational components such as operating systems and platform libraries.  But the list also includes platforms such as Windows, iOS, macOS and SAP, which despite being closed, have empowered tremendous technological progress.  We could say the same about GPS satellites or SpaceX rockets, which operate on proprietary technology.

But the boundary keeps creeping up: we built on top of transistors, then on top of operating systems, on top of the internet, on top of GPS, etc.  There's always reasons why it makes sense for some applications to become platforms and to build more stuff on top / around them.  Think workflow automation, integrations, etc.  I see no reason why even the new layers would need to be open source in order to be highly generative (e.g. both Grafana and Zapier integrate with other systems using their own, almost opposite, strategies). 

In summary: there seems to be no correlation between generativity and open source. (this one actually surprised me)


> Fringe: Optional charitability.

I think part of what's attractive to building "open source" is that it feels good to give away a certain (base) level of service for free.
But it doesn't have to be about giving away source code only. You can give a great free cloud plan, software discounts for students, a public good service such as wikiPedia, discounts based on local market conditions, etc.
I think this boils back down to what we said about what's the best way to build software that is "fit for use" and has longevity.  Whoever can do this best (a community, a company, or a well funded non-profit such as WikiPedia) is best equipped to create a lot of value, and then to decide to not capture some of it.
While this is sometimes done in a genuine way, often giving away code is seen as the start of a relationship which may turn into business relationship, and similarly the free base plans, discounts etc often have the same purpose and serve to not capture value when there isn't much to capture, but there may be more to capture later - e.g. when the student has become a professional.
This can be done in a deceitful way to try to lock in users and try to force expensive conversions/upgrades later, but I think everything we said about market dynamics applies here too.



# conclusion

I don't think free software's "4 freedom's", nor's OSI's "open source definition" capture particularly well what software users primarily care about. And I see many make the mistake of following these ideas, perhaps bit too blindly.  Perhaps because they are the most well known "selection criteria" that are written down so explicitly.

I have written down what I believe to be more relevant criteria / considerations, and tried to reason through how those relate to Open Source.

I seem to arrive at:

* Open Source is best for specific, common, non-critical needs and foundational platform code. Commercialization is optional.
* Commercialization is needed for enterprise/critical/large needs. OSS is optional.

For certain businesses and industries, using a strategy involving "open source" (or any of its other forms, open core, source available, fair source, etc) can be a fantastic way to do it.  A win-win for everyone.  But often, it may not be. (maybe a topic for another day)

For customers, whether software is open source or not seems to matter less than us OSS advocates like to believe. Indirectly, it is relevant when it allows a business to be more healthy (and to charge less), and/or when it improves the product in meaningful ways.  But directly, as such, it doesn't seem to matter.  The "open source as an insurance" idea seems overrated, except for individuals / SME's where it may be more relevant. Beyond that, I think the market auto-regulates and decision makers deserve more credit for making choices based on what criteria are relevant to *them*.


## What about Collaboration?

There's something humane about collaborating with others, and it's a reason we enjoy open source so much.
Does it need to be global community of strangers? It feels nice, perhaps because it's a novelty.  It is not a necessity.  Plenty of ways to collaborate, e.g. with your own colleagues.
Still it feels like a net positive.

All in all, I would always lean towards OSS, all other things equal.  But hopefully it's clear that those other things are usually far from equal.


# DRAFT STUFF - TO BE REMOVED

is the difference (what makes COSS successful) community contributions?



### Issues with OSS
- Compensation
- Not fit for use
- Code needs expertise. It's not about the code
- Perception of Quality if free




community/free contributions:
0   ----- some    --- half    -- much  --- all
                                            ^
                                            virtually impossible for commercial entity (unless the software has strict enterprise requirements, but then it usually is not built from community either)
^
commercial domination
                       ^
                      careful balance: company to work well with community
