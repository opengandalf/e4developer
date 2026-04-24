---
title: "Common Technical Debt in Microservices"
date: 2018-02-11T00:00:00Z
draft: false
description: "Common causes of technical debt in Microservices together with practical solutions. See how bad configuration, coupled services and more can affect you."
categories: ["Microservices"]
cover:
  image: "images/old-machine.jpg"
  alt: "Common Technical Debt in Microservices"
aliases:
  - /common-technical-debt-in-microservices/
  - "/2018/02/11/common-technical-debt-in-microservices/"
ShowToc: true
TocOpen: false
---Working for a consultancy I have the opportunity to talk to large number of software developers across multiple different projects. That gives me an opportunity to see what works and what common problems different organizations are facing. In this article I will show the most common mistakes in microservices that cause technical debt. I suggest what you could be doing instead.

Microservices development can be difficult. Given how new the pattern is, it is no surprise that mistakes are made. The great thing about mistakes is that they are also learning opportunities. It is great when you can learn from your mistakes, but it is even better when you can learn from the mistakes of others!

Before going into specific examples, there are two important things to point out about technical debt:

**Sometimes it is desired to have some technical debt**. If we are building a proof of concept- we may not want to go with production grade infrastructure that we end up deleting. When we are racing to finish some feature that will give our product a killer market advantage- another case when the technical debt can be accepted. High performing teams can use technical debt to their advantage. It is important to realize when you are taking on technical debt. The problem is when it is done blindly and the team only realizes when it is too late. This, the unexpected technical debt, is usually the worst and the most dangerous kind. Either kind (the planned and unplanned) should be recorded by the team so that if there is time for some tech debt work- it can be quickly identified and worked on.

**Technical debt is not just like financial debt- there is more risk involved**. When dealing with financial debt, there are predictable payments involved. Most stock market listed companies want to take on some debt so that they can grow faster- this is called leveraging the business. When we deal with technical debt, the *payments*, so to speak- can vary dramatically. Something may require a few minutes to fix, but potentially make the system fail in production. That risk factor being decoupled from the size of the debt is something quite a bit different than with financial debt. When looking at technical debt, and especially when discussing it with your more business minded colleagues- make sure to highlight and focus on the risks! Work required is important, but risks are the key to prioritization.

With that out of the way, what are the most common causes of technical debt that appear in microservices?

# Leading causes of technical debt in microservices

### Microservices Configuration – Done Badly

This seems to be by far the most common problem! Many enterprises are not really used to the modern way of dealing with configuration files.

**Problem:** Common way to get configuration management wrong is to put specific configuration files for each environment into every microservice. As the number of microservices and environments grows, this starts to grow in the order O(N^2). Before you know it, you need to update 30 properties across 10 microservices (and Git repos) changing 3 configuration files in each. This is not sustainable, causes multiple hours wasted and frustrating bugs.

**Solution**: First, you don’t need environment specific configuration files. This can be handled by Configuration Servers (for example [Spring Cloud Config](https://cloud.spring.io/spring-cloud-config/)) and using environment variables. You could make use of Kubernetes Secrets, Environment variables, anything really that stops you from having to manually include service endpoints, database configurations and other similar things in every microservice for each environment. Service discovery tools such as [Eureka](https://cloud.spring.io/spring-cloud-netflix/) or [Consul](https://www.consul.io/) can help to make it even better.

### Existence of a *God Library*

Developers like libraries. Why wouldn’t we? I don’t know many people who enjoy re-typing or copy-pasting code all over the place. We should put shared code into librarie**s**. The plural form here is the clue…

**Problem:**A library gets created- something called along the lines: *microservices-utilities* or *project-standard-library* that before you know it includes all the potentially shared code in the project. Security, dealing with message queues, some ad hoc business domain logic and more ends up bundled in one library. Now, all your microservices depend on huge number of often unnecessary things and may be impacted in the most unusual ways. Sometimes upgrades to library versions will affect services that should not be affected.

**Solution:**It is simple to deal with this problem if you can see it early enough. Don’t create the *God Library!*Instead use multiple different libraries that have well defined boundaries. This is a common technique in software development and it can be compared to [Interface Segregation](https://en.wikipedia.org/wiki/Interface_segregation_principle) from the [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)) principles. Despite targeting Object Oriented Development, they translate quite well to the world of microservices.

### Poorly implemented security

Securing microservices is more difficult than securing a monolithic application. That does not mean that it is less important!

**Problem:**Securing microservices can be inherently difficult. There are more services that often manipulate with data and can be called in number of ways. With more vectors of attack and more work to do to implement security, we naturally see less of it… This is one of these technical debts that I discussed early- the very risky kind. Some may say technical debt, others may say non-functional requirement. The bottom line is- the risk is huge and so are the vulnerabilities that we often see.

**Solution:**Take security seriously. Think of it from the start. Do not try to build your own security. If you are dealing with Spring Cloud application, get familiar with [Spring Cloud Security](https://cloud.spring.io/spring-cloud-security/) and no matter what you are dealing with, get familiar with [OAuth2](https://oauth.net/2/) and [Open Web Application Security Project (OWASP)](https://www.owasp.org/index.php/Main_Page).

### Highly coupled services

We are often seeing cases where two services, despite being separate, seem to be completely dependent on each other.

**Problem:**When two microservices closely depend on each other, the benefits from loosely coupled services are lost. This often makes the code difficult to write and follow (as the business logic spans the two services) as well as compromises the performance. The problem often gets worse with time rather than improves.

**Solution:**If two microservices closely depend on each other it could be a sign that these should really be a single service. Sometimes the decision what to split into multiple services and what to keep together is done a bit arbitrarily. If the decision does not make sense from the domain perspective, it will be nearly impossible to keep these services loosely coupled. Microservices should be as small as it is practical, no smaller for the sake of their size!

### Deployment is separated from the developers

When talking about the *technical debt* and its causes it is useful to look beyond the process of writing code. How the team interacts with the rest of organisation is also very important. It can make work great or cause countless issues.

**Problem:**Some companies that did not fully adopt the devops mindset do whatever they can do separate the developers from the deployment and the operational aspects of the solution. This often results in misunderstanding, mistakes in configuration and both groups of people spending a lot of time on what other group will solve quickly.

**Solution:**Do everything you can to get the operations and development as close as possible. Sitting closely (co-location, from the business dictionary), having good communication tools (I recommend Slack) and getting people feel that they are part of the same team can help. There is a great book written on the topic: [Devops Handbook](http://itrevolution.com/devops-handbook), that I really recommend if you want to know more.

### Poorly implemented APIs for Orchestration

Orchestration is the most popular method of integrating microservices. There is nothing wrong with making REST calls using JSON seams easy and natural. The technical part of it is usually not the problem- the APIs that are being built are.

**Problem:**Microservices APIs are often created in a chaotic fashion. When implementing a new feature, developer takes required services and adds APIs as she sees fit. This can work, but without any standards agreed upfront or general API design, it often leads to a fragmented API that constantly changes.

**Solution:**Having a stable, well crafted API makes working with Microservices easier. Often the only thing necessary is agreeing some rules about what sort of things should be returned and how methods should be named. It is tricky to recommend a one-size fits all approach here. Your team needs to decide what works best for your project and start following these agreed rules. One thing I found quite useful is to share [Postman](https://www.getpostman.com/) configurations that make it easy to discover and try APIs.

### Avoiding Choreography at all cost

As mentioned above- orchestration is the most popular method of integrating microservices. Orchestration is great, but it is not always the best approach…

**Problem:**Some design problems are solved much easier with messaging than direct calls. If you are having long running business transactions (spanning minutes, hours, days) managing them with databases and REST calls can be much more cumbersome than doing the same with message queues.

**Solution:**Introduce a messaging solution to your microservices architecture. It should be a tool that your team has at their disposal. Not sure where to start? Have a look at RabbitMQ. I also have a [choreography category](http://e4developer.com/category/choreography/) on this blog that may interest you.

# What can we do to get better?

These are some of the most popular causes of technical debt in microservices that I have encountered. These are not all the problems, but if you manage to eliminate all of them, you are definitely above average with your microservices oriented system. This is a constantly evolving space. The worst thing you could do is to stop learning. If your team chose the path of microservices, then you are on the path of learning. Read articles, experiment and enjoy the journey!
