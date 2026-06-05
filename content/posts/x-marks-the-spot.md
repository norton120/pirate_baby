---
title: "X Marks The Spot"
subtitle: "The paths to great fortune and tragedy start at the same fork. You must choose wisely"
date: 2026-06-05
draft: false

---

Chris asked if I could jump on a quick call a few weeks back. I've developed an annoying peccadillo of diving into whatever topic is on my mind at the beginning of a call,  without first confirming with the caller that this is in fact the subject they are calling about; and so, as we connected I immediately launched into app feedback responses with barely a pause for air. Chris waited patiently like they do in the movies, when a supporting character is rattling on about a trivial problem with the dry cleaners while the main character is trying to tell them that aliens have landed in the backyard. 

"I built something with Claude Design. Can I walk you through it?" I had finally shut up long enough for him to course-correct the conversation. He shared his screen, double-clicked a file. Before me, in his browser, was our completed technical accounting app. It looked absolutely nothing like what we had built over the last 18 months. It was perfect. 

He walked me through a happy path, expanding sections and updating values, displaying different levels of information; most of this loosely mapped to what we had already understood about the business data model, but exactly _how_ it came together and why was distinctly different (better). He showed me screens that displayed confidence metrics, chat interfaces linked to specific elements of the reconciliation process - similar in every part to how our software had evolved, but different in tiny, critical ways. Then there were new screens, conversations that had never happened, that suddenly exposed huge gaps in our data model and understanding of the final product. When his ad-hoc demo was completed, I honestly had to take a second to compose myself. I had jumped on this call expecting to issue a quick status update, and instead was being handed the holy grail of software development: a complete, MIT-perfect software specification. Chris had built me a treasure map. 

## The Magic

The conversation around what he had built and his process in building it reflected the most idyllic use of the tool. As Chris and Claude iterated on the html interface, questions surfaced. Conflicts arose, some requiring hard answers Chris didn't have on hand. Cases appeared that required research and input from the team. The act of building a functioning UI prototype forced ambiguity and unknowns into the light, and it did so without needing a single line of application code written ahead of time. 

The product of this effort articulated requirements and _purpose_ for our app in a way that thousands of hours in meetings or a million lines of documentation never would. The prototype showed me in crystal clear Technicolor which things matter to the target users (and just as importantly which _do not_), data dependencies I was missing, order of events, hierarchies, and maybe most importantly, aspirations. If I build this, just like this, we win. This is such an amazing time to be a developer. 

## The Detractors

I was excited about my newfound treasure map, and I shared my elation with other developers in my circle. I was surprised that those who had been approached by stakeholders with similar artifacts were, uh, less enthusiastic.  Criticisms varied, but some general observations:

- The data models in these html prototypes are fictional datasets with little resemblance to the real data state. 

- The prototypes are full of "Escher stairs" - conditions that cannot exist in reality. 

- The UIs are completely out of sync with the real applications - no module parity, styling etc.

- The UI has no allowances for permissions, security, observability, testing... 

I could not wrap my head around the pushback by so many of my colleagues. Who cares if a prototype shows an impossible connection between two points, or represents our data in a completely incorrect way; what really matters is that we now know those points need to be connected, and we understand how the users represent our data in their mental model. When you are handed a treasure map, you don't complain that the boobytrap with the poison spears isn't drawn to scale or uses the wrong font, you are just happy it tells you it is there, so you know when to duck. 

## The Tragic Path

I had missed the difference between what my stakeholder believed he was handing me, and how other, less adept stakeholders viewed their creations. Chris understood that he and Claude constructed an HTML document that _looked_ like an application - similar to a theater stage set, or the dozen well-fed children the state lines up any time someone with a camera visits North Korea. Chris knows his prototype is an artist's rendering; in the past he would have used PowerPoint to slowly, painfully create a lower fidelity version. I have worked with stakeholders using pen and paper sketches, excel sheet finger paintings, wireframe tools etc.  all with the same goal - to communicate to me, in the greatest possible fidelity, what needed to be built. That was what I had here, now in a fidelity beyond pixel perfect. 

But my contemporaries were facing stakeholders that believed they were holding a _completed application_. Not a rendering, not a sketch, but a fully functioning system that just needed some production pixie dust sprinkled on it to be transformed into a real live application. Some stakeholders are already using their HTML sketches across their teams, and with clients, and across the real internet. Many are laptop-hosting the HTML & data files :scream:. This insanity isn't a conscious decision, it is the result of a user telling Claude "my teammates need access to this, make it work" without understanding the consequences of the action. This is no different than if you told a faithfully subservient porter "I don't care if you only have one private compartment left, I want my baby, my full-size wild alligator, my collection of antique live grenades and the brain Gremlin with the glasses from the movie _Gremlins 2: The New Batch_ on your train, and I'm only paying for one compartment!"  Obedience to ignorance can be very, very bad. 

My evaluation of these new prototypes was in the context of a communication medium, similar to tools like Figma and napkin sketches. My evaluation was never as complete, viable software. I was so very lucky that my first stakeholder interaction with this new suite of tools was overwhelmingly positive that I was blind to how wrong this could all go if stakeholders don't understand what they are holding.

### The Map Is The Beginning

What do _Goonies_, _Treasure Island_, _Waterworld_, _Raiders of the Lost Ark_, and countless other treasure hunt movies have in common? They **start** with a map. Knowing where to go and what you can expect along the way is the impetus for the journey, but the journey itself is where the adventure lies - as well as the greatest dangers.  

Stakeholders need to understand that what they have created is exceptionally valuable - it can actually be the key to unlocking software that could otherwise never be built! But it is the very first part of a complex process, not the whole of the story. 

Imagine if the Goonies kids had found One Eyed Willy's map in the attic, shouted "That's it, we're rich now!" and that was the end of the film. The audience in that movie would be confused, because the kids only had a drawing with a treasure chest on it - the bank would still take their houses on Monday. Developers have the same challenge when a stakeholder believes they have built an application with a prototype tool. An interface that looks like a real application but has nothing behind it is an "X" on a map with no real-world value. 

### I Guess This Is Not A New Story

#### Security Has Always Sucked

This feels new and scary at first. 

> A user describes a team ledger app they need to Claude, refines the prototype and gets an HTML page that looks just like a real SaaS product. They tell Claude to "make it available" and now their firewall is opened and they are serving the raw http to teammates over the internet, where they all enter sensitive client data stored in plaintext on the user's machine. 

Yes that is an excellent ghost story to tell around the next dev team campfire. But is this really any different than the buckets of insanity we have always dealt with? 

I went to a marine parts store in rural Virginia a few weeks ago, and was warned ahead of time to bring cash. I watched as the customer in front of me attempted to pay - the cashier said "we only take debit," walked to another room with his card, and then shouted "what's your debit pin" across the store. Apparently that's the system there, and enough people have not pushed back that they have kept it that way. 

The only real new challenge here is that our users need to adapt what silly shit they will not tolerate in the new context. No I won't yell my pin across a store full of strangers. No I won't put customer data into the janky app you built that Chrome makes me acknowledge is dangerous and has a weird http://192.168.50.244:8080 address instead of a real one. Same problem, new surface. That's all. 

#### Good and Bad Stakeholders Have Always Mattered

This also feels new and scary: 

> A stakeholder describes exactly what they want and Claude Design seems to have created it for them, though obviously just as an HTML page. The stakeholder is immediately frustrated by how long it is taking to make the app they think is already done "productionized" and sees the dev team as roadblocks.

A good stakeholder knows that there is so much more that goes into an enterprise application than the UI. A bad stakeholder lacks the self-awareness to understand the scope of what they don't know - Dunning-Kruger exemplified. This isn't new. Terrible clients assume everything is easy, that they could do your job better than you can, and when people are willing to sell them gilded software at the speed they demand it is because you are just too slow. Mr. Hammond wanted his software fast and cheap so he hired Dennis Nedry, and a Tyrannosaurus ate his lawyer as a consequence.  Good stakeholders will learn to use the new tools to communicate their needs more effectively than ever, and bad stakeholders will use them to make even worse decisions. The more things change, the more they stay the same. 

### Please, Build Treasure Maps!

Maybe one of the most exciting parts of this evolution is how informed leadership can be when deciding _what_ to build. Resources are finite, and for every hour of developer time you've got, you'll have 20 hours of good ideas. With fully interactive prototypes, leadership teams can spread out every possible future on the table in front of them. They don't have to imagine, they can interact with every idea first-hand. Good leaders can identify the winning prototypes and then continue to have a first-class medium to communicate with the development team, with a clarity we've never imagined. This is a huge opportunity for good teams to build the right things, together - and for bad teams to footgun themselves like never before. So please, build treasure maps! And then be part of the adventure that follows. 
