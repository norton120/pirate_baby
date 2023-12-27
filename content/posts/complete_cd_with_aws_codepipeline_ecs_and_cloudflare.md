---
title: "A Complete Containerized CD Pipeline With AWS and Cloudflare for 2024"
date: 2023-12-27
draft: true
---
Recently I went about standing up a fresh Continuous Delivery pipeline for a new project. The project is a relatively standard containerized stack with nothing exceptional to speak of, and as our exploratory work was already in AWS I decided to launch this CD in AWS CodePipeline. Furthermore, we wanted to dogfood our long-term infra management (this project is infra abstraction/automation software) and so opted _not_ to use to or CloudFormation templates - that way we could have a fully "Clickops'd" infrastructure for our tools to reclaim and manage. Besides, Clickops is easy right?

To my surprise, nothing worked. Deploying CD for a very standard stack (details to follow) via GUI clicks is a bizarre dance filled with broken states and never-resolvable circular dependencies, magic file/variable names that are either not documented or documented incorrectly (like the variety of spellings for `appspec.yaml / AppSpec.yml / appsec.yml` across AWS CodeDeploy docs), cryptic error codes, and incompatible default settings. Some of this is nothing new - all the clouds have quirks. But I was taken off guard by just how bad, how completely _non-functional_ I was suddenly finding services which I had used comfort
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NTI5ODkyMjhdfQ==
-->