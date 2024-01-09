---
title: "Langchain is a Ticking Timebomb"
subtitle: "predictions in AI"
date: 2024-1-9
draft: false
---

Let me preface this by saying that I very much appreciate the entire Lang* ecosystem. At my shop we rely heavily on Langfuse for development as well as the tagging interface for our training strategy. More than a few platforms have tried to be _the_ framework for language model applications (think Guidance, Haystack etc), and the Lang* team has arguably made the most headway, and done it OSS :metal:. So try not to disregard these observations as contrarian or success-hating; I really _want_ to love LangChain. 

When we began work on our inference engine back in October 2023 (so a millennia ago in LLM time) LangChain was the obvious choice. By the first week of December we had abandoned the framework, and by Christmas we had written our own internal prompt templating module to support a Q1 product launch. Such a drastic architectural change at an equally critical time in the product life cycle is not a thing to take lightly. But the growing collection of red flags became something we could not ignore, and I believe we made the best decision. 

What red flags?

### Dependency Management
If you've been around the Python ecosystem for more than a minute, you know that dependencies are the Achilles' heel of the language. This is true for Python as a whole, but I have found this to be exponentially worse in the data sphere. When Software Engineering, Data Engineering and Data Science coalesce, you find deeply abstracted package dependencies with pins like `Cython=>0.1` that "worked before," and lurk in the darkness of deployed code waiting to ruin your weekend. A few years ago the `snowflake-sqlalchemy` adapter was so often the source of surprise dependency failures that my team would comment `we're not snowflake` whenever a bad pin made it to a PR review. 
The general wisdom is to minimize the surface area of dependencies by importing only what your code needs to survive. 
![take only what you need to survive](https://y.yarn.co/84492e53-9f7f-42c3-a8c3-bd088fe3d7fe_text.gif)

LangChain does the opposite of this. The framework currently boasts over 200 supported integrations, every one of them a dependency. If something breaks in the requirements management of the Discord integration, it breaks your project, regardless of if you use Discord or not. 
In November of 2023 this resulted in what is essentially a text compiling framework that takes 18 minutes to build in a container. It was a hopeful sign when LangChain announced that the framework would be split into `langchain-core` and `langchain-community` packages - great! dependency isolation! But as of now that split is still largely academic. Yes there is a `langchain-core` package, which in itself provides little functionality and still feels extremely coupled to the community ecosystem (more on that in a moment). But if you want any of the integration support you are forced to once again adopt the whole wad of integration spaghetti - back to square one. Before LangChain announced a December 7th date to release `langchain-core`, I had taken two days in November to fork the library and try to carve a `core` implementation out myself. That's when I discovered the next of our red flags. 

### Onion Wrapper Architecture
There are dozens of "I re-implemented LangChain in 40 lines of code" posts on Reddit and Medium; I would love to dismiss them all as clickbait, but in truth our prompt templating engine is a couple hundred lines of readable code, and most of our composable "links" that make up our chains are less than 30 lines. 
The LangChain codebase is understandably rushed (2023 was the AI land grab, and a lot of hard choices are made when speed is so critical). But there is a specific pattern, one quite common with inexperienced Software Engineers under pressure, that doesn't just pepper the code base - it is the primary flavor. That flavor is _onion wrapper_ architecture. It goes something like this:
1. I get a thing working for an extremely specific use case
2. I need some of the functionality from that thing, or all of it in a different context, but it has been a minute and I don't really understand how the first thing works. So I import the first thing, wrap it in another thing in my new module, then expose that thing
3. I need parts from the second thing, but don't really understand how that thing works because it's a sort of mangled version of the first thing, so I import that second thing into a third module and wrap _that_ with more code that works, at the moment. 
4. Rinse and repeat, until changing a single quote in a prompt requires you to have 35 files with 1100 lines each open in your text editor. 
There are a ton of reasons this kind of design happens - unreasonable delivery demands being one of them, a wide-open-door contribution policy being another. We have all worked on _application_ codebases that look like this - they are the ones that crash all the time with no warning, take forever to get back up by piling more spaghetti on the mound, and are nearly impossible to add new features or fixes to. Behaviors are hidden deep in the stack ("where did this random timeout setting come from?!?"), and side-effects are take on a black magic all their own. The idea of building on a _framework_ that looks like this... that's frightening. Frameworks are your bedrock, they are the solid base on which applications are erected. Framework code is arguably the highest form of software development, meta-programming at its most impactful. Frameworks are not a place to ship-now-at-all-costs, they are the code that must be reliable for the applications to flourish.

### Not an Application Framework
This was the last red flag, the proverbial nail in our LangChain-shaped coffin. LangChain describes itself as a "framework for developing applications powered by language models." I disagree. LangChain is a software package, a collection of modules, but it lacks the core elements of what can be reasonably called a framework. It is one thing to develop reusable code elements (these are modules), another thing to make that code portable (these are packages). A _framework_ goes beyond "here's a way to access some functions you can use." It is an inherent architecture, a structure that manages how parts of your code interact with each other. Airflow is a framework - it uses file system organization to create a familiar pattern across airflow instances, makes opinionated design decisions that ensure the _application_ will function as a whole if adhered to. FastAPI is a framework that does not leverage the filesystem - it has a clear pattern using routers, routes, lifecycle events and dependencies. Even with a non-standard implementation of FastAPI most developers can grok what is happening and where with few `ctrl+f` searches. 
Frameworks answer the very difficult question of "how should the parts of my code work together?". LangChain does none of this, and is functionally closer to a library like `requests` than it is to an application framework like _Next.js_ or _Rails_. 
The most glaring example of the is the LangChain documentation, where every example exists as a notebook cell. This reflects how LangChain is designed - specifically for isolated scripting, and not as a component in a multifaceted application. Pick any framework - _Django, Phoenix, Electron_ - and note how many points in the documentation refer to multiple files:
```python
# my_route.py
from my_model import Bla
...
all_the_foos = await Bla.awaitable_attrs.foos


# my_model.py
class Bla(Base):
    foos:list[Foo] = relationship(...)
```
When your framework is designed as a pile of scripts, your application becomes a huge pile of scripts. 

### Huh? Moments
About the time we were realizing that the larger `langchain` package was not what we wanted and began attempting to extract `langchain-core` on our own, a similar discussion thread appeared within the LangChain repo. We were excited to see the parity of thought! But [a comment](https://github.com/langchain-ai/langchain/discussions/13823#discussioncomment-7682401) regarding version strategy stood out to all of the team: 
![versioning](/images/versioning.png)

I read this as "_we are going to break things all the time and we'd rather just ship whatever whenever and not worry about the impact of regressions on your code." The space _is_ changing fast, and because of that fact correct versioning is critical. Many of the language-model-related packages we use are already several _majors_ behind from only a few weeks ago - and that is **our** problem, because the space is moving fast and we need to decide when we will do the painful upgrades. But deciding, as a library, not to correctly version because braking changes are expected often... that's like saying "we know the probability of a heart attack is really high, so we're going to get rid of your fitbits so we don't need to deal with warning signs." 

### I have hope
A month after we made the decision to abandon LangChain, much has changed. `V.0.1.0` was released, promising a stable entrypoint and, eh, interesting ([non-semantic](https://blog.langchain.dev/langchain-v0-1-0/#:~:text=Any%20breaking%20changes%20to%20the%20public%20API%20will%20result%20in%20a%20minor%20version%20bump%20%28the%20second%20digit%29)) versioning (but hey at least they set rules?). LangChain is moving to a sensible [stand-alone packages](https://github.com/langchain-ai/langchain/tree/master/libs/partners?ref=blog.langchain.dev) model for integrations. It would be amazing if we see the project mature into either a stable, reliable library, or evolve into a true llm-application framework. And I'll be the first person to condemn our bespoke code to reside in git history and wire up a Lang*-based chain, when (and if) that day comes. But I am confident that the LangChain of right-at-this-moment will be the very center of unreliable, painfully  brittle code bases that organizations are desperate to get away from this time next year.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NjQwMjE2MDYsLTk4MzY2MjIxMiwtOT
M4NDgwMjg3LC0xNTU3NTgyMjcsMTIxMzQzNjYzOCwxMzgyMzYz
MzRdfQ==
-->