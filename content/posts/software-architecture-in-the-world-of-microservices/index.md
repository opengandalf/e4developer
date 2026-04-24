---
title: "Software architecture in the world of microservices"
date: 2018-12-02T00:00:00Z
draft: false
description: "The topic of software architecture comes up often when discussing microservices. Many newcomers to microservices are not sure how to handle discussing…"
categories: ["Architecture", "Microservices"]
cover:
  image: "images/cropped-e4-dev-twitter.png"
  alt: "Software architecture in the world of microservices"
aliases:
  - "/2018/12/02/software-architecture-in-the-world-of-microservices/"
  - "/software-architecture-in-the-world-of-microservices/"
ShowToc: true
TocOpen: false
---The topic of software architecture comes up often when discussing microservices. Many newcomers to microservices are not sure how to handle discussing architecture and how to make decisions. Should they bring the more traditional role of the software architect, or should everyone just do what they think makes sense? In this article, I will give you my answers to these questions and share some additional advice.

## The high-level view of the entire system

First of all, regardless of what you decide is a good approach to handling architectural decisions, you need to know what your system looks like.

I worked on projects where the real architecture was “tribal knowledge” passed from one group of developers to another and on systems where the up-to-date high-level logical architecture diagram was always on the wall. Guess which projects ended with more efficient, sane architectures?

In order to really start making precise architectural decisions and refactor your system, you really need to know what you are working with. Going in “blind” it is far to easy to make mistakes and overlook side-effects and dependencies.

My first advice is that whatever you decide- put some effort first in creating a high-level logical architecture diagram. Ideally, you would also make some diagrams for data-flow, security and other important aspects of your system.

Working on diagrams may seem like a chore, so make sure you only work on those that are important and genuinely useful to the team.

## The architecture of choices

What makes the architecture of microservices systems more difficult to talk about? I believe it would be these two things:

- Rapid change
- Many choices at every step

I have even written an article describing [microservices as the architecture of choices]({{< ref "/posts/microservices-the-architecture-of-choices" >}}).

With the number of choices at every step, it is clear to me that you can’t just trust your luck and not think about these things. Also, with the rapid pace of development, it is equally clear that you should stay away from [TOGAF](https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework) and similar ideas. (In my humble opinion, you should stay away from TOGAF anyway, but that is for another article).

With these parameters, how do you approach working on the architecture for microservices systems?

## Architectural Decision Records as a system design tool

Architectural Decision Records ([Homepage of the ADR GitHub organization](https://adr.github.io/)) is:

> a software design choice that addresses a functional or non-functional requirement that is architecturally significant.
>
> ADR Homepage

ADRs are not entirely new – Michael Nygard described them already in [this blog post in 2011](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions), but I came in contact with them only in 2018. ThoughtWorks listed them as ADOPT level technology in their [technology adoption radar in 2018](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records).

What is this whole idea about? There are different approaches, but it roughly boils down to:

- For every Architectural Decision (AD) that you will take follow this process.
- For every AD use a template to record:
  - Context
  - Motivation
  - Decision
  - Status
  - Consequence
  - Combination of the above (or something else as required)
- These create ADR (Architectural Decision Records)
- Store them in a place like Git repository, Google docs, Wiki (something that works for your team)

The core idea here is to keep it simple, keep it standardized, keep it accessible.

I believe that for many teams, this is exactly what is needed. You want to know what was decided, when and why. This does not have to take much effort.

Taking this idea a bit further and using Git- you could have architectural decisions as pull requests that get discussed by people. What a great way to get more people involved and heard!

## Stability of a distributed system

Because of the difficulty of building distributed systems like microservices, I recommend adding an additional, more subtle, technique at steering the overall architecture and design. Using Consumer Driven Contracts.

Consumer driven contracts (CDCs) could easily fill a few articles on their own. I am mentioning them here, as a way of letting other systems know, what is important for your system.

If you are not familiar with the concept, check out <https://docs.pact.io/>where you can read an introduction to Pact (a popular CDC tool).

If you are working in a truly distributed fashion (multiple teams, multiple services), you need to find a way of letting other teams know what is architecturally significant to you and your system. One way is using common ADRs, the other is using CDCs.

## Do you need traditional software architects?

I think it is clear that you need to think about software architecture when working with microservices. You also should engage in taking architectural decisions (with the help of ADRs) and evolving your APIs (safely with CDCs).

Does that mean that you need an architect? It depends! It clearly means that if you had one you could probably keep him quite busy. What about:

- Updating the high-level architecture diagrams
- Helping create and progress ADRs
- Working on API design across teams
- Working alongside teams on more challenging problems (security etc.)

I think just these four can be a full-time job on a large enough project. You don’t necessarily need someone with the title, but you definitely need people with the architecture skill.

## Summary

I hope that this article gave you an idea of how to make architecture work in your microservices system. Working on microservices is more difficult than just building monoliths. That means that you not only need a good team of developers, you also need people with sharp architectural intuitions and modern, light-weight processes that work!
