---
title: "When to use a Java framework like Spring?"
date: 2018-07-29T00:00:00Z
draft: false
description: "I have recently been writing a lot about microframeworks and my enthusiasm for them. Even though I think they are amazing, they are not always the answer."
categories: ["Architecture", "Microservices"]
cover:
  image: "images/leaves.jpg"
  alt: "When to use a Java framework like Spring?"
aliases:
  - "/2018/07/29/when-to-use-a-java-framework-like-spring/"
ShowToc: true
TocOpen: false
---![](images/leaves.jpg)

I have recently been writing a lot about microframeworks and my enthusiasm for them. Even though I think they are amazing, they are not always the answer. In this article, I will explore use cases, where a fully featured framework may be just what you need.

## What is the difference between framework and microframework?

Before going deeper into the argument, let’s make sure we are clear what we mean when talking about microframeworks.

[Spark Java](http://sparkjava.com/) and [Javalin](https://javalin.io/) are two great examples. Very simple frameworks, that focus on helping you deal with REST APIs and basic server operations. Not much more. These two examples both are under 15,000 lines of code (Spring Boot Core is about 100,000 before we count all the dependencies).

Full-fledged frameworks like Spring, Grails, different flavours of Enterprise Java (now [Jakarta EE](https://jakarta.ee/)) bring much more to the table. Let’s look at some of the core Spring features:

- Advanced dependency injection
- Advanced aspect-oriented programming (AOP)
- Controllers that can process requests differently with a lot of help from the framework
- Multiple optional dependencies for working with data, security, messaging etc.

There are of course many more differences and features, but this article is not solely about spring.

## When to use a fully featured framework?

When you need to! It really boils down to that. We have identified some core missing features and if you really need them- go for it. Let me give you some examples where frameworks like Spring shine:

- When you are building a large application. Ok, let’s say the dreaded word- monolith. These large applications don’t have to be ugly. Frameworks like Spring can make you build something maintainable.
- When you need a specific capability that the framework provides. If you want to use [Spring Data]({{< ref "/posts/spring-data-microservices-data-companion" >}}) or Spring Security for example. Or you want to make use of multiple capabilities provided by [Spring Cloud]({{< ref "/posts/spring-cloud-blueprint-for-successful-microservices" >}}).
- This may sound controversial, but I think we should lean towards these most popular solutions when working on somebody’s else systems. If you are a consultant (like myself), it is easier to leave your client with a mainstream framework, than a bespoke solution.

I think these are the three main cases for using a fully featured framework. To summarise:

- When building large applications
- When required a specific capability
- When consulting (although this may change when some microframeworks will become mainstream)

There is one more thing though…

## How to use frameworks smartly?

If you decided to use a fully featured framework, do it smartly. I realized the importance of this after reading [Clean Architecture]({{< ref "/posts/discovering-clean-architecture-with-uncle-bob" >}}) by Robert C. Martin. *Uncle Bob* writes a very memorable thing there:

> “Don’t marry the framework”
>
> Robert C. Martin

The idea behind this is that when using a framework, it is very easy to get very coupled with the framework code. Your application stops looking like a *User Account Service* (for example) and starts to look like a *Large Grails Application*.

Marrying the framework means that you will become inseparable from the framework. This is especially risky when developing something larger, where a rewrite is not an option… *“For better, for worse, for richer, for poorer, in sickness and in health…”* Do you trust your framework like that?

How to integrate with a framework smartly? Here is some advice:

- Separate your business logic from the framework code as much as possible. It is ideal to have most of the business logic be free of the framework code. This way you can always re-use it.
- When using things such as database integration, etc. consider following the [Clean Architecture]({{< ref "/posts/discovering-clean-architecture-with-uncle-bob" >}}) advice. Separate this code with a layer of abstraction.
- Make use of [the Dependency Inversion Principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle) to abstract away the framework code.

I really think that [Clean Architecture]({{< ref "/posts/discovering-clean-architecture-with-uncle-bob" >}}) hits the nail on the head here:

![](images/cleanarchitecture.jpg)

To use the framework well, to avoid marrying it- strive to keep your *Use Cases* and *Entities* free of the framework code.

## Summary

I promote [microframeworks]({{< ref "/posts/the-rise-of-java-microframeworks" >}}) a lot. That does not mean that they are always the right tool for the job. There are situations where a fully featured framework like Spring may be a better tool to solve your problem.

If you use frameworks smartly, you may get all the benefits and avoid most of the drawbacks of tight-coupling with the framework. When designing software systems- always think what tool will work best for your use case.
