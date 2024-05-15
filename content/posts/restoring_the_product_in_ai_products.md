---
title: "Restoring the 'Product' in AI Products"
date: 2024-05-14
tags: ["ai","ml","ops"]
draft: false
---
_grounding your ML development lifecycle in commercial reality_

If you subscribe to the Gartner predictive model for AI impact and adoption (a.k.a the "AI Hype Cycle") we are still far from peak (inflated) AI expectations.
![Gartner AI Hype Cycle 2023](https://emt.gartnerweb.com/ngw/globalassets/en/newsroom/images/graphs/swe-hc-image.png)
Casual observation supports the Gartner timeline; every week it seems a new Generative AI breakthrough sends techno-pundits and content creators into a frenzy. This week, the breakthrough is multimodal OpenAI GPT-4o: the long-awaited technological leap forward which will no doubt _fianally_ render the human race obsolete 🙄.

The "hype" in this hype cycle is really a manifestation of misaligned understanding.  Most Generative AI products are firmly in the "let's see if this could even work" phase of development (properly referred to as _experimentation investment_). It is a gambler's bet; we _think_ a thing can be done, and if we turn out to be correct there is potential for a huge return. 

This is very different from the last decade of technology application, one where "we know this tech absolutely works for this application, and is just a matter of implementation." The difference between the two is important. If an Executive allocated capital and headcount for an e-commerce initiative in 2023, there was no question about the viable fundamentals of e-commerce; sure, you can get the marketing wrong, or the UX, or the database design - you can fumble the _implementation_ of an e-commerce solution. But you never have to question if _e-commerce even works in the first place_. With Generative AI, however, that question remains front and center for every new and individualized use case. 

Many business and technology leaders approached AI strategy in 2023 expecting a familiar process and development cycle, instead finding themselves frustrated by products that never seem to graduate beyond demos. Half-baked chatbots and glitchy, disclaimer-laden AI novelty products litter the Gen AI space as a testament to this disconnect. As stated wonderfully by Samir Kumar of Turing Capital in a recent [TechCrunch interview](https://techcrunch.com/2024/04/15/investors-are-growing-increasingly-wary-of-ai/): 
> “We’ll soon be evaluating whether generative AI delivers the promised efficiency gains at scale and drives top-line growth through AI-integrated products and services... If these anticipated milestones aren’t met and we remain primarily in an experimental phase, revenues from ‘experimental run rates’ might not transition into sustainable annual recurring revenue.” 

In other words, consumers are no longer willing to pay for an AI flea circus. We should expect a graduation in the standards and consumer tolerances for applications leveraging AI, and judgement based on performance instead of potential. AI products need to start behaving like _products_ that add tangible value, and not "neat" school science fair projects.  

## Correcting the Course
Maybe you are an Executive growing impatient with the lack of return on your Machine Learning initiatives. Maybe you are an AI Founder watching your runway burn down like the wick of a cartoon bomb as your users fail to convert (or worse yet, churn). Maybe you are an AI or ML Engineer anxious to secure your place before the GenAI music stops. Whoever you are, delivering successful products that incorporate any type of Machine Learning is not all that different from delivering Software in general. The key is understanding how approaches have differed during the GenAI boom, and how they may need to evolve today. 

### Where the Hell is UX and Product? 
![Ignoring the elephant in the room, Copilot](/images/ignoring_elephant_in_the_room.png)

If I was allowed to facepalm my response to only one single pattern in the GenAI craze, this would be it. A stakeholder asks "what will the bot do if the user asks for a refund?" and every head in the room turns to the AI Engineer. Product doesn't know. They own a beautifully detailed user journey map, right up to the big black box titled "Bot Stuff." UX also doesn't know. They can talk at length about font choices and button shading, but shrug when asked what tone the virtual assistant will take with the users. No matter how the AI Engineer answers that question, the room will most certainly melt down as conflicting, unaddressed expectations surface. One stakeholder imagines curt, robotic text responses, while another stakeholder expects a jovial, human-like experience, and nobody has communicated any of this until now. Is it any wonder why a product without product ownership seems lost, or why a user experience design without design seems disjointed? 

Somewhere along the way we decided that AI/ML is the exclusive domain of Data Scientists and ML Engineers, that AI is "smart people magic," a black box that no normal person could ever understand. In fairness, few Data Scientists I know have done much to help the situation. If a Product Owner asks "can the LLM remember things?" they are given an overly technical primer on vector-based RAG, when what they need is an understanding of the features at their disposal and the constraints they must work within. 

However, I have also yet to see a Product team show the slightest interest in owning the feature and behavioral design of generative agents, or a UX team spearhead a plan for natural language user experience (NLUX). Unlike wireframes and brand kits, UX for Natural Language is a whole new domain for most UX Designers. There has been a tremendous focus on the _technical_ aspects of GenAI in the last 18 months, but what about every other discipline in the application ecosystem?  

If we are going to transition GenAI products from exploratory investments into commercial successes, we need to see a comprehensive skills shift across disciplines. It is no longer acceptable that Creative and Product teams exhaustively  craft a homepage layout that speaks to the brand, but then pay no attention to the product that is speaking for the brand with **_actual words_**. 

A set of wireframes illustrates the customer journey across screens and clicks; NLUX designs should illustrate how the conversation between a user and the product must unfold. Happy paths, sad paths, external events, tone, language structure, level of engagement - these are all things Product and UX can flesh out in detail with stakeholders, long before a line of code is written. Of course not everything in the design will be possible or practical - that's where the iterative nature of Software Engineering comes into play. Having a clear, universally understood vision for the product enables AI Engineers to plan and address novel challenges head-on, instead of scrambling on their heels in front of frustrated stakeholders. 

### Is there Demand?
![selling winter coats on the beach, CoPilot](/images/winter_coats.png)

The most fundamental product question seems to have been forgotten by many during the AI gold rush of '23: do people actually want the thing you are building? What proof do you have? Examples abound of useless, unwanted AI products shoehorned into the lives of consumers. There are pointless novelty chatbots baked into every social media platform. Integrated text completions are getting increasingly aggressive about mangling our messages. Most new AI customer service assistants seem remarkably adept at rephrasing "as an AI assistant I am unable to help you" - and not much else. 

Ironically, the nature of many AI products - especially natural language interfaces - makes them straightforward to validate. Whereas testing engagement with a new online billing platform or recommendations engine pretty much requires you to build the thing first, GenAI products that emulate humans can start by _using a human_. 

In an act of [doing things that do not scale](https://paulgraham.com/ds.html), first running a human-powered prototype is a brilliantly simple way to determine if the product in question will actually add value and gain traction. Product and UX designs translate seamlessly into human scripts and interaction guides. If you are a startup founder then this is as simple as chugging a few espressos and firing up a chat window. A larger corporate initiative will need augmented customer service providers, which are easy to find. Emulate the limitations and expectations of the platform you are about to build, and find out if _anyone actually wants this thing_. 

One of my favorite productivity tools added an AI-powered filter builder about a month ago. Instead of typing the filter code `(tomorrow | next+week)`, I can now type `show me events that are scheduled for tomorrow or next week`.  Then the assistant chugs for about 10 seconds, and replaces my natural language text with `(tomorrow | next+week)`.  It's a cute novelty, but the filter already had great typing hints - this new feature is slower and requires more typing than the product they already had. I have not used the AI feature since, and I would be amazed to learn that general adoption has been any different. Take advantage of how unusually easy it is to validate GenAI demand before you build (or as soon as possible if you are already building) and you'll be that much closer to a viable product. 

### Sunset Disclaimers
Here is a banner you won't see:
![Amazon does not need an out clause](/images/unreliable_software.png)
That is because real products cannot come with an escape hatch. The AI Product and Engineering teams are responsible for a consumer experience that is right and reliable, full stop. This doesn't mean _the LLM_ needs to get everything right every time - quite the contrary. Engineers must orchestrate the holistic interaction of software, inference, and user, in alignment with the vision of product, in order to arrive at a reliable and trustworthy experience. 

Unreliable components in systems are not exclusive to GenAI, or remotely new to the Software world in general. A few years ago I worked on an e-commerce platform that was struggling with conversion due to shipping timelines. The problem wasn't the actual deliveries (most orders were delivered in 1-2 days), but the logistics of displaying delivery dates while relying on slow and unreliable vendor feeds. A cop-out would have been to slap an "Estimates are unreliable, and you may get your stuff whenever" disclaimer on the page - but that was not the product experience we set out to deliver. Alternatively, the team could have spent months constructing a labyrinth of brittle branching logic across hundreds of vendors and warehouses, which would have been a nightmare to maintain. 

Instead, free two-day delivery became the default for any item without an available timeline. Simple automated shipping covered the vast majority of orders, and expedited shipping took care of the few slow outliers that turned up during fulfillment. Clear, reliable delivery timelines resulted in a dramatic uptick in conversion, greatly outweighing the occasional cost of expedited shipping. This was the feature as promised, not a watered-down version plastered with disclaimers and excuses. 

If you want your GenAI product to be commercially viable, you can't expect users to bear the brunt of responsibility in a transaction. Get rid of the disclaimers and ship a product that lives up to what it promises.

### Stop Playing
![scientists on a playground, Copilot](/images/scientists_on_playground.png)

Nothing makes my skin crawl like stepping into a Machine Learning stack where one of the repositories is named "Playground." I know that is an unfortunately common nomenclature for experimentation suites, but words matter - and in this case illustrate my issue with Data Science held over from the zero-rate era. 

Commercial Product Engineering teams are not Academia, and the software we write is not intended to promote our personal learning or exploration. Put simply, this is not a place to play. _Experimentation_, the distant cousin to the playground, is an important part of AI/ML development. In Experimentation, the scientific method is applied to stated hypotheses in order to discover new solutions for stated objectives. This experimentation must be systematic and governed by a commercially viable outcome; success is clearly defined and experiments produce metrics reflecting progress toward that success. 

"_Playgrounds_" generally live up to their namesake: Data Scientists haphazardly adjust model parameters, test-drive whatever novel methodologies are in vogue at the moment, and traverse endlessly down experimental rabbit holes totally unrelated to the initial objective. 
 
Experiments report metrics - how many test cases remain in this experiment, how the experiment scores are trending, and if the hypothesis under test is a statistical improvement. Playgrounds generate updates like "I am still working on X" and "Y seems a little better now." 

Individual experimentation failures eventually lead to product success; each systematic failure furthers the process of elimination, closing distance to either finding success or proving exhaustively that the hypothesis is false. Playground failures are actual failures, as each random trial is effectively isolated and contributes no reportable progress towards a definitive result.

Playtime is over. Design, plan, and execute experiments to build a commerically viable product.

### Ground Truth is a Magic Lamp
![data genie, Copilot](/images/data_genie.png)

If you are granted three wishes by a genie, leave no room for interpretation. Ambiguity is how you end up turned into a tortoise ("I want to live for centuries!") or the Mona Lisa ("I want to be famous!"). As you are constructing the ground truth datasets for a GenAI product, leave even less ambiguity in your design. 

Language models will astound you with how creatively they can screw up while still following the rules. They may perfectly extract every book title from 1000 reviews, and then fail the first time they see a sentance with no uppercase letters. They may halucinate if you change "the user" to "a user." They may decide all unknown sirnames should be "Stalone." 

Comprehensive ground truth coverage is how you iterate and avoid regressions. While synthetic datasets can be useful, in my experience nothing compares to diverse human-authored cases. The case above with "the user" and "a user" is a real-world example; I believed that I had created ground truth data in a wide variety of tones and patterns, but it took just one submission from a different team member (with a slightly different writing style) to expose a failing case. Reliability is the cornerstone of any commerically viable product, one that results from methodically eliminating these failing cases. Each new failing case must be captured as ground truth and celebrated as a tiny victory - because every case captured represents one more known permuation that can be definitively solved. The larger the list of failing cases identified, accounted for and corrected, the closer the product is to commerical viability.

This can be a difficult thing for teams (and stakeholders) to wrap their heads around at first; the process is hard, nessesary work, and it differs greatly from classical Software Engineering. That difference, if not understood, can be disasterous: If Engineers and Stakeholders confuse an initial "happy path" demo with a finished product, then identifying failing cases will be negatively viewed as "finding bugs".  Each new case, in actuality a step closer to success, will be perceived as further evidence of failure. Don't go down this path. Success in GenAI is about how many different ways the user can _not_ do the right thing and still achieve the desired result, how tolerant the system can be of deviation. Relentlessly curate and expand ground truth datasets, they are the foundation of a commerically viable GenAI product. 

## Is This A Good Thing?
I tend to think so. The possibilites of GenAI (and a broader interest in all of Machine Learning in general) is more exciting than ever; there are real, tangiable ways this technology can and will improve human life. Meaningful advances come from signal, not noise, and a return to product fundimentals is the best way to dial in focus on products that actually matter. I look forward to fewer happy path demos and more real, viable products we can rely on every day. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjI0NjQwMTg5LDEzMDk0Nzk4MSwtMTI4NT
I0Njk2NCwtMTY2MTcxNDY3MiwxNTk1NDcyMzM5LC0zODc2NTk2
NDIsMTI5Nzc0MTc4NCwtMTg2NjU4MTAzNiwtODI0MDExNTc2LD
EwNDc5NTQzMTUsLTkxMzc4MjcwNSwtMTkyMzcwMDg5Nl19
-->