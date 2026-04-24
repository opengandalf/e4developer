---
title: "Introduction to Concurrency in Spring Boot"
date: 2018-03-30T00:00:00Z
draft: false
description: "When building services with Spring Boot we have to deal with concurrency. There is this misconception that because of using Servlets and getting a new Thread…"
categories: ["Microservices", "Spring Boot"]
cover:
  image: "images/trains.jpg"
  alt: "Introduction to Concurrency in Spring Boot"
aliases:
  - /introduction-to-concurrency-in-spring-boot/
  - "/2018/03/30/introduction-to-concurrency-in-spring-boot/"
ShowToc: true
TocOpen: false
---When building services with Spring Boot we have to deal with concurrency. There is this misconception that because of using Servlets and getting a new Thread allocated per request there is no need to think about concurrency. In this article, I will give some practical advice on dealing with multi-threading in Spring Boot and how to avoid problems it can create.

## Spring Boot Concurrency Basics

The key areas worth considering when thinking about concurrency in Spring Boot applications are:

- **Maximum number of threads –**This is the maximum number of threads that are allocated for dealing with requests to the application
- **Shared external resources**– Calls to external shared resources such as databases
- **Asynchronous method calls**– These are method calls that release the thread back to the thread-pool when waiting for a response
- **Shared internal resources**– Calls to internal shared resources- such as caches and potentially shared application state

We will look at them one after another and see how they can impact the way we write applications with Spring Boot.

## Maximum number of threads in Spring Boot Application

The first thing to be aware is that you are dealing with a limited number of threads.

If you are using Tomcat as your embedded server (default), then you can use the property `server.tomcat.max-threads` to control how many threads you want to allow. This is set to `0` by default which means- use the Tomcat default which is `200`.

It is important to know this, as you may need to scale this number to work effectively with the resources that the service is given. It can also become problematic when dealing with external resources…

## The problem with shared external resources

Calling databases and other REST endpoints can take significant time.

The limited number of threads that you are dealing with means that you really want to avoid long-running, slow, synchronous requests. If you are waiting for some slow process to complete and holding the thread, you are potentially under-utilizing your server.

If you have many long-running threads that are waiting for responses, you may essentially end up with a situation where really fast, simple requests are waiting for long, *“forever-waiting”* requests to terminate.

How can this be improved?

## Asynchronous method calls to the rescue

It often helps to request for multiple things at once. Ideally, if you need to call three services: Service A, Service B, and Service C; **you don’t want to do that**:

- Call Service A
- Wait for a response from Service A
- Call Service B
- Wait for a response from Service B
- Call Service C
- Wait for a response from Service C
- Compose responses from A, B and C and finish the processing

If each service takes 3 seconds to respond, **the whole process would take 9 seconds**. It is much better to do the following:

- Call Service A
- Call Service B
- Call Service C
- Wait for responses from Service A, B, and C
- Compose responses from A, B and C and finish the processing

In this case, you make al three calls without waiting for completion and assuming that services A, B, and C, are not dependent on one another, **it takes 3 seconds to respond**.

The idea of asynchronous and reactive microservices is interesting in itself. I recommend checking out:

- **The [reactive section of this blog](https://www.e4developer.com/category/reactive/), especially [Getting Reactive with Spring Boot 2.0 and Reactor]({{< ref "/posts/getting-reactive-with-spring-boot-2-0-and-reactor" >}})**
- [The reactive manifesto](https://www.reactivemanifesto.org/)
- [Spring Boot 2 and WebFlux](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html)
- [Project Reactor](https://projectreactor.io/) by Pivotal
- [Eclipse Vert.X](https://vertx.io/) – reactive microservices
- [ReactiveX](http://reactivex.io/) (RxJava)

These are all fascinating, but we are focusing on Spring Boot in this article…

## Making asynchronous calls in Spring Boot

How do you enable asynchronous method calls in Spring Boot? You want to start with `@EnableAsync` annotation on your Application class under the `@SpringBootApplication` annotation.

With that enabled, you can use `@Async` annotation in your services that return `CompletableFuture<>`. Because you have `@EnableAsync` , the `@Async` methods will be run in a background thread pool.

If you make a good use of the asynchronous execution, you will avoid many unnecessary dips in performance, making your service as fast and responsive as it is possible.

For the deatils of implementing this in Spring Boot I really recommend checking out [the example from the official Spring website](https://spring.io/guides/gs/async-method/).

## Shared internal resources

While the previous sections deal with things we often have no control over- external resources, we are in full control of the internal resources of the system.

Knowing that we control the internal resources, **the best advice in avoiding issues related to sharing them, is not to share them**!

**Spring Services and Controllers are Singletons by default.** It is important to be aware of that and be very careful. The moment there is a mutable state in your Service, you need to deal with it as you would in any standard application.

Other potential sources of the shared state are caches and custom, server-wide components (often monitoring, security etc.).

If you absolutely need to share some state, here is my advice:

- Deal with immutable objects. You avoid many concurrency related issues if your objects are immutable. If you need to change something- just create a new object.
- Know your Collections. Not all collections are Thread-Safe. A common pitfall is using HashMap assuming that it is Thread-Safe (It is not. If you need concurrent access use ConcurrentHashMap, HashTable or another thread-safe solution.).
- Do not assume third-party libraries are thread-safe. Most code is not, and access to the shared state has to be controlled.
- If you are going to rely on it- learn proper concurrency. I really recommend getting a copy of Java Concurrency in Practice. Written in 2006, but still very relevant in 2018.

## Summary

Concurrency and Multi-Threading in Spring are big and important topics. In this article, I wanted to highlight the key areas that you need to be aware of when writing Spring Boot applications. If you want to be successful when building high-demand, high-quality services, you need to make conscious decisions and trade-offs around this topics. I hope that with this article you know how to get started.
