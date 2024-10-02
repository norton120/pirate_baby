---
title: "The Hindsight Guide to Replatforming"
date: 2024-10-01
tags: ['de','ml']
draft: true
---
I was sketching out architectural recommendations for a client project that, after a successful POC, was ready for the prime-time of production software. I stopped to ask myself _why_ the new diagram I was creating looked vastly different from the architecture of the existing concept software; even when my answers were not wrong (nuanced measures of reliability, speed, scale, security), I could not shake the feeling that this felt familiar in a very bad way. 
I stopped to count the number of replatforms where I have either been directly responsible (i.e. several Modern Data Stack conversions) or indirectly impacted by (Data Warehouse reconciliations between the "old" and "new" systems). I came up with 13. Only 4 of those replatforms turned out to yield positive product or engineering outcomes; that is an estimated 70% failure rate for the replatforms I have witnessed personally. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwODg0Mzk0M119
-->