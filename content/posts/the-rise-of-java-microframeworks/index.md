---
title: "The rise of Java Microframeworks"
date: 2018-06-02T00:00:00Z
draft: false
description: "Together with the growing popularity of microservices and light-weight REST API, we are witnessing another trend in Java: the rise of Java Microframeworks."
categories: ["Architecture", "Java", "Microservices"]
cover:
  image: "images/microframeworks.png"
  alt: "The rise of Java Microframeworks"
aliases:
  - /the-rise-of-java-microframeworks/
  - "/2018/06/02/the-rise-of-java-microframeworks/"
ShowToc: true
TocOpen: false
---Together with the growing popularity of microservices and light-weight REST API, we are witnessing another trend in Java: the rise of Java Microframeworks. Javalin, Micronaut, Spark and many more make building REST APIs a breeze. In this article, I look at this exciting space and share my opinions on their use.

## What is a microframework?

Microframework is a minimalistic web application framework. What usually differs it from more traditional, large applications framework is:

- Focus on simplicity and speed of development
- Usually much smaller codebase
- Lack of some advanced features, such as templating engines, advanced security features etc.

It is not a scientific definition and some frameworks ([Vert.x](https://vertx.io/) for example) sit at the boundary of the two- on one hand, it is lightweight and much smaller than let’s say Spring, but on the other, it is pretty well featured and non-trivial.

It is worth adding that Java did not invent microframeworks. One of the earlier examples is [Sinatra](http://sinatrarb.com/) from Ruby (2007) which inspired quite a few Java microframeworks. I am sure some of the readers will be familiar with even earlier examples- if you are, let me know if the comments!

## Why are microframeworks growing in popularity?

First of all- microframeworks are not yet mainstream. That may soon change especially with the rapid growth of interest in the Serverless Architectures. Serverless really benefits from small and lightweight deployments- if you want to use Java in that context, microframeworks seem like a good choice.

Another big driver for their popularity is the increasing adoption of containers (Docker), containers management systems (Kubernetes) and patterns such as API Gateway. Suddenly, the services do not need to deal with as many problems as they used to.

All that would not matter much if the microframeworks themselves were not easy to work with. The new projects are amazing. I am a huge proponent of Spring Boot in the enterprise, but I can’t deny the elegance of [Javalin](https://javalin.io/). Unbelievable what today’s microframework creators can accomplish in just a few thousands lines of code!

## Tour of microframeworks

Enough talking, let’s look at some of my favorite projects and see how easy they are to work with.

### Javalin

![](images/javalin-logo.png)

> A simple web framework for Java and Kotlin

This was my first encounter with a *“modern”* Java microframework. Javalin is written in Kotlin and has support for both Java and Kotlin. If you want to write a nice REST API, it is a pleasure with Javalin.

Javalin is being actively developed with new versions released every few weeks.

Javalin *Hello World*:

```

import io.javalin.Javalin;

public class HelloWorld {
    public static void main(String[] args) {
        Javalin app = Javalin.start(7000);
        app.get("/", ctx -> ctx.result("Hello World"));
    }
}

```

[Javalin Offical Website](https://javalin.io/)

### Spark Java

![](images/spark.jpg)

> Spark – A micro framework for creating web applications in Kotlin and Java 8 with minimal effort

One of the earlier Java take on microframeworks dating back to 2011. Spark is very small, focused and probably the most commonly used from the frameworks mentioned here.

Spark is being actively developed with bug fixes and maintenance released every few months. New features are added less frequently.

Spark *Hello World*:

```

import static spark.Spark.*;

public class HelloWorld {
    public static void main(String[] args) {
        get("/hello", (req, res) -> "Hello World");
    }
}

```

[Spark Official Website](http://sparkjava.com/)

### Micronaut

![](images/micronaut.png)

> A modern, JVM-based, full-stack framework for building modular, easily testable microservice applications.

With Micronaut, we are getting quite close to the barrier what is considered a microframework and what is not. The framework is very simple, but it packs a bit more than most of the competition. I think of it as a somewhat extremely slimmed down version of Spring Boot.

What is great about Micronaut is their focus on the cloud. Working on AWS and making it easy to write serverless applications is high on their priority list.

The first milestone of 1.0.0 version was only released on May 30th, 2018 so we are in the very early days here. I think Micronaut has a serious chance of being the next big thing, so keep an eye on this one!

Micronaut *Hello World*:

```

import io.micronaut.runtime.Micronaut;

public class Application {

    public static void main(String[] args) {
        Micronaut.run(Application.class);
    }
}

import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;

@Controller("/hello") 
public class HelloController {
    @Get("/") 
    public String index() {
        return "Hello World"; 
    }
}

```

[Micronaut Official Website](http://micronaut.io/)

### Ktor

![](images/ktor.png)

> Easy to use, fun and asynchronous.

Not quite a Java, but rather a Kotlin microframework. Ktor is sponsored and developed by JetBrains- creators of Kotlin and strives at making development easy and fun. I did not have a chance to test it yet but based on the popularity among Kotlin enthusiasts and the JetBrains support, it is worth mentioning it here.

Ktor did not yet release 1.0.0 version, but it should be sometime this year.

Ktor *Hello World*:

```

import io.ktor.application.*
import io.ktor.http.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main(args: Array<String>) {
    val server = embeddedServer(Netty, port = 8080) {
        routing {
            get("/") {
                call.respondText("Hello World!", ContentType.Text.Plain)
            }
            get("/demo") {
                call.respondText("HELLO WORLD!")
            }
        }
    }
    server.start(wait = true)
}

```

[Ktor Official Website](http://ktor.io/)

### Other notable microframeworks

It is very difficult to give an overview of every Java microframework out there. Here is the list of the ones that I did not explore further, but can still be investigated and considered:

- [Ratpack](https://ratpack.io/) – *Ratpack is a set of Java libraries for building scalable HTTP applications. It is a lean and powerful foundation, not an all-encompassing framework.*
- [Jooby](https://jooby.org/) – *Scalable, fast and modular micro web framework for Java.*
- [Akka HTTP](https://doc.akka.io/docs/akka-http/current/) – *The Akka HTTP modules implement a full server- and client-side HTTP stack on top of akka-actor and akka-stream. It’s not a web-framework but rather a more general toolkit for providing and consuming HTTP-based services.*
- [Dropwizard](https://www.dropwizard.io) – *Dropwizard is a Java framework for developing ops-friendly, high-performance, RESTful web services.*
- [Jodd](https://jodd.org/) – *Jodd is set of micro-frameworks and developer-friendly tools and utilities. Simple code. Small size. Good performances. Whatever. Use what you like.*
- [Armeria](https://line.github.io/armeria/) – *Armeria is an open-source asynchronous HTTP/2 RPC/REST client/server library built on top of Java 8, Netty, Thrift and gRPC.*
- [Ninja](http://www.ninjaframework.org/) – *Ninja is a full stack web framework for Java. Rock solid, fast, and super productive.*
- [Pippo](http://www.pippo.ro/) – *It’s an open source (Apache License) micro web framework in Java, with minimal dependencies and a quick learning curve.*
- [Rapidoid](https://www.rapidoid.org) – *Rapidoid is an extremely fast HTTP server and modern Java web framework / application container, with a strong focus on high productivity and high performance.*

Out of that list, I would recommend checking out **Ratpack,** **Jooby, and Dropwizard**. Especially the first two frameworks quite closely follow the microframework philosophy.

## I need more than a microframework!

If you need something light, but fully featured I can recommend two main options:

[Spring Boot](https://spring.io/projects/spring-boot) – *Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can “just run”.*

[Vert.x](https://vertx.io/) – *Eclipse Vert.x is a tool-kit for building reactive applications on the JVM.*

Spring Boot is definitely not micro with all the dependencies that it brings, but the development experience can be quite similar if you are careful with what you chose to use.

## Summary

Working with microframeworks is fun and productive. Sometimes it is too easy to always chose Spring Boot and forget that there is a whole world of Java and Kotlin innovation happening out there. I am particularly excited for Micronaut and Javalin and the way they may influence future JVM development. The ultimate cloud support and ultimate simplicity really appeal to me.

If I missed any of your favorite frameworks (or did not give them justice in my comments), be sure to let me know in the comments section!
