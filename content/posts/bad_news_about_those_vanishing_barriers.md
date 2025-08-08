---
title: "Bad News About Those Vanishing Barriers"
date: 2025-08-06
tags: ['ai','ml']
draft: false
---


There is an old Doug Stanhope bit where a news channel polled their viewers “*Will there be a terrorist attack at this year’s Olympics?*" and the results were:
- 70% no
- 28% yes
- 2% I don’t know.

The punchline is that **none of these people know**, and what the survey really tells us is that 98% of people will have strong opinions about things they can’t possibly know anything about. This is what it feels like reading post after article after blog written by Software Engineers and Linkedin pundits on “AI changing everything” and/or “AI not changing anything.” All those click-hunting posts can be summed up in one simple fact: Unless they have a time machine, nobody alive now definitively knows what effect the big AI butterfly flapping its wings will have on our collective futures.

But one narrative that is definitely *not* true (and I am exhausted hearing it) is the “AI removing the barrier to creation” story \- especially where software development is concerned. This parroted idea builds on a handful of false premises, and you do not need a crystal ball to predict that false premises do not lead to true outcomes \- the predicted outcome being that “everyone will create all the software they need all by themselves.” Don’t get me wrong, this *may actually be the case in the future* \- again, I’ve never been there so I can’t say \- but that outcome will not be due to the removal of creative barriers, **because that’s not a thing**.

### Code is not fucking magic

There is this bizarre mysticism around programming and programming code. I hesitate to even say programming languages, because in truth they aren’t *languages*. They are command syntax written in a native language like English or French. The `play` and `fast-forward` buttons on Netflix aren’t *Netflix language*, they are just commands. But somewhere along the way it became reasonable to say “oh, I can’t code” the same way you would say that you can’t leap over a building or breathe fire; that putting English words in order to perform a task, even a trivial one, is a natural-born skill that you either have or do not, and having or not having this basic ability is immutable fact. Let’s look at Python for example:

```python

for cart_item in shopping_cart:
    if (customer_shipping_address.is_california
        and cart_item.is_california_restricted):
        warn_customer.cannot_ship_to_california()
        shopping_cart.remove_item(cart_item)
```

If you speak English, you know what this loop does. You could show this to someone 100 years ago and they could explain what is happening here, without having ever seen a computer. How is this some ironclad impenetrable barrier that has repressed our future utopia for the last 30 years? Fuck it, let’s turn this into actual English.


> For **each** cart item **in the customer’s** shopping cart,
> if **the** customer's shipping address is **in** California
> and **the** cart item is **a** California restricted **item**,
> warn **the** customer **that we** cannot ship to California
> **and** remove **the** cart item
> from **the customer’s** shopping cart.


Mostly “the”,“and”,“a”,“I” \- filler words that don’t convey any actual meaning. Let’s compare this to a text message from my mother:

```text
went to store, no avocados
want guacamole or not the same?
```
Now let’s make that actual English

> **I** went to **the** store, **and they have** no avocados **in stock**.
> **Do you** want **me to get** guacamole, or **is it** not the same **thing**?

The Python programming language is closer to English than my mother’s texts, yet somehow I am able to visit for the holidays without a crushing “barrier” to our communication.

There is this false notion that interacting with programming code requires you to be intelligent, and that is simply not true. I have met some remarkably dumb people that write code for a living. This is not unlike a misconception by many struggling ESL students that English fluency is a sign of intelligence; the news is full of evidence to refute that idea. What *does* require intelligence is solving complex problems, and that is something Software Engineers do very often, so it is easy to confuse the two. But I would argue that the roles that supposedly benefit from this “unlocked barrier” are also roles that already require solving complex problems \- like founders and CEOs and innovators. So, no barrier there either.

I’m not saying everyone on Earth has the capacity, interest or inclination to write production software, in the same way that not everyone that can read and write in English has the capacity, interest or inclination to become a professional journalist or write novels for a living; but it is not a fucking barrier. Long ago, I learned how to write my first programs (in PHP no less) by Yahoo\! searching “how do you make websites.” There wasn’t any gatekeeping entity I had to apply to for permission to learn the language, or fee I had to pay upfront to access the docs. I didn’t have to go into a crystal chamber like Superman to gain the awesome power of coding. I just had to read things, and do work. Lots of it. But work is not a barrier, it is part of a cost-benefit decision, and these are two very different things. Work is not a thing that prevents you from acting, it is acting in itself. You decide what work you do yourself, and what work you delegate. That’s literally what life is, not a barrier to entry.


### We are here because of delegation

I live on a boat. Boats require constant painting, as ocean creatures love to eat away at the hull and paint keeps the water monsters at bay. I enjoy the process of painting; it is cathartic, and an excuse to step away from the keyboard for some oft-needed vitamin D. However, when I recently hauled the boat out to have her bottom painted, I paid the yard to do the painting. I delegated this work for a few reasons:

- I needed it done quickly (I am paying rent until the boat is back in the water)
- I wanted the paint done well since it is below the waterline (barnacle territory)
- I had too many other things to focus on like cleaning the prop and replacing through-hulls to handle painting as well.

I delegated this work to the yard, and for the price I pay I can hold the yard accountable.

This is why we have jobs as programmers. Not because writing code is some mystical power that only we possess; I know the narrative of the bumbling idiot Founder/CEO is super attractive in the current populist zeitgeist, but I have met a *lot* of Founders over the years and they have always been intelligent and ambitious problem solvers that would certainly be capable of writing code if that was really what they wanted to do (or what had to be done). The choice they make not to write code is one of resources. A Founder will have so many things on their plate \- identifying a target market within the TAM, finding product market fit, hiring the right people, securing capital etc etc. \- that the return on investment for a Founder to learn to build a thing, and then build it, is upside down. Founders want a product built well, something they can stake their success on, and they need it built quickly. So Founders delegate this work to someone they can hold accountable.

Tools don’t change this equation. The boat yard used to sand by hand and paint with a roller, which would take about a week from start to finish. Now they use a bead blaster and paint sprayer, and they can complete the whole job in a few hours. They are even willing to rent me the tools, if I wanted, and I could hypothetically save 80% of what I am paying them by using my own labor. But it doesn’t matter if it is 80%, or 90%, or 99% savings; what I am really paying for is accountability. I need to remove the cognitive load of “bottom paint” from my growing list of things that must happen before my boat splashes, and paying to have an important job done correctly, in the timeframe I need it, with someone else in the loop, is well worth the cost. This is why most of us are writing code today; not because of some invisible barrier that protects our sacred knowledge and keeps the ignorant masses locked outside, but because smart, successful people that need code to work as expected know enough to delegate that to people  they can hold accountable. It doesn’t matter if non-coding Founders can vibe code hello world apps any more than it matters that the shop will rent me a paint sprayer; the kinds of Founders that will be successful and run real businesses don’t have time to own accountability for the software (unless the role of Founder drastically changes in the near future, and then the question becomes who will do all the billions of founder things?).

### Accountability automation would need to change drastically

In a business, accountability is like matter \- it cannot be created or destroyed, only transformed and transferred. For a thing to be automated, the automator must accept responsibility \- and that comes with a cost.

For example: There was a time when humans actually sat in toll booths and collected tolls from people. The human in the toll booth was accountable for both collecting the correct toll and returning the correct change. When automated transponders like EZ-Pass came on the scene, the accountability was transferred from the Toll Collector to the EZ-Pass company \- and this is  evidenced by several million-dollar class-action lawsuits when the devices have erred.

SaaS software also made a progression in automation accountability, as we moved from storing customer information on index cards in a locked file cabinet to cloud databases, and saw the evolution of the data breach.

What we don’t see right now, and I can’t imagine we’ll see very soon, is the evolution of AI vibe-coding platforms that are willing to own the same accountability and “unlock the barrier”. Will lovable.dev or Bolt.new issue TOCs that hold them responsible for the security, accuracy, and uptime of the applications users build? Will these unlocked innovators be willing to trust them? And who does the CEO ultimately call and scream at when it’s 3am, the website is down, and users across the globe are abandoning their carts? When we reach a point where Claude or Gemma is an answer to that question, then accountability has been automated and delegation is a real possibility. But this is a much greater sea change than “it generates code without errors.”

### Work is still work

We may see a point where absolutely everything in the process of building a product or a service is completely automated, and all you have to do is say “build me an ecom site that sells pet rocks” and everything else \- product design, marketing, iterations and evolution of the company \- happens on a server while you scroll TikTok. But is that removing a barrier to creation, or just commoditizing business ownership? Haven’t we had that for years with Wix and Squarespace, and did they eliminate these invisible barriers? I’d argue that actual creation requires actual work, with iterations and deviation and experimentation, and that creeps back in on where a Founder’s time is best spent, and the same delegation paradigm. The idea that your cousin will finally move off the couch in your basement and build a SaaS empire now that it doesn’t require knowing Javascript to do so is… unlikely. The barrier here was never that coding is too hard, it was that another *X-Files* rerun is about to start and Grubhub delivers at 3am.

### Most ideas aren’t that good

Close in step with the utopia/doomsday “breaking down the barriers with AI” chum are the toy app posts. In one post, an Engineer that enjoys playing golf with his inlaws vibe-coded a golf score tracker app in a few hours, with his post commentary along the lines of “this changes everything, anyone can build any app they need now\!”

But really this example is excellent, in that what the author built changes nothing. If there was any value to the family in tracking their golf scores they already would have done it a billion easier ways. It could have been a Google sheet or a Google Form, no code needed. It would have likely been a composition notebook before that if anyone had actually cared. This dude's poor in-laws were most likely frustrated with more stupid techno-app-things their daughter’s husband wants them to use, when they really just want to enjoy a golf outing with their family. And herein lies the rub: it takes no effort to build things of no value, and the fact that it’s even easier to build something nobody cares about now, well… It doesn't change the fact that nobody cares about it. What we will see from this is not era of unchained creation, but a tidal wave of crap solutions in search of problems.

This is a hard lesson we should have learned from the internet: the technology to gave every human being a global voice didn’t tear down the barrier to a hidden creative utopia; it just gave us an unfathomable number of cat memes and GRWM videos.

### Good ideas attract good people
Early in my career I did far too much work on spec. So did pretty much every other Software Engineer, because in the beginning you don't understand that your time is finite and you need money to live. What we all did, and thousands of young Software Engineers still do, is invest time in ideas that they believe in. They take equity or an ownership stake in exchange for a their central part in bringing an idea to life. True, these aren't seasoned Engineers with decades of experience (though us old salts do still find the occasional brilliant opportunity we can't pass up). The movies tell us a story of lone entreprenuirs that believe in a brilliant vision that _nobody else can see_, but that's not reality. In reality, if you can't find anyone to buy in to your vision then you either don't understand it well enough, don't have the chops to be a founder, or it's just not that good an idea. If 100 potential technical co-founders walk away from your dream, turning to a sociopathically agreeable code generator isn't likely to solve the root issue - it is just going to waste more of your time and energy as you traverse down the wrong path.

### But what the hell do I know

My point here isn’t to prognosticate outcomes; the future of genAI as of August 2025 is an exercise in [“If You Meet the Buddha On the Road Kill Him”](https://en.wikipedia.org/wiki/Linji_Yixuan). We are all fellow travelers on the same unknown road, and anyone who claims to know the way is not to be trusted.

My point is that of all the popular foretellings, the idea that there is a brimming tide of remarkable creativity that just needs to be unlocked is fiction, and genAI is the MacGuffin in this script. People that are really going to build something were going to do it with or without the help of a language model. And the most powerful, science-fiction-worthy, superhuman AI in the world won’t make builders out of those that aren’t.