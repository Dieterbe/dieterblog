+++
title = 'Relicensing: What are bad rug-pulls, how to do it right, and some Grafana learnings'
date = 2026-05-13T18:43:53+03:00
+++

The most common question founders ask me is "What's your opinion on rug-pulls and license changes?"
My answer is that the community backlash and controversy are usually exagerated, that license changes are not a bad thing actually, and should be used sparingly.

So let's look at relicensing, why it make sense, when it goes wrong, and how to do it gracefully.  I will include some lessons learned from our relicensing projects at Grafana Labs, though
this blog posts represents only my own opinion and not those of my past employer, Grafana Labs.

## What is relicensing?

Note that we are talking about enterprise software (B2B) only here.  B2C is different, and I have little experience with it.

Let's dig into this, but first we need to address some misconceptions and friction points:

* License changes are always "going forward": any code released under some license can't be taken back.  A more practical way to think about relicensing is as a fork:
  - the company stops maintaining the code base.  It's practically abandoned. Because it was unsustainable.
  - a company sees a path to save the community and project (though under a different license), so they step up and fork the project to continue it.  It just so happens that this company is the same as the previous one, so they can keep the name, the established commercial support system (though sometimes under a new pricing structure), the existing repo, build systems, issue tracker, etc. Which makes the fork more seamless.
* Any person or company is free to reduce or terminate their efforts into any open source project. By law, they only have to honor their commercial agreements.
* The only reason they can fork the project and apply a new license, is because it is their full legal right. Usually they've had that right for years, and have full discretion about when they apply it. If you are a consumer of open source and this comes as a sudden, shocking surprise, it should make you reflect on how well you understand the products and services you have chosen to depend on, above all.

Perhaps this makes it sound more palatable.  In case it doesn't, let's consider some events that probably have happened to you:

* A commercial service/product you depend on becomes decomissioned, bankrupt, too expensive, or is no longer the best solution.
* An open source project you depend on becomes unmaintained, too expensive, or is no longer the best solution.

Anyone who's been in technology for a while, will encounter these scenarios routinely.  It's the reality of using commercial products that live in an economic market or non-commercial projects that depend on the spare time and goodwill of individuals. Mature engineers or tech executives will deal with them without much fuss. Migrations can be annoying or painful, but usually don't cause an outrage.  They are considered part of the job.
You will migrate to an alternative solution; sometimes supported by an existing vendor, a new vendor, a different community, your team, or a combination.  Smart engineers and executives will build a tech stack specifically designed to handle these scenarios elegantly, with abstractions in place, to keep the door open for eventual migrations.  Any mature team will thoroughly consider exactly these ramifications when building upon a technology that locks them in.

A relicensing event is nothing more than an event like any of the above, but with some positive differences:
- renewed trust that your vendor will remain in business (unless they do something incredibly stupid, which is extremely rare)
- instead of being forced to find and implement an alternative, you are offered an additional solution, one which doesn't require a migration, doesn't impact your tech stack, your team's planning and has minimal impact to your existing commercial and customer support relationship with your vendor.

## When re-licensing goes wrong (the "rug-pull")

So, how is it that relicensing events cause controversies, when in fact they are easier to deal with than the more disruptive events which we somehow tolerate better?

I think there are multiple contributing factors, that become deadly when combined:

### 1) The community feels misled and betrayed

This is usually when they were asked to sign a CLA in which they had to hand over ownership or distribution rights of their contributions, especially so when they were lead to believe "it's fine because the license is permissive and we won't change that". Signing such a CLA is your clue that a license change will happen. Not a matter of "if", but "when".
Note, I'm not unequivocally saying CLA's are bad.  I think empowering a vendor can be a good thing. As a contributor, you need simply need to be not naive about the future. As a community, you need to be aware you can always fork. Whether before or after the CLA requirement, or before or after a relicensing event.
But forking only works when you can put together a commnunity of skilled engineers and can truly produce a better package.  Those are the rules of the open source game.

### 2) The event comes with pricing increases or features moved from previously free/open to paid/closed.

Speaks for itself.

### 3) The new license is - or appears - too aggressive.

Different communities and individuals will tolerate different things dependent on what they're used to.  The OSI has a long legacy in maintaining and defending [the most formal and widely accepted definition of "open source"](https://opensource.org/osd).  While it's been disputed by [myself](/posts/open-source-undefined-part-1-the-alternative-origin-story/) and by many others, it is the most widely accepted one.   Nowadays, using the words "open source" around a non-OSI approved license stirs up religious wars without clear winners.  Businesses may avoid or proceed depending on their appetite for media controversies.

Regardless:

- Many users swear by OSI approved licenses (even if it's only as an open core, wrapped by closed proprietary code).  Part of the reason, I think, why our relicensing from apache to AGPL at Grafana was successful and generally pretty well received, is that we stuck with an OSI approved license, even though we retained the open core model.  Sometimes you just need to give people what they want.

- Personally I think there are a lot of interesting Source-Available options such as [Fair Source](/posts/fair-source) which strike a better balance between the rights of both the vendor and its community than open core with an OSI-approved license in the center only.  It seems some communities are slowly warming up to these solutions, though education around it is critical, and the progress is slow.  But ultimately your community of users and customers is the final judge.

### 4) Intentionally vague or incorrect announcements

Some vendors actively try to mislead their users and customers.  Throwing buzzwords like "open" around in a confusing soup of words is not good for your users, and therefore for your business.

### 5) The change feels all "take" and no "give".

For example, Grafana Labs didn't just fork the Apache licensed Cortex database into AGPL licensed Mimir, we [also made sure to open up previously-proprietary functionality](https://grafana.com/blog/announcing-grafana-mimir/) into the new open source project.  As part of this relicensing we raised the bar for what we considered "enterprise only" and opened up everything that no longer met this new bar.   I believe this shows respect to your community and is required for successful business long term. Relicensing should be more about "how can we improve the interests of both parties". A company thinking of a relicensing as a one-way street undermines its own business.

Cynical observers may note that perhaps the trick is to always "juice up" a fat shell of proprietary features when using a permissive open core, just to have something to give to offset a relicensing, but I think it speaks to always seeking the right balance: if you use a permissive license, you need more proprietary features; when you make the license more protective, you can and should include some of those features.

### 6) just the fact that there is a change.

I have also learned that sometimes it's just the fact that something is changing, not the actual thing, that causes some uproar.
When we started Grafana Labs in 2015, our first metrics database - Metrictank - was AGPL licensed from the start, which never caused an issue.
Years later, when we forked the 2nd metrics database we worked on - Cortex - into Mimir and switched from Apache to AGPL for it, we forgot to mention that as part of this transition we were deprecating Metrictank, and merging its best already-AGPL features into (the easier to deploy) Mimir.  That could have reduced the (already small) commotion a bit.


## Relicensing is inevitable.  But the laws of physics dictate that the only way to do it, is to do it right.

As a vendor who controls open source software projects, you don't play in a vacuum.  You are beholden to a lot of external forces.
There's constant changes in market conditions, sentiments and best practices, financing opportunities, competitors gaining or losing strength, cloud vendors giving you more credibility or threatening your business, shifts in available technology, M&A opportunities, talent, export controls etc.

Inevitably, you need to periodically re-asses and adjust every process in your business. E.g. your ICP (Ideal Customer Profile), GTM (Go-To-Market), your offering, support, team structure, partnerships, vendors, etc.  The only constant is change.  The more a change is externally facing / customer-impacting, the more deliberate and careful you should be - as to minimize disruptions - but beyond that,
relicensing is in principle not all that different from any of the other changes you make.  And this why also relicensing events can be reduced, but inevitable.

Ultimately, everything you do, your reputation, the quality and pricing of your offering, the quality of your communication, the appeal of the open source project, etc boils down to an overall "score":

- Are you too aggressive or expensive?  Somebody will fork and/or lure your customers away with an alternative.
- are you not aggressive or expensive enough?  You won't be able to defend your business, and will be overtaken by someone who can build something better (possibly a fork)

For vendors, this means you will only do well if you hit the sweet spot.  You should *always* aim to provide a balanced offering and treat customers right.  A relicensing event is not an opportunity to become more aggressive. The laws of business don't change, you need to retain a compelling offering.
For customers, it means whichever vendor gives you the best overall experience will serve you.  If you are "mistreated" by a rug-pull, you may need a migration but will eventually be served by the vendor who treats you best.

There will be short term and medium term turbulences (e.g. due to lock-in), but eventually, the world rebalances.  There are "laws of physics" in place, ensuring vendors treat customers right; if they don't, another one will.

It also means that the only reason to do a relicensing is to make customers *more* happy on the long term.  The happier you can make your customer, the better your business will be.  If you upset your customers, the worse your business will be.  Any badly received relicensing event is from vendors who think it's OK to upset this balance because they have the lock-in or the market sentiment.  Short term they may be right, but long term, they are wrong.  Even if short term they are able to grow profits and re-invest into their projects and offerings, the burned trust is never worth it.

## Relicensing is good: from permissive to protective.

The playbook seen among many commercial open source vendors is to start with a permissive license (apache2/BSD/MIT) and later relicense to something more protective.
It is often said that this is "bad" or a de-facto rug-pull.  I think this is faulty thinking.  Grafana - and a few other companies - show that it's possible to relicense gracefully, though it's a tricky manoever. There's more examples of a relicensing gone wrong, but those involved also bad communications and overly aggressive changes such as as non-OSI approved licenses.

I would go further and say this can be a *good* model worth designing for.

Early on, you want to boost adoption and remove any restrictions. This grows community, adoption and helps with testing and validating a market. This is good for both the users, the vendor, and early customers.  Later on, the code is relicensed (assuming CLA's are in place although now with AI things are changing). This allows the vendor to protect its business.  Community members are often quick
to complain about the "rights lost", but again here the bigger picture needs to be considered.  If the vendor can protect its business better, it can grow the open source project better.  We saw above how they have limited abilities to abuse any "rights gained".  Users and community are almost always better off.  Either the vendor serves them better, or they will be better served by a new fork or a new competitor.

That said, if a license like AGPL or a Fair Source license makes sense from the get go, then you can start with that and make life easier down the road.


## How to re-license?

Relicensing can be done in a way that isn't seen as a "rug-pull", but instead as a "cleaning house". A transformative make-over that leaves everybody happier.

here are my tips:

* Try to avoid it by choosing a balanced license from the start, but better change something down the road than have analysis paralysis. Especially when getting started.
* Treat your community and customers with respect.
* Never make promises you can't keep.  Don't claim you will never re-license
* Talk with your community.  Figure out their licensing preferences.  See how they react to licenses and licence changes of neighbouring projects.
* Communicate clearly. Whether it's about CLA's or new licenses, especially if they are novel or not OSI compliant. If going for Source-Available type licenses, truthfully educate your community about your real intentions and goals, and the implications of the chosen license. Anything less will backfire.
* If not using OSI approved licenses, either steer clear of "open source" definition debates altogether, or leverage the inevitable debates between those who follow the OSD and those who don't. Pick your poison here :-)
* Consider the "giving" part as much as as the "taking" part.  Happy customer == Good business.

Finally, and this is actually how I usually start my consulting engagements: ask yourself if you really want to be an open source company and why.
Open Source business are about "growing the pie" (creating more value, growing a community around a sustainable project), and consuming a portion of that pie (capturing some of the value).  Restricting previously free features is not a long term smart move. It undermines or reverses the growth of the pie, and you then need to consume ever growing chunks of it. This is not an OSS business based on growth. It's a proprietary business. Which by itself is not "wrong" (though I believe COSS leads to more successfull businesses), it is a very tough pivot and one worth avoiding.

Especially as it relates to "cloud vendors eating our lunch".  You enabled them to legally do it, it's how you built your business.  Deal with it.

