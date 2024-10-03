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
All software has a cost. What 

### Why Do We Replatform?
justifications for a replatform
- fresh clean start
- language or framework has fallen out of style
- 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjY4NTY5NjAsLTM3MDc4MDEwNywtMT
YwNDEzMDA5Nyw3MDg5NDE5NDhdfQ==
-->