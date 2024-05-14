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
The "hype" in this hype cycle is really a manifestation of misaligned understanding.  Most Generative AI products are firmly in the "let's see if this could even work" phase of development (properly referred to as _experimentation investment_). It is a gambler's bet - we _think_ a thing can be done, and if we turn out to be correct there is potential for a huge return. This is very different from the last decade of technology application, one where "we know this tech absolutely works for this application, and is just a matter of implementation." The difference between the two is critical. If an Executive allocated capital and headcount for an e-commerce initiative in 2023, there was no question about the viable fundamentals of e-commerce; sure, you can get the marketing wrong, or the UX, or the database design - you can fumble the _implementation_ of an e-commerce solution. But you never have to question if _e-commerce even works in the first place_. With Generative AI, however, that question remains front and center for every new and individualized use case. Many business and technology leaders approached AI strategy in 2023 expecting a familiar process and development cycle, instead finding themselves frustrated by products that never seem to graduate beyond demos; the half-baked chatbots and glitchy, disclaimer-laden AI novelty products litter the Gen AI space are a testament to this. As stated wonderfully by Samir Kumar of Turing Capital in a recent [TechCrunch interview](https://techcrunch.com/2024/04/15/investors-are-growing-increasingly-wary-of-ai/): 
> “We’ll soon be evaluating whether generative AI delivers the promised efficiency gains at scale and drives top-line growth through AI-integrated products and services... If these anticipated milestones aren’t met and we remain primarily in an experimental phase, revenues from ‘experimental run rates’ might not transition into sustainable annual recurring revenue.” 

We should expect a graduation in the standards and consumer tolerances for applications leveraging AI, a judgement based on performance instead of potential. In short, AI products need to start behaving like _products_, and not school science fair projects.  

Maybe you are an Executive growing impatient with the lack of investment return on your Machine Learning initiatives. Maybe you are an AI Founder watching your runway burn like the wick on a cartoon bomb as your users fail to convert (or worse, churn), or an Engineer anxious to secure your career chair before the GenAI music stops. Lucky for us, this is not a new process; If you are involved in a Generative AI initiative, there are meaningful steps that will set you on the road to success. 

### Where the Hell is Product? 
If I have to choose only element of the Gen AI craze to facepalm over, this is it. 


### Sunset Your Disclaimers
Here is a banner you won't see:
![Amazon does not need an out clause](images/unreliable_software.png)
That is because real products cannot come with an escape hatch. The AI Product and Engineering teams are responsible for a consumer experience that is right and reliable, full stop. This doesn't mean _the LLM_ needs to get everything right every time - quite the contrary. Engineers must orchestrate the holistic interaction of software, inference, and user, in allignment with the vision of product, in order to arrive at a reliable and trustworthy experience. 

Unreliable components in systems are not exclusive to Generatve AI, or remotely new to the Software world. I once worked with an ecom platform that was being _slaughtered_ by Amazon over shipping timelines. The problem wasn't delivery times (most orders were delivered in 1-2 days), but the logistics of displaying delivery dates while relying on slow and unreliable vendor feeds. A cop-out would have been to slap an "Estimates are unreliable, and you may get your stuff whenever" disclamer on the page - but that was not the product experience we set out to deliver. Alternatively, the team could have spent months constructing a labyrinth of brittle branching logic across hundreds of vendors and warehouses. 

Instead, free two-day delivery was the default for any item without an available timeline. Simple automated shipping covered the vast majority of these orders, and expedited shipping took care of slow outliers that turned up during fulfillment. Clear, reliable delivery timelines had a dramatic impact on conversion that greatly outweighed the occasional cost of expedited shipping. this was the feature as promised, not a watered-down version plastered with escape hatch disclaimers. 

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
eyJoaXN0b3J5IjpbLTc5MDY1NDc3OCwtMTk4MDE5MzY2OCwtND
I5MjQxMDg5LC0xNjA5NjcxMTMsLTY5ODYxMzUyMCwtNTA5Mzkx
NzY5LDIwODYxMzg1OTcsMzA5OTY0Nzc4LC0yMDU2MzU5ODI5LD
E1NDM4NjY2NTUsOTA0NzE0OTk3LC0zMzQwMzMxNzIsOTAxOTI1
NzczLC0xNjc5MzAwODQ5LC00OTQxMzgwMzIsLTE1MjU4NTQxNz
EsMTM0ODI4NDIzOCwzNDgxMzQ1MzUsLTc1MzE4NDY3LC02Njk5
NTgwNjRdfQ==
-->