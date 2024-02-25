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
The lion's share of LLM Engineering coverage has been devoted to _prompt engineering_, or crafting the content we submit in a turn so that it produces the most desirable outcome. An entire ecosystem has rapidly developed around prompt design, from prompt engineering classes to prompt exchange marketplaces - all from the idea that with the "perfect prompt" you can coax the "perfect output" a language model. 

Henry, Sandler's character in _50 First Dates_, may have been one of the earliest prompt engineers. Early in the film Henry falls in love with Lucy and agrees not to tell her about her injury, instead wooing her anew each day. His daily "prompts" to re-win her heart begin abysmally, with most ending in rejection. Over time, his technique evolves until Lucy falls for him day after day. We see this same example in countless language model demos, where a meticulously crafted prompt is used to visualize analytics for a dataset or generate a spot-on cover letter. 

But how useful is this prompting, really? In the movie, Henry finally addresses the extreme limitations in a life of infinite first dates, and tells Lucy about her condition. With a language model, a "perfect prompt" executed in isolation is just as limited in value. Complex tasks require many complex steps, each building on a modified state - and this cannot be accomplished in a single turn. While prompt engineering is certainly an important piece of the puzzle, it doesn't remotely solve our problem alone.

## RAG, a newspaper, and a video tape
For both Lucy and the language model, things get interesting once we start externalizing memories. Retrieval Augmented Generation (RAG) is probably a close second to prompt engineering in the sheer volume of attention paid. RAG can be more simply stated as "store text somewhere, then on each turn search that text and add bits to the prompt." The most common RAG implementations today are blind semantic searches, where every user input is searched against the RAG store by semantic similarity, and then the top few search results are combined with the user input as the prompt. They look something like this:

```txt
# prompt with just user input
Question: What is the last thing Todd said before he quit yesterday?
```
```txt
# prompt with vector similarity search results for "What is the last thing Todd said before he quit yesterday?" via embeddings, prepended to prompt
Context:
"Margo: Todd is quitting today!"
"Todd: I am quitting today. I've had enough."
"Clark: I can't believe Todd finally quit, Margo is going to freak."

Question: What is the last thing Todd said before he quit yesterday?
```
The context injected by RAG might be very helpful, or it might be virtually irrelevant. What's more, the question may not require the context at all, and the RAG may just be noise.  

Again _50 First Dates_ does not disappoint with real-world analogs. In the film, Lucy's condition is kept hidden from her with the help of falsified context clues; her father swaps out her newspaper with a reprinted one, passes off a recorded football game as live TV, and paints over a wall every evening so she can re-paint it the next day, none the wiser. This context adds to the prompt and allows Lucy to live a full day (albeit the same one over and over). It does a significantly better job of reaching the desired outcome (Lucy enjoys her day and is able to function within it) than relying completely on the day's organic events. 
Later, Henry introduces the first attempt to be honest with Lucy in the form of a VHS recording. To the plot of the film this is a pivotal moment, as it is Lucy's first step towards regaining agency. With the language model, it is functionally the same as the newspaper and the paint; each turn is potentially better and more informed when it includes RAG content 

But even though Lucy's day is improved through augmentation, she is still not able to enjoy a full and complex life. Her day still resets 

<sub>*Adding context to a prompt and fine-tuning or retraining a model are not really the same thing, but I was willing to take a few liberties with technical accuracy for the sake of clearly demonstrating the subject concepts.</sub> 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA1NTEzNDUyMSwtMjEzMDY4NzU1OSwtMT
UzMDg1MzY2NCw2NzkyNjYzOTAsODUyODU4NDgsLTE4NzcwNjM3
OTEsMjE3MjY1MCwtMjA1MzE3NTU1NywtMjAzMzcyNzE2NSwtMT
MyNzIzMjc2NSwtNjU3MDY5NDMxLDk0NjY4Mjg3NywxNzA5MDEx
NTYyLDEyMTkyNTE2NDMsLTE5NDcxMjU0OTgsMTIyMTQ1Nzc5OC
wtMjU1NTUyNTE2LDE4OTE5MjA0MTUsMTQ4MTkxNTcxNiwxMDI1
OTU1NzI5XX0=
-->