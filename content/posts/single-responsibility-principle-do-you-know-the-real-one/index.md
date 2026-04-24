---
title: "Single Responsibility Principle - do you know the real one?"
date: 2018-10-04T00:00:00Z
draft: false
description: "Single Responsibility Principle, as defined in the very famous set of SOLID principles, is often misunderstood. When asked what it means…"
categories: ["Architecture", "Java", "Microservices"]
cover:
  image: "images/cropped-e4-dev-twitter.png"
  alt: "Single Responsibility Principle - do you know the real one?"
aliases:
  - "/2018/10/04/single-responsibility-principle-do-you-know-the-real-one/"
  - "/single-responsibility-principle-do-you-know-the-real-one/"
ShowToc: true
TocOpen: false
---Single Responsibility Principle, as defined in the very famous set of SOLID principles, is often misunderstood. When asked what it means, most developers go with- “a class should do only one thing”, or something along these lines. This is simplistic and frankly- wrong! Intrigued? Read on!

## Single Responsibility Principle – the real definition

Single Responsibility Principle (SRP), as defined by Robert C. Martin states:

>  “A class should have only one reason to change.”
>
> Robert C. Martin

This is very different from the “a class should do only one thing” version.

In one of his later books ([“Clean Architecture”, reviewed here]({{< ref "/posts/discovering-clean-architecture-with-uncle-bob" >}})) Robert C. Martin goes even further, clarifying his intent behind this principle:

> “A module should be responsible to one, and only one, actor.”
>
> Robert C. Martin – The final version of the SRP from “Clean Architecture”

This is even more precise. Before we go deeper into these definitions let’s look once again why  “a class should do only one thing” is a weird idea…

## A class should do more than one thing!

Ok, so what does that even mean that class should do only one thing? Does that mean that we are only allowed one public method? That there is only one piece of business logic allowed? It is hard to think how this logic applies to classes and OOP.

My guess that this is somehow the principle behind writing good functions being misunderstood and extended to the OOP and SOLID principles.

It is good if each function has a specific goal, and if there is too much logic carried out by a single function, you can then refactor into multiple more specialised functions.

That makes sense on a function level, it does not make sense on a class level.

## “A module should be responsible to one, and only one, actor”

Let’s look at the correct formulation of the Single Responsibility Principle and see what it really means.

First of all, the SRP talks about a module. Uncle Bob clarifies that by that he means a source file. After all, the principle can apply to more than simply classes.

What about the actor that the principle is talking about? It can mean:

- User
- Stakeholder
- A group of users or stakeholders that are requiring the system to change in the same way

After all, if your “User” is let’s say, an “account manager” there could be more users fulfilling that role. It is good to think of that “actor” as a specific type of user in the system. It does not even have to be an actual person.

## An example of the Single Responsibility Principle

Let’s look at a simple example of the Principle:

- Imagine you are implementing a Bookstore application
- You have a class called Book
- The Book has a method called setStockLevel() – an inventory manager is an actor here
- The Book has a method called calculatePrice() – the salesman will be interested
- The Book has a method called getDetails() – the website presentation engine is an actor here

As you can see you have three different groups of actors that may need changes to the same Class.

What are the problems with that?

- There is a risk potential duplication of code if we need to start saving other inventory. This should be separated.
- The same issue appears when pricing algorithm is being developed further or generalised.
- Multiple groups of developers will start having merge issues and completely unrelated code live in the Book class.

What is the solution?

- Keep the Book Class focused. Focus on the methods that are related to the presentation on the website.
- Move the pricing logic into a pricing module that will possibly use the Book class.
- Do the same with the inventory.

There could be many things that the Book class is doing:

- Getting the details of the book
- Getting the picture
- Logging access to the Class for debugging
- etc.

But it will all be oriented around the presentation of the Book to the customer (via a website in that case).

## Why Single Responsibility Principle?

There are many benefits from following the SRP:

- Making code changes easier
- The code is more readable
- Easier to reason about the system
- Fewer reasons to change multiple files, changes become more focused
- Improved encapsulation and cohesion (this is re-phrasing the above partially)
- Together with other SOLID principles, it helps in achieving the Clean Architecture

## Summary

Single Responsibility Principle stated as *“A module should be responsible to one, and only one, actor”* is more nuanced, and ultimately more useful than many developers expect. If you already knew the real SRP, spread the word to those who don’t- if you learned it from my blog- I am happy that I could help!
