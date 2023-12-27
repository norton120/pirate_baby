---
title: "A Complete Containerized CD Pipeline With AWS and Cloudflare for 2024"
date: 2023-12-27
draft: true
---
Recently I went about standing up a fresh Continuous Delivery pipeline for a new project. The project is a relatively standard containerized stack with nothing exceptional to speak of, and as our exploratory work was already in AWS I decided to launch this CD in AWS CodePipeline. Furthermore, we wanted to dogfood our long-term infra management (this project is infra abstraction/automation software) and so opted _not_ to use to or CloudFormation templates - that way we could have a fully "Clickops'd" infrastructure for our tools to reclaim and manage. 
To my surprise, nothing worked. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTczMjIwMDMxOV19
-->