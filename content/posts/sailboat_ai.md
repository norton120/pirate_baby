---
title: "Sailboat Restoration With an AI Agent"

draft: true

---

If your algo has even a dash of AI in it, always-on agents have probably flooded your feed harder than cauliflower-based hors d'oeuvres at a _Lululemon_ company offsite. Everyone seems to have a personal robot that handles _everything_ digital in their lives - from screening emails to scheduling oil changes, nothing says "I _AI_ better than you" than beach meditation while your agent tackles today's outbound. The LinkedIn echo chamber claims that If you are truly _AI Native_ you'd already be both a 100x developer and a solocorn founder, with enough automated efficiency to touch more grass than Tommy Chong along the way. 

This isn't one of those posts. Very little attention will be paid here to software, and even less to the knowledge economy. Like the title says, this is a look at the role artificial intelligence is playing in the restoration of a vintage sailing yacht, right now.  This attempts to be a real-world account of leveraging an AI agent to help refit 41 feet and 9 tons of nearly half-century old sailboat. There are no predictions or speculations here - this is stuff that has already happened and/or is happening today. 

## Why Share This?

Most computer-bound vocations have been turned on their head by AI, none more than Software Engineering. Software development today would be unrecognizable to an Engineer from even a few years ago. The change has been one of specific transformation, namely a shift to command-supervise roles: we used to do X, now we tell a robot to do X and we review/hold accountability. Narratives are everywhere that assume the same type of transformation will happen across the economy eventually, but I think that assumption is a mistake. Outfitting a seaworthy vessel - something humans have done for at least 7,000 years - has proven faster, easier and more accessible with the help of AI, and the impact starkly differs from the white collar change model. I think that's worth a closer look. 

## What Is The Baseline?

Sailboat math isn't exactly 1:1 with real estate, but it is close enough to make a point. The boat is a 1989 *Bayfield* 36 named _Defiant_. Today, her original designer markets a remarkably similar sister ship the *Gozzard* 37 for about \$1M USD. _Defiant's_ purchase price was \$35k. 

<image bayfield and gozzard>

If a million-dollar home sold for less than forty thousand dollars, you'd expect a state similar to how _Defiant_ started last summer; no running water or facilities, minimal working electrical, fire damage, water intrusion, and generally more things broken than working. People like myself choose to refit classic boats like this not because we are insane (well, that's not the only reason), but because the foundations of these vessels are time-tested. The ROI on sweat equity is exceptional on these vessels, and part of the reason/reward is building things instead of buying. Labor cost (especially _knowledgeable_ labor cost) almost always eclipses material expense with a refit like this. And serious planning along the way is a must; weather, parts ordering and arrival schedules, physical constraints within the boat - all these elements need to be choreographed. 

A traditional refit along these lines would cost \$200-300k and  4-5 years. Anecdotally, I've heard of similar refits for less money & longer periods, or much more money in half the time. My goal has been to make _Defiant_ both seaworthy and comfortable for under \$60k, and have her underway in less than a year. Important to keep in mind that I have a day job, so these projects are generally relegated only to nights and weekends. 

As of this writing, she is almost there. _Defiant_ has three working sails, electronic navigation, central air, a fully functioning galley with a gas oven and built-in refrigeration, running water with hot showers and USCG approved septic treatment, a completely renovated lighting system and 300M+ internet. Most importantly, she's slated to leave the dock in the next few weeks. Has the boat been fully restored into a $1M floating SOHO apartment? Not quite yet. Present state is more akin to a nicer triplex in Astoria.  

## The Agent

<image of pis in nav desk>

Everything related to _Defiant_ goes through a single agent instance of [IronClaw](https://github.com/nearai/ironclaw) - basically OpenClaw without all the bloat and insane security risks. I debated running the agent in a SaaS service, but the costs are hard to justify if you want meaningful persistance - so my agent lives locally on a Raspberry Pi5. The agent's name is Stubb - I let it select any character from __Moby Dick_ (except Starbuck who always annoyed me). I initially ran Stubb on Opus 4.6 but the cost exploded, so now he toggles between Qwen3.5 for most tasks and Opus 4.7 when I need smarts. I'll use the web gateway when aboard, but most of the time I just interact with him via telegram. 

So what does Stubb do? 

#### ### Knowledge Capture

<image of github wiki>

People are going insane with knowledge graphs and second brains right now, and good for them; Stubb and I went low-fi and simply created a [github wiki](https://github.com/norton120/svdefiant/wiki) and some basic search/CRUD mcp tools.  I was thankfully consistent with my use of Claude during the earlier parts of the refit, and by mining those early conversations I was able to capture tons of useful specs, hard-won measurements, and research results in one place. 

I make it a point to do all my boat research and investigation through Stubb. Ironclaw routines scrape our conversations, quietly updating the wiki behind the scenes. Stubb also prompts me twice a day to ask questions about the day's scheduled boat work, including reminding me (sometimes nagging me) to grab measurements, model numbers etc. while I have a part in front of me. 

Stubb also asks for pictures. This system is not as clean as I want it yet (Google photos has locked down agent access so I am in the process of migrating to a more friendly platform) but I can email Stubb images that then get formatted and added appropriately to the wiki. 

Having some(one/thing) to remember to capture things, so I don't have to, is huge. And the value of the wiki is hard to overstate; the first time I drove 45 minutes to West Marine and forgot the part I needed to replace, that part number in the wiki paid back all the spent tokens and saved me a lost day of boat work. 

### Scheduling

<image of planner>

When you compress a project like this, time is your most valuable resource. Just compiling and refining the lists of tasks that need to be done can take hours. Parts often need to be ordered from specialty vendors weeks in advance. Boat geometry adds a special kind of chaos - working in one room usually means removing all the stuff and access panels, then making both that room _and_ the room that is temporarily storing that stuff largely unusable. On top of all these moving parts, so much of boat work is heavily dependent on the weather; fiberglass days can't be too cold, varnish won't dry in the rain, and wiring in the lazarette becomes a sauna in the heat.  

This may be the place where Stubb has most significantly earned his keep. We started by pouring all the tasks I had scattered across Google Docs, Todoist, Trello, Things etc into [Github Issues](https://github.com/norton120/svdefiant/issues) - again something simple and free with a solid MCP. Then we went through and labeled issues with priority, difficulty, rough time estimates, what sections of the boat they are in, if we are waiting on parts, and weather constraints. We bucketed the work into milestones. 

Stubb keeps a rolling kanban-style plan of what work needs to be done next and when - coordinating weather, similar section of the boat, and planning around parts arrival. Any of my emails with "order" or tracking numbers get forwarded to Stubb so he can update the issues with estimated parts arrival dates. If the weather shifts, he moves the tasks accordingly. If a part arrives early, same. If I start in on an unscheduled project, he looks for other projects in the same compartment to compound the value of clearing it out. I cannot overstate how helpful this has been, and the number of times in the past I have wasted entire days' efforts because of weather, or missing parts, or double-work moving compartments around. 



If there was any friction to capturing the work that needs to be done the pipeline would break down - so I have gone to great lengths to streamline the process. I add intentionally sparse issues via the GitHub app, or by telling Stubb something needs to be done. Stubb will also add issues I miss. A CI job (GitHub action) runs on every issue creation/change that applies lables (What kind of weather is needed for this work? where in the boat is this located? Does it need parts?) so the classification is frontloaded before the next scheduling run. 

### Building over Buying

At the start of this project _Defiant_ had a non-functional fuel guage in the floor of the guest bedroom. The fuel tank is in the blige and sealed, so there is no reasonable way to determine how much diesel is in the tank (without ripping up the whole salon floor and undoing several sealed panels). Even if I replaced the broken gauge it is still nowhere near the fuel fill where it is actually needed. Ideally, the fuel level sender would just publish to the boat's NMEA2K backbone, so I could easily see the fuel level on all the displays and on my phone; that way I could max out the tank without filling my living room with diesel fumes for a week. 

In the past I would have researched 



The fuel sender. in the past I couldn't have afforded to spend the time to build it, too far out of my core skill set. now I can spend \$4 in parts instead of \$300 for a \$4 box.

### Communicating

Keeping people in the loop is important out here. You get isolated fast. Plus, if people know what you are up to, they often want to help or have ideas. 

- CI reviews all changes to Wiki and blog and publishes "what's new"

- Planner view makes it easy for me, and also for my friends and the marina crew to know what I'm working on
