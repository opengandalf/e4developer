---
title: "Lightweight Kotlin Microservices with Javalin"
date: 2018-03-22T00:00:00Z
draft: false
description: "Introducing Javalin- a micro-framework for building Simple REST APIs for Java / Kotlin. Learn how to write Javalin “Hello World”, what are the “before, after and request” handlers and other core Javalin concepts. Building executable jar with required dependencies explained."
categories: ["Microservices"]
cover:
  image: "images/javalin-logo.png"
  alt: "Lightweight Kotlin Microservices with Javalin"
aliases:
  - "/2018/03/22/lightweight-kotlin-microservices-with-javalin/"
ShowToc: true
TocOpen: false
---There is a lot happening in the JVM space when it comes to microservices development. You have Spring Cloud thriving, Microprofile entering the stage, Vert.x letting you get reactive and Dropwizard being actively developed. What if you want something really simple though? And maybe with some Kotlin? For that you have [Javalin](https://javalin.io/)!

### Introducing Javalin

Javalin is a micro-framework for building simple REST APIs for Java and Kotlin. It comes with embedded Jetty server and is very easy to use.

This simplicity makes Javalin a very enjoyable framework for learning Kotlin. If you are new to Kotlin, the last thing you want to do is to be overwhelmed by a new opinionated framework. You want to focus on the core language features.

How do you get started with Javalin then? You need to add a relevant dependency:

```

<dependency>                        
    <groupId>io.javalin</groupId>   
    <artifactId>javalin</artifactId>
    <version>1.6.0</version>        
</dependency>                       

```

And you can start your service development. The Kotlin “Hello World” example is as simple as:

```

import io.javalin.Javalin;

public class HelloWorld {
    public static void main(String[] args) {
        Javalin app = Javalin.start(7000);
        app.get("/", ctx -> ctx.result("Hello World"));
    }
}

```

Isn’t that great? With a single dependency and just a few lines of Kotlin code, you have a running “Hello World” service on the port 7000.

### Building a REST API with Javalin

At the core of Javalin lies the idea of using `handlers`. There are three main `handlers` types:

- **Before-handlers**: these are matched before every request
- **Endpoint-handlers**: for dealing with specific endpoints
- **After-handlers**: these are run after every request, even if Exception occurred

Let’s look at some code.

To print all the headers for every request to an `/example` endpoint:

```

app.before("/example") { ctx ->   
    println(ctx.headerMap())      
}                                 

```

To implement a `GET` endpoint that will return “Hello World” to the caller:

```

get("/example") { ctx ->     
    ctx.result("Hello World")
}                            

```

To write “Goodbye!” to the console after `\example` gets called:

```

app.after("/example") { ctx ->   
    println("Good bye!")         
}                                

```

You can group these handlers easily in `handlers groups` for clearer typing.

The one thing that really stands out here is the ultimate simplicity! You can do things so naturally, **it makes Javalin feel like the NodeJS of the JVM**.

### Other core ideas in Javalin

Javalin is a micro-framework, so the focus is on keeping things light (in my play-time with the framework is was **consistently starting under 1 second**).

With that lightness in mind, there are only a few other concepts that are part of this micro-framework:

- **Context (**ctx**)** – You have seen that in action when printing headers. This is everything you need to handle http-requests.
- **Access Manager** – It helps you implementing per-endpoint authentication and authorization.
- **Exception and Error Mapping** – These help you deal with your Exceptions on the top-level.
- **Lifecycle Events** – If you need to hook to `SERVER_STARTING`, `SERVER_STARTED` and similar events.
- **Server Setup** – For setting up the embedded Jetty

Once again- the simplicity and clarity of these are exemplary. You really get all the basics necessary and the rest is left for you to deal with.

### Packaging an executable JAR

One thing that could be improved upon in the framework is dealing with the creation of executable JAR. At the moment you have to do it yourself by adding appropriate Maven plugin. I have used the following:

```

<plugin>                                                                
    <groupId>org.apache.maven.plugins</groupId>                         
    <artifactId>maven-assembly-plugin</artifactId>                      
    <executions>                                                        
        <execution>                                                     
            <goals>                                                     
                <goal>attached</goal>                                   
            </goals>                                                    
            <phase>package</phase>                                      
            <configuration>                                             
                <descriptorRefs>                                        
                    <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>                                       
                <archive>                                               
                    <manifest>                                          
                        <mainClass>com.e4developer.MainKt</mainClass>   
                    </manifest>                                         
                </archive>                                              
            </configuration>                                            
        </execution>                                                    
    </executions>                                                       
</plugin>                                                               

```

I think it would be better if Javalin dealt with this problem in a similar fashion to Spring Boot, where this is taken care of for the developer.

**Update:** I got a response from Javalin Twitter Account on this subject: *”(…) The reason why Javalin doesn’t concern itself with Jar creation is because it’s not strictly related to Javalin. If people learn how to do it the Maven/Gradle way, this knowledge will be useful for them in future (non Javalin) projects.”* – This highlights the focus and the philosophy behind the project. I can see why adding this JAR generation may be against the spirit of the project.

### Jackson and SLF4J do not come included

One thing that can be also a bit of catch is lack of Jackson and SLF4J implementations included. I understand the reasons for not including them, and the framework makes it clear in the logs it provides that these are required.

I have used the following dependencies and got everything to work nicely:

```

<dependency>                                                     
    <groupId>com.fasterxml.jackson.core</groupId>                
    <artifactId>jackson-core</artifactId>                        
    <version>2.9.4</version>                                     
</dependency>                                                    
<dependency>                                                     
    <groupId>com.fasterxml.jackson.core</groupId>                
    <artifactId>jackson-databind</artifactId>                    
    <version>2.9.4</version>                                     
</dependency>                                                    
<dependency>                                                     
    <groupId>org.slf4j</groupId>                                 
    <artifactId>slf4j-simple</artifactId>                        
    <version>1.7.25</version>                                    
</dependency>                                                    

```

Not a problem, rather something to be aware of.

### The Javalin Project

Javalin is a well-maintained project. That matters.

The official website <https://javalin.io/> has good [documentation](https://javalin.io/documentation)and interesting [examples](https://javalin.io/tutorials/). This is very important when choosing frameworks even for personal projects.

The project codebase is actively maintained as a [Github Repo](https://github.com/tipsy/javalin/) with regular commits being made. Javalin is written in Kotlin. and there are only 10 contributors, making it an interesting project to get involved in. Apache license makes it a safe choice.

### Summary

Javalin is a fascinating micro-framework. I really see it as a sort of NodeJS of the JVM. Something that is needed with the abundance of opinionated and heavy-weight frameworks out there.

I focused here on using Javalin with Kotlin, but it also works perfectly fine with Java- hence the name!

If you are already using Javalin, please- share your experiences in the comments!
