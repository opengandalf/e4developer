---
title: "Microservices - the Architecture of Choices"
date: 2018-04-18T00:00:00Z
draft: false
description: "One thing that differentiates microservices architecture from more traditional, monolithic development styles is the number of choices that have to be made."
categories: ["Architecture", "Microservices"]
cover:
  image: "images/doors-choices.jpg"
  alt: "Microservices - the Architecture of Choices"
aliases:
  - "/2018/04/18/microservices-the-architecture-of-choices/"
ShowToc: true
TocOpen: false
---![](images/doors-choices.jpg)

One thing that differentiates microservices architecture from more traditional, monolithic development styles is the number of choices that have to be made. Which frameworks (if any) are you going to use? How to deal with configuration, orchestration or choreography etc. It may feel overwhelming. In this article, I will give you some advice on how to approach this *Architecture of Choices* with confidence and success.

I enjoy having multiple choices and making decisions about the architecture. For some people and projects, this is a scary thing. It does not have to be. With the advice presented here, you can take back control and feel positive about the choices that you get to make.

### Knowing what is possible

One thing that scares people away is the notion that they have to know everything, every framework out here. **You don’t have to know every framework out there, but it helps to know about them.**

What I mean by that, is that you don’t have to know how to use Spring, Microprofile, Vert.X, Dropwizard and more… But it helps if you know about them. What are they, what are the pros and cons?

Whenever you are facing a choice of a messaging technology, framework, authentication solution- **do not try to learn everything, but rather try to learn about everything**. What is out there and what it can be used for.

Word of caution- if you are considering a technology, make sure that you are choosing something at least moderately popular and with some future. You can do a quick google search to see if people are blogging about it, check the number of stars on their GitHub repository etc. Try to avoid very niche projects unless you absolutely know what you are doing.

![](images/landscape.jpeg)

### Being open to new ideas

With the idea of learning what is possible, it is crucial to keep an open mind. We developers love to get religious about technology. I don’t think it is a road that gets us far.

I have written previously about the [importance of being humble as a software developer]({{< ref "/posts/the-importance-of-being-humble-as-a-software-developer" >}}). In short- on more than one occasion I dismissed a better solution because I just assumed that I know better. I try to be more open-minded these days.

With microservices still being relatively new, people are constantly challenging the status quo and bringing new ideas to the table. Listen to them, you may find a better solution to your problem. Use your choices.

### Avoiding common pitfalls

There are many choices how to do something right- there are multiple ways to success. **There are also sure ways that will lead you and your projects towards failure**.

Coming from other architecture styles, we are prone to committing similar mistakes. I have written a list of [common technical debt in microservices]({{< ref "/posts/common-technical-debt-in-microservices" >}}) based on my previous experience (one of the benefits of being a consultant!).

Whenever working on a distinct part of your architecture, make sure you familiarise yourself with common pitfalls and best practices. There is often more agreement here than it is with specific choices of technology.

### Architecture and leadership – shared choices

One of the ideas behind microservices is enabling software teams to own the service. That means owning the implementation, testing and often providing support for the service once in production. The DevOps culture in action.

That does not mean, that an overall architecture is not required, or that it is only the team’s internal interest. There is enormous benefit from having a thought-off integration between the services. Knowing how the services are supposed to cooperate.

If one service uses Kafka, another uses RabbitMQ and the third one is attempting to build something on top of Spring Cloud Data Flow- the chaos will ensue. **Some of the choices should be shared choices**.

This is the place for architects and technical leads to step in (even if they do not have those titles- we know who you are!). **If you think that the decision you are about to make will impact numerous teams and services- make it a shared choice**.

I see architects as people predominantly occupied with providing this architectural advice and working it out with the teams. The role of a technical lead is to give visibility to concerns that might not be visible from the outside of the team.

![](images/fleet.jpg)

### The Architecture of choices… and second chances

One thing that should make you calmer about making all these choices is that you also get second chances. I have not seen many *troubled* monoliths successfully transform into great projects… I have seen that with microservices.

I have seen people make major mistakes about how to handle configurations, change their mind about security and split one service into many others and live to tell the tale. With microservices, the scope is always limited and you do get second chances.

With a knowledge that no decision is forever, you can choose something that works now, and in the worst case- replace it later. It really is a game changer when it comes to risk-taking.

**Keep track of your technical debt. With microservices, you will have a fighting chance addressing it.**

### Microservices Blueprints

You don’t have to make all the choices. After all, this architecture style is not completely new. You can model your architecture based on successful implementations and microservices blueprints.

I am a big fan of the Spring ecosystem which provides such blueprint in the form of the Spring Cloud offering. I have reviewed [Spring Cloud in the context of a blueprint on this blog]({{< ref "/posts/spring-cloud-blueprint-for-successful-microservices" >}}).

If you are building a system based on a framework, check what others did, plenty of companies, including the *microservices famous* Netflix are quite open about their journey with microservices. You can model your choices around other’s successes.

### Summary

Microservices architecture truly is the *Architecture of Choices*. Is that bad? In my opinion- no. It is challenging if you are not used to it. With these challenges come opportunities.

I hope that by reading the advice given here, you will face these choices strategically and with more confidence.
