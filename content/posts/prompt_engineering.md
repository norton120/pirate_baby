---
title: "Prompt Engineering"
subtitle: "some data science is black magic"
date: 2024-1-5
draft: true
---
The world never ceases to be filled with new things, and that is exciting. New things are great, but as they come with a learning curve - not the least of which is the language surrounding them. Like when the first coffee shop opened in the little town where I went to college in the late 90s, and we learned to order “express-o” (which was named that, logically, because it was like coffee but _faster_).  

Such is the case today with words like generative AI, large language models, and of course prompt engineering. These words get tossed into every plan and pitch deck with grand assumptions and promises of near-magic; the ratio of experience to conjecture is painfully low, and the noise from an army of pseudo-knowledgeable content creators looking to cash in on the AI gold isn't helping. 

Take the case of ChatGPT, the most widely recognised LLM on the market. Except... ChatGPT isn't an LLM.  ChatGPT (and the accompanying OpenAI API) is a brilliantly engineered software platform, representing billions of dollars of r&d, and hundreds of thousands (if not millions) of software development hours. ChatGPT is as much an LLM as Google search is a NoSQL database. Yes, one of the many, complicated parts of the ChatGPT platform is a set of proprietary Large Language Models. And yes, Google has databases. When you query the OpenAI API, you are interacting with a production endpoint and not a raw LLM. Getting this - the massive delta between an OSS `LLama2` or `Mistral` or `Falcon` model running on AWS Bedrock or GCP Vertex, and querying a polished, consumer-facing product, is tantamount to separating the generative AI wheat from the chaff.

Now on to Prompt Engineering. Not "how to phrase your question to get the best answer from ChatGPT," which I would honestly bucket under product training, but designing the model-level textual interaction templates. Here's a real-world example from earlier this week: the key players are myself (a Data Engineer living in a Data Science world), Woodson (our _actual_ Data Scientist), and a stock `Falcon-7b-instruct` instance.

_prompt_:
```
You are a helpful AI assistant.Assess if the question below is a complete thought that can be responded to without any external context. Respond only 'YES' or 'NO'.

>>QUESTION<< That is fine, just pick one.
>>ANSWER<<
```
_response_:
```
%YES,no\nI agree it is fine but th
```
K. No good. Try again with all the same settings for temperature, stop words etc.
_prompt_:
```
>>INTRODUCTION<<
You are a helpful AI assistant.if the question below is a complete thought that can be responded to without any external context respond YES, otherwise NO.

>>QUESTION<< 
That is fine, just pick one.
>>ANSWER<<
```
_response_:
```
)!
```
Umm.. that's.. worse? Maybe better, because it is shorter? OK again, maybe no special tokens this time, and raise the temperature. 
_prompt_:
```
If the message below is a complete thought that can be responded to without any external context respond YES, otherwise NO.

MESSAGE: That is fine, just pick one.
```
_response_:
```
YESyes
```
Closer, but also incorrect. 
This goes on for about an hour, adjusting the prompt and the settings. I finally get to this: 
```
Determine if this message is a complete statement that requires no external context, respond only with 'yes', otherwise respond only with 'no'.

MESSAGE: That is fine, just pick one.
```
_response_:
```
No
```
WOO! Now I run it 5 more times.
`No`, `Yes`, 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4ODk2MzU1OSwxMDk5OTY0NjA2XX0=
-->