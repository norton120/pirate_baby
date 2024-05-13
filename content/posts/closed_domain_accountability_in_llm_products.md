---
title: Restoring the 'Product' in AI Products
tags: ["ai","ml","ops"]
date: 2024-4-26
draft: true
---
_grounding your ML development lifecycle in commercial reality_

If you subscribe to the Gartner predictive model for AI impact and adoption (a.k.a the "AI Hype Cycle") we are still far from peak (inflated) AI expectations.
![Gartner AI Hype Cycle 2023](https://emt.gartnerweb.com/ngw/globalassets/en/newsroom/images/graphs/swe-hc-image.png)
Casual observation supports the Gartner timeline; every week it seems a new Generative AI breakthrough sends techno-pundits and content creators into a frenzy. This week, the breakthrough is multimodal OpenAI GPT-4o: the long-awaited technological leap forward which will no doubt _fianally_ render the human race obsolete 🙄.
The "hype" of this hype cycle is really a manifestation of missaligned understanding.  Most Generative AI products are firmly in the "let's see if this could even work" phase of develpment (properly referred to as experimentation investment). It is a gambler's bet - we _think_ a thing can be done, and if we turn out to be correct there is potential for a huge return. This is very different from the last decade of technology application, one of "we know this absolutely works and is just a matter of implementation." The difference is critical. If an Executive allocated capital and headcount for an e-commerce initiatve in 2023, there was no question about the viable fundimentals of e-commerce; sure, you can get the marketing wrong, or the UX, or the database design - you can fumble the _implementation_ of an e-commerce solution. But you never have to question if _e-commerce even works_. With Generative AI, however, that question remains front and center for every new and individual use case. Many business and technology leaders approached AI strategy in 2023 expecting a familiar process and development cycle, instead finding themselves frustrated by products that never seem to graduate beyond demos. Half-baked chatbots and glitchy, disclamer-laden AI novelty products litter the Gen AI space. As stated wonderfully by Samir Kumar of Turing Capital in a recent [TechCrunch interview](https://techcrunch.com/2024/04/15/investors-are-growing-increasingly-wary-of-ai/): 
> “We’ll soon be evaluating whether generative AI delivers the promised efficiency gains at scale and drives top-line growth through AI-integrated products and services... If these anticipated milestones aren’t met and we remain primarily in an experimental phase, revenues from ‘experimental run rates’ might not transition into sustainable annual recurring revenue.” 

Rather than a curb of inertia in AI development, we should expect a graduation in the standards and and consumer tolerances for applications leveraging AI.

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

"_Playgrounds_," on the other hand, most often live up to their namesake: Data Scientists haphazardly adjusting model parameters, test-driving whatever novel methodologies are in vogue at the moment, and traversing down rabbit holes totally unrelated to the initial objective. 
 
Experiments report metrics - how many test cases remain, how the scores are trending, and if the hypothesis under test is a statistical improvement. Playgrounds generate updates like "I am still working on X" and "Y seems a little better now." 

<replace>
in software engineering we know things will work and we just need to implement them. In Data Science experiments, we don't know if our thing will work. 
asier to grasp when you consider that the immediate goal of each experiment is not feature success, but _hypothesis elimination_ that will ultimately lead to feature success. What does that mean? We experiment because we do not know what will actually work

because the path to success is that much more complex, it is that much more important we can communicate clearly with metrics and measured progress. 
</replace>

### Remember Product Ownership?



### Treat Ground Truth Like an Evil Genie
Ambiguous wishes are the downfall of fairy tail magic lamps; a man wishes for wealth, and the genie transforms him into a rich miser on his death bed. Your ground truth datasets are as equally sensitive to ambiguity. 

Ground truth datasets for your product should be largely the domain of the Product Owner, and should reflect an iteratively tightening understanding of what success looks like. 

### Ruthlessly Define Success
A few times here I have referenced the definition of success. That definition needs to be, uh.. defined. By Product. Be able to answer any question of "can it do" or "what does it do when" without looking at the AI Engineering team. If your AI Engineering team are the only people that can answer "can it do," that means you left the product design up to them. That is stupid, don't do that. 
Create NLUX scripts - just like websites have wireframes, AI-powered products need language "wireframes" from someone who has thought the experience through without worrying about implementation. Those scripts become test cases, and those test cases produce measures of success that are tangiable and not "I'm working on it"


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NTkxNDQ3OTIsLTQyOTI0MTA4OSwtMT
YwOTY3MTEzLC02OTg2MTM1MjAsLTUwOTM5MTc2OSwyMDg2MTM4
NTk3LDMwOTk2NDc3OCwtMjA1NjM1OTgyOSwxNTQzODY2NjU1LD
kwNDcxNDk5NywtMzM0MDMzMTcyLDkwMTkyNTc3MywtMTY3OTMw
MDg0OSwtNDk0MTM4MDMyLC0xNTI1ODU0MTcxLDEzNDgyODQyMz
gsMzQ4MTM0NTM1LC03NTMxODQ2NywtNjY5OTU4MDY0LC0xNjE1
NzY2NDNdfQ==
-->