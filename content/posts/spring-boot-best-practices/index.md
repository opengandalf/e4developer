---
title: "Spring Boot - Best Practices | E4developer"
date: 2018-08-06T00:00:00Z
draft: false
description: "Spring Boot is the most popular Java framework for developing microservices. In this article, I will share with you the best practices for working with Spring…"
categories: ["Microservices", "Spring Boot"]
cover:
  image: "images/spring-boot-best-practices.png"
  alt: "Spring Boot - Best Practices | E4developer"
aliases:
  - "/2018/08/06/spring-boot-best-practices/"
ShowToc: true
TocOpen: false
---

# Spring Boot – Best Practices

![](images/spring-boot-best-practices.png)

Spring Boot is the most popular Java framework for developing microservices. In this article, I will share with you the best practices for working with Spring Boot that I have gathered by using it in professional development since 2016. I base these on my personal experience and writings of recognized Spring Boot experts.

In this article, I focus on practices specific to Spring Boot (most of the time, also applicable to Spring projects). If you want to learn about the Java best practices, I recommend *“Effective Java”* which I [review in a separate article](https://www.e4developer.com/2018/05/09/effective-java-microservices-require-effective-java/).

The following best practices are listed in no particular order.

## Use Auto-configuration

One of the flagship features of Spring Boot is its use of Auto-configuration. This is the part of Spring Boot that makes your code simply work. It gets activated when a particular *jar* file is detected on the classpath.

The simplest way to make use of it is to rely on the Spring Boot Starters. So, if you want to interact with Redis, you can start by including:

```

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>

```

if you want to work with MongoDB, you have:

```

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>

```

and so on… By relying on these starters, you are relying on a tested and proven configuration that is going to work well together. This helps to avoid the dreaded [Jar Hell (nice dzone.com article linked)](https://dzone.com/articles/what-is-jar-hell).

It is possible to exclude some classes from the Auto-configuration, by using the following annotation property: *@EnableAutoConfiguration(exclude={ClassNotToAutoconfigure.class})*, but you should do it only if absolutely necessary.

Official documentation on Auto-configuration can be found [here](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-auto-configuration.html).

## Use Spring Initializr for starting new Spring Boot projects

This best practice comes from Josh Long (Spring Advocate, [@starbuxman](https://twitter.com/starbuxman)).

Spring Initializr (<https://start.spring.io/>) gives you a dead easy way to start a new Spring Boot project and load it with the dependencies you may need.

Creating your application with the Initializr ensures that you are picking up the tested and approved dependencies that will work well with Spring auto-configuration. You may even discover some new integrations that you were not aware exist.

## Consider creating your own auto-configuration for common organizational concerns

One more from Josh Long (Spring Advocate, [@starbuxman](https://twitter.com/starbuxman))- this one is for power users.

If you are working in an organization that relies heavily on Spring Boot and you have common concerns that need to be solved, you can [create your own auto-configuration](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-developing-auto-configuration.html).

This task is more involved, so you need to consider when the benefits are worth the investment. It is easier to maintain a single auto-configuration than multiple bespoke configurations, all slightly different.

If you are publishing your library to open-source, providing a Spring Boot configuration will greatly ease the adoption for thousands of users.

## Structure your code correctly

While allowing you a lot of freedom, there are some basic rules worth following then laying out your source code.

- Avoid using the default package. Make sure that everything (including your entry point) lives in a well-named package. This way you will avoid surprises related to wiring and component scan.
- Keep your *Application.java*(your entry Class) in the top-level source directory.
- I recommend keeping Controllers and Services together in modules that are oriented around functionality, but this is optional. Some very good developers recommend keeping all Controllers together. Stick to one style!

## Keep your @Controller’s clean and focused

Controllers are supposed to be very thin. You can read about the [Controller pattern explained as part of GRASP here](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)#Controller). You want Controllers to coordinate and delegate, rather than to execute actual business logic. Here are the key practices:

- **Controllers should be stateless**! Controllers **are by default singletons** and giving them any state can cause massive issues.
- Controllers should not execute business logic but rely on delegation.
- Controllers should deal with the HTTP layer of the application. This should not be passed down to Services.
- Controllers should be oriented around a use-case / business-capability.

To go deeper here, would be to start discussing the best practices for designing REST APIs. These are worth learning about regardless if you want to use Spring Boot.

## Build your @Service’s around business capabilities

Services are another core concept in Spring Boot. I find it best to build services around *business capabilities/domains/use-cases*, call it what you want.

Applications with Services called something like *AccountService, UserService, PaymentService*are much easier to deal with than those with *DatabaseService, ValidationService, CalculationService* etc.

You could decide to go with a 1-to-1 mapping between Controllers and Services. That would be ideal. That does not mean, that Services can’t use each other!

## Make your database a detail – abstract it  from the core logic

I used to be unsure of how to best treat database interaction in Spring Boot. After [reading “Clean Architecture”](https://www.e4developer.com/2018/07/14/discovering-clean-architecture-with-uncle-bob/) by Robert C. Martin, it is much clearer to me.

You want your database logic abstracted away from the Service. Ideally, you don’t want a Service to know what database it is talking to. Have some abstractions that encapsulate the persistence for your Objects.

Robert C. Martin argues passionately for making your database a “detail”. That means not coupling your application to a specific database. It used to be very rare that you would ever switch databases. I have noticed that with Spring Boot and modern microservices development- things move much quicker.

## Keep your business logic free of Spring Boot code

With the lessons from the “Clear Architecture” in mind, you should also protect your business logic. It is very tempting to mix all sorts of Spring Boot code there… Don’t do it. If you resist the temptation, you will keep your business logic reusable.

It is common for parts of services to become libraries. These are much easier to create if you don’t have to remove a lot of Spring annotations from your code.

## Favour Constructor Injection

This one comes from Phil Webb (Current Lead of Spring Boot, [@phillip\_webb](https://twitter.com/phillip_webb)).

One way to keep your business logic free from Spring Boot code is to rely on Constructor Injection. Not only is the *@Autowired* annotation optional on constructors, you also get the benefit of being able to easily instantiate your bean without Spring.

## Be familiar with the concurrency model

One of the most popular articles I ever wrote is *[“Introduction to Concurrency in Spring Boot”](https://www.e4developer.com/2018/03/30/introduction-to-concurrency-in-spring-boot/)*. I believe the reason for this is that this area is often misunderstood and ignored. With that, comes problems.

In Spring Boot- Controllers and Services are by default Singletons. That introduces possible concurrency problems if you are not careful. You are also usually dealing with a limited thread-pool. Familiarise yourself with these concepts.

If you are using the new WebFlux style of Spring Boot applications, I have explained how that works in [“Spring’s WebFlux / Reactor Parallelism and Backpressure”](https://www.e4developer.com/2018/04/28/springs-webflux-reactor-parallelism-and-backpressure/).

## Externalise and mature your configuration management

This point goes beyond Spring Boot, although it is a common problem that happens when people start creating multiple similar services…

You can manually deal with configuring a Spring application. If you are dealing with dozens of Spring Boot applications you need to mature your configuration management.

I recommend two main approaches:

- Use a configuration server, something like [Spring Cloud Config](https://cloud.spring.io/spring-cloud-config/)
- Store all your configuration in environment variables (that could be provisioned based on git repository)

Either of these options (the second one more) requires you to dab a bit in the DevOps area, but this is to be expected in the world of microservices.

## Provide global exception handling

You really need a consistent way of dealing with exceptions. Spring Boot provides two main ways of doing that:

1. You should use *HandlerExceptionResolver* for defining your global exception handling strategy.
2. You can annotate your Controllers with *@ExceptionHandler*. This can come useful if you want to be specific in certain cases.

This is pretty much the same as in Spring and the Baeldung has a detailed article on [Error Handling for REST with Spring](https://www.baeldung.com/exception-handling-for-rest-with-spring) that is well worth reading.

## Use a logging framework

You are probably aware of that, but you should be using a Logger for logging rather than doing it manually with *System.out.println()*. This is easily done in Spring Boot with pretty much no configuration. Just get your logger instance for the class:

```

Logger logger = LoggerFactory.getLogger(MyClass.class);

```

This is important, as it will let you set different logging levels as necessary.

## Test your code

This is not Spring Boot specific, but it warrants a reminder! Test your code. If you are not writing tests, then you are writing legacy code from the get-go.

If someone else comes to your codebase, very quickly it may become dangerous to change anything. This can be even riskier when you have multiple services depending on each other.

Since there are Spring Boot best practices, you should consider using [Spring Cloud Contract](https://cloud.spring.io/spring-cloud-contract/) for your Consumer Driven Contracts. It will make your integration with other services much easier to work with.

## Use testing slices to make your testing easier and more focused

This one comes from Madhura Bhave (Spring Developer, [@madhurabhave23](https://twitter.com/madhurabhave23)).

Testing code with Spring Boot can be tricky- you need to initialize your data layer, wire numerous services, mock things… It actually does not have to be that hard! The answer is- use testing slices.

With testing slices, you can wire-up only parts of your applications as necessary. That may save you a lot of time and ensure that your tests are not coupled to things that you are not using. There is a blog post titled [Custom test slice with Spring Boot 1.4](https://spring.io/blog/2016/08/30/custom-test-slice-with-spring-boot-1-4) from spring.io that explains that technique.

## Summary

Thanks to Spring Boot, writing Spring based microservices became easier than ever. I hope that with these best practices, your implementation journey will not only be quick but also more robust and successful in the long run. Good luck!

## Thank you!

I would like to thank the following people for helping me make this article better:

- **Marcin Grzejszczak** ([@MGrzejszczak](https://twitter.com/MGrzejszczak)) – for retweeting my blog post and getting the attention of the Spring team
- **Josh Long** ([@starbuxman](https://twitter.com/starbuxman)) – for the feedback and additional best practices
- **Phil Webb** ( [@phillip\_webb](https://twitter.com/phillip_webb)) – for the feedback and additional best practices
- **Madhura Bhave** ([@madhurabhave23](https://twitter.com/madhurabhave23)) – for the feedback and additional best practices

Thanks a lot for that guys! Spring Boot has a really fantastic community!
