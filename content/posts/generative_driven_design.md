---
title: "GDD: Generative Driven Design"
date: 2024-12-29
draft: true
---

_Reflective generative AI software components as a development paradigm_

Nowhere has the proliferation of generative AI tooling been more aggressive than in the world of software development. It began with GitHub Copilot’s supercharged autocomplete, then exploded into direct code-along integrated tools like Aider and Cursor that allow software engineers to dictate instructions and have the generated changes applied live, in-editor. Now tools like Devin.ai aim to build autonomous software generating platforms which can independently consume feature requests or bug tickets and produce ready-to-review code.

The grand aspiration of these AI tools is, in actuality, no different from the aspirations of all the software that has ever written by humans:  to automate human work. When you scheduled that daily CSV parsing script for your employer back in 2005, you were offloading a tiny bit of the labor owned by our species to some combination of silicon and electricity. Where generative AI tools differ is that they aim to automate the work of automation. Setting this goal as our north star enables more abstract thinking about the inherit challenges and possible solutions of generative AI software development.

{{< box info >}}
:star: Our North Star: Automate the process of automation
{{< /box >}}

## The Doctor-Patient strategy

Most contemporary tools approach our automation goal by building stand-alone “coding bots.” The evolution of these bots represents an increasing success at converting natural language instructions into subject codebase modifications. Under the hood, these bots are platforms with agentic mechanics (mostly search, RAG, and prompt chains). As such, evolution focuses on improving the agentic elements - refining RAG chunking, prompt tuning etc.

This strategy establishes the GenAI tool and the subject codebase as two distinct entities, with a unidirectional relationship between them. This relationship is similar to how a doctor operates on a patient, but never the other way around - hence the Doctor-Patient strategy.


{{ < figure src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcDp2anibyh0x6w2WT2zKpMlewkfx-zeaLEPSLXbO7gVtchOvukJgZae10j5c6jpUkQ03kO2dBHxbKglp-uw9srOsZ9jOZYzw8bKE3twCs7c0HLCOdOZfo81ZGCi6QBUEi1EJJx9g?key=1Ec4WTZPrC6aBjphQTmHteq8" title="the Doctor-Patient strategy of agentic coding" caption="the Doctor-Patient strategy of agentic coding approaches code as an external corpus. Image by ethan@pirate.baby" > }}

A few reasons come to mind that explain why this Doctor-Patient strategy has been the first (and seemingly only) approach towards automating software automation via GenAI:
-  **Novel Integration**: Software codebases have been around for decades, while using agentic platforms to modify codebases is an extremely recent concept. So it makes sense that the first tools would be designed to act on existing, independent codebases.
-  **Monetization**: The Doctor-Patient strategy has a clear path to revenue. A seller has an GenAI agent platform/code bot, a buyer has a codebase, the seller’s platform operates on buyers’ codebase for a fee.  
-  **Social Analog**: To a non-developer, the relationship in the Doctor-Patient strategy resembles one they already understand between users and Software Developers. A Developer knows how to code, a user asks for a feature, the developer changes the code to make the feature happen. In this strategy, an agent “knows how to code” and can be swapped directly into that mental model. 
-  **False Extrapolation**: At a small enough scale, the Doctor-Patient model can produce impressive results. It is easy to make the incorrect assumption that simply adding resources will allow those same results to scale to an entire codebase.
    
The independent and unidirectional relationship between agentic platform/tool and codebase that defines the Doctor-Patient strategy is also the greatest limiting factor of this strategy, and the severity of this limitation has begun to present itself as a dead end. Two years of agentic tool use in the software development space have surfaced antipatterns that are increasingly recognizable as “bot rot” - indications of poorly applied and problematic generated code.

 {{ < figure src="" caption="Bot Rot: the degradation of codebase subjected to generative AI alteration. AI generated image created by Midjourney v6.1" > }}

Bot rot stems from agentic tools’ inability to account for, and interact with, the macro architectural design of a project. These tools pepper prompts with lines of context from semantically similar code snippets, which are utterly useless in conveying architecture without a high-level abstraction. Just as a chatbot can manifest a sensible paragraph in a new mystery novel but is unable to thread accurate clues as to “who did it”, isolated code generations pepper the codebase with duplicated business logic and cluttered namespaces. With each generation, bot rot reduces RAG effectiveness and increases the need for human intervention.

Because bot rotted code requires a greater cognitive load to modify, developers tend to double down on agentic assistance when working with it, and in turn rapidly accelerate additional bot rotting. The codebase balloons, and bot rot becomes obvious: duplicated and often conflicting business logic, colliding, generic and non-descriptive names for modules, objects, and variables, swamps of dead code and boilerplate commentary, a littering of conflicting singleton elements like loggers, settings objects, and configurations. Ironically, sure signs of bot rot are an upward trend in cycle time and an increased need for human direction/intervention in agentic coding.

## A practical example of bot rot
This example uses Python to illustrate the concept of bot rot, however a similar example could be made in any programming language. Agentic platforms operate on all programming languages in largely the same way and should demonstrate similar results.

In this example, an application processes TPS reports. Currently, the TPS ID value is parsed by several different methods, in different modules, to extract different elements:

```python
# src/ingestion/report_consumer.py
…
def parse_department_code(self, report_id:str) -> int:
“””returns the parsed department code from the TPS report id”””
dep_id = report_id.split(“-”)[-3]
return get_dep_codes()[dep_id]
…

# src/reporter/tps.py
…
def get_reporting_date(report_id:str) -> datetime.datetime:
“””converts the encoded date from the tps report id”””
stamp = int(report_id.split(“ts=”)[1].split(“&”)[0])
return datetime.fromtimestamp(stamp)
```

A new feature requires parsing the same department code in a different part of the codebase, as well as parsing several new elements from the TPS ID in other locations. A skilled human developer would recognize that TPS ID parsing was becoming cluttered, and abstract all references to the TPS ID into a first-class object:

```python
# src/ingestion/report_consumer.py
from models.tps_report import TPSReport

def parse_department_code(self, report_id:str) -> int:
“””Deprecated: just access the code on the TPS object in the future”””
report = TPSReport(report_id)
return report.department_code
```

This abstraction DRYs out the codebase, reducing duplication and shrinking cognitive load. Not surprisingly, what makes code easier for humans to work with also makes it more “generative-friendly;” consolidating the context into an abstracted model reduces noise in RAG, improving the quality resources of the next generation.

An agentic tool must complete the same task without architectural insight, or the agency required to implement the above refactor. Given the same task, a code bot will generate additional, duplicated parsing methods or, worse, generate a partial abstraction within one module and not propagate that abstraction. The pattern created is one of a poorer quality codebase, which in turn elicits poorer quality future generations from the tool. Frequency distortion from the repetitive code further damages the effectiveness of RAG. This bot rot spiral will continue until a human intervenes with a git reset.

## An inversion of thinking

The fundamental flaw in the Doctor-Patient  strategy is that it approaches the codebase as a single-layer corpus, serialized documentation from which to generate completions. In reality, software is non-linear and multidimensional - less like a research paper and more like our aforementioned mystery novel. No matter how large the context window or effective the embedding model, agentic tools disambiguated from the architectural design of a codebase will always devolve into bot rot.

How can GenAI powered workflows be equipped with the context and agency required to automate the process of automation? The answer stems from two well-established concepts in software engineering.

### TDD

Test Driven Development is a cornerstone of modern software engineering process. More than just a mandate to “write the tests first,” TDD is a mindset manifested into a process. For our purposes, the pillars of TDD look something like this:
-   A complete codebase consists of application code that performs desired processes, and test code that ensures the application code works as intended.
-   Test code is written to define what “done” will look like, and application code is then written to satisfy that test code.
    
TDD implicitly requires that application code be written in a way that is highly testable. Overly complex, nested business logic must be broken into units that can be directly accessed by test methods. Hooks need to be baked into object signatures, dependencies must be injected, all to facilitate the ability of test code to assure functionality in the application. And here is the first part of our answer: for agentic processes to be more successful at automating our codebase, we need to write code that is highly GenAI-able.

Another important element of TDD in this context is that testing must be an implicit part of the software we build. In TDD, there is no option to scratch out a pile of application code with no tests, then apply a third party bot to “test it.” This is the second part of our answer: Codebase automation must be an element of the software itself, not an external function of a ‘code bot’.

### Refactoring

The earlier Python TPS report example demonstrates a code refactor, one of the most important higher-level functions in healthy software evolution. Kent Beck describes the process of refactoring as “for each desired change, make the change easy (warning: this may be hard), then make the easy change.” This is how a codebase improves for human needs over time, reducing cognitive load and, as a result, cycle times. Refactoring is also exactly how a codebase is continually optimized for GenAI automation! Refactoring means removing duplication, decoupling and creating semantic “distance” between domains, and simplifying the logical flow of a program - all things that will have a huge positive impact on both RAG and generative processes. The final part of our answer is that codebase architecture (and subsequently, refactoring) must be a first class citizen as part of any codebase automation process.

## Generative Driven Development

Given these borrowed pillars:
-   **For agentic processes to be more successful at automating our codebase, we need to write code that is highly GenAI-able**.
-   **Codebase automation must be an element of the software itself, not an external function of a ‘code bot’**.  
-   Codebase architecture (and subsequently, refactoring) must be a first class citizen as part of any codebase automation process.
    

  

An alternative strategy to the unidirectional Doctor-Patient takes shape. This strategy, where application code development itself is driven by the goal of generative self-automation, could be called Generative Driven Development, or GDD<sup>1</sup>.

  

GDD is an evolution that moves optimization for agentic self-improvement to the center stage, much in the same way as TDD promoted testing in the development process. In fact, TDD becomes a subset of GDD, in that highly GenAI-able code is both highly testable and, as part of GDD evolution, well tested.

  

To dissect what a GDD workflow could look like, we can start with the aforementioned pillars:

  

### 1. Writing code that is highly GenAI-able

In a highly GenAI-able codebase, it is easy to build highly effective embeddings and assemble low-noise context, side effects and coupling are rare, and abstraction is clear and consistent. When it comes to understanding a codebase, the needs of a human developer and those of an agentic process have significant overlap. In fact, many elements of highly GenAI-able code will look familiar in practice to a human-focused code refactor. However, the driver behind these principles is to improve the ability of agentic processes to correctly generate code iterations.

  

Some of these principles include:

  

-   High cardinality in entity naming: Variables, methods, classes must be as unique as possible to minimize RAG context collisions.
    
-   Appropriate semantic correlation in naming: A Dog class will have a greater embedded similarity to the Cat class than a top-level `walk` function. Naming needs to form intentional, logical semantic relationships and avoid semantic collisions.
    
-   Granular (highly chunkable) documentation: Every callable, method and object in the codebase must ship with comprehensive, accurate heredocs to facilitate intelligent RAG and the best possible completions.
    
-   Full pathing of resources: Code should remove as much guesswork and assumed context as possible. In a Python project, this would mean fully qualified import paths (no relative imports) and avoiding unconventional aliases.
    
-   Extremely predictable architectural patterns: Consistent use of singular/plural case, past/present tense, and documented rules for module nesting enable generations based on demonstrated patterns (generating an import of SaleSchema based not on RAG but inferred by the presence of OrderSchema and ReturnSchema)
    
-   DRY code: duplicated business logic balloons both the context and generated token count, and will increase generated mistakes when a higher presence penalty is applied.
    

  

### 2. Tooling as an aspect of the software

Every commercially viable programming language has at least one accompanying test framework; Python has pytest, Ruby has RSpec, Java has JUnit etc. In comparison, many other aspects of the SDLC evolved into stand-alone tools - like feature management done in Jira or Linear, or monitoring via Datadog. Why, then, are testing code part of the codebase, and testing tools part of development dependencies?

  

Tests are an integral part of the software circuit, tightly coupled to the application code they cover. Tests require the ability to account for, and interact with, the macro architectural design of a project (sound familiar?) and must evolve in sync with the whole of the codebase.

  

For effective GDD, we will need to see similar purpose-built packages that can support an evolved, generative-first development process. At the core will be a system for building and maintaining an intentional meta-catalog of semantic project architecture. This might be something that is parsed and evolved via the AST, or driven by a ULM-like data structure that both humans and code modify over time - similar to a .pytest.ini or pom.xml file in TDD.

  

This semantic structure will enable our package to run stepped processes that account for macro architecture, in a way that is both bespoke to and evolving with the project itself. Architectural rules for the application such as naming conventions, responsibilities of different classes, modules, services etc. will compile applicable semantics into agentic pipeline executions, and guide generations to meet them.

  

Similar to the current crop of test frameworks, GDD tooling will abstract boilerplate generative functionality while offering a heavily customizable API for developers (and the agentic processes) to fine-tune. Like your test specs, generative specs could define architectural directives and external context - like the sunsetting of a service or move to a new design pattern - to inform the generations.

  

GDD linting will look for patterns that make code less GenAI-able (see [Writing code that is highly GenAI-able]()) and correct them when possible, raise them to human attention when not.

  
  

### 3. Architecture as a first-class citizen

Consider the problem of bot rot through the lens of a TDD iteration. Traditional TDD operates in three steps: red, green, refactor.

-   Red: write a test for the new feature that fails (because you haven’t written the feature yet)
    
-   Green: write the feature as quickly as possible to make the test pass
    
-   Refactor: align the now-passing code with the project architecture by abstracting, renaming etc.
    

  

With bot rot only the “green” step is present. Unless explicitly instructed, agentic frameworks will not write a failing test first, and without an understanding of the macro architectural design they cannot effectively refactor a codebase to accommodate the generated code. This is why codebases subject to the current crop of agentic tools degrade rather quickly - the executed TDD cycles are incomplete.

  

By elevating the missing “bookends” of the TDD cycle in the agentic process and integrating a semantic map of the codebase architecture to make refactoring possible, bot rot will be effectively alleviated. Over time, a GDD codebase will become increasingly easier to traverse for both human and bot, cycle times will decrease, error rates will fall, and the application will become increasingly self-automating.

  

## A day in the GDD life

  

A GDD Engineer opens their laptop to start the day, cds into our infamous TPS report repo and opens a terminal. Let’s say the Python GDD equivalent of pytest is something called py-gdd.

  

First, they need to pick some work from the backlog. Scanning over the tickets in Jira they decide on “TPS-122: account for underscores in the new TPS ID format.” They start work in the terminal with:

  

```bash

>> git checkout -b feature/TPS-122/id-underscores && py-gdd begin TPS-122

```

A terminal spinner appears while py-gdd processes. What is py-gdd doing?

-   Reading the jira ticket content
    
-   Reviewing current semantic architecture to select smart RAG context
    
-   Reviewing the project directives to adjust context and set boundaries
    
-   Constructing a plan, which is persisted into a gitignored .pygdd folder
    

py-gdd responds with a developer-peer level statement about the execution plan, something to the effect of

“I am going to parameterize all the tests that use TPS IDs with both dashes and underscores, I don’t think we need a stand-alone test for this then. And then I will abstract all the TPS ID parsing to a single TPS model.”

  

Notice how this wasn’t an unreadable wall of code, unimportant context and comment noise?

  

The Engineer scans the plan, which consists of more granular steps:

1.  Updating 12 tests to parameterized dash and underscore TPS IDs
    
2.  Ensuring only the new tests fail
    
3.  Updating 8 locations in the code where TPS IDs are parsed
    
4.  Ensuring all tests pass
    
5.  Abstracting the test parameterization to a single test fixture
    
6.  Migrating all 12 tests to the new fixture, confirming that they pass with each migration
    
7.  Creating a new TPS model
    
8.  Duplicating all the TPS model logic from the application in the new model
    
9.  Confirming tests all still pass
    
10.  Swapping in the new model at each of the 8 locations, confirming the tests pass with each
    
11.  Updating the semantic architecture to be aware of the new TPS model and edges in the graph that associate with it
    
12.  Updating method names in 2 of the locations to be more semantically distinct
    

  

On confirmation, the terminal spinner appears again. Text appears in red:

  

```bash

Problem in step 3 - I am unable to get all tests to pass after 2 attempts

```

The Engineer looks at the test code and sees that the database test factory is hard-coded to the old ID type and cannot accept overrides - this explains why the py-gdd cannot get the updates to pass. The Engineer explains this via in-terminal chat to py-gdd, and a new sub-plan is created:

  

1.  Roll back main plain step 1
    
2.  Modify database test factory to accept an override for TPS ID
    
3.  Confirm that all tests now pass
    
4.  Update main plan step 1 to include overriding database test factory with parameterized value
    
5.  Re-apply main plan step 1
    

  

In addition, back in the main plan the step “update semantics for database test factory” is added.

  

The Engineer confirms again, and this time the plan completes successfully, and a Pull Request is created in GitHub.

  

py-gdd follows up with a list of concerns it developed during the plan execution:

  

```bash

concerns:

- there are several lower-level modules simply named “server” and this is semantically confusing.

- the tps_loader module aliases pandas as “pand” which is non-standard and may hinder generation.

- there are no test hooks in the highly complex “persist_schema” method of the InnatechDB class. This is makes both testing and generation difficult.

```

  

The Engineer instructs py-gdd to create tickets for each concern. On to the next ticket!

  

## The CI/CD of GDD

In this vision, an Engineer is still very heavily involved in the mechanical processes of GDD. But it is reasonable to assume that as a codebase grows and evolves to become increasingly GenAI-able due to GDD practice, less human interaction will become necessary. In the ultimate expression of Continuous Delivery, GDD could be primarily practiced via a perpetual “GDD server.” Work will be sourced from project management tools like Jira and GitHub Issues, error logs from Datadog and CloudWatch needing investigation, and most importantly generated by the GDD tooling itself. Hundreds of PRs could be opened, reviewed, and merged every day, with experienced human engineers guiding the architectural development of the project over time. In this way, GDD can become a realization of the goal to automate automation.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNTgwMjcyOThdfQ==
-->