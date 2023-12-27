---
title: "A Complete Containerized CD Pipeline With AWS and Cloudflare for 2024"
date: 2023-12-27
draft: true
---
Recently I went about standing up a fresh Continuous Delivery pipeline for a new project. The project is a relatively standard containerized stack with nothing exceptional to speak of, and as our exploratory work was already in AWS I decided to launch this CD in AWS CodePipeline. Furthermore, we wanted to dogfood our long-term infra management (this project is infra abstraction/automation software) and so opted _not_ to use to or CloudFormation templates - that way we could have a fully "Clickops'd" infrastructure for our tools to reclaim and manage. Besides, Clickops is easy right?

To my surprise, nothing worked. Deploying CD for a very standard stack (details to follow) via GUI clicks is a bizarre dance filled with broken states and never-resolvable circular dependencies, magic file/variable names that are either not documented or documented incorrectly (like the variety of spellings for `appspec.yaml / AppSpec.yml / appsec.yml` across AWS CodeDeploy docs), cryptic error codes, and incompatible default settings. Some of this is nothing new - all the clouds have quirks. But I was taken off guard by just how bad, how completely _non-functional_ I was suddenly finding these services which I had used happily for years. 

Maybe I have gotten too comfortable with infra as code, or maybe ECS and CodePipeline have gotten significantly more brittle in the last year. Maybe this is the multiverse where AWS services are much, much worse and I am a lost traveler. Whatever the reason, I decided that once this project was successfully deployed I would codify the process, in detail, as a guide for others (and my future self). This is that guide.

## How To Guide: 

{{< box warning >}} 
**Do not skim this guide!** If you are like me, you normally skim over these things, copy the code examples, and refer back when you hit errors. **Don't do that.** The ClickOps process here is like a ritual dance, missing one tiny step will anger the AWS gods and _you will have to start over from the beginning._ Suck it up and read the whole thing, and follow exactly step by step, or pain will follow.
{{< /box >}}

### Legend
To minimize repetition I am going to use the following icons as shorthand:
- :monocle_face: **Copy exactly.** I know, AWS docs or a tutorial might claim you can change the filename or specify the path somewhere; my experience has been that not all the configs are respected, and often only the default paths/names actually work. If you choose to deviate, best of luck to you.

### Steps
1. #### Start your magic files.
Our pipeline needs 3 files placed in the root directory of your project. 
2. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDc1MzU5MjY2LDIwMDc2MDg4NDMsLTg1MD
E5MTAxOV19
-->