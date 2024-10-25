---
title: "Dreaming of a Dynamically Typed World"
date: 2024-10-23
tags: ['software', 'op-ed']
draft: true
---
In 1967 computer scientist Melvin Conway made an observation that came to be known as _Conway's Law_.
> Organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations.

Conway's Law is why you will often find rigid, silo'ed tables modeled into the data architecture of rigid companies with silo'ed business departments, or scrambled and obviously unplanned relationships across software entities at bootstrap startups; code reflects the human environment in which it develops.

Recently a post by a young developer caught my attention; this developer noted (rather snarkingly) the contridiction between Python type hints and, by extension, _Pydantic_ Python as an effectively strongly-typed version of the language, with the traditional _Pythonic_ mantra of duck typing. The frustration was warranted, and sometimes it takes fresh eyes that are not aware of the historical context to call out a bad situation. Best practices are not written in a vacuum by wise old neckbeards and then chistled in a specification for all to obey; these practices are codified reflections of developer community behavior, in much the same way that _Webster's Dictionary_ reflects the evolition of English (and is not the root cause of that evolution). If the best practices of Python typing are becoming increasingly contradictory, it mirrors the increasingly contridictory nature in which the software development community approaches designing Python software - and this got me thinking. 

What if Conway's Law extrapolates beyond the walls of the office? What if, just as the DNA of an organization determines the ultimate shape of that organization's applications, the social architype held by humanity's software developers determines the evolution of our programming languages? What if Python is changing in the same way that the people _writing_ Python are changing? 

Consider the appeal of dynamically typed languages and, by extension, the practice of duck typing, when Python 2.0 was released in the year 2000 <sup>1</sup>. 
To the many proponents at the time, dynamic typing was the flexible answer to the rigid structure and beurocracy of design found in statically typed languages. Your code no longer needed to declare _what_ something was and be bound to that identity - it could start life as a `str` and evolve to a `list` or a `dict` or maybe even a `ProtcolConstructorElement` - it didn't matter. Duck typing extends that lack of identity; it is unimportant what the thing _is_, and only important what the thing _does_. If an object needs a method `convert_to_pdf` to get a job done, and it has that method, then the object is qualified to do the job. If not, then the software must deal with the error of an unqualified object - or look for a different possible method such as the `to_pdf` supported by other, also qualified objects. The point of duck typing in dynamic programming was to deal with the object's ability, not the object's identity - if it quacked, treat it like a duck. 

If you share formative years with Python (a child of the 1980s-90s) you probably remember the phrase "be colorblind." This was the overwhelming message in education and popular culture at the time, a message that taking an individual's external identity into consideration, even _seeing_ or _acknowledging_ that identity, was morally wrong; that an idividual must be judged soley by their words and, most importantly, actions, and by nothing else. I can attest with at least anachdotal evidence of how that message shaped the way I view the world, by way of the most scientifically rigorous of methods - recounting a casual conversation I had last week at a party. The conversation topic circled around representation in media, as one of the younger partygoers was postulating that the tail end of the TV sitcom era was particularly awful at only telling one story - the white one. No one, myself included, gave protest. But then the conversation shifted to reminiscing about some of the shows we watched religously as kids, and among my list:
 
* [Hanging with Mister Cooper](https://www.imdb.com/title/tt0103435/)
* [Fresh Prince of Bel-Air](https://www.imdb.com/title/tt0098800/)
* [Star Trek: Deep Space Nine](https://www.imdb.com/title/tt0106145/)
* [Family Matters](https://www.imdb.com/title/tt0096579/)
* [Different Strokes](https://www.imdb.com/title/tt0077003/) (syndicated)
* [the Cosby Show](https://www.imdb.com/title/tt0086687/) 

I remembered watching _Family Matters_ instead of _Full House_ because Carl Winslow was much cooler than Danny Tanner. I remembered that Mister Cooper was a relatable mentor, while the next door neighbor in _Boy Meets World_ was creepy. But earlier in the conversation it hadn't occured to me how much of my TV family was black. My mind hadn't registered what they _were_, in part because that thinking was decidedly out of fashion at the time those memories were formed. Is the way I remembered those characters - by their actions and interfaces - really all that different from cringing any time I see `if isinstance(x, y):`  in a Python codebase? The heyday of dynamcially typed OOP languages like Python and Ruby coencided with societal pressure to "be colorblind" in a way that is hard to ignore.

Then consider the era that gave rise to TypeScript and Pydantic - the 2010s. After a decade of dynamically typed code, many developers were tired of "magic soup" - applications filled with cryptic round-about logic and side effects that were impossible to debug, and class names that looked like the author was in training for BBC Countdown. These developers craved the structure, order, and simplicity of pattern matching, and with that came the return of typing and functional programming. 

Both TypeScript and Pydantic-based Python start every method with a single question: "what are you?" The identity of the object is the base for all proceeding business logic. It does not matter if the calling function invokes an `update()` method which the object is able to fulfill, if the type does not match the call will never execute. This confirmation of type occurs at every functional exchange in TypeScript and as much of the typed Python codebase as inherits from `Pydantic.BaseModel`, effectively starting every transaction and sub-transaction with a declaration of identity. "As a `ProductUpdateRequest` object, I have an `update()` method I can execute for you." 
Around this same time, we saw the emergence of identity-forward thinking in academic circles, politics and business, and a growing importance placed on identity that has carried into today. I think it is safe to assume that anyone reading this will have been around in the last ten or so years, and as such I will leave you to draw your own parallels between the software and the burgeoning social norms reguarding identity - you don't need my party stories for that.

 This observation is not an indictment of either the static or dynamic typing language paradigms, both have strengths and weaknesses. For example, how many times have you written this little gem in duck-typed Python and felt dirty after? 
```python
 def standardize_args(arg:Iterable):
     """make arg safe to iterate on"""
     if isinstance(arg, str):
         return [arg]
     return arg
```

 “Accept either a string or a list of strings” is one of those times that duck typing just sucks. The most straightforward way to get this done is to pattern match object identity, because both a `str` and any other iterable will qualify for iteration- they can both “do the job” but the string will do it incorrectly, and you won’t know until it is too late. 

Rigid typing, however, can create the potential for a serious coupling issue. Consider this adapter interface: 
```python
class Interface(BaseModel):
    adapter: XAdapter
```
 For each new adapter you want to support, you will need to update your typing. If the adapter evolves and now has variations or child classes, you need to update your typing. If you want to support other interfaces as adapters (assuming they already implement the needed signatures)… you guessed it, typing needs to change. Keep in mind that none of the _code_ ever changes in these examples, but the typing must be continuously updated. 
```python
class Interface(BaseModel):
	 adapter: Union[XAdapter, Type[YAdapter], ZAdapter, LocalInterface, Type[ExternalInterface] # this goes on, and on, and on...
```
Coupling like this begets more coupling, as a whitelist of types is just too tempting for a junior developer to resist. Why build agnostic interfaces when you can peek under the hood of specific adapters and hard-wire depenencies to their internals? This is a crack through which the spaghetti sneaks in. 

The solution might be a future where we explicitly type either statically, _or_ dynamically, based on which is the best tool for the job. Pydantic already supports a form of duck typing with generic type classes `Iterable`, `Callable`, `Awaitable`, `Hashable`;  these types care not what a thing _is_, only what it _does_ (sound familar?). Using `typing.Any` in Pydantic Python feels as code-smelly as duck typing with `isinstance()` -  but what if correcting that feeling is as simple as aliasing `Any` with `DuckType` ?
```python
from typing import Any as DuckType
from pydantic import BaseModel

class Interface(BaseModel):
name: str
description: str
adapter: DuckType # I intend to duck type this!

def send_message(self, message:str): 
    prepped_message = self.some_cool_pre_process(message)
    try: 
	    self.adapter.send_message(prepped_message) 
    except AttributeError as e:
        raise ValueError("adapter must implement 'send_message', not implemented in adapter %s", self.adapter) from e
```
`DuckTytpe` tells our PR reviewers (and future Us) to expect the duck typing, and call it out if that logic is missing. Maybe even in a way that the next wave of smarter linters can detect and declare "Where's the duck!?!"
I lean pretty heavily towards Pydantic Python these days (and typed cou

As for the sociology part, I am no expert in humanity. I am sure that my bias towards colorblind thinking is hardcoded from youth in a way that makes it hard (if not impossible) for me to see the moral appeal of identity typing, and I'll leave it at that. But back to my purpose in this exploration - noting the simlilarity in the way we _think_ and the way we _program_ - it is hard to deny that the similarity is, at the very least, and interesting one. 




<sub>1. Python as a language has been around since the late 1980s, however Python 2+ is really where it begins to reflect what most would consider "modern Python" in a way that is applicable to the conversation</sub>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MDY4NjgzNDQsNjI3OTQ5NjM2LDU5Nz
E4NzQxMiwtMTc2NDc1NDMwMiwxOTE3MzY0Mjc0LC03NDU5OTcz
ODYsLTY0NjU3MDQ4MywxOTExMTU4OTM3LC00NzE5ODU2NDMsND
M3MzQzMDYxLC0zOTk3MjQ0MzMsLTExNTY4NzQwNzAsLTEzNDg4
ODUyMDQsLTIxNzU2NzY1NCwxNzMyOTcwMDU0LDIwMTY2MTIyNT
QsMjAxNjYxMjI1NCw1NzY2NDc4OTAsLTY5MzYwNzYxMCwxMDkw
NTUwMjM4XX0=
-->