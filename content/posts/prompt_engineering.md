---
title: "Prompt Engineering"
subtitle: "some data science is black magic"
date: 2024-1-5
draft: true
---
The world never ceases to be filled with new things, and that is exciting. New things are great, but as they come with a learning curve - not the least of which is the language surrounding them. Like when the first coffee shop opened in the little town where I went to college in the late 90s, and we learned to order “express-o” (which was named that, logically, because it was like coffee but _faster_).  

Such is the case today with words like generative AI, large language models, and of course prompt engineering. These words get tossed into every plan and pitch deck with grand assumptions and promises of near-magic; the ratio of experience to conjecture is painfully low, and the noise from an army of pseudo-knowledgeable content creators looking to cash in on the AI gold isn't helping. 

![Prompt Engineering](https://i.kym-cdn.com/entries/icons/original/000/010/692/You_Keep_Using_That_Word_meme_banner.jpg)

Take the case of ChatGPT, the most widely recognised LLM on the market. Except... ChatGPT isn't an LLM. ChatGPT (and the accompanying OpenAI API) is a brilliantly engineered software platform, representing billions of dollars of R&D, and hundreds of thousands (if not millions) of software development hours. ChatGPT is as much an LLM as Google Search is a NoSQL database. Yes, one of the many complicated parts of the ChatGPT platform is a set of proprietary Large Language Models, just as Google Search has databases of a sort. When you query the OpenAI API, you are interacting with a production consumer-facing endpoint, not a raw LLM. Understanding this - the massive delta between an OSS `LLama2` or `Mistral` or `Falcon` model running on AWS Bedrock or GCP Vertex, and querying a polished, consumer-facing product, is tantamount to separating the generative AI wheat from the chaff.

Now on to Prompt Engineering. Not "how to phrase your question to get the best answer from ChatGPT," which I wish everyone would start calling what it is, _product training_, but designing model-level textual interaction templates. Here's a real-world example from earlier this week: the key players are myself (a Data Engineer living in a Data Science world), Woodson (our _actual_ Data Scientist), and a stock `Falcon-7b-instruct` instance. I started early in the morning, trying to fix a stubborn link in our prompt chain:

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
**lk)!
```
Umm.. that's.. worse? Maybe better, because it is shorter? OK again, maybe no special tokens this time, and raise the temperature. 
_prompt_:
```
If the message below is a complete thought that can be responded to without any external context respond YES, otherwise NO.

MESSAGE: That is fine, just pick one.
```
_response_:
```
YESyes<backpage
```
Closer, but also incorrect, and still not stopping where I want it. 
This goes on for about an hour, adjusting the prompt and the settings. I finally get to this: 
```
Determine if this message is a complete statement that requires no external context, respond only with 'yes', otherwise respond only with 'no'.

MESSAGE: That is fine, just pick one.
```
_response_:
```
No
```
WOO! Now I run it 5 more times in a row.
`No`, `Yes`, `YES`, `YesNo`, `Yes`

At this point I start thinking about re-entering a career in the food service industry.

Just then Woodson walks into the office. He looks over my head (which is rested firmly forehead-planted on the desk, my fist b ) at the prompt terminal on the massive computer screen in front of me.
"Where's the temp? OK drop that to point one. Invert the question to ask if the message requires external context, add a second sentence with yes or no, lowercase, get rid of that period, and ...(pauses to slurp iced tea)... make the word message lowercase, get rid of the space in front of the colon. Try it now."

_prompt_
```
Does this message require external context for you to respond? Answer yes or no

message:That is fine, just pick one.
```
_responses (x5)_
`Yes`, `Yes`, `Yes`, `Yes`, `Yes` (this is correct, remember we inverted it)

"How did you do that?!?"
"Wish I could tell you man. I just did."
He went on to talk about how I need to think about narrowing the conversational focus, sounding more like Maharishi Mahesh Yogi explaining the mechanics of transcendental meditation than a Software Engineer talking compiler bugs.

This is a new sport. This kind of practice requires a different kind of thinking, and I am not entirely convinced it can be effectively translated through teaching. Maybe it will be like music; most of us can take tuba lessons and be part of the middle school band, but few will ever be good enough to play music professionally at _any_ level - not just the proverbial (and in this case, actual) rock stars, but even so much as to cover the bills of a modest lifestyle. To be able to craft text that effectively coaxes gold from language model mire is, at the moment, a bit of an art form. 
There are likely people all over the globe that have never considered an interest in programming or computer science, but are naturally exceptionally gifted at this new dark art. There are people working a New Jersey gas pump, or pulling lobster pots from a bay in Maine, or entering medical claims in an office in Tulsa, that would look at the same block of text and say "yeah just invert the question, and that word needs to be lower case" like it was placing the last piece in a jigsaw puzzle. Wilt Chamberlain was a bellhop when the world of professional basketball first discovered him. 
I guess it is all relative; to some developers, SQL is database incantation, or JavaScript is a world of broken promises (pun intended). I personally believe that wood framing, electrical work, and plumbing are logical skills that can be learned, shared, and practiced, whereas any task involving drywall or spackle requires a pact with the devil to produce a half-way decent looking outcome. 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzE3NjMyMDU1LDYxNDEwNzUwNSw1OTMyOD
E1NTgsMTA5OTk2NDYwNl19
-->