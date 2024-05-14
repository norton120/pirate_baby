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

## Correcting the Course
Maybe you are an Executive growing impatient with the lack of investment return on your Machine Learning initiatives. Maybe you are an AI Founder watching your runway burn down like the wick of a cartoon bomb, as your users fail to convert (or worse yet, churn). Maybe you are an AI or ML Engineer anxious to secure your place before the GenAI music stops. Whoever you are, delivering successful products that incorporate any type of Machine Learning is not all that different from delivering any other Software. Let's dive into where they do differ, and how that might be corrected. 

### Where the Hell is UX and Product? 
If I was allowed to facepalm my response to only one single pattern in the GenAI craze, this would be it. A stakeholder asks "what will the bot do if the user asks for a refund?" and every head in the room turns to the AI Engineer. Product doesn't know - they have a detailed user journey map that leads right up to the big black box titled "Bot Stuff." UX doesn't know - they can talk at length about font choices and button shading, but have no idea what type of tone the virtual assistant will take when interacting directly with the user. No matter how the AI Engineer answers, the room will most certainly melt down as conflicting, unaddressed expectations surface; one stakeholder imagines curt, robotic text responses, while another stakeholder expects a jovial, human-like experience. Is there any wonder why a product without product ownership seems lost, or why one without cohesive user experience design seems disjointed? 

Somewhere along the way we decided that AI/ML is the exclusive domain of Data Scientists, that it is the "smart people magic" black box that no normal person could ever understand. In fairness, few Data Scientists I've known do much to help the situation. A Product Owner asks the team "can the LLM remember things?" and is given an overly technical primer on vector-based RAG; what they needed was applicable understanding of the features they have at their disposal, and the constraints they must work within. 

But I have also yet to know a Product team that has shown interest in owning the product features and behavior design of generative agents, or a UX team that spearheaded a plan for natural language user experience (NLUX). Some of this gap is just a reflection of how recently the technology has become mainstream; UX Designers know how to build wireframes, but UX for Natural Language is a whole new domain. 

If we are going to transition GenAI products from exploratory investments into commercial successes, we need to see a skills shift across the entire application team. It is no longer acceptable that Creative and Product labor ad nauseam with concern for what a page layout says about the brand, but pay no attention to what the thing that is actually speaking for the brand, with **words**, is saying. 

A set of wireframes illustrates the customer journey across screens and clicks; NLUX designs should illustrate how the conversation between a user and the product must unfold. Happy paths, sad paths, external events, tone, language structure, level of engagement - these are all things Product and UX can flesh out in detail with stakeholders, long before a line of code is written. Of course not everything in the design will be possible or practical - that's where the iterative nature of Software Engineering comes into play. But having a clear, understood vision for the product enables AI Engineers to plan and address novel challenges head-on, instead of scrambling on their heels in front of frustrated stakeholders.

### Sunset Disclaimers
Here is a banner you won't see:
![Amazon does not need an out clause](images/unreliable_software.png)
That is because real products cannot come with an escape hatch. The AI Product and Engineering teams are responsible for a consumer experience that is right and reliable, full stop. This doesn't mean _the LLM_ needs to get everything right every time - quite the contrary. Engineers must orchestrate the holistic interaction of software, inference, and user, in alignment with the vision of product, in order to arrive at a reliable and trustworthy experience. 

Unreliable components in systems are not exclusive to GenAI, or remotely new to the Software world. A few years ago I worked on an e-commerce platform that was struggling with conversion due to shipping timelines. The problem wasn't the actual deliveries (most orders were delivered in 1-2 days), but the logistics of displaying delivery dates while relying on slow and unreliable vendor feeds. A cop-out would have been to slap an "Estimates are unreliable, and you may get your stuff whenever" disclaimer on the page - but that was not the product experience we set out to deliver. Alternatively, the team could have spent months constructing a labyrinth of brittle branching logic across hundreds of vendors and warehouses, which would have been a nightmare to maintain. 

Instead, free two-day delivery became the default for any item without an available timeline. Simple automated shipping covered the vast majority of orders, and expedited shipping took care of the few slow outliers that turned up during fulfillment. Clear, reliable delivery timelines resulted in a dramatic uptick in conversion, greatly outweighing the occasional cost of expedited shipping. This was the feature as promised, not a watered-down version plastered with disclaimers and excuses. 

If you want your GenAI product to be commercially viable, you can't expect users to bear the brunt of responsibility in a transaction. Get rid of the disclaimers and ship a product that lives up to what it promises.

### Stop Playing
Nothing makes my skin crawl like stepping into a Machine Learning stack where one of the repositories is named "Playground." I know that is an unfortunately common nomenclature for experimentation suites, but words matter - and in this case illustrate my issue with Data Science held over from the zero-rate era. 

Commercial Product Engineering teams are not Academia, and the software we write is not intended to promote our personal learning or exploration. Put simply, this is not a place to play. _Experimentation_, the distant cousin to the playground, is an important part of AI/ML development. In Experimentation, the scientific method is applied to stated hypotheses in order to discover new solutions for stated objectives. This experimentation must be systematic and governed by a commercially viable outcome; success is clearly defined and experiments produce metrics reflecting progress toward that success. 

"_Playgrounds_," generally live up to their namesake: Data Scientists haphazardly adjust model parameters, test-drive whatever novel methodologies are in vogue at the moment, and traverse endlessly down experimental rabbit holes totally unrelated to the initial objective. 
 
Experiments report metrics - how many test cases remain in this experiment, how the experiment scores are trending, and if the hypothesis under test is a statistical improvement. Playgrounds generate updates like "I am still working on X" and "Y seems a little better now." 

Individual experimentation failures eventually lead to product success; each systematic failure furthers the process of elimination, closing distance to either finding success or proving exhaustively that the hypothesis is false. Playground failures are actual failures, as each random trial is effectively isolated and contributes no reportable progress towards a definitive result.

### Is there Demand?
The most fundamental product question seems to have been forgotten by many during the AI gold rush of '23: do people actually want the thing you are building? What proof do you have? Examples of useless, unwanted AI products being shoehorned into our lives are already everywhere. There are pointless novelty chatbots now built into every social media platform. Integrated text completions are getting increasingly aggressive about mangling our messages. Most new AI customer service assistants seem remarkably adept at rephrasing "as an AI assistant I am unable to help you" - and not much else. 

Ironically, the nature of many AI products - especially Natural Language interfaces - makes them remarkably easy to validate. Whereas testing engagement with a new online billing platform or recommendations engine pretty much requires you to build the thing first, GenAI products are typically emulating humans. So... _you can start by using a human_. In an act of [doing things that do not scale](https://paulgraham.com/ds.html), first running a human-powered prototype is a brilliantly simple way to determine if the product in question will actually add value and gain traction. [Product and UX designs](#where-the-hell-is-ux-and-product?) translate seamlessly into human scripts and interaction guides. If you are a startup, you can load up on espresso and power it yourself. If you are part of a larger corporate initiative, augmented customer service providers are easy to find. Emulate the limitations and expectations of the platform you are about to build, and find out if _anyone actually wants this thing_ enough to justify the cost of building it. 

One of my favorite productivity tools recently added an AI powered filter builder - so instead of typing `(tomorrow | next+week)` I can type `show me events that are scheduled for tomorrow or next week`.  Then the assistant chugs for about 10 seconds, and replaces my natural language text with `(tomorrow | next+week)`.  It 

### Treat Ground Truth Like an Evil Genie
Ambiguous wishes are the downfall of fairy tail magic lamps; a man wishes for wealth, and the genie transforms him into a rich miser on his death bed. Your ground truth datasets are as equally sensitive to ambiguity. 

Ground truth datasets for your product should be largely the domain of the Product Owner, and should reflect an iteratively tightening understanding of what success looks like. 


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA5ODk4NjQ5LDk5OTA1MTkxNSwtMTc4Mz
A2NjE3MiwtMTk4MDE5MzY2OCwtNDI5MjQxMDg5LC0xNjA5Njcx
MTMsLTY5ODYxMzUyMCwtNTA5MzkxNzY5LDIwODYxMzg1OTcsMz
A5OTY0Nzc4LC0yMDU2MzU5ODI5LDE1NDM4NjY2NTUsOTA0NzE0
OTk3LC0zMzQwMzMxNzIsOTAxOTI1NzczLC0xNjc5MzAwODQ5LC
00OTQxMzgwMzIsLTE1MjU4NTQxNzEsMTM0ODI4NDIzOCwzNDgx
MzQ1MzVdfQ==
-->