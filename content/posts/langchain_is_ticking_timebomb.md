---
title: "Langchain is a Ticking Timebomb"
subtitle: "predictions in AI"
date: 2024-1-9
draft: true
---

Let me preface this by saying that I very much appreciate the entire Lang* ecosystem. At my shop we rely heavily on Langfuse for development as well as the tagging interface for our training strategy. More than a few platforms have tried to be _the_ framework for language model applications (think Guidance, Haystack etc), and the Lang* team has arguably made the most headway, and done it OSS :metal:. So try not to disregard these observations as contrarian or success-hating; I really _want_ to love LangChain. 

When we began work on our inference engine back in October 2023 (so a millennia ago in LLM time) LangChain was the obvious choice. By the first week of December we had abandoned the framework, and by Christmas we had written our own internal prompt templating module to support a Q1 product launch. Such a drastic architectural change at an equally critical time in the product life cycle is not a thing to take lightly. But the growing collection of red flags became something we could not ignore, and I believe we made the best decision. 

What red flags?

### Dependency Management
If you've been around the Python ecosystem for more than a minute, you know that dependencies are the Achilles' heel of the language. This is true for Python as a whole, but I have found this to be exponentially worse in the data sphere. When Software Engineering, Data Engineering and Data Science coalesce, you find deeply abstracted package dependencies with pins like `Cython=>0.1` that "worked before," and lurk in the darkness of deployed code waiting to ruin your weekend. A few years ago the `snowflake-sqlalchemy` adapter was so often the source of surprise dependency failures that my team would comment `we're not snowflake` whenever a bad pin made it to a PR review. 
The general wisdom is to minimize the surface area of dependencies by importing only what your code needs to survive. 
![take only what you need to survive](https://y.yarn.co/84492e53-9f7f-42c3-a8c3-bd088fe3d7fe_text.gif)

LangChain does the opposite of this. The framework currently boasts over 200 supported integrations, every one of them a dependency. If something breaks in the requirements management of the Discord integration, it breaks your project, regardless of if you use Discord or not. 
In November of 2023 this lead to what is essentially a text compiling framework that takes 18 minutes to build in a container

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNDI3NjgxNDQsLTE1NTc1ODIyNywxMj
EzNDM2NjM4LDEzODIzNjMzNF19
-->