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

simply handing off the output of your first solution to the user and wrapping it with a disclaimer is not Software Engineering, it is order taking. Viable products are accountable, even when their individual components are not. 

### Stop playing
Nothing makes my skin crawl like stepping into a Machine Learning stack where one of the repositories is named "Playground." I know that is an unfortunately common nomenclature for experimentation suites, but words matter - and in this case illustrate the issue. 

Commerical Product Engineering teams are not Acedamia, and the software we write is not intended to promote our personal learning or exploration. Put simply, this is not a place to play. _Experimentation_ is an important part of AI/ML development, and by systematically applying the scientific method we can discover new techniques and solutions. That experimentation should be governed by a commerically viable outcome - we know exactly what success looks like, we experiment with laser-focus toward that definition of success, and we have concrete metrics in place to tell us when that success has been achieved. "Playgrounds" often manifest in practice what the name implies: haphazardly adjusting parameters, trying out whatever novel methodology is in vogue this morning, traversing down rabbit holes totally unrelated to the initial goal. At standup, Engineers in the playground say things like "still working on it." 
Experimentation, on the other hand, results in concrete feedback. "Today I am going to run through the matrix of affinity mask weights, the current match on ground truth is at 86% and we are targeting 90% or better with this experiment." 
Be able to explain exactly what you are doing in an experiment, or it is just playing. 

### Treat Ground Truth Like an Evil Genie
All variations of the Genie story have one thing in commin


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY2NjMwOTY3MiwtOTY2MzUyNzE4LDEwNT
IzODMyODIsNjE2NDc5NDc3LDY2NjUzMjUxNCw4MzcwNzcyMzAs
MTM3Nzg0OTUzNCwxNzkzMzQyMTc0LDgxMzQ4NTgyMiwtNjE4Mj
M3NzY3LDE3OTY3Mzc2OTYsLTE5MDk5NDA3NDYsMTU4Mjk2NjQ0
Myw0NTI0MzU0MjYsLTE1MjM4OTkxNTcsODU5Njg3MjUzLC0xMT
k3MjAyMzk4XX0=
-->