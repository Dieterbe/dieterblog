---
title: "Complementing an AI Agent with deterministic scripts using SWAMP"
draft: false
---

In my very first experiments with AI agents, I was using them to manipulate many rows in CSV files.
I learned pretty quickly that rather than asking the agent to make the change, you're better off asking it to write a script to do it, and then running the script.
This has many advantages: it's easier to inspect and validate the logic, make refinements (either with the agent or manually) - possibly iterating many times before getting it right -, save it for reuse on other files, and ensure the exact same operation is applied across all rows.
As a bonus, for non-trivial workloads it also tends to go faster and use fewer tokens.

Turns out that however good LLMs are at reasoning tasks, for deterministic (and larger-scale) changes, traditional code works better.
My first self-taught lesson with agents was: **don't use it for everything, certainly not to replace traditional code**.
Code and LLMs can be very complementary, and soon after, agents started automatically generating scripts and running them.

## SWAMP...Club?

That was 2025. Which raises the question: what happens if you further develop this idea into a first-class system that can be used by individuals or by teams?
The answer: [SWAMP](https://swamp.club), although it took me a long time to figure that out.

The website throws a lot of inexplicable stuff at you that's really not relevant and that you can skip.
For example, why does it say that it's a club? After using it for many months, I still don't know. It's an open source developer tool that anyone can download and use.
Why does a devtool create profiles for its users (here's [mine](https://swamp-club.com/u/dieter)) and put them on a mysterious, undocumented [leaderboard](https://swamp-club.com/leaderboard)?
I still don't really know. It seems like it's based on collected usage telemetry. I don't know any other devtool that does this, but I guess it may help engage more people. I ignore this.

Some staff members write brilliant blog posts (e.g. [Paul Stack's](https://stack72.dev/)). A lot of these are about "building the machine that builds the machine", or in other words having managed software factories: AI writes software by reducing human interactions to some key inputs and relying heavily on AI code generation, AI auto code reviewing, and various forms of automated quality testing. That's how SWAMP is built, and the topic dominates a lot of the discourse. Paul has this [great post](https://stack72.dev/the-community-pull-request-is-dead/) about why pull requests are dead and why they built their own ticketing system.
However fascinating and relevant to SWAMP's development, it has little to do with what SWAMP actually is and does.

## So then, what is SWAMP actually?

Swamp has extensive [docs](https://swamp-club.com/manual), but these are also quite dense. Let me paraphrase and simplify a bit and explain how I see what it really boils down to.

**Swamp helps you build and reuse deterministic scripts, manage their input and output data, and run them. Inside or outside an AI agent.**

Specifically:

* It lets you abstract out pieces of work into reusable "models", which it implements for you as TypeScript code, like a class in OOP.
* It lets you instantiate these models and call methods on them. Like objects in OOP, you can just use them without needing to read the class' code. This is just running a CLI command. If you have the agent do it for you, it does not need to load any code into its context, saving tokens.
* The swamp CLI tool automatically collects and stores method output data in a repository, neatly organized by model, method invocation, version, etc. You can inspect the data and reuse it in other invocations, or load some of the data into your agent context window, but you don't need to.
* You can feed output from one model run into another and construct entire workflows. You don't even need an AI agent; you can just run these as a CLI command.
* It has a public repository where people can contribute and share useful models. The most popular ones now are for system administration, using S3, etc. When you're actually using the skills (see below) and express a need, swamp will find relevant extensions for you.
* It also ships a bunch of skills that guide you and your agent through all of the functionality. This works incredibly well.
* It also has various features for enterprises, larger scale uses, vaults, etc.

## Use cases

More people are starting to write about their [use cases](https://swamp-club.com/use-cases) (and here's an interesting [CI one](https://www.adamhjk.com/blog/a-practical-guide-to-reducing-token-spend/)), but it's certainly not limited to sysadmin and software development stuff.

I use swamp models and workflows for:

* extracting my body weight values out of [body.build](https://body.build), my friend's body weight values out of [logseq](https://logseq.com) (my 2nd brain), converting them into CSV, and uploading them into a private [Grafana Cloud](https://cloud.grafana) dashboard where my friend and I can keep track of our weight loss journey.
* extracting location clues out of various sources such as GPX coordinates in my Google Photos, so I can construct a location history and make sure I comply with tax laws (which count the number of days spent in a country, etc.).
* managing a Raspberry Pi and querying Prometheus (I made [an extension](https://swamp-club.com/extensions/@dieter/prometheus) for that—well, actually Swamp built it) and managing a local Grafana dashboard (using [this extension](https://swamp-club.com/extensions/@keeb/grafana)). I have a local monitoring setup and am troubleshooting an internet issue. Offloading the grunt work to code (swamp models) and leaving reasoning to the agent works incredibly well. The two work hand in hand to help me build a detailed diagnostics report. I still use Ansible in this stack, but expect to migrate the sysadmin work to swamp as well, as it should handle config drift better since it can reason about the live state of the system.

The best part is that all of this was basically on autopilot, with very little human oversight needed.
All of these seem kind of random, but I guess that's the point: you can use swamp for anything. I suspect I will probably start using it for more and more random things.
