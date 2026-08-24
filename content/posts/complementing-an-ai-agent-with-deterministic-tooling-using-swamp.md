+++
title = 'Complementing an AI Agent with deterministic tooling using SWAMP'
date = 2026-08-24T21:59:53+03:00
+++

In my very first experiments with AI agents, I wanted to manipulate many rows in CSV files.
I learned pretty quickly that rather than asking the agent to make the change, you're better off asking it to write a script to do it, and then running the script.
This has many advantages: it's easier to inspect and validate the logic, make refinements (either with the agent or manually), you can iterate on the logic as needed, save it for reuse on other files, and ensure the exact same operation is applied across all rows.
As a bonus, for non-trivial workloads it also tends to go faster and use much fewer tokens.

Turns out that however good LLMs are at reasoning tasks, for deterministic (and larger-scale) changes, traditional code works better.
My first self-taught lesson with agents was: **don't use it for everything, certainly not to replace traditional code**.
Code and LLMs can be very complementary, and soon after, agents started automatically generating scripts and running them.

## Introducing SWAMP

When you take the above idea of offloading deterministic computation out of an agent and into scripts, and develop it further into a refined, comprehensive system that can be used by individuals or by teams. What do you get?
The authors of [SWAMP](https://swamp.club) may explain it differently, but I think of SWAMP is exactly that.


Swamp has extensive [docs](https://swamp.club/manual), but these are quite dense.
Let me paraphrase, simplify, and explain what it really boils down to (IMHO).

**Swamp helps you build and reuse deterministic scripts, manage their input and output data, and run them. Inside or outside an AI agent.**

Specifically:

* It lets you factor out pieces of work into reusable "models" which have methods, just like classes in OOP. These are glorified scripts, implemented in TypeScript.
* It lets you instantiate these models and call the methods via a cli tool which wraps the code.  Like objects in OOP, you can just use them without needing to read the class' code. If you have the agent do it for you, it does not need to load any code into its context, saving tokens.
* If the invocation output would have gone to stdout (like with scripts), it would mean an agent running it would need to load this all into its context (expensive tokens!).  Instead, something much smarter happens.  The swamp CLI tool automatically collects and stores method output data in a repository, neatly organized by model, method invocation, version, etc. You can query and inspect the data and reuse it in other invocations, or load some of the data into your agent context window, if you want to.
* You can feed output from one model run into another and construct entire workflows. You don't even need an AI agent; you can just run these workflows as a CLI command.
* It has a public repository where people can contribute and share useful models. The most popular ones now are for system administration, S3, etc. When you're actually using the skills (see below) and express a need, swamp will find relevant extensions for you.
* It also ships a bunch of skills that guide you and your agent through all of the functionality. This works incredibly well.
* It also has various features for enterprises, larger scale uses, vaults, etc.

## Use cases

The above was a bit theoretical.  More people are writing about their [use cases](https://swamp.club/use-cases) (and here's an interesting [CI one](https://www.adamhjk.com/blog/a-practical-guide-to-reducing-token-spend/)), but it's certainly not limited to sysadmin and software development stuff.

I use swamp models and workflows for:

* extracting my body weight values out of [body.build](https://body.build) as CSV data (that's one model), my friend's body weight values out of my 2nd brain - [logseq](https://logseq.com) - into CSV (via another model), and uploading them into a private [Grafana Cloud](https://cloud.grafana) dashboard where my friend and I can keep track of our weight loss journey (this is several method calls on the Grafana model, first one to download the dashboard, to patch it in place, to update the new version, etc)
* extracting location clues out of various sources such as GPX coordinates in my Google Photos, and constructing a location history and make sure I comply with tax laws (which count the number of days spent in a country, etc.).
* managing a Raspberry Pi and querying Prometheus (Swamp helpfully made [an extension](https://swamp.club/extensions/@dieter/prometheus) to query Prometheus) and managing a local Grafana dashboard (using [this extension](https://swamp.club/extensions/@keeb/grafana)). I have a local monitoring setup and am troubleshooting an internet issue. Offloading the grunt work to code (swamp models) and leaving reasoning to the agent works incredibly well. The two work hand in hand to help me build a detailed diagnostics report. I still use Ansible in this stack, but expect to migrate the sysadmin work to swamp as well, as it should handle config drift better since it can reason about the live state of the system.

All of these seem kind of random, but I guess that's the point: you can use swamp for anything! I suspect I will probably start using it for more and more random things.

The best part is that all of this was built basically on autopilot, with very little human oversight needed.

## The confusing bits

If you decide to check out SWAMP, I just want to make you aware of some confusing bits:

* I don't know why it's called a "club". There's nothing exclusive about it.  It's a great open source devtool that anyone can download and use.
* It creates public user profiles (here's [mine](https://swamp-club.com/u/dieter)) and puts them on an undocumented [leaderboard](https://swamp-club.com/leaderboard).  None of this is relevant to using it. I think the leaderboards are hooked up to telemetry sent from the CLI tool, which I suppose are a way to gamify the experience. I personally ignore all this stuff.  You may want to disable telemetry but I haven't bothered.
* There's some very interesting content surrounding SWAMP.  I find the blog of swamp team member [Paul Stack](https://stack72.dev/) particularly interesting. But a lot of it is about "building the machine that builds the machine": managed software factories that minimize human interaction and rely heavily on AI code generation, automated reviews, and automated quality testing. That's how SWAMP is built. And of course they use SWAMP models and workflows in their "software factory".  But you don't need to buy into that vision to benefit from SWAMP.  And the tool feels solid. I guess all their automated testing pays off.
* The ["Lab"](https://swamp-club.com/lab) is their own bug tracker. You can't create an account to do anything there. It's all managed by "the machines" and staff.  Paul's [post about why pull requests are dead](https://stack72.dev/the-community-pull-request-is-dead/) explains this quite well.

## Conclusion

I found SWAMP a very nifty tool to add rigor to my AI workflows, or to create standalone tools and workflows that I can also run completely outside of AI.
So install it, find some basic repetitive or annoying task, and just ask your agent to help you.  It'll guide you through doing it all via swamp, it works beautifully!
