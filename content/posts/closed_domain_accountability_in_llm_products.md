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
That is because real products cannot come with an escape hatch. The AI Engineering team is responsible for making the consumer experience right and reliable, full stop. This doesn't mean _the LLM_ needs to get everything right every time - quite the contrary. Engineers must orchestrate the holistic interaction of software, inference, and user to arrive at a reliable and trustworthy experience. 

I once worked with an ecom platform that was being _slaughtered_ by Amazon over shipping timelines. The problem wasn't our actual delivery times (most orders were delivered in 1-2 days), but the logistics of displaying delivery dates while relying on slow and unreliable vendor feeds. We could have slapped an "Estimates are unreliable, and you may get your stuff whenever" disclamer on the page - but that was not the product experience we set out to deliver. We could have also built out a labyrinth of branching logic that would have been a brittle bear to maintain. 

Instead we standardized on free two-day delivery for anything we couldn't reliably calculate via API calls. Simple automated shipping covered the vast majority of these orders, and expedited shipping (which we paid for) took care of slow outliers that turned up during fulfillment. Clear, reliable delivery timelines had a dramatic impact on conversion that greatly outweighed the occasional cost of expedited shipping. We delivered the whole of the feature we promised, not a watered-down version plastered with escape hatches. 

As expectations for Generative Engineering become more grounded in consumer reality, the limitations of a product's parts will not excuse the failings of the sum. That means thinking outside the prompt and beyond your RAG strategy, doing a lot of hard Data Engineering, or Software Engineering, or Product Development - or all of the above - to move past the disclaimers and deliver what you promise.


### Stop playing
Nothing makes my skin crawl like stepping into a Machine Learning stack where one of the repositories is named "Playground." I know that is an unfortunately common nomenclature for experimentation suites, but words matter - and in this case illustrate my issue with production Data Science. 

Commercial Product Engineering teams are not Academia, and the software we write is not intended to promote our personal learning or exploration. Put simply, this is not a place to play. 
_Experimentation_ is an important part of AI/ML development. In Experimentation, the scientific method is applied to stated hypotheses in order to discover new solutions for stated objectives. This experimentation must be systematic and governed by a commercially viable outcome; success is clearly defined and experiments produce metrics reflecting progress toward that success. 

"_Playgrounds_," on the other hand, most often exactly what the name implies: Data Scientists haphazardly adjusting parameters, trying out whatever novel methodology is in vogue at the moment, and traversing down rabbit holes totally unrelated to the initial objective. 
 
Experimentation, on the other hand, results in concrete feedback. "Today I am going to run through the matrix of affinity mask weights, the current match on ground truth is at 86% and we are targeting 90% or better with this experiment." 
Be able to explain exactly what you are doing in an experiment, or it is just playing. 

### Treat Ground Truth Like an Evil Genie
In every genie story someone falls prey to the curse of ambiguous wishes. The genie twists assumptions, plays on words, and transforms every wish into a curse. 

Ground truth datasets for your product should be largely the domain of the Product Owner, and should reflect an interatively tightening understanding of what success looks like. 

### Ruthlessly Define Success
A few times here I have referenced the definition of success. That definition needs to be, uh.. defined. By Product. Be able to answer any question of "can it do" or "what does it do when" without looking at the AI Engineering team. If your AI Engineering team are the only people that can answer "can it do," that means you left the product design up to them. That is stupid, don't do that. 
Create NLUX scripts - just like websites have wireframes, AI-powered products need language "wireframes" from someone who has thought the experience through without worrying about implementation. Those scripts become test cases, and those test cases produce measures of success that are tangiable and not "I'm working on it"

### Use. Metrics. 
If there is one critical difference between open-ended 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc3NDU4MDcwMywtMTYxNTc2NjQzLDEyOD
Y5MzcwNTQsLTE2MTI5MzM3MzQsMTMwOTg5MDA4OCwtMTY2MDQ2
NTYzLDkzNzI0OTMwMiwxMzE1MDk3NDU1LDkzMTgwMzk0NSwtOT
Y2MzUyNzE4LDEwNTIzODMyODIsNjE2NDc5NDc3LDY2NjUzMjUx
NCw4MzcwNzcyMzAsMTM3Nzg0OTUzNCwxNzkzMzQyMTc0LDgxMz
Q4NTgyMiwtNjE4MjM3NzY3LDE3OTY3Mzc2OTYsLTE5MDk5NDA3
NDZdfQ==
-->