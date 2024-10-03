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

#### Software is Content, Not Depreciating Assets
Most roadmap decks include an architecture diagram that looks something like this: 
<image>
We often use motors to represent our "workhorse" business applications because that mirrors an industrial model we can understand. And yes, our applications do _run_ on physical hardware - servers and disk drives and devices - that wear out over time. But it is a false analog to imply that the _software_ has worn out - that simply is not how software works. Shakespere's _Romeo and Juliet_ has been read likely billions of times by billions of people over the last 400 years, and yet the prose is as impactful as the day it was written. Many printed copies of the text may have worn to dust, but that has no impact on the play itself so long as it continues to be replicated. You application software is not something that wears down with use, and it does not need to be replaced like a hot water heater with a finite shelf life.

#### You Can't Get There From Here
All programming languages eventually compile down to the same instructions, just like all human languages eventually compile down to the same understanding of the world. The argument that you can only accomplish a certain task in a certain programming language is false, and the extrapolation of that argument - i.e. "we need to change languages/frameworks before we can implement that feature" is by extension false. 
This is not to say that one language cannot be remarkably more suited for a challenge than another; it is 

#### Old is Inferior, New Superior

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MjI1MDA3MzMsLTM3MDc4MDEwNywtMT
YwNDEzMDA5Nyw3MDg5NDE5NDhdfQ==
-->