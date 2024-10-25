---
title: "Dreaming of a Dynamically Typed World"
date: 2024-10-23
tags: ['software', 'op-ed']
draft: true
---
In 1967 computer scientist Melvin Conway made an observation that came to be known as _Conway's Law_.
> Organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations.

Conway's Law is why you will often find rigid, silo'ed tables modeled into the data architecture of rigid companies with silo'ed business departments, or scrambled and obviously unplanned relationships across software entities at bootstrap startups; code reflects the human environment in which it develops.

Recently a post caught my attention, from a young developer noting the contridiction between Python type hints (and by extension _Pydantic_ as effectively strongly-typed Python) with the traditional _Pythonic_ mantra of duck typing. Sometimes it takes fresh eyes that are not aware of the historical context to call out a bad situation, and this is one of those times. Best practices are not defined in a specification, written in a vacuum by wise old neckbeards; these practices are the codified reflection of developer community behavior in the same way that _Webster's Dictionary_ reflects the evolition of English (and does not act to effect that evolution). If the best practices of Python typing are becoming increasingly contradictory, it mirrors the increasingly contridictory nature in which the software development community approaches designing Python software - and this got me thinking. 

What if Conway's Law can be extrapolated beyond the walls of the office? What if, just as the DNA of an organization determine the ultimate shape of that organization's applications, the human social architype held by humanity's software developers will decide the evolution of our programming languages? What if Python is changing in the same way that the people _writing_ Python are changing? 

Consider the appeal of dynamically typed languages and, by extension, the practice of duck typing, when Python 2.0 was released in the year 2000 <sup>1</sup>. 
To many proponents at the time dynamic typing was the flexible answer to the rigid structure and beurocracy of design found in statically typed languages. Your code no longer needed to declare _what_ something was, and was no longer bound to that identity - it could start life as a `str` and evolve to a `list` or a `dict` or maybe even a `ProtcolConstructorElement` - it didn't matter. Duck typing is the extension of that lack of identity; it is unimportant what a thing _is_, and only important what a thing _does_. If an object needs a method `convert_to_pdf` to get a job done, and it has that method, then the object is qualified to do the job. If not, then deal with the error of an unqualified object - or look for a different possible method `to_pdf` supported by other, also qualified objects. The point of duck typing in dynamic programming was to deal with the object's ability, not the object's identity. 
If you share your formative years with Python (child of the 1980s-1990s) you probably remember the phrase "be colorblind." This was the overwhelming message in education and popular culture at the time - that taking identity into consideration, even _seeing_ or _acknowledging_ that identity, was morally wrong; that an idividual must be judged soley by their words and, most importantly, actions, and nothing else. I can attest with at least anachdotal evidence of how that message shaped the way I view the world, by way of the most scientifically rigorous methods - recounting a casual conversation I had last week at a party. The conversation topic somehow landed on representation in media, and one of the younger partygoers was lecturing on how the late sitcom era of TV was particularly awful at only telling one (read: white) story, to which no one, myself included, disagreed. But when the conversation shifted to listing off the specific shows we watched religously as kids:
 
* Hanging with Mister Cooper
* Fresh Prince of Bel-Air
* Star Trek: Deep Space Nine
* Family Matters
* Different Strokes
* the Cosby Show

I remembered watching Fa
 
Is it all that surprising that the heyday of dynamcially typed OOP-forward languages like Python and Ruby coencided with societal pressure to "be colorblind" in our interactions with others? 

<sub>1. Python as a language has been around since the late 1980s, however Python 2+ is really where it begins to reflect what most would consider "modern Python" in a way that is applicable to the conversation</sub>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MTg4NTkzNjAsMjAxNjYxMjI1NCwyMD
E2NjEyMjU0LDU3NjY0Nzg5MCwtNjkzNjA3NjEwLDEwOTA1NTAy
MzhdfQ==
-->