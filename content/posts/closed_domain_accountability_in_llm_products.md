---
title: Closed Domain Accountability In LLM Products
tags: ["ai","ml","ops"]
date: 2024-4-26
draft: true
---
_grounding your ML product lifecycle in commerical reality_

If you subscribe to the Gartner predictive model for AI impact and adoption (a.k.a the "AI Hype Cycle") we are still far from peak AI expectations.
![Gartner AI Hype Cycle 2023](https://emt.gartnerweb.com/ngw/globalassets/en/newsroom/images/graphs/swe-hc-image.png)

The endless stream of incredible Linkedin LLM product demos seem to support this model. But another narrative is also taking shape; one of false claims and frustrated users, automation promises unfulfilled, nightmare customer experiences and AI-powered products gone rogue. What I hear on calls and consults is executives with waining patience. There is still an overwhelming excitement around the potential application of large (and small) language models, but the reckless abandon with which AI initiatives were undertaken in 2023 seems to be sobering up. This impending reality check in the AI space is probably not your friend if you play investment shell games for a living; but for those of us that create value by _actually shipping stuff that works_, this is a welcome change in the tide. Rather than a curb of inertia in AI development, we should expect a graduation in the standards and and consumer tolerances for applications leveraging AI.

What does this mean in practice? For one, get ready for AI-powered products to be judged by performance instead of potential.  

So how do we make the transition from squishy intangibles and moving delivery targets to ship _products_ and _features_ that are an unquestionable success?

### Sunset your disclaimers
Here is a banner you won't see:
![Amazon does not need an out clause](images/unreliable_software.png)
That is because products cannot come with an escape hatch. You need to get it right and get it reliable, full stop. 
This doesn't mean _the LLM_ needs to get it right - it means that you, the Engineer, need to find a path between the user, the LLM, and the software you are creating that provides a reliable and trustworthy experience. 

I once worked with an ecom platform that was getting _slaughtered_ by Amazon over shipping timelines. The problem wasn't the actual delivery time - the majority of orders were less than two days from a warehouse - it was the logistics of displaying an estimated delivery date using slow vendor feeds. 

We could have slapped a disclamer "estimates may be innacurate and you may get your stuff whenever" - but that wasn't the product we wanted to deliver. So we built out a simple system: 

1. Display the best guess estimate based on available information
2. Determine the _actual_ timeline once the order has been placed
3. If the actual was greater than the estimate, upgrade the shipping _for free_ to get the actual to match the estimate



### Stop playing

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEzODgyMTk1Nyw2MTY0Nzk0NzcsNjY2NT
MyNTE0LDgzNzA3NzIzMCwxMzc3ODQ5NTM0LDE3OTMzNDIxNzQs
ODEzNDg1ODIyLC02MTgyMzc3NjcsMTc5NjczNzY5NiwtMTkwOT
k0MDc0NiwxNTgyOTY2NDQzLDQ1MjQzNTQyNiwtMTUyMzg5OTE1
Nyw4NTk2ODcyNTMsLTExOTcyMDIzOThdfQ==
-->