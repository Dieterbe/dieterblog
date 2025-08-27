+++
title = 'Body.build: a new free public fitness platform from the ground up'
date = 2025-08-04T12:53:29+03:00
draft = true
+++

TLDR: I graduated top of class from the world's most advanced personal trainer course so that I can build an open source, free-access fitness platform with applications and a new data library to empower next-gen fitness apps.

The fitness community & industry seems largely dysfunctional.

## Today's problems

1) Content mess on social media

Social media is flooded with redundant, misleading content, e.g. endless variations of the same "how to do 'some exercise'" videos, repackaged daily by creators chasing relevance. Deceiving clickbait to farm engagement.  (notable exception: [Sean Nalewanyj](https://www.youtube.com/@Sean_Nalewanyj) has been consistently authentically accurate, while still entertaining). Some content is actually great, but is extremely hard to find, needs curation, and sometimes context.

2) Selling "programs" and "exercise libraries"

Coaches/vendors sell workout programs and exercise instructions as if they are proprietary "secret sauce".  They aren't. They usually repeat what is already widely understood or overcomplicate in an attempt to differentiate.  (The strongest aspect in copyright law is the choreographic/expressive expect, and this is still pretty weak).  Workout programs are either sold as a one-size-fits-all or have limited personalisation options and often are based on outdated information.  Accommodating injuries, adjusting programs across multiple goals (e.g. combining with sports) or across time requires expensive expertise, if you can even find it.

Many exercise libraries exist, but they require royalty payment fees. Even the most "free" project, [darebee](https://darebee.com/) has hefty restrictions around reuse and modifications.  Anyone who wants to build a new app (even a non-commercial one) needs to either license a commercial library, recreate their own, or use a free open source one - I've checked several and let's just say there's quality and legal concerns.  (WikiPedia is more liberal, but is too text-based and can't easily be used by applications)

3) Suboptimal AI's

When you ask an AI for guidance, it sometimes does a pretty good job, often it doesn't, because:
- Unclear sources: AI's regurgitate whatever programs they were fed during training, sometimes written by experts, sometimes by amateurs.
- Output degrades when you need a specific personalized advice and when you need adjustments over time (such as volume, intensity, etc) which is actually a critical piece for developing well.
- Hallucinations still happen.
- Today's systems are text based. They may seam cheap today, because vendors are subsidizing the true cost in an attempt to capture the market. But it's inefficient, inaccurate and financially unsustainable.  It also makes for a very crude user interface.

I believe the tomorrow's AI's will have domain specific richer datamodels (not just text) and UI's and require a better source of data.

4) Lock in over freedom

Good coaches can bring value via in-person demonstrations, personalization, holding clients accountable and helping them adopt new habits.
The most well known coaches on social media found a way to scale up their revenue by launching their own apps, some of these seem actually quite good but suffer from the typical downsides that we've seen in other software domains such as vendor lock-in, lack of data ownership or compatibility across apps, lack of customization, high fees, etc; it seems that this space is also ripe for open source disruption. 

## Tomorrow's solutions

I want to make a difference. In 2024-2025 I participated in the [Menno Henselmans Personal Trainer course](https://mennohenselmans.com/online-pt-course/). This is the most in-depth, highly accredited, science based course program for personal trainers that I could find. Earlier this year I graduated Magna Cum Laude, top of class.

With that out of the way, I could train and coach individuals directly. But as a software engineer I know that even a small software project can grow to change the world.
What Wikipedia did for articles, is what I aspire to make for fitness: a free public service comprising information, hands-on tools and mobile applications.
This will also require a new "foundational platform".  I've started prototyping both the platform and some tools on [body.build](https://body.build).  I hope to grow a project and a community around it that will outlive me.  It is therefore [open source](https://github.com/Dieterbe/body.build/).

#### Apps

Thus far I've built:
- a calorie calculator
- weight lifting volume calculator
- program builder
- a crude exercise explorer.

Soon I plan to start working on a mobile companion app to execute on your programs, have quick access to exercise demonstrations/cues, and log performance.  Data will be unlocked to do your own analysis, and a personal interest to me is the ability to track cues and variations of exercise and analyze which work better.

#### Foundational platform

To support such next-gen tools - ones written by people, and others written by AI - we need a platform.  This consists of two parts: an exercise library, and a set of algorithms that encode scientific principles. (which can be exposed as "tools" in AI lingo)

##### The exercise "library"

The library should be liberally licensed and not restrict reuse.
It needs in-depth awareness that goes beyond what apps typically contain and include:
- modeled relationships between exercises
- customization options (and their trade-offs
- detailed biomechanical data (such as muscle involvements and loading patterns across the range of muscle length and different joint movements


For actual demonstration videos, you can legally link to existing videos and often also embed them under fair use and under the [standard youtube license](https://support.google.com/youtube/answer/2797468?hl=en).  We can simply leverage existing high quality content, but it needs expertise to do so, which is one of the reasons I took the course.
Moreover, by combining multiple sources of information from different creators, we can highlight different (and sometimes conflicting) advice, which you can then try, track and see what works best for you.

[Body.build](https://body.build) today has a prototype of this.

##### Algorithms

Through the course, I learned about various principles (validated by decades of coaching experience and by scientific research) to construct optimal training based on input factors (e.g. optimal workout volume depends on many factors, including sex, sleep quality, food intake, etc.) Similarly, things like optimal recovery timing or excercise swapping can be calculated, using well understood principles).

Rather than thinking of workout programs as the main product I think of them as just an artifact that can be generated by first determining an individual's personal parameters, and then applying these algorithms on them.  Better yet, instead of predefining a rigid multi-month program (which only works well for people with vary consistent schedules), this approach allows to generate guidance at any point in any day. Which would work better for people with inconsistent agenda's.


With that in place, we can build next-gen applications on top (AI powered if you like).

## I need help


My main struggles:
- Marketing: determining who to build it for, reaching them and building tools optimally to solve their actual needs. Develeopers vs users, pro-users vs amateurs.  body.build is quite advanced, and for now I'm exposing a lot of that into the UI, thereby selecting for the niche of nerdy "type 1" weight lifter who obsess over details. The type of people who would obsessively scroll instagram or youtube for the latest workout tips (who will now hopefully have a better way)
- UX and UI design

If you think you can help, please reach out!  In the meantime, I will keep working on the library, applications, and keep persuing formal education to infuse into the project.


what do build and who do i build it for? then marketing


mareting.. can AI do it now?
plus dan slimmon feedback
- different ways to contribute, UI/UX, engineering, not all needs expertise



what will it unlock? workflows
* detailed analysis of (and comparison between) different workout programs 
* just-in-time workout generation. "my legs are sore from yesterday's hike. in 2 days i have yoga class. i have time this morning for 30 min between meetings and/or this evening at the gym. what workout should i do? remember that i reported elbow tendonitis symptoms in my last strength workout"
