# Behold, I Teach You The Factory

*The software factory is the singular conclusion of software engineering. This is the software factory, in detail.* 



Over the last two years I have incessantly beaten the drum that self-writing software is an inevitability. My uncompromising belligerence to this end, and to the ill-fit nature of the previous decades' lingering SLDC, has kept me at odds with the school of the UberDev harness; but signals are now strong that the era of the single-player, local agentic harness is coming to an end. The time of the software factory is upon us, and as evidence to that effect, what is written here is not theoretical. The elements described are taken from working software delivery systems, in production now. The capabilities required are proven. The problems they solve are already here. 

## Why The Software Factory is Inevitable

It is not enough to say a thing *will be* without saying why. Here is that why.

### Security

The old model of software development struggled to cope with a modest 60-70 CVEs a day; today the rate is three times that and climbing. Supply-chain attacks and zero day exploits can now be leveraged at machine speed. It is ludicrous that each member of an engineering team would use a single machine to write code, access every company system, debug production, and read their email - and yet that was business-as-usual in yesterday's SDLC. Campbell's soup uses industrial kitchens, in part, to make sure every can of Chicken Noodle ships without any added Salmonella. Software can no more continue to be built and maintained on developer laptops than Campbell's could have employees safely brew up pots of soup in their home kitchens. 

### Resource Use

Human-orchestrated agentic harnesses are a ridiculously inefficient use of the technology, and orchestrating agentic harnesses are a ridiculously poor use of the humans. The predominant workflow at the moment is not one of design, but an anachronistic cargo-cult - the result of rapid evolution. Engineers once typed commands into terminals, and that was how software was made. Now they type commands into terminals, but mostly because that's what they did before everything changed. Over and over they type "approved," more to preserve the theater of what software development "should look like" than out of utility. The same way we imagine a leather-aproned cobbler crafting our new Italian loafers; those loafers came off an assembly line of conveyor belts and gears, and so will our software come from similar machinery.

### Consistency

Test-driven developers have long understood the value of deterministic, idempotent, comprehensive proof. Migrating the development process from a bespoke "crafting" of code to an automated system creates deterministic, idempotent, comprehensive process, with equally reliable results. Checks are this repeatable process manifested;  instead of a human developer saying “we don’t use static methods, please make these class methods,” we design an automated check that finds static methods and corrects them *every single time*. 

### Autonomy

Codifying the process means the software survives the humans that make it, and is ready for the next humans to maintain it. The Ford assembly line never halts production because a single linchpin employee calls in sick (“Ted is the only person that knows how to install headlights” is not a thing); so will the software factory free organizations and engineers from key-person dependencies. 

### Speed To Delivery

Unburdened by human meddling, software can build and repair software at a previously unimaginable pace. Our lingering need for the theater of control, that idle blocking while an agent waits for a human to click “approve” on code they didn’t read and specs they didn’t audit, that masks the true rate  of delivery and incident response possible.The delta in delivery speed between the current single-player agentic harnesses and the software factory is difficult to overstate. A factory never sits idle, sleeps, or pauses for the pageantry of response. A factory addresses every test, every check, every concern at machine speed. A factory begins to investigate production errors before a human would even see the alert. 

 As an aside, I’ve heard it said that the agentic workflows today are “fast enough,” and that another leap in speed offers little return. I would counter than today's single-player harness workflows are only "fast enough" for the very legacy SDLC we aim to surpass. Consider, as a parallel, the story of refined aluminum; once a metal more valuable than gold, the discovery of cheap refinement transformed the metal of emperors into the stuff of soda cans and storing leftovers. Today's agentic workflows are fast enough to wildly surpass the expectations of yesterday's software teams, but they do not yet deliver the near-instant response that must exist for software evolution to be a negligible-cost commodity. 

### Quality of Craft

Counterintuitively, automating the delivery process means architecture and refactoring become necessary first-class citizens. In the past, refactoring and architectural decisions were sidecars to delivery - quality fairy dust was  sprinkled over the codebase in tiny, justifiable doses. Decoupling abstract quality concerns from feature delivery is a direct result of speed; when spending human cycles to improve design, legibility, and pattern architecture no longer means giving up feature cadence, a meaningful space for those concerns becomes easier to carve out. Furthermore, the sentiment towards vibe coding creates legitimacy within the software factory for these efforts; if a common concern around 100% agent-generated code is quality and sound architecture, then dedicating human resources towards pure code quality and sound architecture efforts is easy to justify.

### Clarity

At this moment in history, all software professionals are thinking the same thing: "What will my job be? *Will* my job even exist? Where do I fit in all this long-term?" The software factory begins to provide concrete answers to those questions. Not in the pylant and unsatisfying platitudes of enhancement-not-replacement that companies have parroted for the last two years (often right before mass human layoffs), but in a tangible, post-agentic way. When we define the software factory with agents front and center, and then outline new human roles that complement that system, we are answering the very human question of "where will I belong in this new world."

## The Northstar

The idealized software factory is one that is entirely autonomous - completely able to meet every stakeholder need, deliver every new feature, and address every issue or error instantly, perfectly, and completely, and to do so with zero human involvement. 

The perpetual pursuit of this unattainable goal informs our efforts as Engineers; **our primary work, then, is not to affect the application(s) governed by the factory, but instead to address each and every instance where the factory failed to deliver perfectly, failed to deliver completely, and failed to do so without human involvement.** The question then becomes not "what should be different about the resulting code/plan/tests" but "what should be different about the factory that produced the undesirable output."

No part of the software factory can succeed until the Engineers that govern it understand and internalize this Northstar. A Campbell's Soup factory chef who discovers a vat of poorly-seasoned tomato bisque is not to break out their spices and fix the offending batch - that is not their role. The chef must find the flaw in the factory, fix the process, eliminate the potential of the same mistake in the future. So in the same way must our Software Engineers evolve.

## The Elements & Machines of the Software Factory

Software factory implementations differ in instance-level execution, and it is easy to become distracted by those differences - so we will focus on the macro-level commonalities of all software factories. Your organization may have regulatory constraints or product facets that shape your tooling, the way a factory producing shoes leverages a conveyor belt while a soup factory utilizes sanitary pipe. The components enumerated here are the basic building blocks from which all software factories derive. 

### Work Items

All work needs some basic unit - we will call those units "work items" to keep from clouding the discussion. You may call them "Issues" or "Tickets" or "Stories" or "Epics" or "Features" or "Bananas" - it does not matter. The importance is the idea of a finite unit of work that has a justified reason for existing (which can be a desire for improvement, addressing of a bug, an evolution of execution etc.) and a definition of success. 

{{< figure src="software_factory/items.png" caption="tickets, tasks, issues - the name does not matter. The software factory needs basic units of work." >}}

### Artifacts

The outputs that collectively satisfy a work item. How a team elects to define these artifacts is again an area of great contention at the moment, and I will argue that the exact delineation and definition of each artifact is less important than the collective ability of *artifacts* + *checks* (below) to prove that a *work item* has been satisfied. I will outline an example artifact set here that has worked well with matching checks in practice, but this is by no means an absolute commandment. The example artifacts: 

- **The Spec.** A prose description of the work to be done. Includes acceptance criteria/definition of done, constraints, context. Clearly defines the *what* and the *why*, explicitly excludes the *how* (code or pseudocode, file names, configs etc). 
- **The Test Matrix.** A table demonstrating how the test suite will prove a work item has been satisfied. This table lists the name, action (add/delete/update), and reason for each test. 
- **The Code.** An isolated git branch containing changes to the codebase which satisfy the Test Matrix, and in turn fulfill the work item as defined by the Spec.

Artifacts serve as hooks, checkpoints for the software factory to evaluate work product. Again, it does not really matter how artifacts are broken down as long as the combination of artifacts + checks against those artifacts facilitate automated, recursive quality assurance. 

### Checks

The codified representation of every statement which must be true for a work item to be satisfied. In our theoretical perfect software factory, checks are an *absolute* and *fully exhaustive* representation of conditions to be met - and by meeting them, the software proves that it is in fact ***perfect***. In practice, checks are the way in which our factory Engineers transfer human intervention into automation. Checks must act on each layer of artifacts - because artifacts without checks provide no value to the system. Some examples of checks (paired with the examples of artifacts above): 

- A check against the Spec to ensure that vertical slices of work are being delivered (avoiding "layer cake" delivery of DB, then service, then UI)
- A check against the Test Matrix to ensure that features from external libraries are not under test (no "test that SQLAlchemy returns an item with the matching ID")
- A check that the `pytest` suite succeeds against the branch code

Traditional software tests are a subset of checks, as are linting, formatting, and static code analysis tools. The superset of checks also include elements that require subjective analysis - "does this agree with our design pattern?" "Is this a minimalist approach to the problem" etc. 

### Agent Runtimes

Software factory work must take place in purpose-built, single use environments that are intentionally designed for purpose. Perfect automation in a non-sterile environment cannot be achieved, as the guard rails needed for such automation directly conflict with the requirements of multi-use hardware. Again, the explicit design of each runtime *instance* is not the focus here and we must not let it distract from the core, important fact that explicit runtimes *must* exist, and each *must* be designed for a single use. I provide these examples based on working runtimes in my experience to demonstrate the intent: 

- **Work Item Runtime.** A container on virtualized hardware (think ECS/Cloud Run) with resources and dependencies required only to build and test the application code. Source control access is limited to retrieving the main code branch and pushing to the designated work branch. Credentials, if any are required, are scoped to the work branch only. Similar minimalist rules for egress, service discovery, web search and package acquisition. 
- **Production Hotfix Runtime.** A container with explicit, single-use credentials allowing read access to production assets and infrastructure, a read-only filesystem (including a read-only copy of the deployed codebase). Highly restricted egress rules. Tools limited to identifying the cause of a production issue/outage and outlining a work item to repair the issue. 
- **Check Runtime.&#32;**A container with minimal required resources and dependencies needed to execute checks against a branch of code, and report back results to the work item agent.
- **Infosec Runtime.** A container with minimal required resources and dependencies dedicated to reviewing known CVEs, white-hat penetration testing of the codebase etc.

How the agent runtimes are defined becomes the ongoing work for our Infosec role (more on that later). In this way the safety and security of the software factory is elevated; sanitary runtimes become a core concern of the factory instead of the localized, best efforts of individuals. 

### Approvals

The software factory may be deconstructed simply as a recursive process of refinement that eventually results in approved changes to the codebase. Approval, in a minimalist sense, means every check has succeeded for a given body of work. While last decade's SDLC thinks of approvals as humans clicking an "approve" button on a pull  request, no part of the software factory explicitly requires such a step. It may be sufficient, and perhaps eventually even ideal (depending on your regulatory environment and your organization's tolerance for change) to define approval without any human intervention. Such a system would be the realization of the idealized XP paradigm of *continuous deployment*. 

Regardless of how an approval is defined, the software factory must have a clear, programmatic state of "approved" from which numerous other processes may hinge. 

### Code Walkthroughs

Checks can only be developed and refined when those Engineers involved possess an intimate, comprehensive understanding of both the codebase and the whole of the application. The software factory must facilitate such understanding by elevating the process of discovery beyond the traditional pull request; it is not enough to present massive code diffs, and in fact, these diffs become less effective at communicating intent and effect as the developers cease to author changes themselves. 

Code walkthrough must evolve to communicate intent and effect holistically. The approach I have taken is to mirror the traditional "lunch-and-learn," where an Engineer with a particular domain expertise will disseminate this knowledge across the team, acting as both guide and historian. 

<pair>

### Demos

In lockstep with code walkthroughs is the live test-driving of new code in a demo environment. Sanity-checking any change to the application must be frictionless. Users, stakeholders, and spot-checking developers must be able to confirm with a live application instance that the proof of success is genuine. 

### Feedback & Observability Surface

The software factory must have uninterrupted conduits of input from every node in the application network. Customer feedback, stakeholder requests, application and service errors - all are work that must be addressed by the factory, and addressed without the aforementioned friction of human meddling. Engineers must focus on improving the speed, correctness, and completeness of the software factory's resolutions of external demands, and forgo the theater of human intervention in the process. Evolution here is not only just the fallacy that a human "pushing the button" at 3AM somehow improves an outcome; it is embracing, *demanding* that the software factory satisfactorily addresses the issue autonomously - and hold the human accountable during business hours *only if it did not*.  

### Security Surface

It is impossible, or at least impractical, to decouple the inevitability of the software factory from the corresponding explosion in threats/bad-actor activity. An exploit now becomes a tragedy at machine speed, and therefore security must evolve from development sidecar to central focus. In the same way that a clipboard hangs next to every industrial freezer with a series of thermostat measurements and accountable signatures, the regular, systematic, and comprehensive review of application security must be core to the operation of the software factory.  

### Product Ownership Automation

Features, bugs, and work items of all kinds never exist in a vacuum. External to the passing of checks, the software factory must coordinate work within the entire organizational context. This can mean: 

- Code freeze during an in-person demo of the application for the board of directors
- Prioritizing the confirmation of a successful hotfix over the deployment of a new feature
- Expediting an application update to help close an important deal

The software factory must perpetually act with context, and communicate both such context, reasoning, and the resulting decisions to the Engineering team.

## The Human Roles of the Software Factory

Truly great systems - those most near to perfection - are often populated by humans who appear to do very little and with very little urgency. Industrial-level success is not denoted by breathtaking heroics; rather by the steady, predictable banality of well-oiled mechanization. The software factory offers the hero of yesterday's SDLC no quarter. The indispensable tribal sage, the caffeine-fueled martyr of impossible deadlines, the code-artist with their tortured brilliance - all no more belong in the software factory than a leather-aproned cobbler belongs in the control room of a *Nike* assembly line. 

This is not to diminish the importance, aptitude, or skill required of the Engineers populating a software factory; quite the contrary, it is important that we understand *"what got us here will not take us there."* 

Consider the example of a contemporary commercial shipping vessel Captain. Traditional ocean-crossing craft required scores of skilled crewmen to maintain heading calculations, anticipate weather and sea conditions, plot and maintain course, and keep lookout for approaching ships or uncharted obstructions. The modern Captain has GPS, NOAA weather forecasts, digital chart plotters, AIS and Radar - each technology far more effective than the human analog it replaced. 

Does this mean the modern sea Captain is somehow the lesser of his predecessor? Hardly. Today's Captain is responsible for safely shepherding vessels the size of small cities, in conditions that would swallow yesterday's tall ships whole and leave no trace. Modern global shipping networks operate in tolerances of hours and minutes, not weeks and months. It is reasonable to assume that Christopher Columbus could no more helm a modern oil tanker than the crew from *Most Dangerous Catch* could pilot his *Nina* or his *Pinta*.   

The roles identified here are positions that make up a complete team, not job titles or identities. I suspect that, similar to an on-call rotation, various levels of structure and organization will develop around how they are assigned. They may be called different things, some functionality may be combined and other functions dispersed - as always, the goal here is not to get bogged-down in minutiae, but to understand the essential roles humans must play in the software factory.

### Ground Pounder

When ground pounding, an Engineer focuses on the work items in flight. Ground pounders dip into active agent sessions, spot-audit Specs, and playback code walkthroughs of proposed the day's changes. Ground pounders offer the most direct feedback to the work as it is happening - they are the source of reviews and comments, critiques of Specs and tests. Ground pounders effect the closest measure the factory has to individual units of work delivered.

### Floor Walker

In the whirling chaos of a factory operating at full-speed, it is important to have individuals paying attention to "the forest from the trees." Floor walking means exploring the codebase and understanding; questioning larger architectural patterns, digging into unfamiliar services, and understanding outliers. Where a ground pounder might ask "why did you decide to make this new function async?", a floor walker would ask "Does this middleware agree (or not) with the larger service architecture we use across the codebase? Please explain." Floor walkers ensure that the localized focus of ground pounding does not lose sight of the larger architectural picture.

### Infosec

Each day brings new CVEs, changes in use patterns, and novel system combinations. Infosec work for an Engineer is twofold; sanity-checking the daily patches and expanded resource requests that address new public CVEs and feature development, while supporting white-hat agents that actively pentest the application and the factory itself. 

### Retro

While the ground pounders labor to create agent feedback, Engineers working retro strive to prevent a need for that feedback in the future. Retros focus on each instance where a human found reason to intervene with the agent, and dissect *why*. Opportunities for automation are identified. Could a check be created to flag this defect for the agent, or context updated to avoid it in the first place? Retro findings inform incremental automation that ultimately moves a software factory closer to unattainable perfection. 

## Behold, the Software Factory

<software factory image>

Let us consider how these components come together in practice.

### Today is Monday

And our software factory is hard at work. 

Our ground pounder opens up the three active tickets in the factory UI: the first one is a request from sales to add multiple currencies for international deals, the second a bug discovery from the app help-bot, and finally a log warning of a repeatedly slow query. She plays the first walkthrough, is satisfied with what she finds, and approves the work. Skeptical of the second ticket, she drops into the active session and presses the agent hard to justify the changes - however upon a closer look she realizes that the bug is indeed a software issue (and not user error). On the last ticket she adds feedback to the SQL query in the code suggesting additional filters. 

Today's floor walker is learning all about how database connections are managed across the app. He comments to the walkthrough agent that no global query timeout exists and that could potentially deadlock the application if slots fill up. The agent creates a new ticket. 

The infosec Engineer for the day supervises three new package updates and reviews the outcome of a (today at least) flawless pentest performance. 

The Engineer on retro reviews the earlier intervention in the help-bot ticket, and agrees with the retro agent assessment that no change was needed (the human Engineer was in error). The next retro, reviewing the SQL query feedback, offers a new check specifically for SQL predicates: "does the SQL query predicate specify only the minimum dataset required to satisfy the use case?" 

The product ownership agent identifies a relationship between the new SQL check, the architectural feedback, and the recently fixed slow query, and drafts a new ticket to address the gap with a purpose-built query abstraction. 

The new multi currency feature, the bug fix, and the better-performing query are live in production before lunch. The cycle continues. 

## Moving Beyond Implementation

This is the software factory. Built in *Rust* or *Go*, on AWS or GCP, it makes no difference. Calling the work *issues* or *tickets* does not matter. What matters is the shift in mindset from "*people who author and maintain code"* to "*people who build and maintain systems that author and maintain code*." This is only the future in the way that Monday is tomorrow; on any greater scale the software factory is already here. 
