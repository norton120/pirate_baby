---
title: "50 First Dates With MemGPT"
date: 2024-02-25
draft: true
---
## preamble
The drive home from the movie theater was not going well. My then-girlfriend sat arms crossed in the passenger seat, the red glow from the traffic light matching her mood. "You can't just let it be romantic. Why do you have to ruin everything!?!" We had just seen _50 First Dates_, a classic Sandler/Barrymore romance about a woman who's brain injury prevents her from forming long-term memories. In the movie, Lucy (Barrymore) constructs her own "external memory" via her diary; a clever plot device, but one that required suspension of disbelief that I just could not abide. I had done shorthand math while the credits were rolling: If Lucy's average diary entry took 20 minutes to write (that is less than most people, and most people aren't trying to compensate for brain damage), each entry would take roughly half that time - so about 10 minutes - to read. Reading a week's entries would take more than an hour to read. By the 6 month mark, her daily catch-up reading about her past would require more hours than are in a day. Romantic? Yes. Realistic? No. And so we argued. I believe the conversation went something like this: 
_"But what if every Sunday she made wrote a cheat sheet for the past week, and then she only read those? That would take less time. " 
"Even a weekly summary would become unreadable in less than a year." 
"OK, then what if she summarized those cheat sheets?? She could keep making the history smaller and smaller." 
"Yeah but eventually she'd loose too much detail and the summaries would be useless. "
"But she'd still have her daily journals for when she needs those details!" 
"How would she ever search that? We're back where we started."_

Twenty years later, the "Lucy problem" is a perfect lens to help us understand one of the most important challenges in designing a Large Language Model Agent Framework. The solution proposed by [researchers at UC Berkeley](https://research.memgpt.ai/) is remarkably innovative and offers exciting potential - and it is a solution that bears significant resemblance to the one I was arguing against during that car ride home. It looks like I owe someone an apology.

## Lucy the language model: a near-perfect analogy
Large Language Models are, in reality, just functions. You input at least one argument (text) and they output in kind. This output is the product of the model's business logic, combined parameters, and internal arguments - one of those arguments being the training data used to develop the inference model. This training data serves as the model's "memories"; without it the LLM would output very little of value, similar to a holding a deep conversation with a newborn. 
The training data "memories" in an large language model are fixed at inference time, exactly like Lucy's memories in the movie. She has developed experiences and gathered information up to a very specific point (in her case, the day of her accident); from that day forward, she interprets stimuli based on the exact state of her mind, her memories, at that time. This is _precisely_ how inference with a large language model operates - fixed to the moment the training was complete, and the resulting function was pickled. 

Each time the LLM function is executed (here we will refer to this combined execution and response as a _turn_, borrowing from chat nomenclature) is exactly like one single day in the life of Lucy. With the model temperature turned down to 0 (deterministic) each turn with the same input will look exactly like Lucy's early routine - repeating the same day over and over (and baking a lot of identical birthday cakes). An LLM cannot form new "memories" as a pure inference endpoint, any more than Lucy can. 

The natural next strategy is to prepend those new "memories" as part of the text passed to the LLM function, effectively augmenting the training data of the language model for the duration of the turn*. However language model context windows - the combined amount of text that can be input and output in a single turn - are limited in size. Again, this is _exactly_ how Barrymore's character experiences the world; her context window is one single day. Just as I argued so many years earlier that Lucy's memories would eventually take longer to consume than there are hours in a day for her to retain them, new knowledge that must be included in a turn in order for the language model to produce a useful output quickly outgrows the available context window. 

## The limits of prompt engineering
The lion's share of language model Engineering coverage has been devoted to _prompt engineering_, or crafting the content we submit in a turn so that it produces the most desirable outcome. Prompt engineering is an important part of t


<sub>*Adding context to a prompt and fine-tuning or retraining a model are not really the same thing, but I was willing to take a few liberties with technical accuracy for the sake of clearly demonstrating the subject concepts.</sub> 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyNDM2NTQ0OSw2NzkyNjYzOTAsODUyOD
U4NDgsLTE4NzcwNjM3OTEsMjE3MjY1MCwtMjA1MzE3NTU1Nywt
MjAzMzcyNzE2NSwtMTMyNzIzMjc2NSwtNjU3MDY5NDMxLDk0Nj
Y4Mjg3NywxNzA5MDExNTYyLDEyMTkyNTE2NDMsLTE5NDcxMjU0
OTgsMTIyMTQ1Nzc5OCwtMjU1NTUyNTE2LDE4OTE5MjA0MTUsMT
Q4MTkxNTcxNiwxMDI1OTU1NzI5LDExNTk1Mzk5ODIsLTI1ODcx
NDE2M119
-->