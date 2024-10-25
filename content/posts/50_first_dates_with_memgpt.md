---
title: "50 First Dates With MemGPT"
date: 2024-02-25
tags: ['ai','ml']
draft: false
---
## preamble
The drive home from the movie theater was not going well. My then-girlfriend sat arms crossed in the passenger seat, the red glow from the traffic light matching her mood. "You can't just let it be romantic. Why do you have to ruin everything!?!" We had just seen _50 First Dates_, a classic Sandler/Barrymore romance about a woman who's brain injury prevents her from forming long-term memories. In the movie, Lucy (Barrymore) constructs her own "external memory" via her diary; a clever plot device, but one that required suspension of disbelief that I just could not abide. I had done shorthand math while the credits were rolling: If Lucy's average diary entry took 20 minutes to write (that is less than most people, and most people aren't trying to compensate for brain damage), each entry would take roughly half that time - so about 10 minutes - to read. Reading a week's entries would take more than an hour. By the 6 month mark, the daily catch-up on her past would require more hours of reading than are in a day. Romantic? Yes. Realistic? No. And so we argued.
I believe the conversation went something like this:

_"**Her**: But what if every Sunday she made wrote a cheat sheet for the past week, and then she only read those? That would take less time. "_
_"**Me**: Even a weekly summary would become unreadable in less than a year."_
_"**Her**: OK, then what if she summarized those cheat sheets?? She could keep making the history smaller and smaller."_
_"**Me**:  Yeah but eventually she'd lose too much detail and the summaries would be useless."_
_"**Her**: But she'd still have her daily journals for when she needs those details!"_
_"**Me**: How would she ever search that? We're back where we started."_

Twenty years later, the "Lucy problem" is a perfect lens to help us understand one of the most important challenges in designing a Large Language Model Agent Framework. The solution proposed by [researchers at UC Berkeley](https://research.memgpt.ai/) is remarkably innovative and offers exciting potential - and it is a solution that bears significant resemblance to the "Lucy solution" I was arguing against during that car ride home. It looks like I owe someone a long overdue apology.

## Lucy the language model: a near-perfect analogy
Large Language Models are, in reality, just functions. You input at least one argument (text) and they output in kind. This output is the product of the model's business logic, combined parameters, and internal arguments - one of those arguments being the training data used to develop the inference model. This training data serves as the model's "memories"; without it the LLM would output very little of value, similar to attempting a deep conversation with a newborn.
The training data "memories" in an large language model are fixed at inference time, exactly like Lucy's memories in the movie. She has developed experiences and gathered information up to a very specific point (in her case, the day of her accident); from that day forward, she interprets stimuli based on the exact state of her mind, her memories, at that time. This is _precisely_ how inference with a large language model operates - fixed to the moment the training was complete, and the resulting function was pickled.

Each time the LLM function is executed (here we will refer to this combined execution and response as a _turn_, borrowing from chat nomenclature) is exactly like one single day in the life of Lucy. With the model temperature turned down to 0 (deterministic) each turn with the same input will look exactly like Lucy's early routine - repeating the same day over and over (and baking a lot of identical birthday cakes). An LLM cannot form new "memories" as a pure inference endpoint, any more than Lucy can.

To compensate for this with an LLM, the natural next step is to prepend those new "memories" as part of the text passed to the LLM function effectively augmenting the training data of the language model for the duration of the turn<sup>1</sup>. However language model context windows - the combined amount of text that can be input and output in a single turn - are limited in size. Again, this is _exactly_ how Barrymore's character experiences the world; her context window is one single day. Just as I argued so many years earlier that Lucy's memories would eventually take longer to consume than there are hours in a day for her to retain them, new knowledge that must be included in a turn in order for the language model to produce a useful output quickly outgrows the available context window.

## The limits of prompt engineering
The lion's share of LLM Engineering coverage has been devoted to _prompt engineering_, or crafting the content we submit in a turn so that it produces the most desirable outcome. An entire ecosystem has rapidly developed around prompt design, from prompt engineering classes to prompt exchange marketplaces - all from the idea that from the "perfect prompt" you can coax the "perfect output."

Henry, Sandler's character in _50 First Dates_, may have been one of the earliest prompt engineers. Early in the film Henry falls in love with Lucy and agrees not to tell her about her injury, instead wooing her anew each day. His daily "prompts" to re-win her heart begin abysmally, with most ending in rejection. Over time his technique evolves until Lucy consistently falls for him every day. We see this same example in countless language model demos, where a meticulously crafted prompt is used to visualize analytics for a dataset, or generate a spot-on cover letter.

The examples are impressive, but how useful is this prompting really? In the movie, Henry finally addresses the extreme limitations in a life of infinite first dates, and tells Lucy about her condition. With a language model, a "perfect prompt" executed in isolation is just as limited in value. Complex tasks require many complex steps, each building on a modified state - and this cannot be accomplished in a single turn. While prompt engineering is certainly an important piece of the puzzle, it isn't remotely a holistic solution to our problem.

## RAG, a newspaper, and a video tape
For both Lucy and the language model, things get interesting once we start externalizing memories. Retrieval Augmented Generation (RAG) is probably a close second to prompt engineering in the sheer volume of attention paid in LLM-related content. RAG can be more simply stated as "store text somewhere, then on each turn search that text and add bits to the prompt." The most common RAG implementations today are blind semantic searches, where every user input is searched against the RAG store by semantic similarity, and then the top few search results are combined with the user input as the prompt. They look something like this:

```txt
# prompt with just user input
Question: What is the last thing Todd said before he quit yesterday?
```
vs
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
Later, Henry introduces the first attempt to be honest with Lucy in the form of a VHS recording. To the plot of the film this is a pivotal moment, as it is Lucy's first step towards regaining agency. With the language model, it is functionally the same as the newspaper and the paint; each turn is potentially better and more informed when it includes RAG content, but it is still very much an isolated turn without true external state management.

Regardless of which Lucy consumes - the fake newspaper or Henry's real VHS tape - improvement in Lucy's life is limited to the outcome of that day. Lucy still has no agency to live a full life, just as our language model can take no meaningful steps towards completing a complex task.

Just like prompt engineering, RAG is a piece of the puzzle, but it is not the answer in and of itself.

## A mind with a diary
Let's review that theory from the car. What if Lucy kept a diary, and then managed this "external memory" by summarizing, consolidating, and making herself cheat sheets? Unlike her father's newspapers or Henry's VHS tapes, this memory would be completely under her control. _She_ decides what information is critically important, what memories can be forgotten, and what knowledge should live on in "cold storage" to be dredged up only when required. The film touches on this idea (though it took my romance-ruining logic to really see it played out in detail). With an external memory like this, Lucy is now unbound from her context window. She can pursue her interests for as long as they take, participate actively in the mundane but important events of life, have a family, _live_. She can make a menu for the week on Monday, go shopping for groceries Wednesday, and cook them on Friday - all the elements of agency returned to her by a few notebooks and todo lists.

This is remarkably similar to the premise behind the [MemGPT](https://memgpt.ai/) project<sup>2</sup>. The context window, chat history, and RAG knowledge store are treated as tiered "memories"; each memory can be written and purged by the LLM using tool calls.
Instead of approaching each turn as an isolated prompt + RAG + input = response, the "core" memory (the context window content) is processed continually as a daemon, with a new turn on each "heartbeart." Just as each day Lucy is presented with her notes and todo list from the previous day, with each turn the language model is presented with the core memory assembled by the previous turn. During that turn the language model can edit this core memory, move information out of core and into archival memory, or search/recall from archival memory and add that back to core, and these changes will apply to the core memory presented in the next turn.

Here's a walk-through of how an agent could work (with a bit of pseudo-code) to answer a user's question about a company. The agent has a core memory describing itself and the user, a history section containing the last five messages, and a list of tools the agent can call. This core memory is passed as the prompt in a turn every 10 seconds, or sooner if externally triggered.
1. On the first pass the agent calls the `archive_lines()` tool to move the 2nd paragraph of the user information to cold storage. Why? because the system prompt informs the agent of the current and max memory sizes, and instructs the agent to self-adjust when needed.
2. On the next pass, the tool call request and result are the newest entries in the core memory history (the 2 oldest from the last turn have been moved to recall memory and are not visible). This turn the agent calls `pause_heartbeats()` to wait for external stimuli, as it detects nothing else to update in it's own core memory.
3. The next turn is triggered by a user message, which is the newest history entry in this turn's core memory. The user message says "how many people are in the Seattle office?" and the agent's first action is to call the `get_employee_list()` tool, along with the internal monologue message "I must get the list of employees and count only the ones in the Seattle office. I must then send the message back to the user" .
4. On the next turn, the agent tool call, internal monologue, and tool call result are in the core memory history, but the original user message has been pushed out. On this turn the agent's internal monologue is "65 employees are in the Seattle office. I must retrieve the original question so I can answer it correctly" and the tool call is `retrieve_message(user, -1)` to get the last message from the user.
5. On the next turn, the agent calls `send_message("there are 65 employees in the Seattle office")`, and responds to the user.

And the beat goes on.

This "language model operating system" is a starkly contrasting view of how inference services could function to complete complex, multifaceted tasks. It also changes the paradigm of "evolution" as an agent, allowing the application to adjust and self-correct. Prompts and RAG become correctable elements within a generative "cycle"; if a RAG search is ineffective or prompt misses the mark, it can be re-tried or compensated for on the next turn. Most distinctly important from single-turn agent design, the results of this self-managed memory are cumulative. This is an absolute necessity for true agency.

I am very excited about what a framework built on this concept could mean; adding stimuli to a well-appointed agent (or cluster of agents) becomes an execution layer that evolves beyond text generation and an ROI that grows exponentially with the complexity of its' charge. A language model operating in this fashion is still a language model - a function, not a sentient being - but it crosses a threshold of appearance that is the stuff of Sci-Fi. More importantly, it adds a critical element to the generative equation that I just don't see autonomous agency succeeding without: repetition. Humans don't immediately think every required thought and blurt out the perfect response in one breath; we take steps, ask questions that uncover new questions, pause to consider internally, and _arrive_ at an answer. By bestowing that same capacity on an application, this language model operating system could be a new paradigm in computing.

For those of us building user-facing agents, this is a concept worth focus and cycles. Single-turn prompt libraries and slice-and-dice embedding building to RAG away bad responses was the best idea we had in the dark AI days of 6 months ago, but I don't think they will get us where we want to go. In _50 First Dates_ Lucy married Henry, became a mom, and sailed to Alaska, all because she was restored the agency to own her mind and manage her memories. Language model agents need the same in an "operating system" if we want to unlock them.

Join me next time, when we explore the parallels between Happy Gilmore and K8S (hint: there are none).



**Footnotes:**
<sub>1. Adding context to a prompt and fine-tuning or retraining a model are not really the same thing, but I was willing to take a few liberties with technical accuracy for the sake of clearly demonstrating the subject concepts.</sub>

<sub>2. Note that throughout this writing I am referring to the concepts introduced by the research behind MemGPT, not the implementation itself. The nomenclature, pseudo-code, and description of events here are not intended to reflect the software project.</sub>

**MemGPT Citation:**
<sub>
packer 2023 memgpt, MemGPT: Towards LLMs as Operating Systems,
authors: Packer, Charles and Wooders, Sarah and Lin, Kevin and Fang, Vivian and Patil, Shishir G. and Stoica, Ion and Gonzalez, Joseph E.,
arXiv preprint arXiv:2310.08560</sub>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0ODI3MTkyOSwtMTU4NDExMzA2MywtND
E0Nzg3OTc5LDM1ODEzNzk0NSwtMjEzMDY4NzU1OSwtMTUzMDg1
MzY2NCw2NzkyNjYzOTAsODUyODU4NDgsLTE4NzcwNjM3OTEsMj
E3MjY1MCwtMjA1MzE3NTU1NywtMjAzMzcyNzE2NSwtMTMyNzIz
Mjc2NSwtNjU3MDY5NDMxLDk0NjY4Mjg3NywxNzA5MDExNTYyLD
EyMTkyNTE2NDMsLTE5NDcxMjU0OTgsMTIyMTQ1Nzc5OCwtMjU1
NTUyNTE2XX0=
-->