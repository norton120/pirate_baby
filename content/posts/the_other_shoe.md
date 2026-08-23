---
title: "The Other Shoe"
date: 2026-08-21
tags: ['ai','ml']
draft: false

---

It is hard to believe that we are nearly half a decade into the genAI gold rush. It can feel centuries longer and also impossibly more recent in the same memory. Those first signals of real agentic coding filled us in the field with wild speculation about the future; would we be digital puppet masters, orchestrating the strings of agent armies, or possibly glorified Product Owners with only a pinch of the truly technical remaining? Maybe we'd be Cyborg independent contributors, cranking out pixel-perfect applications at unthinkable speeds, or maybe we'd go extinct - the buggy whip makers of our generation. Way back then, we would spar with each other over which cyberpunk dystopia we believed would prove prophetic. But I think - beyond the nervous laughter and false, pessimistic bravado that accompanies any need to summon bravery when charging into the unknown - I think we were _optimistic_ back then. Maybe naively so. I think we saw the tools and the tech developing, we understood the magnitude of the change that was to come, and we foolishly believed we could control (or at least meaningfully influence) the outcome in our own realm. I remember saying things like 

> "*It used to take a month of hard burn to ship something we can now ship in two days - so we'll deliver in a week, the clients will be thrilled, and we'll work half as much.*" 

What's more, I know that I believed what I was saying at the time. History favors the argument; the five day work week and the decline of child labor are low-hanging fruit if you are intent on arguing that work-life gets perpetually less burdensome as society makes progress.

# On Agentic Development

What gets forgotten is that while industrialization made five day work weeks the standard, life was quite miserable for those caught in the transitional period. Henry Ford famously had to _double_ factory worker salaries to get employees to stay after introducing the assembly line. The job had become monotonous, soul-crushing and exhausting, and the workers didn't want to do it anymore even with the invention of weekends. This point begs consideration: while the future of the collective human race might be one of near-utopian prosperity made possible by AI, that future may be one built on a foundation littered with our crushed remains - the poor mortals caught up in the AI transition meat grinder. 

As an industry, I think Software Engineering drastically underestimated how long it would take our client base to adapt expectations. Many decades ago, we figured out how to combine silicon - basically rocks - with electricity, and make them do math. It took users years to embrace and expect the technology of math-rocks (ie calculators). Then, we taught those same rocks to send pictures and words over phone lines, and another decades-long adoption ensued. Now, we've taught those same rocks to talk - really talk, just like a person, and do work for us, and sometimes even pretend to _be_ us. The great Software Developer misstep was believing talking rocks would remain a thing of wonderment for our clients long enough for us to get a running start in front of the technology. We collectively presumed that by the time consumers were demanding seven-day turnarounds, we'd be ready to consistently ship in two. Instead we saw our client's suspension of disbelief mutate supernaturally with exposure to consumer AI products; ChatGPT and Claude CoWork made techno-magic instantly mundane, and our carefully cultivated mutual understanding of what is both possible and realistic in software development was dashed against the rocks by ubiquitous generative AI. 

> Rocks can talk now, so why can't you have my IP-laden, bleeding-edge SaaS app in production by 9AM tomorrow? 

The effect is zero-sum. Agentic development may have made us 10X faster, 10X more effective Software Engineers, but commercial agentic products have diluted our perceived value by at least that. 

### Software Engineers As Cartilage

A dramatic and oft-undiscussed consequence of agentic coding is our collective loss of agency as Software Engineers. There was something romantic about the egalitarian nature of development pre-agentics. Tools were inconsequential; the product of an Engineer with the most expensive JetBrains IDE and every DataDog/CircleCI/Github subscription imaginable could still be _buried_ by an app written by some kid in Southeast Asia with a Windows XP desktop and nothing but Vim. 

Today that level playing field is gone; there is no question that resources are the exponent value in the equation. In the hands of a capable engineer, absolutely nothing will have a greater impact on the speed, quality, and magnitude of software development than frontier models with tokens to burn. That same kid can hammer away in Vim until his fingers and eyeballs bleed, until he collapses and dies with one last `:w` , and not make a fraction of the progress two dozen well-scaffolded agents have made in the same time. 

This newfound dependency on LLM access means that ultimately, we no longer hold control of our destiny. Our augmented development capacity with these tools is such that, when they become unavailable, development stops. Switching back to hand-coding would be the equivalent of walking from NY to LA because your car broke down. It is almost always faster and more logical to wait for your car to be fixed. 

And these tools do become unavailable, a lot. Inference providers have not figured out reliability yet - not even close. Anthropic's outage rate would warrant a breach of contract with any mature service provider, and yet this is what we get from a firm targeting \$2T in valuation. 

<figure style="border-color:#efefef; padding: 1px;">
<img src="/images/aposematism.png"
  <figcaption>Beware anything with colorful stripes!</figcaption>
</figure>

For decades, a Software Developer's agency was complete - and so, in turn, was that Developer's responsibility. When a bulldozer breaks down on a construction site, the job is delayed. The foreman has a mental model distinguishing the driver from the equipment; Software Engineering does not have that at the moment. Anthropic recently released Opus 5 and it has proven to be a massive step backwards for the platform. Anyone doing heavy lifting with Claude Code suddenly found their primary work tool inoperable (the agent abandons well-established codebase conventions, goes of on destructive lunatic tangents, ignores clear instructions and spouts walls of gibberish). We waited for the tool to get better, to fix itself. It didn't. It still hasn't. 

While the construction foreman does not throw a shovel at the bulldozer driver and demand that they move mountains by hand, that is exactly the kind of accountability-without-agency Software Engineers have lived with over the last quarter. The new table stakes expectations - days to complete work that would have required months before agentics - are completely dependent on unreliable tools served by nascent companies in a fledgling industry. This is where Developers are getting crunched - acting as shock absorbers between unmoving business and unreliable tooling vendors. 

### As Things Stand Today, This Shit Is Going To Kill Us

I am not speaking metaphorically here. A single human nervous system is just not equipped to withstand continued exposure to whatever full-scale, full-throttle agentic development does to the host over time. And before the token-whore children in the cheap seats pipe up about how they are running 345 agents at once every day and have never felt better, I am talking about actual software development, not stacking a dozen agents against code you never eyeball and _really hoping_ :crossed_fingers: that what the bots agreed on came out decent. If you are using agentic workflows to create long-term-maintainable, enterprise-quality software for which you have an ongoing personal responsibility, and you are shipping that code as fast as the tools enable you to ship, then you know exactly the phenomenon I am struggling to describe here. There is a unique type of burnout, a draining not just of energy but of _life force_, that comes from long-term, intense agentic coding. I think it has to do with context management; in the manual coding days you needed to keep sections of the codebase in your head while you wrote - the size of these sections governed by the size of the change you were making. You could generally only write one set of changes at a time, and so you only needed context for that one change in your head. But agentic coding lets you - scratch that, **demands** you - run dozens of changes at once, each with their own context. The changes fly past each other in the codebase and your mind becomes a busy airfield, with you the stressed-out air traffic control agent trying to prevent a catastrophe. 

<figure >
    <img src="/images/matrix.avif"/>
    <figcaption>
        Anthropic's new, soon-to-be-released Claude Pod 1.0
    </figcaption>
</figure>

It is simple math - what used to take months now takes hours. That means the contextual build, decision and architecture processes that our brains used to spread over enough time to go from ugly holiday sweaters to beach bbqs now happens between breakfast and lunch. I'm not a doctor, but I know something is very wrong here. Whenever I finally close my laptop at night, I feel like I've spent a day with that machine from *The Princess Bride*. For me the experience is universal - regardless of what software I'm developing, if it is agentic, it is the same sensation of being _drained of life_. There is no state of flow,  no endorphin jolts, no sense of personal victory - just the low, siphoning action of the agentic pump, text streaming down in a flow that may as well be my own vitality. I wait for the PR to review, and I jiggle the life pump if the flow gets stuck - confirm an action, correct a test, provide credentials - so the extraction of my will to exist can continue. I use `/rc` and `Termux` so I can keep the pump running when I step away - at the DMV, the grocery store, sitting at a bar having a \$16 old-fashioned, never once offloading the full context from 130k lines of code from my addled brain. 

<figure>
   <img src="/images/princess_bride.jpg"/>
    <figcaption>
        Westley was actually just trying to change a button font using Opus 5.
    </figcaption>
</figure>

When TIG welding was first invented in 1941, it was a mechanical miracle. With science we could suddenly join metals via an electrochemical bond stronger than the parts. It changed the way we build, the way we manufacture, even the types of products that were possible. But welding galvanized steel has nasty side effects for those doing the work - a condition we now call metal fume fever. I wonder if today's Agentic Software Developers will someday have a place in history next to these welders, or the commercial insulation folks with mesothelioma, or the old painters with lead poisoning. 

### I Still Believe Multiplayer Agentics Is The Answer

I wrote about this a while back that [the Pull Request needs to die](https://pirate.baby/posts/the_pull_request_needs_to_die/). Pull Requests are the mastubatory perpetuation of a process that no longer has any relevance with how we author code, and they are exacerbating the agentic burnout problem. In a nutshell: 

{{< box note >}}



*Say you have ten developers on a team today. You likely have eight with Claude on mostly autonomous loops coding a ticket, pushing a PR, responding to comments, and then merging.*

*You have two devs actually reading ALL the code that ten devs are generating (their own code as part of development, and then everyone else's code in the PR review process). You effectively have eight people behaving as very expensive cron jobs, and two people burning the fuck out as human batteries, powering the workload of the whole team. The PR process encourages this, because the eight cron jobs still look amazing based on the mismatched way the old flow measures contribution. :man_facepalming:.*

{{< /box >}}



Slack just launched [Slack Code](https://slack.com/features/code-channels) which I hope is either a huge success, or an inspiration for whatever agentic multiplayer coding finally evolves into. While I don't believe any _one_ human nervous system can handle the load of these tools turned up to eleven - a team of humans can create a pool of resources that trends towards balance. I ramble enough about this in that PR piece, so I won't belabor the subject here any more. 

## On Building Agentic Software

While the whole of Software Engineering has been dramatically disrupted in the genAI roller coaster, it is a shallow ripple across a still pond when compared to the raging sea of change in Data Science. 

In 2012, The _Harvard Business Review_ called the role of Data Scientist "the sexiest job of the 21st century." They were the modern day alchemists, masters of a realm that we all understood to be both mysterious and powerful (with mystery only exceeded by its' power). That realm, the art of producing concrete value from the plastic soup of statistics, was once aptly described to me by a brilliant Data Scientist as "gift wrapping clouds for a living." 

Engineers and technical leadership used to make room for these folks to breathe, and created needed abstraction from immediate stakeholder demands. That is how science works; You experiment methodically, the process takes as long as it takes, and if you try to force it, you are likely to spoil the efforts. Spinning up a Data Science team used to require both an appetite for novel intellectual property, and a stomach for the (sometimes infuriatingly slow) scientific method. With the rise of commercial LLM inference SaaS, that mysterious and powerful realm is suddenly just an API key away. Gone are those guard rails, and that mutual understanding. 

Deep in those plug-and-play inference providers still beats a mysterious, powerful non-deterministic inference function heart. What you get from the service is unreliable content by _design_ - that's the nature of generative AI. Remember, AI stands for "Artificial Intelligence." Humans, who supposedly have the actual biological intelligence from which we model this artificial stuff, had a popular game in the 1970's called _Simon._ The point of the game was to hit the colored lights, repeating the pattern the game displayed. Sometimes we'd get the patterns right. Sometimes, we wouldn't. We're non-deterministic by nature, and so is the artificial version of us that these services now offer on tap. 

<img src="/images/simon.jpg"/>

Half a century of computing has schooled our users that computers are deterministic, software is concrete and Software Developers are both directly responsible for the correct output of that software and completely in control of how quickly and correctly that software evolves. If you needed a program to add two numbers together in 1999, the developer was personally in control of how long it took to make that program. If the program returned 2+2 as 7, the programmer made a mistake. Users also know what Data Science looks like; they can leverage a demand planning forecast or loss ratio regression without fixating on granular specifics or prediction decimal points. 

Building agentic-integrated software products lie somewhere between the two worlds, and we haven't found the balance yet. This new exposure is every Data Scientist's worst nightmare. 

>  The app should tell me exactly what I expect it to say, and if it doesn't, the software is broken.

And maybe this is the ugliest part of where we are, the jagged clash of mental models between former Data Scientists, Data Engineers, and Software Engineers who's worlds have been abruptly slammed together into one big binary stone soup. Integrating ML models with a consumer-facing application was once a deliberate process, bridging the religious-caste creativity of probabilities science with the military-caste structure of application code. The extended time and cost of building those models meant the integrations evolved at a pace at which both sides had time to adapt. But with instant inference, the disconnect is stark. 

Let's say we have a generative harness that can prepare and submit a complete S-Corp federal tax return for a user. 

- It gets the return 100% correct 74% of the time. 

- It gets the return between 80-99% correct 22% of the time.

- It erases all the tax documents and deletes the return 4% of the time. 

To the Data Scientist, the harness **works**. This is a success, and the question now is an ROI determination for the business - how much additional research investment do we want to move that 74% number? 

To the Software Engineer, the harness is **broken**. They see the agent not do what is expected, even once, and they think in terms of binary - it is not right, so it must be failure. To them "It sometimes works" is indicative of bad code, not a property of probability science. 

Both are right in their own realm - but now those realms have nearly zero air gap between them. We need to redefine how these pieces fit together before the incompatible world views drive both sides of the equation insane. 

## And So, The Other Shoe Drops

I think it is safe to say the VC fun-money days of the early AI gold rush are firmly behind us. With them went a sense of wonder and infinite possibility, replaced by a growing number of harsh, sometimes bordering on dystopian, realities. The winners (as always) will be those that adapt. 



We have to rethink how we work as software teams, let go of outdated paradigms that no longer fit, and redefine our relationships with those for whom we build. If we are going to eliminate the space between ML and application software, we have to blend the qualitative thinking of Data Science into the very quantitative processes of Software Engineering, and develop warrior-priests that know instinctively both when to demand determinism and how to evaluate inference. 



And we need to move quickly, before we are lost in the transition. 


