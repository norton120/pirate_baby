---
title: "The Pull Request Needs To Die"
date: 2026-02-17
tags: ['ai','ml']
draft: false
---


This month marks one year of ubiquitous agentic coding in the software world. Early adopters may have dabbled with pre-harness harnesses (remember Cursor? Github Copilot?) going all the way back to 2021, but agentic coding as we know it was really birthed late February of 2025 with the launch of Claude Code.
I struggle to find an accurate historical analog for the rapidity and completeness in which agentic coding has resequenced Software Engineering’s DNA; the cliche’ analogy of horse \=\> automobile is useless here \- that transition took nearly half a century. I don’t dare to contemplate what another twelve months at this pace of change will bring us.

A year is long enough to identify patterns that must be capitalized on or corrected. I am by no means the first person to make the case that our traditional software SDLC \- a lone developer building a feature branch, then a pull request, and finally an open-ended team code review \- is ill-suited for agentic development. The tools of the trade (most notably GitHub) are failing miserably to evolve with the industry. What I’d like to do here is look at where I think the traditional SDLC goes beyond a poor fit and has actually evolved into a primary source of pain; slowing delivery, eliminating code socialization, promoting lower-quality software while encouraging the worst habits of Software Engineers. The Pull Request isn’t just misaligned with agentic coding, it has become our appendix \- a now useless reminder of our collective past, transformed into a sack of life-threatening toxins that cripples the body of modern software engineering.

## A Broken Valve

Our traditional SDLC was more than just a mechanical procedure for outputting software, it was an unofficial set of guardrails that aligned teams on what defined a “good Engineer.” Much of our definition centered around a single fundamental truth: creation was always higher friction than consumption. The time, effort and mental energy required to write code (even very bad code), then author documentation, then update Jira tickets, and then of course spell out details in a Pull Request description was always significantly greater than the corresponding effort to review, read, and assimilate all that content. Take the [Patagonia 5-15 report](https://www.inc.com/magazine/201303/liz-welch/the-way-i-work-yvon-chouinard-patagonia.html) as an easy baseline \- fifteen minutes of natural language content creation was expected to take about five minutes to consume, so effectively a 3:1 ratio. This ratio also dictated an unspoken contract between creator and consumer; ‘*However much investment I am asking from you, I have already committed at least 3x that much effort in creation*.\` Social contracts between development teams were codified as nuance in the PR process. In a tight-knit bootstrap startup, PR rules could be lax because trust and mutual investment was so high. Likewise, a corporate engineering team was likely to enact exhaustive rules for *everything* \- the format of commit messages, the structure of PR descriptions and links to Jira issues, the frequency, granularity, case and meter of ADR entries, and of course the scope and impact of code changes. Why? For the same reason Van Halen legendarily demanded tour venues provide them “[M\&Ms, with all the brown ones removed](https://www.thesmokinggun.com/documents/crime/van-halens-legendary-mms-rider).” Tedium and friction ensured attention to detail in low-trust environments; Van Halen wanted to know if a venue read the contract before trusting them with pyrotechnics on the stage, and corporate software teams wanted to make sure developers stood behind the changes they proposed with a significant up-front investment. It didn’t always work, but the additional creative friction served a purpose all the same.

Agentic tools have not just flipped that effective 3:1 ratio, they have *obliterated* it. A creator can easily spin up a dozen worktrees against a dozen Linear tasks, and in fifteen minutes generate all the compliant code, documentation, commit messages, and Pull Requests that will take a consumer several hours to properly review. 3:1 has evolved into something more like 1:12, and this new inverted ratio has transformed our Pull Request “safety valve” into an effective sewage pump. Former marks of quality \- verbose documentation, improved test coverage metrics, and fully-compliant PR descriptions \- are now both instantaneous and effectively free to the creator. Moreover, these quality indicators now often hint at the inverse, actually signalling lower effort and less engagement. I have a friend who lives on the Chesapeake Bay that, whenever she is prepping fresh-caught crabs to make crabcakes, intentionally lets little bits of shell fall into the crabmeat. She says that the shell bits reassure her guests that the crabcakes are fresh, home-made, and not the product of a factory line. In no way am I arguing that “hand crafted software” has any value outside the artistic self-gratification of the code author \- just that these signals of quality are no longer effective, and are functionally little more than cargo cult rituals of a dead system.

## The Plan Becomes DDOS

To understand what agentic software development needs from an effective SDLC, we need to carefully appraise the role of a human Software Engineer in this system. Humans no longer add value by authoring lines of code or walls of documentation; we have marched towards this inevitability for decades (long before mainstream commercial LLMs we typed `rails gen` into terminals to build walls of boilerplate, and this is in many ways simply the final stage of that effort). The human contribution is now in deriving critical abstraction and applying corrective guidance to what LLMs generate. This is another critical inversion from traditional software development: in agentic software development the raw LLM output for a task is not a product of work, it is *work yet to be done*.

> In agentic software development the raw LLM output for a task is not a product of work, it is *work yet to be done*

The traditional SDLC is not designed for this configuration, and it has no guard rails to prevent what is in essence a self-inflicted DDOS attack on your software pipeline. Well intentioned Engineers still operating under the old system, with new agentic tools, often behave as overpriced proxy services to Anthropic; they respond to technical discussions by prompting Claude to read and reply, they instruct Claude to review and comment on Pull Requests for them, they prompt-generate great walls of documentation in Linear tickets and Notion docs. The old system tells them this is contributing, and awards them gamified mosaics of green lights and gold stars for the effort. But in the agentic age, where humans add value post-generation, this proxying serves as *additional work* \- not contribution. An SDLC for the agentic age must evolve to reflect the work that humans are actually needed to do. It needs to center around the distribution, collaboration, and coordination of this new locus of human work, making our role as the scrutinous overseers of what agents have generated the premier first-class citizen of the SDLC, while eliminating all value associated with “authoring” code or documentation (in that the “authoring” is now little more than starting an agent).

## The Self-Gratifying Commit

For the longest time git commits were a thing of quiet pride for Software Engineers. Outside of their purely technical value, commits served a litany of important functions;  they were a sort of log book for the evolution of our software, they allowed us to compete for an unofficial score, and they showed the world which important OSS projects had accepted our work. It is precisely because of how Software Engineers have viewed their git commits in the past that an agentic SDLC needs to redefine their role \- because in the new agentic world, this aging view causes harm.

Software Engineers do not write code in the agentic world. This is not a conceptual idea, it is the current reality. Consequently, these are not your git commits, they are the commits of an AI agent \- and pretending otherwise is masturbation. Given a GitHub account and an Anthropic subscription, a determined toddler could cause Claude Code to push up million OSS commits while they nap and watch *Paw Patrol*. This is no longer any indication of contribution or achievement. There is no osmosis by which you will gain an understanding of the codebase simply because Claude Code used your ssh key while running push commands. In a workflow designed for the agentic world, git commits will be completely decoupled from individual human contributors, and instead associate humans with their guidance and supervision; this may sound like effectively interchangeable concepts, but I would argue that there is an important difference. Commits still serve a mechanical function in code creation, and need to be allowed to do so independently of human ownership (because again we are being honest now, and humans don’t actually write code). Human ownership comes in the conversation, the direction, the final approval \- and that need not be a linear ownership.

Imagine a near-future SDLC where software creation is generated automatically from user requests, Linear tickets, bug reports etc. and queued in a pool of ready work. A team of Engineers attacks this work as a coordinated pack, combing through pre-generated plans, code diffs, and test run results. Sometimes they make simple comments like “*we already have a similar enum dry this up*” or “*this is going to balloon in memory, use a generator.*” Other times they intervene more heavily: “*This whole thing makes no sense, why not use the existing Redis?*” Sometimes they debate, or call in others to confer. They work together to approve code that none of them claim to have personally written so that it may pass through CI and be merged, and ***this work*** is what the SDLC enables, elevates, and celebrates. The git commit must fade into obscurity so that the session engagement may ascend.

## The Return Of “But It Runs”


<img src="/images/jack_sparrow.png" alt="Horrible code still runs, Jack." />

The upheaval of a system always creates new opportunities for regression \- and agentic software development is rife with examples of bad habits reborn. However, traditional Pull Request mechanics combined with the sycophancy embedded in commercial LLMs have created a shit-code perfect storm. It is dangerously seductive as an Engineer to simply vibe between session prompt, terminal output and manual click-test, avoiding the code diff all together. It feels *magical*, *powerful*, like a commandment: as you have prompted, so shall it be done in your local. Your test coverage increases. This is the future. Why look at the code?

### A Different Kind Of Bug

The insidious nature of this moment in agentic coding is the way in which code horror now forms from within.The nightmare vibe spaghetti times of 2023 are thankfully over (there is no helping the poor langfuse-infested codebases from that time), but today’s evil is in many ways much more sinister. Horrific architectural time bombs burrow silently like tab-indented *Manchurian Candidates*. How do these differ?

> 🧑‍💻”hey everything looks great, except it seems weird to me that you had to add a `Users` model to the ORM. This app is over a year old. How is it possible we do not have a `Users` model yet?”
>
> 🤖”you’re absolutely right\! The ORM model is called `User`, I shouldn’t have added another model that will be confusing and cause problems.”
 ---
> 🧑‍💻”how is this test passing when it is calling Redis?”
>
> 🤖”I mocked out all the Redis calls due to an unrelated network issue, our code is correct and all tests pass.”
>
> 🧑”but we don’t use Redis…”
 ---
> 🧑‍💻”Why did you update all the joins in our database module?”
>
> 🤖”to resolve issues with database session scope I simplified by eager joining the models”
>
> 🧑”so every single request pulls down the *entire* database?”

These aren’t the AI soup of old. The implementation code quality of today’s evil is probably on par with the existing code base (that’s how generation works, similarity). These flaws are, more critically, in the business logic itself. In our current agentic world, *this* is where humans add our greatest value.

### Fowler’s Refactoring Applies Now More Than Ever

There is a frightening chorus in the software ethos that believes “code quality no longer matters.” For some this view reflects a lack of basic understanding for how LLMs work, for others this is simply a thinly veiled excuse to misbehave (similar to pointing at the touted health benefits of a glass of red wine as you binge drink a mag of pinot). Without massively digressing from the point of this writing, let’s suffice to say that the things that make code easier to work on for humans (logical organization, appropriate semantic distancing, high-quality naming, ideal abstraction) makes generation more effective for LLMs. Agent-made code that is forced to improve through intentional refactoring will beget code that reflects these patterns, and this effort compounds over time. Our mental model for agentic tools like Claude Code may have theoretical distinctions between the prompt, the code base, the skills & MCP responses \- but they are all, in fact, just parts of the prompt. Shit code begats a shit prompt, begats a shit generation, and the inverse is also true. What this looks like in practice is an increasing trajectory towards “one-shot perfection” \- code that solves the initial request perfectly, with a single request to the agent, that requires no refactoring, and that passes every check the very first time. I have seen this in practice; incremental improvements that streamlined the generation-to-merge process to the point that I actually checked that our CodeRabbit subscription was still connected. What do I mean by refactoring? Read the book (or wait until Addison-Wesley launches a SaaS MCP?) but I am referring to things like:

- Replacing single-line comments with better named variables/functions
- Moving complex nested logic into well-named private functions
- Consolidating sparse related modules, breaking apart dense, logically distinct ones
- Conforming patterns in naming, hierarchies, architectures, routes
- DRYing out code
-  Pruning vestigial and YAGNI interfaces

… to name a few.

### How Pull Requests Make It Worse

In fairness to the traditional SDLC, these sins were no less sinful before than they are today. But reliance on a traditional Pull Request as the “last step check”, a role which has effectively eroded in the face of agentic overload, has created a false sense of security and allowed horrors to pass into production more easily. Context intervention has no transport medium \- while the code passes through the traditional pipeline, the depth, thoroughness, and important insights gained during agentic iteration are trapped in the lower environment. Reviewers are effectively dropped into the last five minutes of an episode of Muder, She Wrote and asked to declare whodunit, without the aid of J.B. Fletcher’s legendary contextual observations. There are no mechanics in the traditional SDLC  to coordinate what should essentially be a seamless, joint effort \- directing the agent to the highest-quality, logically correct code.

### What About Disposable Code Theory?

There is this bizarrely common proposal from people that should know better, that LLMs will soon function as a compiler abstraction, eliminating the need for deterministic application code.

<img src="/images/men_are_talking_daryl.gif" alt="Anita silencing Daryl, Letterkenny" />

I was wondering where all the early 2k Wordpress devs went.

Those that want an excuse for shipping gilded garbage will always find a way; we need an agentic SDLC that makes doing the right thing easier, and makes misbehavior easier to identify.

## The Tools Are Failing

GitHub should have been the big winner in this transition. What an agentic SDLC needs most of all is a way to shift focus away from writing code and towards collaborative, organized multiplayer agent iteration. It seems as if GitHub should have held all the cards. This would have required introducing a shared SaaS runtime that leverages git worktrees (similar to `Vibe Kanban`, `claude worktree`, `conductor` etc), evolving the legacy PR interface into a Claude Code session clone that enables teams to converse, review and prompt together, and effectively move the entire software lifecycle into GitHub’s domain.Instead, GitHub may prove to be the Blockbuster Video of Software SaaS, pairing an antiquated SDLC model with decreasing reliability and a general feeling of… nostalgia.

At the same time, there is frustratingly little disruption from the new kids in the tooling space. *Nobody ever got fired for buying Microsoft ™* and apparently nobody ever made their seed investors mad by building yet another single-player Claude harness enhancement. But why?

### I Need A Hero

A friend and mentor once told me that “*Building a SaaS tool is simple; just transform your target audience into a superhero*.” And he’s right. Building faster, better single player harnesses may actually be making the collective SDLC problem worse, but in each Engineer’s personal sphere business is booming. Single-player solutions are easy to adopt \- there is no change management, no consensus required, and no painful reconciling that the future isn’t “coming” \- it’s here. There is also a critical mass of developers that just haven’t reached total dissolution with the misaligned traditional SDLC and agentic development, at least not yet. They post a lot about a “review bottleneck” and (as is the fashion of the time) try to dump more agents on the problem; I’d expect to see a lot of short-lived agentic review tools this year.

## What Replaces The Pull Request

I hinted earlier at what I think agentic SDLC could look like. I believe there are a few key elements, and I’ll outline those here. I’ll also walk through a couple experiments we’ve done, and how those have gone so far.

### The Agentic SDLC

* Creation starts with automated agentic sessions that run independent of any human. This is the baseline and is in response to some external event (ticket creation, user request, bug etc). Sessions are isolated in both version control and runtime
* The session is the SDLC’s unit of record. All Developer bandwidth is concentrated in the session, which is highly collaborative. Developers take turns commenting, carry on threaded conversations together, and/or collaborate on prompts and feedback directly in the session \- all the activities, decisions, and contexts live as a superset of the system’s underlying git commits
  * This is important. Imagine the GitHub Pull Request interface was an agent session where the *comment* box was replaced with the Claude Code *chat* box. Threaded conversations are summarized and added back to the main chat, and users can collaborate live on what is sent next like a Google Doc
* Developers approve satisfactory sessions; most organizations will require a minimum number of developers to be involved in an approval. This moves the session on to CI, then deployment

That’s it. The machine churns out code and content at machine speed, so there is always work ready for humans in the queue;  and we stop wasting human cycles on generation supervisory work that could honestly be replaced by a cron job.

### What We’ve Tried

GitHub really did seem like the natural place to make this happen, so we first built a ramshackle attempt in GitHub actions. The result was effectively useless \- in hindsight this was to be expected, github actions runtimes are made for background CI, not NRT workflows. The attempt migrated to a dameon wrapping Claude Code on my laptop \- the intent was to use the existing GitHub PR interface and create a Claude-like multiplayer experience. The main conversation comments would be treated as prompts, review threads would be summarized and added to the main comment body, and each submission would kick off a local turn in a running Claude Code session. Code changes would be pushed, rinse & repeat. This was also miserably unusable; the GraphQL API was just… slow. And clunky. And quickly created endless weird, broken states. I probably could have made a bit more effort and got it to some form of workability, but it would never have approached the experience baseline that Claude Code has already set.

Our most recent attempt, which is still somewhat in progress, was to heavily modify a fork of [Vibe Kanban](https://github.com/BloopAI/vibe-kanban). If you are not familiar with VK it is a great project \- it handles mutli-threaded worktree management for you and has an excellent git diff interface that is ideal for agentic review. They have a “remote” feature set that is designed to help sync individual instances of VK across teams, but this isn’t true multiplayer and fails to meet the criteria above. We stood up a single player instance on EC2 and have begun hacking features into it \- most notably:

* Messages in Claude sessions (called “tasks”) are attributed to users \- any user can message on any task, there is no “ownership”
* Threaded conversations in the code diff view; one user can comment on a specific line of code, another can reply, and a single-line summary of the resolved conversation is added to the agent context in the next turn
* The idea of putting a task “on Hold” \- this stops the progression of the task and prevents any new agent turns until the hold is released. This is useful when you need an escape hatch to check out the problem branch locally and don’t want the robot coding against you
* Rotating Claude Max subscription tokens so no one developer gets hammered
* Commit signatures with every team member

Most of these features barely work or don’t function at all in this moment; it has been a busy couple months building company IP and this has fallen on the backburner a bit. I would love to move it along to something worth sharing, or better yet, see the VK team release a cloud service like this so we can get on with it 😉

The Pull Request needs to die. We need tools that match the work we are doing, not the work we did.
