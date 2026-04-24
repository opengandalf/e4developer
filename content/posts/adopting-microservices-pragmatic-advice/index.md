---
title: "Adopting Microservices - Pragmatic Advice"
date: 2018-05-25T00:00:00Z
draft: false
description: "Your company wants to adopt microservices. You are either really happy or terrified. A change like this can be great for those wanting to learn and improve…"
categories: ["Architecture", "Microservices"]
cover:
  image: "images/practical.jpg"
  alt: "Adopting Microservices - Pragmatic Advice"
aliases:
  - /adopting-microservices-pragmatic-advice/
  - "/2018/05/25/adopting-microservices-pragmatic-advice/"
ShowToc: true
TocOpen: false
---Your company wants to adopt microservices. You are either really happy or terrified. A change like this can be great for those wanting to learn and improve their systems, but it does not come without its perils. If you want to be successful you will have to be pragmatic…

Undoubtedly you have heard about microservices by now. I have seen many people skeptical about adopting the pattern and its potential value. The good news is- you can be pragmatic about the adoption, taking what works best and at the pace that suit you.

## Why are microservices even possible?

First of all- microservices are only becoming popular now because only now they became practical. In order to get microservices to work well you need a few things:

- Microservices friendly frameworks – like Spring Boot or Javalin (and more)
- Easy deployment – possibly with Docker or other containers
- Easy provisioning – cloud computing plays a role here
- Good monitoring

If these were available earlier, someone would have tried SOA as microservices. Speaking of SOA…

## Service Oriented Architectures – an established idea

If you have been working with enterprise software for a while there is a good chance that you are familiar with the Service Oriented Architecture – SOA.

SOA is an approach to your architecture that is focusing on delivering specialized, decoupled services. Because of the technical limitations, we used to implement SOA on large enterprise servers, using something like enterprise service bus. It was not ideal, but sometimes it worked really well.

With microservices, you can have a similar mentality. You want to focus on delivering services, don’t worry too much about the *“micro”* part. With that approach, you may build something that you are more comfortable with, using much more modern tools and approach.

## Don’t stress about the size

![](images/mini.jpg)

This is the most important advice I can give you. Some people obsess over the *“micro”* part of microservices. Making them too small is often worse than making them slightly larger than necessary.

If you want to be “scientific” about the way you think about responsibilities of your microservices, think of [Bounded Contexts](https://martinfowler.com/bliki/BoundedContext.html). And if in doubt- making a microservice slightly larger than necessary is not the end of the world.

You want to be pragmatic here. If you make them too small, you may be overwhelmed by the intense communication that happens between your services.

## Make it easy for yourself

If you adopt microservices with the idea of getting everything right from the start you are setting yourself an incredibly hard task. I recommend you start with what’s easy. Here are some ideas:

- Move away from Spring to Spring Boot
- If you are not a Spring user, try a microframework like [Javalin](https://javalin.io/) or [Micronaut](http://micronaut.io/)
- If you are considering Choreography- do not go all in from the start. I gave a [talk on that topic]({{< ref "/posts/practical-choreography-with-spring-cloud-presentation" >}}).
- Focus on your DevOps capability- it can be seen as a prerequisite for success with full-scale microservices approach. I write more about it in this [blog post for Scott Logic](https://blog.scottlogic.com/2018/04/30/devops-as-a-key-to-success-with-microservices-approach.html).
- If you don’t want to go all in with DevOps- focus on a solid Continous Integration pipeline, this is what will give you most value.
- For cloud integration- adopt some technologies from the Spring Cloud suite
- Try microservices by separating the easily separable part of your system, or when adding a new, separate, service
- You get the idea!

## Choose what works for you

Beyond making it easy, it is important to recognize that microservices are not a tick-boxing exercise. Due to the complexity of the task, what works for you may differ to what the established “best practices” say.

It is important to be aware of the “best practices” so whenever you chose to do something slightly different it is by choice, not by accident.

I would be especially careful when trying to adopt CQRS/Event Sourcing or other potentially difficult patterns. Don’t feel pressured to adapt Kafka if you have ActiveMQ that works well for you. Reactive microservices with WebFlux may be an overkill etc. I hope you get the idea.

There is no need to remove everything that you have currently and replace it with the flashiest and most hyped solutions. If you have alternatives that work well for you- consider keeping them.

## Avoid common pitfalls

![](images/danger.jpg)

Despite the best intentions, you may fall into one of the common traps of microservices. This is not an easy approach, so you should familiarise yourself with [Common Technical Debt in Microservices]({{< ref "/posts/common-technical-debt-in-microservices" >}}).

For details, you can read the original article, but it summarises as:

- Microservices Configuration – Done Badly
- The existence of a *God Library*
- Poorly implemented security
- Highly coupled services
- Deployment being separated from the developers
- Poorly implemented APIs for Orchestration
- Avoiding Choreography at all cost

There are also potential problems with specific technologies that you may choose. Make sure you do your homework and chose your tech smart. After all, [microservices is the architecture of choices]({{< ref "/posts/microservices-the-architecture-of-choices" >}}).

## Summary

Microservices may be difficult, but you are not obliged to do everything at once. With this new architecture, style came a wealth of technologies and techniques that can help any service oriented architecture. Even if you are not going with microservices, familiarise yourself with this approach, as the amount of innovation and useful tools is staggering!
