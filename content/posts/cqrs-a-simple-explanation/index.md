---
title: "CQRS - a simple explanation"
date: 2018-03-11T00:00:00Z
draft: false
description: "Command Query Responsibility Segregation (CQRS) is a pattern that causes quite a lot of confusion. With the popularity of microservices and the event-based…"
categories: ["Architecture", "Microservices"]
cover:
  image: "images/cqrs-canyon.jpg"
  alt: "CQRS - a simple explanation"
aliases:
  - "/2018/03/11/cqrs-a-simple-explanation/"
ShowToc: true
TocOpen: false
---![](images/cqrs-canyon.jpg)

**Command Query Responsibility Segregation (CQRS)** is a pattern that causes quite a lot of confusion. With the popularity of microservices and the event-based programming model, it is important to know what CQRS is. In this article, I will provide you with a simple explanation.

To understand CQRS it is important to get some basic terms and concepts right. The first that often appears next to CQRS is CRUD.

## What is CRUD?

CRUD stands for Create, Read, Update and Delete. When you think about this, this is what most basic software systems do. You have some records, you may want to read some records, update them, create or delete.

If you want to build a system, a reasonable starting point would be using the same model for retrieving object as well as updating object.

Let’s think of an example here. Assume you want to write a *“Book Store Application”.*You may have a *BookInventoryService*that lets you do things such as add new books to the inventory, mark some of them as loaned out, check if you have a specific book etc. That would be a very simple CRUD system.

## What is a Command in the CQRS context?

A Command is a method that performs an action. These would be the Create, Update and Delete parts of a CRUD system.

There is really not much more to it. In the *BookInventoryService* adding new books or marking them as loaned out would be carried out by Commands.

## What is a Query in the CQRS context?

A Query is a method that returns Data to the caller without modifying the records stored. This is the Read part of a CRUD system.

Coming back to *BookInventoryService –*Queries would be responsible for finding details about specific books or checking if a book is loaded out.

## Command Query Responsibility Segregation (CQRS)

Now, when we look at Command Query Responsibility Segregation it may become clearer what it is all about. The goal is to **segregate**the **responsibilities**for executing **command** and **queries**.

This simply means that in a CQRS system, there would be no place for *BookInventoryService*that is responsible for both queries and commands. You could have *BookInventoryInformationService* and maybe *BookLendingService* or more.

This does not sound like the most practical thing. And **in most cases, this is not practical**. If you are not sure if you need CQRS, then don’t impose CQRS on your system.

## What CQRS often implies

When talking about CQRS people often mention a few other concepts in the same sentence.

##### Separate domain model

CQRS **does not require using separate domain model for queries and commands**. It is often logical to go that route, but you could also use separate domain model for queries and commands, yet do not segregate the responsibilities.

##### Event Sourcing

Event Sourcing is not a requirement CQRS. You can find a great explanation of event sourcing on this [eventuate.io blog post](http://eventuate.io/whyeventsourcing.html). I think they capture the essence of how Event Sourcing works pretty spot on:

> A business object is persisted by storing a sequence of state changing events. Whenever an object’s state changes, a new event is appended to the sequence of events. Since that is one operation it is inherently atomic. A entity’s current state is reconstructed by replaying its events.

Looking at that idea it is clear how CQRS helps. Commands are in effect streams of events that are persisted in the system. Queries then interpret these events. Using same domain model, or not separating these responsibilities would be a mistake.

##### Choreographed systems

While event sourcing is a radically different architecture, the choreography is often more familiar to microservice developers.

When talking about choreography we mean event-driven distributed systems. Rather than microservices being told what to do explicitly, they subscribe to some event source and react to events as they happen.

While these kinds of systems often implement CQRS, this is not the definition.

## My thoughts on CQRS

As I already mentioned, in most systems it is not necessary to implement CQRS. Moreover, the added complexity may end up detrimental to the system design.

I think that Choreographed/Event-Drive architecture is often the better choice when designing microservices system of non-trivial complexity. In this context, CQRS may be something that is worth thinking consciously about.

Many articles on CQRS take your understanding of the basic concept for granted. If you are interested in the pattern and event-driven service, now it is a good time to check them out:

- [Martin Fowler on CQRS](https://martinfowler.com/bliki/CQRS.html)
- [Greg Young explains the basics of CQRS](http://codebetter.com/gregyoung/2010/02/16/cqrs-task-based-uis-event-sourcing-agh/)
- [LosTechies busting some CQRS myths](https://lostechies.com/jimmybogard/2012/08/22/busting-some-cqrs-myths/)
- Developing Transactional Microservices Using Aggregates, Event Sourcing and CQRS: [parts 1](https://www.infoq.com/articles/microservices-aggregates-events-cqrs-part-1-richardson) and [part 2](https://www.infoq.com/articles/microservices-aggregates-events-cqrs-part-2-richardson)
