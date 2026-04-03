---
title: "Using Redis in Microservices Architecture"
date: 2018-08-03T00:00:00Z
draft: false
description: "In this article, we will look closer at a fascinating open source project. Meet Redis! You may be familiar with Redis already, in that case…"
categories: ["Architecture", "Choreography", "Microservices", "Spring Boot"]
cover:
  image: "images/redis-microservices.jpg"
  alt: "Using Redis in Microservices Architecture"
aliases:
  - "/2018/08/03/using-redis-in-microservices-architecture/"
ShowToc: true
TocOpen: false
---In this article, we will look closer at a fascinating open source project. Meet Redis! You may be familiar with Redis already, in that case, you may be interested in the different use cases it has for microservices architecture. Read on to see how this “*in-memory data structure store, database, cache, and message broker”* can make your system better!

## What is Redis?

I already revealed that in the introduction. To repeat (using [redis.io](https://redis.io/) own words):

> Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.

In practice, that means that we can use Redis to store and retrieve data. We can do that with a very good performance, potentially (not necessarily) sacrificing some durability of that data.

Redis is also an open source project- that’s great news! We will be able to get hands-on without any obstacles in our way.

## Redis and Docker

As with most things these days, I really recommend that you use Docker for playing with Redis. If you have never used Docker before I wrote a [short intro]({{< ref "/posts/microservices-toolbox-docker" >}}).

I have used Redis version 4.0.8 in this article. If you don’t care about which version of Redis you run, but you want the latest, you can start the container with the following command:

`docker run --name my-redis -d redis`

This will expose port 6379 (the default) for connecting to Redis.

You can also run your Redis with a persistent storage to a volume `/data` if you wish:

`docker run --name my-redis -d redis redis-server --appendonly yes`

If you don’t know about volumes yet, Docker has a [good documentation about them](https://docs.docker.com/engine/tutorials/dockervolumes/).

Speaking of documentation, if you actually consider running Redis in production, I strongly advise you read the [official docker repo documentation for Redis](https://hub.docker.com/_/redis/).

You now know how to run Redis with Docker. For standalone installation, please check [redis.io/download](https://redis.io/download) – this should be up to date!

## Redis and Spring Boot

Redis is extremely popular and plays nice with most libraries. Since I enjoy and recommend Spring Boot, I will show you how easily the two integrate.

The only dependency you need to add to your POM file is:

```

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>

```

One of the main benefits of using `spring-boot-starter-data-redis` is that you don’t have to do any configuration yourself. Spring autoconfiguration shines once again. You can define properties in your `application.properties` as per usual in Spring Boot.

Let’s make a simple application where we can store notes and retrieve them using Redis.

First, we need `Note` object defined:

```

package com.e4developer.springredis;

import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Note")
public class Note {
    @Id private final String id;
    private final String message;

    public Note(String id, String message) {
        this.id = id;
        this.message = message;
    }

    public String getId() {
        return id;
    }

    public String getMessage() {
        return message;
    }
}

```

This object is annotated as `@ReisHash` so it can get persisted in Redis using `NoteRepository`:

```

package com.e4developer.springredis;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NoteRepository extends CrudRepository<Note, String> {}

```

The one last thing to add is the `NoteController` to bring these things together:

```

package com.e4developer.springredis;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Optional;

@Controller
public class NoteController {

    @Autowired
    private NoteRepository noteRepository;

    @PostMapping("/notes/{id}")
    public ResponseEntity<String> setNote(@RequestBody String message, 
                                          @PathVariable("id") String id){
        Note note = new Note(id, message);
        noteRepository.save(note);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @GetMapping("/notes/{id}")
    public ResponseEntity<optional<Note>> readNote(@PathVariable("id") String id){
        Optional<Note> note = noteRepository.findById(id);
        return new ResponseEntity<>(note, HttpStatus.CREATED);
    }
}

```

Now you can save and retrieve `Notes` using GET and POST requests! We made use of [Spring Data here that I looked at before]({{< ref "/posts/spring-data-microservices-data-companion" >}}).

If you want to work more closely with Redis and Spring, you should familiarize yourself with the [Spring Data Redis documentation](https://docs.spring.io/spring-data/redis/docs/2.1.0.M3/reference/html/).

Since using Redis is nice and easy, let’s look at the most common use-cases for it in the microservices world.

## Redis – Microservices Cache

One of Redis’s strongest suits its the caching capability it provides. If you need to temporarily store data and share it between microservices – Redis is the go-to choice.

With the fine-grained eviction policies at your disposal and stellar performance, it is hard to see why you would need anything else?

This is where many developers under-appreciate it. While Redis is a great caching solution, it offers much more…

## Redis – In-memory Database

As I already mentioned, Redis describes itself as *“in-memory data structure store, database”*first. It is in fact, an outstanding NoSQL product.

Many services can benefit from using in-memory databases. They often significantly outperform normal databases on most metrics.

A common use case would be a large amount of read-only data that is rarely modified. You can have a traditional database maintaining the record and in-memory database providing read-only performance. This is just one of many in-memory database use cases.

## Redis – Database

If you need to have your data persisted- don’t fret. Redis also have you covered.

Redis uses a clever mix of:

- RDB – snapshots of your dataset at specified intervals
- AOF – persisted log of every write operation received by the server

To provide speed and data reliability as required. This is an interesting topic and the Redis website contains a good comparison of [RDB and AOF pros and cons](https://redis.io/topics/persistence).

One thing is clear- if you wish to use Redis for persistence, the project is more than ready to provide a robust solution to the problem.

## Redis – Message Broker

The last, perhaps the most surprising, capability that Redis provides is its Pub/Sub mechanism.

If you are interested in microservice choreography- it is a viable solution. Using Redis may be simpler than setting up RabbitMQ and it is definitely simple than dealing with the intricacies of Kafka.

Redis PUB/SUB model is very simple and nicely covered in the [short section on the official website](https://redis.io/topics/pubsub).

If you are unsure what microservices choreography is, I have recorded a short video about it:

## Summary

I wrote that article to promote Redis as a great tool for building microservices solutions. Having a tool that can be your cache, database and a messaging component in one can make your microservices life simpler.

Remember, Redis is much more than simply a caching solution!
