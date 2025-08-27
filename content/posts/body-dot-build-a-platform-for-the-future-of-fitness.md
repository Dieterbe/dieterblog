+++
title = 'Body.build: a platform for the future of fitness'
date = 2025-08-27T12:53:29+03:00
draft = true
+++

TLDR: A software engineer with a dream, undertook the world's most advanced personal trainer course. Despite being the odd duck amongst professional athletes, coaches, and body builders, graduated top of class, and is now starting a mission to build a free and open source fitness platform to power next-gen fitness apps and a wikiPedia-style public service.  But he needs your help!

## The fitness community & industry seem largely dysfunctional.

1) Content mess on social media

Social media is flooded with redundant, misleading content, e.g. endless variations of the same "how to do 'some exercise'" videos, repackaged daily by creators chasing relevance. Deceiving clickbait to farm engagement.  (notable exception: [Sean Nalewanyj](https://www.youtube.com/@Sean_Nalewanyj) has been consistently authentic, accurate, *and* entertaining). Some content is actually great, but extremely hard to find, needs curation, and sometimes context.

2) Selling "programs" and "exercise libraries"

Coaches/vendors sell workout programs and exercise instructions as if they are proprietary "secret sauce".  They aren't.  As much as they like you to believe otherwise, workout plans and exercise instructions are not copyrightable.  Specific expressions of them, such as video demonstrations are, though there are ways such videos can be legally used by 3rd parties, and I see an opportunity for a win-win model with the creator, but more on that later. This is why the seller usually simply repeat what is already widely understood, replicate (possibly old and misguided) instructions or overcomplicate in an attempt to differentiate.  Furthermore, workout programs (or rather, a "rendition" of it) often have no or limited personalization options.  The actually important parts, such as adjusting programs across multiple goals (e.g. combining with sports), across time (based on observed progression) or to accommodate injuries, assuring consistency with current scientific evidence, requires expensive expertise, and is often missing from the "product".

Many exercise libraries exist, but they require royalties. To build a new app (even a non-commercial one) you need to either license a commercial library or recreate your own.
I checked multiple free open source ones, but let's just say there's serious quality and legal concerns.
Finally, WikiPedia is legal and is favorably licensed, but is too text-based and can't easily be used by applications.

3) Sub-optimal AI's

When you ask an LLM for guidance, it sometimes does a pretty good job, often it doesn't, because:
- Unclear sources: AI's regurgitate whatever programs they were fed during training, sometimes written by experts, sometimes by amateurs.
- Output degrades when you need specific personalized advice or when you need adjustments over time which is actually a critical piece for progressing in your fitness journey. Try to make it too custom and it starts hallucinating.
- Today's systems are text based. They may seam cheap today, because vendors are subsidizing the true cost in an attempt to capture the market. But it's inefficient, inaccurate and financially unsustainable.  It also makes for a very crude user interface.

I believe future AI's will use data models and UI's that are both domain specific and richer than just text, so we need a library to match.
Even "traditional" (non-AI) applications can gain a lot of functionality if they can leverage such structured data.

4) Closed source days are numbered

Good coaches can bring value via in-person demonstrations, personalization, holding clients accountable and helping them adopt new habits.  This unscalable model puts an upper limit on their income.
The better known coaches on social media solve this by launching their own apps, some of these seem actually quite good but suffer from the typical downsides that we've seen in other software domains such as vendor lock-in, lack of data ownership, incompatibility across apps, lack of customization, high fees, etc;
We've seen how this plays out in devtools, enterprise, in cloud.  According to more and more investment firms, it's starting to play out in every other industry (just check the [OSS Capital portfolio](https://oss.capital/portfolio/) or see what Andreesen Horowitz, one of the most successful VC funds of all time [has to say on it](https://a16z.com/open-source-from-community-to-commercialization/)): software, is becoming open source in all markets. It leads to more user-friendly products and is the better way to build more successful businesses. It is a disruptive force. Board the train or be left in the dust.

## What am I going to do about it?

I'm an experienced software engineer. I have experience building teams and companies.  I'm lucky enough to have a window of time and some budget, but I need to make it count.
First thing I did is to educate myself properly on fitness.  In 2024-2025 I participated in the [Menno Henselmans Personal Trainer course](https://mennohenselmans.com/online-pt-course/). This is the most in-depth, highly accredited, science based course program for personal trainers that I could find.  It was an interesting experience being the lone software developer amongst a group of athletes, coaches and body builders.  Earlier this year I graduated Magna Cum Laude, top of class.

![Right: one of the best coaches in the world. Left: this guy](https://body.build/docs/assets/images/dieter-menno-f89418d879626e6792eaf76e6f73d166.jpg)

Now I am a certified coach, who learned from one of the top coaches worldwide with decades of experience.  I can train and coach individuals.  But as a software engineer I know that even a small software project can grow to change the world.
What Wikipedia did for articles, is what I aspire to make for fitness: a free public service comprising information, but more so hands-on tools applications to put information into action.
Perhaps give opportunities to industry professionals to differentiate in more meaningful ways.

To support the applications, we also need:

* an exercise library
* an algorithms library (or "tools library" in AI lingo)

I've started prototyping both the libraries and some applications on [body.build](https://body.build).  I hope to grow a project and a community around it that will outlive me.  It is therefore [open source](https://github.com/Dieterbe/body.build/).

### Next-gen applications and workflows

Thus far [body.build](https://body.build) has:
- a calorie calculator
- a weight lifting volume calculator
- a program builder
- a crude exercise explorer (prototype)

I have some ideas for more stuff that can be built by leveraging the new libraries (discussed below):

- a mobile companion app to perform your workouts, have quick access to exercise demonstrations/cues, and log performance.  You'll own your data to do your own analysis, and a personal interest to me is the ability to try different variations or cues (see below), track their results and analyze which work better for you. (note: I'm maintaining [a list of awesome OSS health/fitness apps](https://github.com/Dieterbe/awesome-health-fitness-oss), perhaps an existing one could be reused)
- detailed analysis of (and comparison between) different workout programs, highlighting different areas being emphasized, estimated "bang for buck" (expecting size and strength gains vs fatigue and time spent)
- just-in-time workout generation. Imagine an app to which you can say "my legs are sore from yesterday's hike. In 2 days I will have a soccer match. My availability is 40 min between two meetings and/or 60min this evening at the gym. You know my overall goals, my recent workouts and that I reported elbow tendinitis symptoms in my last strength workout. Now generate me an optimal workout".

### The exercise library

The library should be liberally licensed and not restrict reuse. There is no point trying to "protect" content that has very little copyright protection anyway. I believe that "opening up" to reuse (also commercial) is not only key to a successful project, but also unlocks commercial opportunities for everyone.

The library needs in-depth awareness that goes beyond what apps typically contain and include:
- exercises alternatives and customization options (and their trade-offs)
- detailed biomechanical data (such as muscle involvements and loading patterns across the range of muscle length and different joint movements

Furthermore, we also need the usual textual description and exercise demonstration videos.
Unlike "traditional" libraries that present a singular authoritative view, I find it valuable to clarify what is commonly agreed upon vs where coaches or studies still disagree, and present an overview of the disagreement with further links to the relevant resources, which could be an Instagram post, a YouTube video or a scientific study)
A layman can go with the standard instructions, whereas advanced trainees get an overview of different options and cues, which they can check out in more detail, try and see what works best for them.  No need to scroll social media for random tips, they're all aggregated and curated in one place.

Our library (liberally licensed) includes the text and links to 3rd party public content.  The 3rd party content itself is typically subject to stronger limitations, but can always be linked to, and often also embedded under fair use and under the [standard YouTube license](https://support.google.com/youtube/answer/2797468?hl=en), for free applications anyway.  Perhaps one day we'll have our own content library, but for now we can avoid a lot of work and promote existing creators' quality content. Win-win.

[Body.build](https://body.build) today has a prototype of this. I'm gradually adding more and more exercises. Today it's part of the codebase, but at some point it'll make more sense to separate them out, and use one of the [Creative Commons](https://creativecommons.org/) licenses.

### The algorithms library

Through the course, I learned about various principles (validated by decades of coaching experience and by scientific research) to construct optimal training based on input factors (e.g. optimal workout volume depends on many factors, including sex, sleep quality, food intake, etc.) Similarly, things like optimal recovery timing or exercise swapping can be calculated, using well understood principles).

Rather than thinking of workout programs as the main product I think of them as just a derivative, an _artifact that can be generated_ by first determining an individual's personal parameters, and then applying these algorithms on them.  Better yet, instead of pre-defining a rigid multi-month program (which only works well for people with very consistent schedules), this approach allows to generate guidance at any point in any day. Which would work better for people with inconsistent agenda's.

[Body.build](https://body.build) today has a few of such codified algorithms, I've only implemented what I've needed so far.

## I need help

I may know how to build some software, and have several ideas on new types of applications that can be built that can be beneficial to people.  But there is *a lot* that I haven't figured out yet!
Maybe you can help?

Particular pain points:

1) Marketing: developers don't like it, but it's critical.  We need to determine who to build for? (coaches? developers? end-users? beginners or experts?). What are their biggest issues to solve? How do we reach them?  Marketing firms are quite expensive.  Perhaps AI will make this a lot more accessible.  For now, I think perhaps it makes most sense to build apps for technology & open source enthusiasts who geek out about optimizing their weight lifting and body building.  The type of people who would obsessively scroll Instagram or YouTube hoping to find novel workout tips (who will now hopefully have a better way). I'ld like to bring sports&conditioning more to the forefront too, but can't prioritize this now.
2) UX and UI design.

Developer help is less critical, but of course welcome too.

If you think you can help, please reach out on [body.build discord](https://discord.gg/YUcS6btXYD) or [X/Twitter](https://x.com/bodydotbuild), and of course [Check out body.build!](https://body.build/) and please forward this to people who are into both fitness and open source technology! Thanks!
