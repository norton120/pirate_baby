---
title: "50 First Dates With MemGPT"
date: 2024-02-25
draft: true
---
## preamble
The drive home from the movie theater was not going well. My then-girlfriend sat in the passenger seat of my pickup, red glow of the traffic light excentuating her scowl. "You can't just let it be romantic, you have to ruin everything!" The movie was "50 First Dates", a classic Sandler and Barrymore romance about a woman who's brain injury prevents her from forming new long-term memories. In the movie, Lucy (Barrymore) builds her own "external memory" by keeping detailed journals each day. A clever plot device, sure, but I just couldn't live with the math (or let anyone else live with it). If her journal entries took 20 minutes a day to write (that is less than most people, and most people aren't trying to compensate for brain damage), each page would take roughly half that time - so 10 minutes - to read. That means reading a week's journals would take her an hour each day. A month of journals would take her nearly half the day (assuming she stopped to eat) to read. Within a few months, all she would have time to do is read about her past; by the 6 month mark, her daily reading would take more hours than are in a day. Romantic? Yes. Realistic? No. And so we argued, the complexity of her logic growing in lock-step with the rising emotions. 

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
eyJoaXN0b3J5IjpbLTIwNTMxNzU1NTcsLTIwMzM3MjcxNjUsLT
EzMjcyMzI3NjUsLTY1NzA2OTQzMSw5NDY2ODI4NzcsMTcwOTAx
MTU2MiwxMjE5MjUxNjQzLC0xOTQ3MTI1NDk4LDEyMjE0NTc3OT
gsLTI1NTU1MjUxNiwxODkxOTIwNDE1LDE0ODE5MTU3MTYsMTAy
NTk1NTcyOSwxMTU5NTM5OTgyLC0yNTg3MTQxNjMsOTgwNzg4Nz
QxLC0xNDMwNTE0ODEsNDc3MTc4ODAwXX0=
-->