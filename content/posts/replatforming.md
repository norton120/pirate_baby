---
title: "The Hindsight Guide to Replatforming"
date: 2024-10-01
tags: ['de','ml']
draft: true
---
I was sketching out architectural recommendations for a client project that, after a successful POC, was ready for the prime-time of production software. I stopped to ask myself _why_ the new arch diagram I was creating looked vastly different from the architecture of the existing concept software; even when my answers seemed solid (they included specific measures of reliability, speed, scale, security), I could not shake the feeling that this felt familiar in a very bad way. I paused to count the number of replatforms I have either been directly responsible for (i.e. several Modern Data Stack conversions) or indirectly impacted by (Data Warehouse reconciliations between the "old" and "new" systems) over the last fifteen years. I came up with thirteen replatforms. Of those thirteen, only four eventually yielded positive product or engineering outcomes; that is a roughly 70% failure rate among replatforms I have personally witnessed. No wonder anything that resembles a re-write, re-architecture, or re-thinking gives me immediate pause. 

### What counts as a replatform?
The exact boundries of what would constitute a replatform are a bit fuzzy, and the distinction between a replatform, refactoring, and the natural evolution of features within a code base can be hard to define. In theory, a replatform is the decision to tear down or replace existing software with something entirely new. This new element could be a change in software framework, a total shift in architecture, or translation into an entirely different programming language (or all three at once!). In the physical world, replatforming would be analogous to bulldozing a derelict building and constructing a new one where the original building had stood. Just like in the real world, developers often play semantics to navigate politically; where the home builder in our real-world example might leave a few feet of the original foundation intact in order to file remodel permits and avoid new construction fees, a software engineering team may leave trivial processes running on the legacy system to avoid a potentially negative _replatform_ label. For purposes here we will use _replatform_ to mean any project where the bulk of an appliation's business logic is migrated to a new framework, architecture, and/or programming language. Contrasting _replatforms_ are _refactors_, where the existing application is re-written (in part or in full) in the same language, framework, and architecture, without changing the externally perceivable functionality of the application. It is worth noting that a refactored application may be modified as a side effect of a refactor - pages may load faster, function more reliably, or cost less to operate - but these improvements are fallout from a refactor's primary concern of making the _codebase_ better. 

### Replatforming is Expensive
All software has a cost. What makes the cost of a replatform so much more painful than feature investment is that there is often no perceivable difference to the business after the cost is incurred. The legacy software did X and Y, and after a $2Million replatform project, the software still does X and Y. That $2 Million got you to the _potential_ for new feature Z, which was hypothetically difficult or impossible while still on the legacy platform. A common mitigation strategy is to pork barrel a replatform in with highly desired features, making the cost that much more palatable. "We will need to rebuild the app if we want feature Z" links the considerable time and cost of the replatform to feature Z, not the replatform itself. 

### Why Do We Replatform - on the surface
There are common themes that typically lead to the conclusion that a replatform is in order. You can expect to find many (or all) of these in a roadmap deck that is calling for replatforming investment: 

- legacy application is unreliable, slow, expensive, old
- fresh clean start
- language or framework has fallen out of style
- limitations of the language or framework
- performance
- hiring challenges with the legacy framework or language

### Why Do We Replatform - under the skin
There are many unspoken motivators for a replatform, and these are the ones to be most aware of and challange the most boldly. 

- signify the reign of a new king
- language preference among engineers
- distant mountain syndrome
- politics
	- system A is owned by team B, and I want to own this so I'll create system C that is owned by me
- novelty, group think & shiny object syndrome
	- old == bad
	- "everybody knows x is faster than y"
- boredom and career stagnation
- fear of obsolescence
	- "if we work in Cobolt how will I ever get a job after this?"

### Logical Falacies of Replatforming
Some common justifications for a software replatform are blatently incorrect, and rely on either a lack of or intentional disreguard for subject matter understanding to persist.

#### Software is Content, Not a Depreciating Asset
Most roadmap decks include an architecture diagram that looks something like this: 
<image>
We often use motors to represent our "workhorse" business applications because that mirrors an industrial model we can understand. And yes, our applications do _run_ on physical hardware - servers and disk drives and devices - that wear out over time. But it is a false analog to imply that the _software_ has worn out - that simply is not how software works. Software is instructions to a computer, stored as text, and text is content - like song lyrics or a novel. Shakespere's _Romeo and Juliet_ has been read likely billions of times by billions of people over the last 400 years, and yet the prose is as impactful today as the day it was written. While many of the printed copies may have worn to dust, this has had no impact on the play itself so long as it continues to be replicated. You application software is not something that wears down with use, and it does not need to be regularly replaced like a hot water heater or a lawnmower with a finite usable life.

#### You Can't Get There From Here
All programming languages eventually compile down to the same machine instructions, just like all human languages eventually compile down to the same inner-congative understanding of the world. The argument that you can only accomplish a certain task in a certain programming language is false, and the extrapolation of that argument - i.e. "we need to change languages/frameworks before we can implement this feature" is by extension false. 

That is not to say that one language cannot be remarkably more suited for a challenge than another; it is likely much more effective to write a collection of famous French love poetry in the French language than, say, Manderin Chineese. But to say such a thing is impossible, that is simply not true. 

#### Newer is Better
Iterative improvement is a core to software development. We learn from experience, and as such software tooling generally exists somewhere along an upward trend line of faster, more reliable, more secure, and easier to work with. It is easy to assume, then, that newer software will always be all these things over it's predecessor. 
But the difference between new and old is often more about the effort to get there than the end product. It is not that older software is inherintly less secure than newer software, just that it is likely easier to get to the same level of security when starting from scrach. Legacy software already exists, and the amount of effort required by that software's creators is irrelivent. Maybe the older framework takes 200% more coding effort to perform at the same speed as the newest framework, but 175% of that work is _already done_. The 25% of effort invested today is still far less than the 100% of effort required to replatform. And there is no future-proofing here; the newest framework will soon be dethroned by another novel framework, and your replatformed application will require that same 25% effort to keep up - such is the perpetual cycle of software development. While good incremental improvement to a long-lived codebase can result in a remarkably hardened and resiliant application, one that reflects years (even decades) of accumulated learning and adaptation, leaping from trend to trend is an excellent way to perpetually re-invent a software wheel.

### Replatform Red Flags
Whether you are an engineering leader considering an application replatform or 
### When Replatforming Should Be Refactoring

### When Replatforming is the Right Answer

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MDEwNDI2MDgsLTE1MzIyMzI5MDIsLT
E2NjQ3MjY3ODQsLTM3MDc4MDEwNywtMTYwNDEzMDA5Nyw3MDg5
NDE5NDhdfQ==
-->