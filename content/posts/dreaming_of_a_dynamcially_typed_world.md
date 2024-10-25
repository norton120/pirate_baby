---
title: "Dreaming of a Dynamically Typed World"
date: 2024-10-23
tags: ['software', 'op-ed']
draft: true
---
In 1967 computer scientist Melvin Conway made an observation that came to be known as _Conway's Law_.
> Organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations.

Conway's Law is why you will often find rigid, silo'ed tables modeled into the data architecture of rigid companies with silo'ed business departments, or scrambled and obviously unplanned relationships across software entities at bootstrap startups; code reflects the human environment in which it develops.

Recently a post by a young developer caught my attention; they noted the contridiction between Python type hints (and by extension _Pydantic_ as effectively strongly-typed Python) with the traditional _Pythonic_ mantra of duck typing. Sometimes it takes fresh eyes that are not aware of the historical context to call out a bad situation, and this is one of those times. Best practices are not defined in a specification, written in a vacuum by wise old neckbeards; these practices are the codified reflection of dev community behavior in the same way that _Webster's Dictionary_ reflects the evolition of English (and is not the root cause of that evolution). If the best practices of Python typing are becoming increasingly contradictory, it mirrors the increasingly contridictory nature in which the software development community approaches designing Python software - and this got me thinking. 

What if Conway's Law extrapolates beyond the walls of the office? What if, just as the DNA of an organization determines the ultimate shape of that organization's applications, the human social architype held by humanity's software developers determines the evolution of our programming languages? What if Python is changing in the same way that the people _writing_ Python are changing? 

Consider the appeal of dynamically typed languages and, by extension, the practice of duck typing, when Python 2.0 was released in the year 2000 <sup>1</sup>. 
To the many proponents at the time, dynamic typing was the flexible answer to the rigid structure and beurocracy of design found in statically typed languages. Your code no longer needed to declare _what_ something was and be bound to that identity - it could start life as a `str` and evolve to a `list` or a `dict` or maybe even a `ProtcolConstructorElement` - it didn't matter. Duck typing extends that lack of identity; it is unimportant what the thing _is_, and only important what the thing _does_. If an object needs a method `convert_to_pdf` to get a job done, and it has that method, then the object is qualified to do the job. If not, then the software must deal with the error of an unqualified object - or look for a different possible method such as the `to_pdf` supported by other, also qualified objects. The point of duck typing in dynamic programming was to deal with the object's ability, not the object's identity - if it quacked, treat it like a duck. 
If you share formative years with Python (child of the 1980s-1990s) you probably remember the phrase "be colorblind." This was the overwhelming message in education and popular culture at the time - that taking identity into consideration, even _seeing_ or _acknowledging_ that identity, was morally wrong; that an idividual must be judged soley by their words and, most importantly, actions, and nothing else. I can attest with at least anachdotal evidence of how that message shaped the way I view the world, by way of the most scientifically rigorous of methods - recounting a casual conversation I had last week at a party. The conversation topic circled around representation in media, as one of the younger partygoers was postulating that the late sitcom era of TV was particularly awful at only telling one story - the white one. No one, myself included, gave protest. But when the conversation shifted to reminiscing about some of the shows we watched religously as kids:
 
* Hanging with Mister Cooper
* Fresh Prince of Bel-Air
* Star Trek: Deep Space Nine
* Family Matters
* Different Strokes
* the Cosby Show 

I remembered watching _Family Matters_ instead of _Full House_ because Carl Winslow was much cooler than Danny Tanner. I remembered that Mister Cooper was a less creepy mentor than the next door neighbor in _Boy Meets World_. But I didn't remember that a lot of my TV family was black. My mind hadn't registered what they _were_, in part because that thinking was decidedly out of fashion at the time those memories were formed. Is the way I remembered those characters really all that different from cringing any time I see `if isinstance(x, y):`  in a codebase? The heyday of dynamcially typed OOP-forward languages like Python and Ruby coencided with societal pressure to "be colorblind" in a way that is hard to ignore.

Consider the era that gave rise to `TypeScript` and `Pydantic` - the 2010s. After a decade of dynamically typed code, many developers were tired of "magic soup" - applications filled with cryptic round-about logic and side effects that were impossible to debug. Class names that looked like the developer was training for Countdown on the BBC. They wanted structure, order, and simplicity of pattern matching, and with that came the return of typing and functional programming. 

Both TypeScript and Pydantic start every method with a single question: "what are you?" The identity of the object is the base for all proceeding business logic. In this case it does not matter if the calling function invokes an `update()` method and the object has an `update()` method, if the object type is wrong this call will never get that far. This confirmation of type occurs at every functional exchange in TypeScript and as much of the typed Python codebase as inherits from `Pydantic.BaseModel`, effectively starting every transaction and sub-transaction with a declaration of identity. "As a `ProductUpdateRequest` object, I have an `update()` method I can execute for you." 
Around this same time we saw the emergence of identity-forward thinking in academic circles, politics and business. Examples abound of the growing importance placed on identity during this time period; as it’s safe to assume that anyone reading this has reasonably vivid memories of the last 10 years, I will leave you to draw your own parallels.

 This is not an indictment of either the static or dynamic typing language paradigms, both have strengths and weaknesses. For example, how many times have you written this little gem? 
 ```python
 def standardize_args(arg:Iterable):
     if isinstance(arg, str):
         return [arg]
     return arg
```

 “Accept a string or a list of strings” is one of those times that duck typing sucks. The most straightforward way to get this done is to pattern match object identity, because both a `str` and any other iterable will qualify for iteration- they can both “do the job” but the string will do it incorrectly, and won’t know until it’s too late. On the other hand, unnecessary rigid typing creates the potential for a serious coupling issue. Consider an adapter interface: 
```python
class Interface(BaseModel):
    adapter: XAdapter
```
 For every new adapter you want to support, you need to update your typing. If the adapter evolves to have variations, children etc., you need to update your typing. If you want to support other interfaces as adapters, which also already implements all the needed methods and attributes… you guessed it, typing needs to change. Keep in mind that none of the code in the adapters or interfaces have changed, but the typing still needs to continuously update. 
```python
class Interface(BaseModel):
	 adapter: Union[XAdapter, Type[YAdapter], ZAdapter, LocalInterface, Type[ExternalInterface] # this goes on, and on, and on...
```
 This coupling begets more coupling, as an exclusive white list of types can be too tempting for a junior developer to resist peeking under the hood and hard-wiring dependencies on an adapter’s internals. 

The solution could be a future where we explicitly type statically or dynamically based on which is the correct tool for the job. Pydantic already supports a form of duck typing with type classes `Iterable`, `Callable`  etc - which care less about what a thing _is_ and more about what it _does_ (sound familar?). Using `typing.Any` today feels as code-smelly as duck typing with `isinstance()`.  But what correcting that is as simple as aliasing `Any` with `DuckType` ?
```python
from typing import Any as Duck
from pydantic import BaseModel

class Interface(BaseModel):
name: str
description: str
adapter: Duck # I intend to duck type this!

def send_message(self, message:str): 
    try: 
	    self.adapter.send_message(message) 
    except AttributeError as e:
        raise ValueError("adapter must implement 'send_message', not implemented in adapter %s", self.adapter) from e
```
`Duck` tells future us and our PR reviewers to look for the duck typing. If it's missing that is an easy conversation to have. 


<sub>1. Python as a language has been around since the late 1980s, however Python 2+ is really where it begins to reflect what most would consider "modern Python" in a way that is applicable to the conversation</sub>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NDI5NjM2MzAsNTk3MTg3NDEyLC0xNz
Y0NzU0MzAyLDE5MTczNjQyNzQsLTc0NTk5NzM4NiwtNjQ2NTcw
NDgzLDE5MTExNTg5MzcsLTQ3MTk4NTY0Myw0MzczNDMwNjEsLT
M5OTcyNDQzMywtMTE1Njg3NDA3MCwtMTM0ODg4NTIwNCwtMjE3
NTY3NjU0LDE3MzI5NzAwNTQsMjAxNjYxMjI1NCwyMDE2NjEyMj
U0LDU3NjY0Nzg5MCwtNjkzNjA3NjEwLDEwOTA1NTAyMzhdfQ==

-->