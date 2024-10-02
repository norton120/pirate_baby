---
title: "The Hindsight Guide to Replatforming"
date: 2024-10-01
tags: ['de','ml']
draft: true
---
I was sketching out architectural recommendations for a client project that, after a successful POC, was ready for the prime-time of production software. I stopped to ask myself _why_ the new arch diagram I was creating looked vastly different from the architecture of the existing concept software; even when my answers seemed solid (they included specific measures of reliability, speed, scale, security), I could not shake the feeling that this felt familiar in a very bad way. I paused  back and count the number of replatforms I have either been directly responsible for (i.e. several Modern Data Stack conversions) or indirectly impacted by (Data Warehouse reconciliations between the "old" and "new" systems). I came up with thirteen replatforms in the las fifteen years. Only four of those replatforms turned out to yield positive product or engineering outcomes; that is a roughly 70% failure rate among replatforms I have personally witnessed. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzY0MzAyMjczXX0=
-->