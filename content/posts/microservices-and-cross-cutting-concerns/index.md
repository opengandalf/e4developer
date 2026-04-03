---
title: "Microservices and cross cutting concerns"
date: 2018-09-09T00:00:00Z
draft: false
description: "When thinking about microservices, we mostly imagine autonomous teams working on independent services. Despite all that independence, things such as log…"
categories: ["Architecture", "Microservices"]
cover:
  image: "images/technical-forum.jpg"
  alt: "Microservices and cross cutting concerns"
aliases:
  - "/2018/09/09/microservices-and-cross-cutting-concerns/"
ShowToc: true
TocOpen: false
---![](images/technical-forum.jpg)

When thinking about microservices, we mostly imagine autonomous teams working on independent services. Despite all that independence, things such as log aggregation and security benefit from a system level thinking. In this article, I will discuss these concerns and give my advice on how to approach them.

There are different kinds of microservices systems. Some of them are truly independent when every microservice is nearly indistinguishable from a third-party API, other- because of either necessity or practicality, rely on shared infrastructure or concepts.

When looking at these cross-cutting concerns, you should always keep in mind what kind of system are you working on. One thing may be a good choice in organisation A and a terrible mistake in organisation B. Advice given here does not give you the mandate to stop being critical!

With this warning out of the way, let’s look at the common cross-cutting concerns in microservices architectures.

## Authentication / Authorization

The first thing worth thinking about is the approach to the authorization and authentication within the system. Some of the questions worth asking are:

- Does every service need to be secured?
- How to verify if a request is authentic- do we just limit the possible callers and assume that they have a right to execute anything?
- If we are going with a shared authorization scheme, what roles are we going to use int he system?

Regardless of how you look at the problem, it makes little sense to make separate decisions, to answer these questions differently for each service.

## Log Aggregation and Distributed Tracing

Another thing that benefits from a system level thinking and consolidated strategy is dealing with logs. Having the ability to see a request journey through multiple different microservices is an extremely useful debugging tool.

I wrote a  whole article about [Tracing messages in Choreography with Sleuth and Zipkin]({{< ref "/posts/tracing-messages-in-choreography-with-sleuth-and-zipkin" >}}) if you would like to know more about this topic.

In general, a tool like ELK stack (Elasticsearch, Logstash, Kibana) is invaluable once your microservices move from development into production.

## Configuration Management

Getting your configuration management right is the difference between pleasant, scalable microservice architecture and a configuration mess like you have not seen it before.

There are multiple ways to fight this- Spring Cloud Config and storing configuration in the environment are among the most popular options.

This section, like others in this article, could easily be an article (or a series) in itself. I can’t possibly tell you enough about configuration management here, so I strongly advise you to research this area.

## Service Discovery / Load Balancing

One of the key benefits of microservice architectures is its scalability. You may easily scale any part of the system to meet the demand. Regardless if this is done dynamically or not, you will need to know how to route traffic between all these different services.

Service Discovery and Load Balancing are the two very common practices that should be employed here. You may argue that this is not a truly cross-cutting concern and that individual microservices should not be aware of this setting. I agree with you, but someone needs to take care of it. Especially if it impacts service deployment configuration.

## Use of shared libraries

Ok, you may be aware of that, but it still comes up surprisingly often when talking with developers new to microservices. The question is: *“Can we have shared libraries between microservices?”*.

*“…Yes! Of course, you can!”*Just make sure that you are not introducing coupling and dependencies. Utility libraries that are versioned well (maybe with [SEMVER](https://semver.org/)) and don’t introduce coupling are perfectly fine.

## Use of shared domain model

This is the real cross-cutting concern… Can we have a shared domain model?

Many developers will tell you – *absolutely no!*I don’t fully agree here. While you shouldn’t share the exact same code between a server and a client API, I think it is perfectly ok to share client API domain model. Again, as long as you are not forcing others to use it.

I have written a more nuanced answer to this question in my [Code reuse in microservices architecture – with Spring Boot](https://blog.scottlogic.com/2016/06/13/code-reuse-in-microservices-architecture.html) for Scott Logic.

To reiterate: You should not share the code between the Server API and a client. You can create a shared Client API library that is versioned and maintained well. This can be shared, but sharing should not be enforced.

I found this approach to avoid most drawbacks of straight-up sharing and limit the problems with never-ending copy-paste of often simple, yet verbose code.

## Automated Testing

If you are delivering a system, rather than a single microservice, you will be interested in the interactions between these services. I found that in microservices architecture, these interactions can be very brittle if not tested properly.

If you can get your product/project/company to adopt *consumer-driven contracts* across the services, you will quickly see the benefits. The two technologies that I recommend looking up here are:

- [Pact](https://docs.pact.io/) – if you want to go the mostly technology agnostic route.
- [Spring Cloud Contract](https://cloud.spring.io/spring-cloud-contract/) – if you enjoy the Spring ecosystem. Spring Cloud Contract also works with non-Spring and non-JVM projects!

Both are a great choice!

## Summary

Have no illusion- these are not all the cross-cutting concerns that you may encounter in the wild when working with microservices. It turns out that when you deliver a system as a whole, even autonomous and independent teams should sometimes talk to each other!

In order to deal with concerns like that I recommend that you consider:

- **Hosting a regular technical-forum** when team representatives can meet and discuss problems of these natures.
- If you don’t need this formalised, just talk between teams about these issues.
- Don’t pretend that cross-cutting concerns don’t exist in microservices systems.

I hope this was an interesting read. If you can think about other cross-cutting concerns that come up in microservices architectures a lot, let me know on [twitter](https://twitter.com/e4developer) or in the comments!
