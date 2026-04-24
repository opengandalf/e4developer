---
title: "Getting Reactive with Spring Boot 2.0 and Reactor"
date: 2018-04-11T00:00:00Z
draft: false
description: "Reactive programming is gaining a rapid popularity in the JVM community. With Java 9 natively embracing the Reactive Streams and Spring Boot 2.0…"
categories: ["Reactive", "Spring Boot"]
cover:
  image: "images/reactor-spring.png"
  alt: "Getting Reactive with Spring Boot 2.0 and Reactor"
aliases:
  - "/2018/04/11/getting-reactive-with-spring-boot-2-0-and-reactor/"
ShowToc: true
TocOpen: false
---Reactive programming is gaining a rapid popularity in the JVM community. With [Java 9 natively embracing the Reactive Streams]({{< ref "/posts/reactive-streams-in-java-introducing-the-new-spi" >}}) and Spring Boot 2.0 including the WebFlux, it is hard to argue with this statement. Spring uses Reactor for its own reactive support and WebFlux relies on that support. In this article, I will show you how to get into reactive programming with Reactor and Spring Boot 2.0.

### What is Reactor?

Project Reactor is quite well described by the tagline on their [official page](https://projectreactor.io/):

> Reactor is a fourth-generation Reactive library for building non-blocking applications on  
> the JVM based on the Reactive Streams Specification

To re-phrase, it is a library for building reactive applications on the JVM that is based on the [Reactive Streams Specification](http://www.reactive-streams.org/).

I have recently blogged about the [Reactive Streams native SPI support in Java 9]({{< ref "/posts/reactive-streams-in-java-introducing-the-new-spi" >}}) and as of the time of writing, Reactor does not use that yet. Since the SPI is quite new, I hope Reactor will switch to it in the near future.

### Core ideas behind Reactor

As already mentioned, Reactor is based on the [Reactive Streams Specification](http://www.reactive-streams.org/).

Reactor provides two implementations of the `Publisher` as defined by the specification- **Flux** and **Mono**. Understanding of these two concepts is crucial to understanding Reactor. Let’s have a look at the `Publisher` interface:

```

public interface Publisher<T> {
    public void subscribe(Subscriber<? super T> s);
}

```

If allowing `subscribe` was all that we could do with **Flux** and **Mono**, then they wouldn’t be that impressive. Flux and Mono do much more, but before jumping into examples let’s define them:

- **Flux**, an Asynchronous Sequence of 0-N Items
- **Mono**, an Asynchronous 0-1 Result

### Mono and Flux explained by example

For me it was easiest to understand what Mono and Flex are with a few examples:

**Mono and Flux can be used in a static way, either a sequence of 0-1 items (Mono) or 0-N items (Flex):**

```

Mono<String> emptyMono = Mono.empty();
Mono<String> staticMono = Mono.just("e4developer");

Flux<Integer> emptyFlex = Flux.empty();
Flux<Integer> numbersOneToTen = Flux.range(1, 10);
Flux<String> staticFlex = Flux.just("e4developer", 
                                       "reactive", 
                                        "reactor");

```

**Mono and Flux values are being processed by subscribing to them:**

wordsFlex .subscribe(word -> System.out.println(word));

This snippet will print the values `"e4developer", "reactive", "reactor"` as you would expect when iterating the list. The key rule of Mono and Flux is:

> Nothing Happens Until You subscribe()

**Mono and Flux can be used in a dynamic way. You can make use of the `FluxSink` to bind the subscription:**

```

public class EventListener {
                                                 
    int count = 0;                               
    FluxSink<String> sink;                       
                                                 
    void generate() {                            
        while (count < 10) {
            sink.next("event " + count);
            count++; 
        }
        count++;
    }

    public void register(FluxSink<String> sink) {
        this.sink = sink;
    }
}

```

```

Flux<String> dynamicFlux = Flux.create(sink -> {
    EventListener eventListener = new EventListener();
    eventListener.register(sink);
    eventListener.generate();
});

dynamicFlux.subscribe(System.out::println);

```

In the code above, the `create()` method will be called every time new subscription is created. Make sure you are passing listeners here rather than generators.

Flux and Mono offer many additional features, and if you wish to use them in production, I recommend checking the [Reactor core features reference](https://projectreactor.io/docs/core/release/reference/#core-features).

### A few words on threading and parallelism in Reactor

Threading is an important part of Reactor, as one of the motivations behind Reactive Streams is better utilization of threads.

In Reactor you deal with threading by selecting the kind of `Scheduler` you want to `publishOn` or `subscribeOn`:

```

Flux.range(1, 100).publishOn(Schedulers.parallel());

```

You can also make use of `Schedulers` when building intervals based Flux:

```

Flux.interval(Duration.ofMillis(100), Schedulers.newSingle("dedicated-thread"));

```

To learn more about Schedulers and different types that you have at your disposal have a look at [Reactor reference](https://projectreactor.io/docs/core/release/reference/#schedulers).

It is worth to make clear that using `.publishOn(Schedulers.parallel())` will not make your code run in parallel! You are only using a specific Thread pool designed to match your machine available parallelism.

If you actually want to run through your Subscription in a parallel fashion you should use the `.parallel()` method instead:

```

Flux.range(1, 1000)
        .parallel(8)
        .runOn(Schedulers.parallel())
        .subscribe(i -> System.out.println(i));

```

### Make your synchronous calls asynchronous

When writing your application in a reactive fashion you want to get rid of blocking synchronous calls. Sometimes, you will have to make such a call (often to external resources). To do that use the following pattern:

```

Mono wrapBlockingCode = Mono.fromCallable(() -> {
    return /* blocking synchronous call */
});
wrapBlockingCode = wrapBlockingCode (Schedulers.elastic());

```

We are making use of `elastic` Scheduler to create a dedicated Thread as required.

### Where does Spring 2.0 come in?

One of the brand new features in Spring 2.0 is the incorporation of WebFlux. To use it in your project you can simply use the following dependency:

```

<dependency>                                            
    <groupId>org.springframework.boot</groupId>         
    <artifactId>spring-boot-starter-webflux</artifactId>
</dependency>

```

WebFlux is a vast framework, so I will give you the basics of what it brings:

- It brings Reactor as a dependency
- Contains support for reactive HTTP and WebSocket clients
- Changes the embedded server to reactor-netty as it requires support for the Servlet 3.1

With that you can start writing Controllers that look more like this:

```

@RestController
public class FeatureController {

    public FeatureController() {
    }

    @GetMapping("/features")
    Flux<String> list() {
        return Flux.just("Features 1"
                       , "Features 2"
                       , "Features 3");
    }

    @GetMapping("/features/{id}")
    Mono<String> findById(@PathVariable String id) {
        return Mono.just("Features "+id);
    }
}                      

```

Did you notice `Flux` and `Mono` we just discussed? These are the bread and butter of reactive development wtih WebFlux.

### How to get Reactor without Spring Boot 2.0 or without WebFlux

If you are not yet using Spring Boot 2.0, or you want only parts of your application to be reactive, you can bring the Reactor on its own by adding the following BOM:

```

<dependencyManagement>                          
    <dependencies>                              
        <dependency>                            
            <groupId>io.projectreactor</groupId>
            <artifactId>reactor-bom</artifactId>
            <version>Bismuth-RELEASE</version>  
            <type>pom</type>                    
            <scope>import</scope>               
        </dependency>                           
    </dependencies>                             
</dependencyManagement>                         

```

and the depndency:

```

<dependency>                                 
    <groupId>io.projectreactor</groupId>     
    <artifactId>reactor-core</artifactId>    
</dependency>

```

### Summary

Reactive programming and Reactive Streams bring a new style of programming to the server-side. Asynchronous, non-blocking processing brings plenty of benefits but can be challenging. I hope that after reading this article you are ready to start exploring the use of Reactor or even WebFlux in your own project. I believe that this is just the beginning of the reactive revolution!
