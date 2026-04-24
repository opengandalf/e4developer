---
title: "What you need to know about Spring Boot 2.0 (RC1)"
date: 2018-01-31T00:00:00Z
draft: false
description: "Spring Boot 2.0 release brings a variety of features. Learn about the changes to the Actuator module, Micrometer introduction, how to migrate and more!"
categories: ["Microservices", "Spring Boot", "Spring Cloud"]
cover:
  image: "images/spring-boot-2-1024x277.jpg"
  alt: "What you need to know about Spring Boot 2.0 (RC1)"
aliases:
  - "/2018/01/31/what-you-need-to-know-about-spring-boot-2-0-rc1/"
ShowToc: true
TocOpen: false
---With Spring Boot 2.0 release just around the corner (at the time of writing we have RC1) it is important to see what changes it brings. Even if you are not planning to migrate shortly, it is good to see what is new in this biggest Spring Boot release since the 1.0 version. In this blog post I won’t go through every detail, but cover the most important things.![](images/spring-boot-2-1024x277.jpg)

##### No more support for Java 7 and below

Java 8 becomes a minimum requirement with Spring Boot. The [release notes for the first milestone](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.0.0-M1-Release-Notes) do not elaborate on that point further. Most developers will probably agree that this is for the better and if somehow you are still below Java 8 and planning to use the latest Spring Boot… Now you have a good business reason to upgrade.

##### Multiple changes to property names and packages – this comes with support

Spring Boot team decided to extensively refactor their package structures and properties. While the package name changes will require some refactoring to get your code working again, it may be a bit difficult to see how to translate all these properties. Don’t worry- Spring Boot has you covered with the *spring-boot-properties-migrator* module. This will basically print diagnostic information on the startup (to help you fix the config) and make the old config work temporarily. All you need to do to make use of it is to include the following dependency in your pom file:

```

<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-properties-migrator</artifactId>
</dependency>

```

This is a must if you are actually migrating to Spring Boot 2.0 from a lower version.

##### Spring Boot Gradle plugin mostly rewritten

This is only relevant to you if you were making use of this plugin before (or if you are a Gradle fan looking to start working with Spring Boot). The changes here are far too extensive to cover in a blog post, so I will refer you to  [the latest Snapshot of the Gradle plugin guide in pdf](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/gradle-plugin/reference/pdf/spring-boot-gradle-plugin-reference.pdf).

##### Multiple changes to the Security module

The main goal here was to simplify the default security configuration. From the version 2.0 as soon as you put Spring Security on the class path, the default security configuration will kick in. This time the Spring team decided for the most secure option- everything will be secured by default. If you added Actuator to your project, it will be secured as well. You may be affect by these changes if you use any of the following properties:

- security.basic.authorize-mode
- security.basic.enabled
- security.basic.path
- security.basic.realm
- security.enable-csrf
- security.headers.cache
- security.headers.content-security-policy
- security.headers.content-security-policy-mode
- security.headers.content-type
- security.headers.frame
- security.headers.hsts
- security.headers.xss
- security.ignored
- security.require-ssl
- security.sessions

Good news here is that there are couple great blog post on the subject written by Spring authors themselves: [Security changes in Spring Boot 2.0](https://spring.io/blog/2017/09/15/security-changes-in-spring-boot-2-0-m4) and [Spring Boot Security 2.0](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-Security-2.0). Check them out if you are using these modules.

##### Large changes to Spring Boot Actuator

Spring Boot Actuator is probably one of the most popular Spring Boot modules. The fact that it is getting some major overhaul should be of interest to you! What changed about Actuator? Mostly everything! You can expect changes with programming model, configuration, security and response format of some endpoints.

If you are implementing your custom Actuator endpoints, you should read [Migrating a custom Actuator endpoint to Spring Boot 2](https://github.com/spring-projects/spring-boot/wiki/Migrating-a-custom-Actuator-endpoint-to-Spring-Boot-2) written by the Spring Boot maintainers. If you are generally interested into how the new Actuator works- the [new API Documentation](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/actuator-api/html/) is already online.

It seems that the main reason behind changes to the Actuator module was enabling its use outside of Spring Boot and Spring MVC. This technology agnostic approach will hopefully result in even more interest and support potentially from the outside of the Spring community.

##### Spring Boot own metrics replaced with Micrometer support.

You might have not heard of Micrometer ([official website](https://micrometer.io/)) before. The best way to explain what it is, would be to borrow from their own elevator pitch welcoming you to their website:

> Micrometer provides a simple facade over the instrumentation clients for the most popular monitoring systems, allowing you to instrument your JVM-based application code without vendor lock-in. Think SLF4J, but for metrics.

I think this describes Micrometer perfectly! If you are using Actuator, then Micrometer would be already there. If you are planning on using Micrometer (and I think you definitely should!) there is a very good guide about integrating with Spring Boot 2 already [available on the official website](http://micrometer.io/docs/ref/spring/2.0).

![](images/micrometer.jpg)

##### Support for the remote debugging over HTTP is removed

To be honest this one worries me a bit. I always found it very useful to have that option available. I am sure that workarounds can be found (and with microservices being really small this is not as crucial as with monoliths). This was removed due to the issues with JDK 9, so I have some hope that it may be brought back.

##### Upgrading libraries and Tomcat version across the board

The key requirements for minimum versions of different libraries and tools are as follows:

- Tomcat – 8.5
- Hibernate – 5.2 (with some more minor changes to JPA)
- Gradle – 4.2

There are also myriad of smaller libraries upgrades that are present in most Spring Boot releases, so we won’t be going into details here.

### Summary

Spring Boot 2.0 brings plenty to the table. The nature of the changes it more evolutionary than revolutionary. This is still the Spring Boot that so many Java developers (and other JVM citizens) grew to love. Changes that brought Micrometer and modernized Actuator are aimed at opening up the ecosystem and making use of the best solutions available anywhere (not only in the Spring world). With packages and properties renamed and re-design we gain more maturity and even better foundation on which we can build our Microservices. I am looking forward to the future Spring Boot release and progress that they will bring!
