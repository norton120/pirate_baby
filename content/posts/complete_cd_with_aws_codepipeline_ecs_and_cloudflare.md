---
title: "A Complete Containerized CD Pipeline With AWS and Cloudflare for 2024"
date: 2023-12-27
draft: true
---
Recently I went about standing up a fresh Continuous Delivery pipeline for a new project. The project is a relatively standard containerized stack with nothing exceptional to speak of, and as our exploratory work was already in AWS I decided to launch this CD in AWS CodePipeline. Furthermore, we wanted to dogfood our long-term infra management (this project is infra abstraction/automation software) and so opted _not_ to use to or CloudFormation templates - that way we could have a fully "Clickops'd" infrastructure for our tools to reclaim and manage. Besides, Clickops is easy right?

To my surprise, nothing worked. Deploying CD for a very standard stack (details to follow) via GUI clicks is a bizarre dance filled with broken states and never-resolvable circular dependencies, magic file/variable names that are either not documented or documented incorrectly (like the variety of spellings for `appspec.yaml / AppSpec.yml / appsec.yml` across AWS CodeDeploy docs), cryptic error codes, and incompatible default settings. Some of this is nothing new - all the clouds have quirks. But I was taken off guard by just how bad, how completely _non-functional_ I was suddenly finding these services which I had used happily for years. 

Maybe I have gotten too comfortable with infra as code, or maybe ECS and CodePipeline have gotten significantly more brittle in the last year. Maybe this is the multiverse where AWS services are much, much worse and I am a lost traveler. Whatever the reason, I decided that once this project was successfully deployed I would codify the process, in detail, as a guide for others (and my future self). This is that guide.

## How To Guide: 
We are setting up a blue/green deployment of a containerized application. The application uses docker-compose locally with one application container, one db container, a sidecar container (in our case logging, but can be anything) and an nginx container to serve web content. In AWS our stack will be:

- CodePipeline to manage our blue/green deployment via CodeBuild and CodeDeploy
- A single ECS service running on Fargate
- A single Elastic Load Balencer
- ECR for storing our container images
- SecretsManager for managing our environment variables
- Github as our source code provider
- CloudFlare for our DNS and proxy provider
There are numerous security groups, IAM roles etc needed in combination to make this all work, along with support elements like 
  


{{< box warning >}} 
**Do not skim this guide!** If you are like me, you normally skim over these things, copy the code examples, and refer back when you hit errors. **Don't do that.** The ClickOps process here is like a ritual dance, missing one tiny step will anger the AWS gods and _you will have to start over from the beginning._ Suck it up and read the whole thing, and follow exactly step by step, or pain will follow.
{{< /box >}}

### Legend
To minimize repetition I am going to use some shorthands:
- The :monocle_face: icon means **Copy exactly.** I know, AWS docs or a tutorial might claim you can change the filename or specify the path somewhere; my experience has been that not all the configs are respected, and often only the default paths/names actually work. If you choose to deviate, best of luck to you.
- The aws account number for the examples will be `123456789012`. You can find-replace with your account. 
- The project name will be `bash-dog`.  You can find-replace with your project name.
- The AWS region will be `us-east-2`. You can find-replace with your default region. 

### Steps
1. #### Start your magic files.
Our pipeline needs 3 files placed in the root directory of your project. 
The `taskdef.json` which should look 
2. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbODY5OTMwMDYyLDE1OTcyODc3ODMsMjAwNz
YwODg0MywtODUwMTkxMDE5XX0=
-->