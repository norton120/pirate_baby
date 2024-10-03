---
title: "The Hindsight Guide to Replatforming"
date: 2024-10-01
tags: ['de','ml']
draft: true
---
I was sketching out architectural recommendations for a client project that, after a successful POC, was ready for the prime-time of production software. I stopped to ask myself _why_ the new arch diagram I was creating looked vastly different from the architecture of the existing concept software; even when my answers seemed solid (they included specific measures of reliability, speed, scale, security), I could not shake the feeling that this felt familiar in a very bad way. I paused to count the number of replatforms I have either been directly responsible for (i.e. several Modern Data Stack conversions) or indirectly impacted by (Data Warehouse reconciliations between the "old" and "new" systems) over the last fifteen years. I came up with thirteen replatforms. Of those thirteen, only four eventually yielded positive product or engineering outcomes; that is a roughly 70% failure rate among replatforms I have personally witnessed. No wonder anything that resembles a re-write, re-architecture, or re-thinking gives me immediate pause. 

### What counts as a replatform?
The exact boundries of what would constitute a replatform are a bit fuzzy, and the distinction between a replatform, a refactoring, and natural evolution of a code base can be hard to define. In theory, a replatform is the decision to tear down or replace existing software with something entirely new. This new element could be a change in software framework, an architecture, or different software language entirely. This would be analogous to bulldozing a derelict building and constructing a new one where it stood. 
But 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzk4NDc4NjMyLDcwODk0MTk0OF19
-->