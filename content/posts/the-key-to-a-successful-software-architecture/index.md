---
title: "The Key to a Successful Software Architecture | E4developer"
date: 2018-07-21T00:00:00Z
draft: false
description: "Recently I have read and reviewed “Clean Architecture” by Robert C. Martin. Very entertaining book. It made me think about the main quality that good software…"
categories: ["Architecture", "Microservices"]
cover:
  image: "images/the-key.jpg"
  alt: "The Key to a Successful Software Architecture | E4developer"
aliases:
  - "/2018/07/21/the-key-to-a-successful-software-architecture/"
ShowToc: true
TocOpen: false
---

# The Key to a Successful Software Architecture

![](images/the-key.jpg)

Recently I have read and [reviewed *“Clean Architecture*“](https://www.e4developer.com/2018/07/14/discovering-clean-architecture-with-uncle-bob/) by Robert C. Martin. Very entertaining book. It made me think about the main quality that good software architectures exhibit. What is this quality? It is the existence of clear boundaries and well-defined modules. If you don’t agree with me- keep reading and I am sure we will find some common understanding.

## Divide and Conquer

![](images/roman-empire-1024x827.jpg)

The famous maxim of Divide and Conquer (Latin: *dīvide et imperā*) is defined as:

> gaining and maintaining power by breaking up larger concentrations of power into pieces that individually have less power than the one implementing the strategy

It applies to software in a rather intuitive way. Often when imagining the system as a whole it may seem daunting. Implementing a large banking application can seem like an insurmountable task! Implementing a REST API or building messaging layer may seem more reasonable.

Creating well-defined components can help us direct our efforts appropriately and build some parts of the system to a production-level quality before others are even started.

The challenge here is building the right thing and not building too much (You aren’t gonna need it – YAGNI). This is why the understanding of the final architecture is important. It can guide our decisions regarding individual components, even when implementing them in isolation.

## Delegating Control

Components can often be implemented in isolation. That means that we can have multiple people or even teams working on them separately, at the same time, without stepping on each other toes.

Since we started with a semi-military maxim, we can continue with that theme. This delegation of control is a strategy that helped the Prussian army prevail in the Austro-Prussian and Franco-Prussian Wars. Helmuth von Moltke recognised the importance of delegating control. He favoured:

> directives stating his intentions, rather than detailed orders

This is all, really fascinating stuff and if you are interested in the history of military strategy, you can read more about that in [Moltke’s theory of war](https://en.wikipedia.org/wiki/Helmuth_von_Moltke_the_Elder#Moltke's_theory_of_war) summarised on Wikipedia.

![](images/napoleon.jpg)

Implementing large software systems is not war (although sometimes it feels like a military campaign with many fronts), but the lesson stands. With components, we can guide the evolution of the system by stating intentions and responsibilities, while delegating the ownership and implementation to another team.

## Striving for Simplicity

So far, it seems that components are the silver bullet (I don’t know why I refer to the military all the time today!) that can solve (bullets *“solve”* problems in a rather grim way) all of our architectural problems.

The problem with components is that they should be simple on two levels, yet it can be difficult to achieve.

### Components – internal simplicity

We are talking about high-cohesion here. We want the components to have a clear purpose and clear reasons for changing. This is often difficult to achieve, hence everyone in a development team should be aware of these guiding principles. [SOLID principles](https://en.wikipedia.org/wiki/SOLID) apply here.

### Components – simplicity in integration

To achieve true simplicity, you need to look at dependencies between components. If you end up with a set of inter-dependent, tightly coupled components, you have failed at achieving simple (clean) architecture.

### Components – being pragmatic

The difficulty in designing good components is linked to the balance, between making the components practical for the developers here and now, and making the components *“good citizens”* of our architecture diagram.

Being pragmatic is important. If you want to focus on one thing, make sure that your component is clearly separated and can always be replaced. Simplicity in integration often trumps internal simplicity.

## Keeping Options Open

I have pointed the clear separation of a component as more important than the simplicity of a component itself. Why is that? In order to be successful, we need to be able to react to changes. The “soft” is part of “software” for precisely that reason. We build software (rather than hardware) because we want an option to change as a part of the product.

What can help us keep our options open:

- Well defined components
- Clear separation between components
- Keeping the “details isolated” – database, frameworks, etc. as much as practical

This is really what [Clean Architecture](https://www.e4developer.com/2018/07/14/discovering-clean-architecture-with-uncle-bob/) explains very well. Good architectures are architectures that can change and adapt.

![](images/the-clean-architecture.jpg)

## Components – the Enablers of Architecture

I don’t want to give you an impression that components are only important for the Clean Architecture as described by Robert C. Martin. In fact, let’s look about some other architectures:

- **Microservices** – *“Small Autonomous services that work together, modelled around a business domain”* ([definition by Sam Newman](https://www.e4developer.com/2018/07/02/microservices-definition/)) – You can see components as microservices here.
- **Hexagonal Architecture** – *“Hexagonal Architecture is a form of application architecture that promotes the separation of concerns through layers of responsibility.”* ([definition from culttt.com](https://www.culttt.com/2014/12/31/hexagonal-architecture/)) – I can’t see how you can separate concerns and build laters of responsibility without components.
- **Data, context, and interaction (DCI)** – *“The paradigm separates the domain model (data) from use cases (context) and Roles that objects play (interaction). “* (from [Wikipedia](https://en.wikipedia.org/wiki/Data,_context_and_interaction)) – Separation of different concepts is once again at the heart of the architecture.
- **Service-oriented architecture (SOA)** – I don’t think I need a quote here. SOA has “components” (as Services) pretty much in the name.
- Any architecture styles different than BBOM ([Big Ball of Mud](https://en.wikipedia.org/wiki/Big_ball_of_mud)) that I can think of

In order to implement any of the above architecture styles, you need skill in designing components and separating concerns. I hope you agree with me by now- building components is the key skill to any successful software architecture.

## Summary

I wanted to write about components to remind ourselves what lies at the heart of software development. Developing and designing systems that work and can change.

Architects are often guilty of thinking on the too high level and forgetting about components and developers tend to focus too much on the code, sometimes forgetting the bigger picture. This is a reminder for all of us- let’s take good care of our components!
