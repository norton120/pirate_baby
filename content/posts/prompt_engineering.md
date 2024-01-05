---
title: "Prompt Engineering"
subtitle: "some data science is black magic"
date: 2024-1-5
draft: true
---
The world never ceases to be filled with new things, and that is exciting. New things are great, but as they come with a learning curve - not the least of which is the language surrounding them. Like when the first coffee shop opened in the little town where I went to college in the late 90s, and we learned to order “express-o” (which was named that, logically, because it was like coffee but _faster_).  

Such is the case today with words like generative AI, large language models, and of course prompt engineering. These words get tossed into every plan and pitch deck with grand assumptions and promises of near-magic; the ratio of experience to conjecture is painfully low, and the noise from an army of pseudo-knowledgeable content creators looking to cash in on the AI gold isn't helping. 

Take the case of ChatGPT, the most widely recognised LLM on the market. Except... ChatGPT isn't an LLM.  ChatGPT (and the accompanying OpenAI API) is a brilliantly engineered software platform, representing billions of dollars of r&d, and hundreds of thousands (if not millions) of software development hours. ChatGPT is as much an LLM as Google search is a NoSQL database. Yes, one of the many, complicated parts of the ChatGPT platform is a set of proprietary Large Language Models. And yes, Google has databases. When you query the OpenAI API, you are interacting with a production endpoint and not a raw LLM. Getting this - the massive delta between an OSS `LLama2` or `Mistral` or `Falcon` model running on AWS Bedrock or GCP Vertex, and querying a polished, consumer-facing product, is tantamount to separating the generative AI wheat from the chaff.

Now on 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTExMDY4MDYwNCwxMDk5OTY0NjA2XX0=
-->