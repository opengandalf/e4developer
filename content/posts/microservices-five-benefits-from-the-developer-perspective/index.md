---
title: "Microservices - Five benefits from the developer perspective"
date: 2018-01-14T00:00:00Z
draft: false
description: "Looking at the main benefits of microservices for developers. Technical flexibility and architecture strengths discussed among other benefits."
categories: ["Microservices"]
cover:
  image: "images/cropped-e4-dev-twitter.png"
  alt: "Microservices - Five benefits from the developer perspective"
aliases:
  - "/2018/01/14/microservices-five-benefits-from-the-developer-perspective/"
  - "/microservices-five-benefits-from-the-developer-perspective/"
ShowToc: true
TocOpen: false
---I have started this blog to share my technical insight and passion with the wider development community. I would not be true to myself if I did not start by explaining why I enjoy working with microservices.

### You are free to use modern technologies

One of the big problems related to working with large, monolithic applications is that you are locked in with your technology. This problem is actually twice as bad as it may seem at first. The first part is that older, more proved framework are more likely to be chosen. That means you are unlikely to stay on the forefront of innovation, something that many developers value. The second part of the issue is that one something is chosen, it usually takes large effort (often too large) to make any significant change.

Working with microservices I had a pleasure to work with both Spring and Grails based microservices, making use of the latest versions of the respective frameworks. Seeing this modern technology in the enterprise is a refreshing breath of fresh air!

### Encapsulation and segregation of responsibility is natural

One of the great promises of SOA (Service Oriented Architecture) were self-contained services. In a way black boxes. This is why I don’t see microservices as something drastically different than SOA, rather its modern incarnation. When we tried implementing SOA on the older style, large Java EE applications run on JBoss, Websphere it was too easy to make a mistake. You want to separate your services communicating via some message bus and then suddenly one developer decides: *“What is a call between friends?”.*I am joking here, but the abstraction was way too easy to break by someone making mistake or trying to cut corners.

With microservices, these boundaries are stricter. When things are run as separate microservices it is not so easy to make such a mistake. things are separated naturally. It results with cleaner abstraction and codebase that is nicer to work with.

### The architecture is easier to see and enforce

When dealing with microservices, the architecture is often quite obvious. Services are run on separate containers and often named quite well. There is no need to look into the documentation or read a copious amount of source code. This enables architects and whoever is responsible for this level of design on the project to have their vision implemented clearly. The fact that each part of the system is smaller and well separated makes it even possible to quickly review the code and make sure that nothing questionable is happening.

Explicitly naming the microservices also gives developers and everyone else common, unambiguous way of talking about different components of the system.

### Changing code is much easier

I found it much easier to change the code in a project where microservices were implemented than in an average monolith. Once again the focus of the service and the brevity are your biggest allies. It is also helpful that re-building, re-running tests and starting microservice is often much faster than doing similar work with a monolithic application.

I did not mention here the fact that modern microservices framework such as [Spring Boot](https://projects.spring.io/spring-boot/) or [Grails](http://www.grails.org/) have a laser focus on cutting down unnecessary configuration and boilerplate code that so often gets in the way of understanding. I believe that what Spring Boot has done is made microservices accessible to a wider group of developers, thanks to these efforts.

### Thorough testing is possible and expected

I have seen very few monoliths with an automated testing coverage that made everyone confident in the system stability after the release. Nearly always, there is a large manual testing/qa team required. For an average enterprise, it is very difficult to thoroughly automate such a large and complex system.

Microservices, when they define good contracts in their APIs, are not so intimidating. With a good level of unit testing, thoroughly tested endpoints and some integration testing where necessary, it is much easier to be confident that the system will behave as necessary.

Another benefit of having this sort of separation is that code change made in one service can’t affect what is happening in the remaining services. This drastically reduces the chance of unexpected errors. Of course in SOA this should be the case as well, but as I mentioned- SOA by the book always was a rare sight.

### Summary

There are more benefits for adopting microservices and each developer will find some other reasons why certain architectures suit them. There are also many potential pitfalls that do not exist in other architectures- these will be discussed in another post. Enjoy your microservices!
