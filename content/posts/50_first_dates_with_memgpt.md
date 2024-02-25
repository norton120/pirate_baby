---
title: "50 First Dates With MemGPT"
date: 2024-02-25
draft: true
---
## preamble
The drive home from the movie theater was not going well. My then-girlfriend sat arms crossed in the passenger seat, the red glow from the traffic light matching her mood. "You can't just let it be romantic. Why do you have to ruin everything!?!" We had just seen _50 First Dates_, a classic Sandler/Barrymore romance about a woman who's brain injury prevents her from forming long-term memories. In the movie, Lucy (Barrymore) constructs her own "external memory" via her diary; a clever plot device, but one that required suspension of disbelief that I just could not abide. I had done shorthand math while the credits were rolling: If Lucy's average diary entry took 20 minutes to write (that is less than most people, and most people aren't trying to compensate for brain damage), each entry would take roughly half that time - so about 10 minutes - to read. Reading a week's entries would take more than an hour. A month of journals would take her nearly half the day (assuming she stopped to eat) to read. Within a few months, all she would have time to do is read about her past; by the 6 month mark, her daily reading would take more hours than are in a day. Romantic? Yes. Realistic? No. And so we argued, the complexity of her logic growing in lock-step with the rising emotions. 

_"But what if she summarized every week and just read the summaries?" 
"Even a weekly summary would become unreadable in less than a year." 
"Then she summarized those? She could keep making the history smaller and smaller, that's kind of how memories work!" 
"At some point she'd loose too much detail - memory gets vague, but we can still recall super specific details when they matter."
"Well then she could go back to the daily notebooks when she needs those details!" 
"She wouldn't be able to go anywhere. She'd be chained to a room full of notebooks in order to function!"_

The rest of the ride was very quiet. 

I couldn't have imagined that 20 years later I would find myself faced with the  same problem as the fictional Henry while building an artificial intelligence agent, or that the most interesting solution to the problem - and maybe the most revolutionary - resembles most the solution I had been arguing against that night. 

Jenni if you're reading this, sorry about that. 

## a near-perfect analogy
Large Language Models are, in reality, just functions. You input at least one argument (text) and they output in kind. The output is a product of the model - more specifically, of the "memories" or training data that the model has been assembled with. Without this training data, the LLM would output very little of value - similar to a conversation with a newborn. 
But the training data "memories" of the model are fixed at inference time - exactly like Lucy in the movie. She has developed experiences and gathered information to a very specific point (in her case, the day of her accident) and she will forever process what shes, hears and learns with a "model" fixed to that day. This is _exactly_ how our LLM function operates - fixed to the moment it was pickled. 

So our next 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTMyNjkxMjA5LC0yMDUzMTc1NTU3LC0yMD
MzNzI3MTY1LC0xMzI3MjMyNzY1LC02NTcwNjk0MzEsOTQ2Njgy
ODc3LDE3MDkwMTE1NjIsMTIxOTI1MTY0MywtMTk0NzEyNTQ5OC
wxMjIxNDU3Nzk4LC0yNTU1NTI1MTYsMTg5MTkyMDQxNSwxNDgx
OTE1NzE2LDEwMjU5NTU3MjksMTE1OTUzOTk4MiwtMjU4NzE0MT
YzLDk4MDc4ODc0MSwtMTQzMDUxNDgxLDQ3NzE3ODgwMF19
-->