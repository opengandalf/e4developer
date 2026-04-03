---
title: "Should you use Spring Boot in your project? | E4developer"
date: 2018-09-24T00:00:00Z
draft: false
description: "Spring Boot is enjoying, a seemingly never-ending growth of popularity. While only released in 2014, it has managed to overtake the Java serverside in less than…"
categories: ["Architecture", "Microservices", "Spring Boot"]
cover:
  image: "images/should-you-use-spring-boot.jpg"
  alt: "Should you use Spring Boot in your project? | E4developer"
aliases:
  - "/2018/09/24/should-you-use-spring-boot-in-your-project/"
ShowToc: true
TocOpen: false
---

# Should you use Spring Boot in your project?

![](images/should-you-use-spring-boot.jpg)

Spring Boot is enjoying, a seemingly never-ending growth of popularity. While only released in 2014, it has managed to overtake the Java serverside in less than five years. When starting a new project, a sensible question to ask is- *“should I use a Spring Boot?”*. In this article, I will help you answer this question!

Every project is different, but we can use some characteristics with which we can compare them. Based on these characteristics I will advise you if Spring Boot is generally a good idea.

## Are you working on Microservices Architecture?

One of the main selling points of Spring Boot is its use for microservices architectures. I will agree here- I have used Spring Boot to implement the microservices architecture in production for large enterprise and it works well.

What I would point out though, is that many companies keen on using Spring Boot, sort of miss the trick by not looking at Spring Cloud. I previously wrote about [Spring Cloud as a Blueprint for Microservices Architecture](https://www.e4developer.com/2018/01/22/spring-cloud-blueprint-for-successful-microservices/) – I really think this is a good way to think about it. If you are already thinking about using Spring Boot and implementing microservices – check out Spring Cloud and what it has to offer.

Is Spring Boot a good choice for microservices architecture? **Definitely yes!**

## Is your project using Kotlin?

Kotlin seems to be getting very popular, very quickly. Since about mid-2017 there seem to be a major interest in the language and developers are keen to use it on the server side.

If you are a Kotlin enthusiast considering Spring Boot, I have some great news for you. Spring Boot 2.0 is built on top of Spring 5 which brings much better support for Kotlin. You can read about it in the article published on the official Spring website- [Introducing Kotlin support in Spring Framework 5.0](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0).

Is Spring Boot a good choice when working with Kotlin? **Definitely yes!**

## Are you going to use Serverless Architecture?

![](images/lambda-function-riff.jpg)

Another trend that is gaining in popularity is the Serverless Architecture. With AWS Lambda and Azure Functions, it is getting easier and easier at running your system… *“without servers”*. I put that term in quotes as there seem to be some arguments about what that means. I let you be the judge.

With some gymnastics, you can run your Spring Boot serverless, but should you? I would argue that this is not the best use of either Spring Boot or Serverless Architectures.

What should you use instead? If you like what the guys behind Spring are doing, you should check out [Project Riff](https://projectriff.io/). It is still in its early stages, but rather interesting.

On an off-chance for sounding heretical on my own blog- maybe even consider another language? Java works serverless, but I am not convinced that using the JVM is the best approach. If you disagree, let me know in the comments.

So… Is Spring Boot a good choice for Serverless Architectures? **I don’t think so.**

## Are your developers new to Spring?

Spring is a large ecosystem and it can feel daunting having to learn it from scratch. If your team has never used it before, you may be wondering if it is the right choice?

I had a pleasure working on Spring Boot project with a number of developers who had no experience of Spring at all. I found that Spring Boot has a rather nice learning curve. You can get the basics very quickly and autoconfiguration guides you as you learn the framework.

I actually found Spring Boot to be one of the most beginner friendly serverside frameworks out there. Perhaps this is one of the reasons for its wild popularity?

If you looking for a good place to start learning Spring Boot I can recommend [Pluralsight](https://www.e4developer.com/pluralsight) for its courses (I wrote an [article about learning with Pluralsight](https://www.e4developer.com/2018/08/12/learning-java-spring-microservices-with-pluralsight/) and I am an affiliate) and the amazing collection of [official Spring guides](https://spring.io/guides).

Is Spring Boot a viable choice for teams with no Spring experience? **Definitely yes!**

## Is your codebase expected to be very Simple?

![](images/javalin-spark.jpg)

What if you don’t think you need all the features that Spring Boot offers. You are maybe not interested in the dependency injection and the wonders of autoconfiguration. You just want to write some simple REST APIs.

Here you have a choice- Spring Boot is still great for basic REST APIs, but you could give a chance to microframeworks like [Javalin](https://javalin.io/) and [Spark Java](http://sparkjava.com/).

I have elaborated much more on that point in [The Quest for Simplicity in Java Microservices](https://www.e4developer.com/2018/07/08/the-quest-for-simplicity-in-java-microservices/).

Is Spring Boot viable choice for simple REST APIs? **Definitely yes, but also check out microframeworks!**

## Summary

![](images/spring-boot.png)

It seems that Spring Boot is a great choice for most modern serverside development. Is that really a surprise? Spring Boot is incredibly popular for a reason!

Before you pick Spring Boot though, make sure that you are not falling for the *“If all you have is a hammer, everything looks like a nail”* trap and use the right tool for the job. Especially when going serverless or trying to write something [“simple”](https://www.e4developer.com/2018/07/08/the-quest-for-simplicity-in-java-microservices/).
