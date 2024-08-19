+++
title = 'Fair Source'
date = 2024-08-16T09:57:53+02:00
draft = true
+++

[Fair Source](https://fair.io/) is the latest option for software projects driven by a single vendor wanting to combine monetization, a high rate of contributions to the project (supported by said monetization), community collaboration and direct association with said software project.

Source-available & Non-Compete licensing have existed in various forms, and have been tweaked and refined for decades, in an attempt to combine just enough proprietary conditions with just enough of Open Source flavor, to find that perfect tradeoff in keeping a vendor, and their community and customers happy.

Succintly, Fair Source licenses provide much of the same benefits to users as Open Source licenses, except outsiders are not allowed to build their own competing service based on the software, however after 2 years, the software automatically becomes MIT or Apache2 licensed, and at that point you can pretty much do whatever you want.

Earlier projects such as - not to be confused - [Fair Code](https://faircode.io/) and [Commons Clause](https://commonsclause.com/) are similar, except they don't have the delayed open source publication.

It seems we have reached an important milestone in 2024: on the surface, "Fair Source" is yet another new initiative that positions itself as a more business friendly alternative to "Open Source", but the delayed open source publication (DSOP) model has been refined to the point where the licenses are succint, clear, easy to work with and should hold up well in court.
Several technology companies are choosing this software licensing strategy (Sentry being the most famous one, you can see the others on their website).

My 2 predictions:
* a governance legal entity will appear soon, and a trademark will follow after.
* we will see 50-100 more companies in the next couple of years.

In this article, I'ld like to share my perspective and address some - what I believe to be - misunderstandings in current discourse.


### The licenses

At this time, the Fair Source ideology is implemented by the following licenses:

* [FSL](https://fsl.software/)
* [FCL](https://fcl.dev/)
* [BSL/BUSL](https://mariadb.com/bsl-faq-mariadb/)

The latter are more tricky to understand can have different implementations.
FCL and FSL are nearly identical. They are clearly and concisely written and embody the Fair Source spirit in the most pure form.

Seriously, try running the following in your terminal. Sometimes as an engineer you have to appreciate legal text when it's this concise, easy to understand, and diffable!

```
wget https://raw.githubusercontent.com/keygen-sh/fcl.dev/master/FCL-1.0-MIT.md
wget https://fsl.software/FSL-1.1-MIT.template.md
diff FSL-1.1-MIT.template.md FCL-1.0-MIT.md
```

I will focus on FSL and FCL and FSL, the Fair Source "flagship licenses".

### Is it "open source, fixed", or an alternative to open source? Neither.

I've seen people refer to Fair Source as "an alternative" to Open Source, as "an improved Open Source", and to FSL as if it is Open Source.  
I don't think it's any of these.  Let me explain.

First, we'll need to agree on what the term "Open Source" means. It has come under some scrutiny. But let's go with the OSI definition, which is also what the folks behind FSL/Fair Source seem to agree with: after some initial conversations about FSL using the "Open Source" term, they've defined their own new term and I've seen a lot of meticulous work (e.g. [fsl#2](https://github.com/getsentry/fsl.software/issues/2) and [fsl#10](https://github.com/getsentry/fsl.software/issues/10) on how they articulate what they stand for.
See my other article, [Why does the OSI get to police what Open Source means](/posts/why-does-the-osi-get-to-police-what-open-source-means)

The Open Source Definition debate is why I hope the Fair Source folks will file a trademark if this projects gains more traction.

Importantly, **OSI's definition of "Open Source" includes non-discrimination and free redistribution**.

<br>

When you check out code that is FSL licensed, and the code was authored:

1) less than 2 years ago: it's available to you under terms similar to MIT, except you cannot compete with the author by making a similar service using the same software
2) more than 2 years ago: it is now MIT licensed. (or Apache2, when applicable)

While after 2 years, it is clearly open source, the non-compete clause in option 1 is not compatible with the set of terms set forth by Open Source.  (such a license is often referred to as "Source Available")
I think this is very clever approach, but I think it's not all that useful to compare Fair Source to Open Source. It has a certain symmetry to Open Core:
* In an Open Core product, you have a "scoped core": a core built from open source code which is surrounded by specifically scoped pieces from proprietary code, for a indeterminate, but usually many-year or perpetual timeframe
* With Fair Source, you have a "timed core": the open source core is all the code that's more than 2 years old, and the proprietary bits are the most recent developments (regardless which scope they belong to).

Open Core and Fair Source both try to balance open source with business interests: both have an open source component to attract a community, and a proprietary shell to make a business more viable.
Fair Source is a licensing choice that's only relevant to business, not individuals. How many business monetize pure Open Source software? I can count them on one hand.  The vast majority go for something like Open Core.  This is why the comparison with Open Core makes much more sense.

**A lot of the criticisms of Fair Source suddenly become a lot more palatable when you consider it an alternative to Open Core.**

As a customer, which is more tolerable? proprietary features or a proprietary 2-years worth of product developments? I don't think it matters nearly as much as some of the advantages Fair Source has over Open Core:

- Users can view, modify and distribute (but not commercialize) the proprietary code. (with Open Core, you only get the binaries)
- It follows then, that the project can use a single repository and single license (with Open Core, there are multiple repositories involved)

Note that you can also devise hybrid approaches, and turn some of these assymetries into symmetries. Here are some ideas:

* a Fair Source core and Closed Source shell. (more defensive than Open Core or Fair Source seperately). (e.g. [PowerSync does this](https://www.powersync.com/legal/overview)) 
* an Open Source core, with Fair Source shell. (more open than Open Core or Fair Source seperately).
* Open Core, with Source Available shell (users can view, modify and distribute the code but not commercialize it). I would like to see this. This would be the "true" symmetrical counterpart to Fair Source. It would also allow to put all code in the same repository.  Although this benefit works better with Fair Source because any contributed code will definitely become open source, thus incentivizing the community more.
* etc.



### Non-Competition

The [FSL introduction post](https://blog.sentry.io/introducing-the-functional-source-license-freedom-without-free-riding/) states:

> In plain language, you can do anything with FSL software except economically undermine its producer through harmful free-riding


The issue of large cloud vendors selling your software as a service, making money, and contributing little to nothing back to the project, has been widely discussed under a variety of names. This can indeed severely undermine a project's health, or kill it.

(Personally, I find discussions around whether this is "fair" not very useful.  Businesses will act in their best interest, you can't change the rules of the game, you do have control over your own licensing and strategy)

Here, we'll just refer use the same terminology that the FSL does, the "harmful free-rider" problem


The statement is factually incorrect.  Something like this would be more correct:

> In plain language, you can do anything with FSL software except offer a similar paid service based on the software when it's less than 2 years old.


What's the difference? There are different forms of competition that are *not* harmful free-riding.

Multiple companies can offer a similar service/product which they base on the same project, which they all contribute to. They can synergize and grow the market together. (aka "non-zero-sum" if you want to sound smart). I think there are many good examples of this, e.g. Hadoop, Linux, Node.js, OpenStack, Opentelemetry, Prometheus, etc.

When the [FSL website](https://fsl.software) makes statements such as "You can do anything with FSL software except undermine its producer", it seems to forget some of the best and most ubiquitous software in the world is the result of synergies between multiple companies collaborating.

Furthermore, when the company who owns the copyright on the project turns their back on their community/customers wouldn't the community "deserve" a new player who offers a similar service, but on friendly terms? The new player may even contribute more to the project. Are they a harmful free-rider? Who gets to be judge of that?

Let's be clear, FSL allows no competetion whatsoever, at least not during the first 2 years.  What about after 2 years?

Zeke Gabrielse, one of the shepherds of Fair Source, [said it well here](https://keygen.sh/blog/keygen-is-now-fair-source/):

> Being 2 years old also puts any SaaS competition far enough back to not be a concern

Therefore, you may as well say **no competition is allowed**. Although, in Zeke's post, I presume he was writing from the position of an actively developing software project.
If it becomes abandoned, the 2 years countdown is an obstacle, an overcomable one, that eventually does let you compete, but in this case, the copyright holder probably went bust, so you aren't really competing with them either.  The 2 year wait can be needlessly painful for folks in such a situation.  If a company is about to go bust, they would likely immediately release their Fair Source code as Open Source, but I wonder if this can be automated via the actual license text.

## Perverse incentives

Humans are notoriously bad about predicting 2nd order effects.   So I like to try to. What could be some second order effects of Fair Source projects? And how do they compare to Open Core?

* can companies first grow on top of their Fair Source codebase, take community contributions, and then make an internal closed source fork, shutting out the community? The answer to this may depend on what kind of CLA is in place. (with Open Core, you can't take in external contributions on proprietary parts, but can similarly relicense the core)
* if you enjoy a privileged position where others can't meaningfully compete with you based on the same source code, that can affect how the company treats its community and its customers. It can push through undesireable changes, it can price more aggressively, etc. (these issues are the same with Open Core)
* With Open Source & Open Core, the company is incentivized to make the code well understood by the community. Here, it would still be sensible (in order to get free contributions), but at the same time, by hiding design documents, subtly obfuscating the code and witholding information it can also give itself the edge for when the code does become Open Source.

### Developer sustainability

The [FSL introduction post](https://blog.sentry.io/introducing-the-functional-source-license-freedom-without-free-riding/) also says:

> We value user freedom and developer sustainability. Free and Open Source Software (FOSS) values user freedom exclusively. That is the source of its success, and the source of the free-rider problem that occasionally boils over into a full-blown tragedy of the commons, such as Heartbleed and Log4Shell.

F/OSS indeed doesn't involve itself with sustainability, because of the simple fact that Open Source has nothing to do business models and monetization.
As stated above, it makes more sense to compare to Open Core.

It's like saying asphalt paving machinery doesn't care about funding and is therefore to blame when roads don't get built. Therefore we need tolls. But it would be more useful to compare tolls to road taxes and vignettes.

Of course it happens that people dedicate themselves to writing open source projects, usually driven by interest, don't get paid, get volumes of support requests (incl from commercial entities), which can become suffering, and can also lead to codebases becoming critically important, yet critically misunderstood and fragile. This is clearly a situation to avoid, and there are many ways to solve the problem ranging from sponsorships (e.g. [GitHub](https://github.com/sponsors), [tidelift](https://tidelift.com)), bounty programs (e.g. [Algora](http://algora.io)), direct funding (e.g. [Sentry's 500k donation](https://blog.sentry.io/we-just-gave-500-000-dollars-to-open-source-maintainers/)) and many more initiatives that have launched in the last few years. Certainly a positive development.  Sometimes formally abandoning a project is also a clear sign that puts the burden of responsibility onto whoever consumes it and can be a relief to the original author.  If anything, it can trigger alarm bells within corporations and be a fast path to properly engaging and compensating the author.  There is no way around the fact that developers (and people in general) are generally responsible for their own wellbeing and sometimes need to put their foot down, or put on their business hat (which many developers don't like to do).  No amount of licensing can change this hard truth.


Furthermore, you can make money via Open Core around OSI approved open source projects (e.g. [Grafana](https://grafana.com)), consulting/support, and many companies that pay developers to work on (pure) Open Source code (e.g. Meta, Microsft, Google, etc).  Companies that try to achieve sustainability (and even thriving) on pure open source software for which they are the main/single driving force, are extremely rare. ([Chef](https://chef.io) tried, and now [System Initiative](https://www.systeminit.com/about-us/) is trying to do it better. I remain skeptical but am hopeful and am rooting for them to prove the model)


Doesn't it sound a bit ironic that the path to getting developers paid is releasing your software via a non-compete license?

Do we reach developer sustainability by preventing developers from making money on top of projects they have or want to contribute to?

(Open Core shuts out people similarly, but many of the models above, don't. Note, Fair Source *does* allow to make money via consulting and auxiliary services *related* to the software)

### AGPL

The [FSL website](https://fsl.software/) states:

> AGPLv3 is not permissive enough. As a highly viral copyleft license, it exposes users to serious risk of having to divulge their proprietary source code.

Just when I thought the industry had moved beyond this fear mongering, it appears again on the FSL website. Complying with AGPL is rather easy, my rule of thumb is to say you trigger copyleft when you "ship".  Most engineers have an intuitive understanding of what it means to "ship" a feature, whether that's on cloud, or on-prem.  In my experience, people struggle more with patent clauses or the relation between trademarks and software licensing.   

Even Heather Meeker, the lawyer consulted to draft up the FCL has spoken out against both the [virality] discourse (https://heathermeeker.com/2019/03/05/open-source-and-the-eradication-of-viruses/) and [AGPL FUD](https://heathermeeker.com/2023/10/13/agpl-in-the-light-of-day/)

Furthermore, it seems a bit strange to say FSL is more permissive than AGPL, when FSL has a clear non-compete clause, and the AGPL allows any and all forms of competition.


### Conclusion

I think Fair Source (and FSL) has a lot to offer.  It's a very compelling alternative to Open Core. As it stands today it's more generous towards the community than Open Core is.  It's well executed.
It ties up a lot of loose ends from previous initiatives (Source Available, BSL and other custom licenses) into a neat package. It's easy to implement and is arguably more viable than Open Core is, in its current state today.   Although I think CLA's may be warranted which would introduce some complexity again. 
When comparing to Open Source, the main question is: **which is worse, the "harmful free-rider problem", or the non-compete?** (Anecdotally, my gut feeling says the former, but I'm on the look out for data driven evidence).
When comparing to Open Core, the main question is: **is a business more viable keeping proprietary features closed, or making them source-available (non-compete)?**.

As mentioned, there are many more hybrid approaches possible.  For a business thinking about their licensing strategy, it may make sense to think of these questions separately:

* should our proprietary shell be time based or feature scoped?
* should our proprietary shell be closed, or source-available?


I certainly rather see companies and projects appear as Fair Source rather than not at all.  (same with Open Core, for that matter).  I think there are some options left to explore, such as the Open Core with an source available (instead of closed) shell.  Something to consider for any company doing Open Core today.
