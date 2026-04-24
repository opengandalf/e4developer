---
title: "Effective Java Microservices require Effective Java"
date: 2018-05-09T00:00:00Z
draft: false
description: "Writing good software requires using the right tools. Choosing the right frameworks, libraries and designing smart systems. With all that to learn and worry…"
categories: ["Books", "Career", "Java", "Microservices"]
cover:
  image: "images/effective-java.jpg"
  alt: "Effective Java Microservices require Effective Java"
aliases:
  - "/2018/05/09/effective-java-microservices-require-effective-java/"
  - "/effective-java-microservices-require-effective-java/"
ShowToc: true
TocOpen: false
---Writing good software requires using the right tools. Choosing the right frameworks, libraries and designing smart systems. With all that to learn and worry about, it is easy to forget about another very important thing: using your programming language wisely. In this article, I want to introduce you to *“Effective Java”*by Joshua Bloch. 

## *Effective Java*– back to “basics”

With the JVM ecosystem moving faster than ever, it is easy for us to forget that writing good software is more than using frameworks correctly.

There are some key things we should always consider when writing code. These things are largely independent of the framework we use. I always like to ask these questions when performing code review:

- **Is the code readable and easy to understand?**
- **Is the code maintainable?**
- **Is the code correct?**
- **Does it follow agreed best practices?**

If you are an experienced Java developer, you may have developed an instinct and knowledge that helps you answer these questions. But how do you get better at it?

Imagine that you could have one of the best Java developers in the world explain to you how they answer these questions? Joshua Bloch, one of the main authors of Java Collections Framework certainly qualifies as world-class. He also compiled a list of 90 *Items*worth considering when writing Java. Having him explain to you how to write effective Java is the premise of this book.

Once you read through these rules and understand the reasoning behind them, you will really start to feel like you are becoming a native speaker of the Java language.

## So what about microservices, why is it related?

I have spent the last two years of my professional life working with Spring Boot and Grails based microservices. Both are great technologies (I prefer Spring Boot if you are asking), that enable you to deliver value rapidly… Neither of these technologies excuses you from writing bad code!

In my experience, microservices architectures are quite difficult. There are a lot of moving parts and the integration between different services can prove challenging. **That only emphasizes the need to write absolutely rock-solid code in your services**.

With the complexities of the architecture, you want the services to be simple. In order for them to be simple, you not only have to divide your domain model correctly, you also need to write clean maintainable code.

The speed that we get from modern microservices frameworks, should not stop us from writing quality code. Chances are that the service will be written quickly, but it may be maintained for years. Developers spend much more time reading code than writing new code. **Let’s do everyone a favour and write Java Microservices using the native speaker version of Java.**

Java is not a new language, we know what good Java looks like. With the update of *“Effective Java”* to cover Java 9, you get an expert advice on how to write good modern Java.

## What the book covers

What exactly the book covers? Given that you can look up the index of the book on Amazon, I feel that I can share it here as well. You get 12 information-packed sections:

1. **Introduction –** well, this one is not so information packed!
2. **Creating and Destroying Objects –** basic and crucial to pretty much any Java application.
3. **Methods Common to All Objects –** ABC ofdealing with Java Objects.
4. **Classes and Interfaces –**good overview of OOP practices in Java.
5. **Generics –**a Deeper look into generics and polymorphism.
6. **Enums and Annotations –**explanation of the often misunderstood and underused features of the language.
7. **Lambdas and Streams –**how to deal with the new feature that we got with Java 8.
8. **Methods –**good rules for working with methods explained.
9. **General Programming –**mix of general programming recommendations.
10. **Exceptions –**a guide to dealing with the ever confusing Java Exception framework.
11. **Concurrency –**solid intro to Java Concurrency and best practices.
12. **Serialization –**serializing Java Objects.

As you can see, the book subject domain is very broad. It stands out from many others, as it manages to stay deep and insightful despite that. This is achieved by picking specific *Items* and examining them in-depth. Take for example:

*44. Favor the use of standard functional interfaces.* – Where we get a deep look at functional interfaces in Java and best practices around their use. One of the new and interesting additions from Java 8, that I don’t think is widely enough used or understood.

You get 89 other *Items* that each gets a few pages of in-depth explanations and discussion.

## Summary

*“Effective Java”*by Joshua Bloch is one of the best books on Java that I have ever read. If you are writing Java in any context, I can’t recommend that book enough to you.

While always chasing the latest and most exciting new frameworks and architectures, sometimes it is good to slow down. It is good to look back at basics and make sure that we stand on a solid foundation. *“Effective Java”*can give you that foundation.
