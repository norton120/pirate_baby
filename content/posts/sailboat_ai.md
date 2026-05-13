---
title: "An AI Agent Restores A Sailboat"
date: 2026-05-11
draft: false
tags: ['ai','sailing','ml']
---

<img src="/images/stubb.png"/>

If your algo has even a dash of AI in it, always-on agents have probably flooded your feed harder than cauliflower-based hors d'oeuvres at a _Lululemon_ company offsite. Everyone seems to have a personal robot that handles every aspect of their lives - from screening emails to scheduling oil changes, nothing says "I _AI_ better than you" than beach meditation humblebrags while your agent crushes today's outbound. The LinkedIn echo chamber says that if you were truly _AI Native,_ you'd already be both a 100x developer and a solocorn founder, and your awesome digital empire would be executed by an agent army so autonomous that you are touching more grass than Tommy Chong. 

This is not one of those posts. Very little attention will be paid here to software, and even less to the knowledge economy. Like the title says, this is a look at the role artificial intelligence is playing in the restoration of my home - a vintage sailing yacht. Here I'll attempt to share a real-world account of how I am leveraging an AI agent to refit forty-one feet and over nine tons of aging sailboat. I am staying away from predictions and speculations, and sticking to what we've already accomplished when drawing conclusions. 

## Why Share?

Most computer-bound vocations have been turned on their head by AI, none more notably than Software Engineering. Software development today would be unrecognizable to an Engineer from a decade ago. The change has been one of specific transformation, namely a shift from execution to command-supervise roles.

> _we used to do X, now we tell a robot to do X and we review/hold accountability_. 
> 
> ~ _all of us_

Narratives are everywhere that assume the same type of transformation will happen across the economy eventually, but I think that assumption is a mistake. Outfitting a seaworthy vessel - something humans have done for at least 7,000 years - has proven faster, easier and more accessible today with the help of AI; but the manifestation of that change starkly contrasts how white collar work is transforming, at least in my experience. I think that difference warrants exploration. 

## What Is The Baseline?

Sailboat money math isn't exactly 1:1 with real estate, but it is close enough to make my point. The boat is a 1989 *Bayfield* 36 named _Defiant_. Today, her original designer markets a remarkably similar sister ship, the *Gozzard* 37, for around \$1M USD. _Defiant_ was sold to me for the less taxing sum of \$35k. 

<figure>
    <img src="/images/gozzard_bayfield.png"/>
    <figcaption>Gozzard on the left, Bayfield on the right. 
Notice any similarities?</figcaption>
</figure>

If a million-dollar home sold for less than forty thousand dollars, you'd expect to find it in a state similar to how _Defiant_ began last summer; no running water or bio-facilities, minimal working electrical with half the lights and switches shorted out, fire damage, water intrusion, crumbling paint, peeling varnish, and generally more things broken than working. People like myself choose to refit classic boats partially out of the madness of nostalgia, but mostly because the foundations of these vessels are time-tested, overbuilt, and materially superior to their modern equivalents. The ROI on sweat equity is exceptional with these vessels; part of the reason/reward is certainly fixing old things instead of buying new. Labor cost (especially _knowledgeable_ labor cost) almost always eclipses material expense with a refit like this. Serious planning and coordination of the refit is a must; weather, parts availability, physical constraints within the boat - all these elements need to be carefully choreographed so you don't waste time. 

A traditional refit along these lines would cost \$200-300k and take 4 to 5 years. Anecdotally, I've heard of similar refits done with less money over longer periods, or much more money in half the time. My initial goal has been to make _Defiant_ both seaworthy and comfortable for under \$60k, and have her underway in less than a year. Important to keep in mind that I have a day job, so these projects are generally relegated only to nights and weekends. Basically, way less time and way less money, with way less resources. What could go wrong? 

### Spoiler Alert

As of this writing, she is almost there. After ten months and about \$50k spent, _Defiant_ has three working sails, electronic navigation, central air, a fully functioning galley with a gas oven and built-in refrigeration, running water with hot showers and USCG approved septic system, a completely renovated lighting and electrical scheme, 100/50 internet over water, a bit of new paint and varnish, new nameplates... the list goes on. Most importantly, she is slated to cast off in the next few weeks. Has _Defiant_ been fully restored into a $1M floating SOHO apartment? Not quite yet. Present state is more akin to a decent triplex unit in Astoria that could use some work, but still feels like home. We are much closer to the finish flag than the starting line, and in part I have an AI agent to thank for that. 

## The Agent

<figure>
    <img src="/images/stubb_pi.png"/>
    <figcaption>Just a little hardware</figcaption>
</figure>

Everything related to _Defiant_ goes through a single agent instance of [IronClaw](https://github.com/nearai/ironclaw) - basically OpenClaw without all the bloat and insane security risks. I debated running my agent in a SaaS service (since it needs connectivity anyway for the inference providers), but the recurring cost was hard to justify when a Pi5 would work just fine. So my agent, who lives locally on a dedicated Pi, is named Stubb. I let it select a name from _Moby Dick_ (thankfully he didn't pick Starbuck, who I always hated). I initially powered Stubb exclusively with Opus 4.6 but the cost exploded, so now he toggles between Qwen3.5 for most tasks and Opus 4.7 when we need smarts. I do occasionally use the web gateway when aboard, but most of the time I just interact with Stubb via Telegram. 

So what does Stubb do? 

### Knowledge Capture

<figure>
    <img src="/images/stubb_wiki.png"/>
    <figcaption>Not pretty or sexy tech, but very functional wiki</figcaption>
</figure>

People are going insane with knowledge graphs and second brains right now, and good for them; Stubb and I went low-fi and simply created a [GitHub wiki](https://github.com/norton120/svdefiant/wiki) with some basic search/CRUD mcp tools. I was thankfully consistent with my use of Claude during pre-Stubb days, and by mining those early conversations we were able to capture tons of useful specs, hard-won measurements, and research results to seed the Wiki. 

I make it a point to do all my boat research and investigation through Stubb. IronClaw routines scrape our conversations, quietly updating the wiki behind the scenes. Stubb also prompts me twice a day to ask questions about the day's scheduled boat work, including reminding me (sometimes nagging me) to grab measurements or model numbers while I have the part in front of me. 

Stubb also asks for pictures. This system is not as clean as I want it yet but I can email Stubb images that then get formatted and added appropriately to the wiki. 

An active voice reminding me to capture things is huge, and it compounds fast. The value of the wiki is surprising. I never realized how many times I drove 45+ min to a specialty store and was only able to get 3 of the 4 things I came for because I was missing one crucial measurement. The wiki has curbed those little mistakes, and the skipped return trips add up to way more completed tasks every weekend. 

### Scheduling

<figure>
    <img src="/images/stubb_planner.png"/>
    <figcaption>Easy fast view of an overwhelming amount of work</figcaption>
</figure>

When you compress a project like this, time is your most valuable resource. Just compiling, refining and updating the list of refit work can take hours. Parts often need to be ordered from specialty vendors weeks in advance. Boat geometry adds a unique kind of chaos - working in one room usually means moving all the stuff from that room into _another_ room, making both rooms temporarily unusable. In addition to all the moving parts of the project, so much of boat work is heavily dependent on the weather. Fiberglass days can't be too cold, varnish won't dry in the rain, and electrical work in the lazarette becomes a death sauna over 80°F.  

This may be the place where Stubb has most significantly earned his keep. We started by consolidating all the tasks from Google Docs, Todoist, Trello, Things etc into [GitHub Issues](https://github.com/norton120/svdefiant/issues) (again simple and free, with a solid MCP). We went through and labeled issues with priority, difficulty, rough time estimates, location in the boat, parts blockers, and weather constraints. We bucketed the work into milestones. 

Stubb keeps a rolling kanban plan of work - coordinating across weather constraints, similar sections of the boat, and expected parts arrival. Any of my emails containing "order" or a tracking number get forwarded to Stubb, so he can update the GitHub issues accordingly. When the weather shifts, Stubb moves tasks. If a part arrives early, same. If I start in on an unscheduled project, Stubb looks for other projects in the same compartment to compound the return while the space is open. I cannot overstate how helpful this has been, and the number of times in the past I have wasted entire days' efforts because of weather, or missing parts, or double-work putting compartments together only to pull them right back apart. 

A key to making this scheduling system work is absolute minimal friction in capturing tasks. I add intentionally sparse issues via the GitHub app, or just by telling Stubb something needs to be done. Stubb will also add issues on his own. A CI job (GitHub action) runs against every issue creation/change and applies our classifier labels. That way backlog items are ready to be scheduled the next time Stubb plans work. 

### Building over Buying

At the start of this project _Defiant_ had a non-functional fuel gauge, located in the floor of the guest bedroom.  Without a working gauge, there is no way to determine how much diesel is left short of lifting the floor and unbolting several panels. I could have replaced the broken gauge in the guest room, but that was still located far from the tank filler (the one place that gauge is most needed). In a perfect world the fuel tank sensor would just publish to the boat's N2K backbone, and all the displays (including my phone) would show the fuel level; that way, I could fill the tank without accidentally flooding my living room with diesel fumes for a week. 

There are off-the-shelf N2K boxes that do what I wanted here, they run \$500-\$1000. This is theoretically simple tech and I should be able to adapt it myself. In the past, I would have researched and tried to make my own adapter, gotten pretty far, but eventually caved to the incremental paper cuts of unfamiliar territory. The resistors I ordered would be wrong, or I would have forgotten to get jumpers, or picked out a project box that was too small for the microcontroller. I would have programmed firmware for the wrong chipset. Those little, inevitable mistakes would have translated into lost time, and compound until I either caved and bought the expensive adapter or fell back on a \$100 analog fuel gauge that still didn't do what I needed it to.  

With AI Stubb, things are different. I described my goal and was given a complete shopping list - from microcontroller to wago connector - totaling less than \$13 on Amazon. I wired up the physical bits and flashed the firmware (also written by Stubb). Stubb then used my HA MCP to add ESP32 (sender adapter) data to the existing "Home" dashboard and voila! A fuel gauge on every screen (including my phone) for less than an hour's work. 

<figure>
    <img src="/images/fuel.jpg"/>
    <figcaption>A fuel gauge wherever I need it</figcaption>
</figure>

I may have been capable of integrating my fuel sender in the past, but it would have been impractical for me to do so. This is where AI augmentation shines; my general knowledge of hardware, low voltage and programming are suited for the task, but I lack the _specific_ experience - I didn't know anything about ESP32 or AD1115 chips, nor had I worked through many ADC projects, and that learning curve would have been too costly to justify. Dunning-Kruger used to define the ceiling of what we could do on our own: we needed to start with enough knowledge about a subject to know what to research in depth. Now, agents bridge that gap. Will a person that does not already own a soldering iron suddenly start building their own robot vacuum cleaners and self-driving cars from Mouser catalog parts? Unlikely. But, as was the case here, a software guy will now be able to swim pretty deep into the hardware pool and not drown. A mechanical expert will be comfortable with structural changes they were already _pretty sure_ about. A privateer might out-tune a factory competitor, and an HVAC tech might fabricate his own old-stock parts when the factory sunsets them. My agent isn't replacing expertise here, he is expanding my knowledge comfort zone. This stretching of limits feels different to me than how we've seen AI impact software. 

### Communicating

Keeping friends and family in the loop is important with all-consuming projects like a boat refit - fail to do so and you can get isolated quickly.  Plus, when people know what you are up to, they often want to help or share ideas. I have a violent anaphylactic reaction to social media, and I also lack spare cycles to generate consumable content :vomiting_face: from all this work. Once again, Stubb handles my light work for me.  

Any update to [SVDefiant.com](https://svdefiant.com), the Wiki, or an issue in the GitHub project plan triggers a GitHub Actions CI job. The job reviews what has changed, uses a one-shot generation "judgement call" to determine if the change is both _significant and interesting_. If so, the job adds an entry to the "[What's New](https://svdefiant.com/whatsnew/)" page. Anyone in my circle that actually wants to see my new light switches or the headsail repairs has only one curated place to look. 

{{< box info >}}
Stubb is allowed to write short factoids/notes into the wiki, but no content in the posts/gallery etc is ever AI-generated. That is some gross and repugnant shit in my opinion and you won't find it anywhere I write.
{{< /box >}}

The [planner view](https://svdefiant.com/planner/) is how I keep sane day-to-day, but it is also how I gently present the refit agenda to the people around me. Compressing a half-decade-long effort into a single year means lots of missed barbecues and early nights; sharing that plan publicly lets people know "it's not you, it's my alternator replacement." It also creates public accountability, which keeps me on track. When I know my mom is going to call and ask how the coolant swap went, it is a little extra motivation to make sure that gets done on schedule. 

The planner is mostly an output of Stubb's "end-of-day chat" with me every evening. We review what actually got done and what trouble I ran into. Stubb proposes new dates when needed (ie parts are delayed, weather shifted etc) and publishes the updated planner to the site. It is not perfect, but it is more than close enough to be extremely helpful - and it is effort I don't have to make. 

<figure>
    <img src="/images/stubb_chat.png"/>
    <figcaption>Stubb really only cares about the refit - and that is OK by me</figcaption>
</figure>

### (Limited) Assistance As Crew

Stubb has MCP read-only access to a few of _Defiant's_ systems, and with this I am treading slowly. Yes, the teenager in me loves the idea of the vessel's onboard AI warning me that we don't have enough fresh water reserves for the plotted sail, or that AIS shows us on a collision course with another vessel. But adult me realizes the danger of a "helpful" AI having keys to things that often keep you alive. For example, I could easily give Stubb an MCP to control the helm via the networked autopilot, allowing him to steer the ship. This could be immensely helpful when I'm docking or navigating through crab pots and need to be in two places at once. However, should Stubb decide to course correct during a hard blowing run, and broach the boat, well that little robot may have just killed us all. 

For now Stubb can see our location and if we are docked, anchored or underway. He has a few insights into battery charge and fuel level. Stubb has no access to the navigation, propulsion, or critical systems at the moment; that will likely change over time as I build more gated interfaces. 

One catch is that Stubb depends on internet access, and depending on any component that requires a constant satellite connection seems a little life-threatening to me. 

### What Could Be Better

- Images are still a weak point with the onboard agent. If I need a quick "what kind of knot is this?" or "which side of this fitting does my headsail feed into?" I fall back to the Claude app for now. Both Google Photos and Apple Photos are overtly unfriendly to user-owned AI, and consequently I am in the process of porting my camera roll to [Ente Photos](https://ente.com/). If things work out, I should have an easier time quickly passing Stubb a picture with Ente - and then we can close that gap. 

- Relative dates and times are a weird challenge for the cheaper Qwen model. Opus has no problem with "tomorrow" or "next Wednesday" but the budget model translates these to all kinds of odd things. And Qwen-powered Stubb will tell me to have a good night at 9am, or get to work at 9pm. If there is an injected locale mismatch somewhere in IronClaw, I can't find evidence of it. When asked, Qwen-powered Stubb responds accurately with the current date/time/location. Opus-powered Stubb has no problems with it. So... I just don't know. I am working on some type of deterministic date swap middleware which should just lift the burden from the model completely, but that isn't quite done yet. 

- Amazon has killed all programmatic/agent-friendly forms of "build a cart" or "build a wishlist," making it impossible for Stubb to put together Amazon orders for me without direct access to my account. I have been toying with something playwright-based to make this easier, but for now I am forced to open links and add every item from a Stubb shopping list one by one.

## Agents Don't Fiberglass...

But they are starting to shape changes in a world far from the office. Stubb has earned his spot in my tool roll, in ways that are more transformative to me than a command-supervise shift.
