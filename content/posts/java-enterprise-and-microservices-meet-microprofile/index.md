---
title: "Java Enterprise and Microservices - meet Microprofile! | E4developer"
date: 2018-01-21T00:00:00Z
draft: false
description: "Microprofile is the Enterprise Java answer to microservices. This is an introduction to Microprofile with list of current and future features."
categories: ["Microservices"]
cover:
  image: "images/microprofile.png"
  alt: "Java Enterprise and Microservices - meet Microprofile! | E4developer"
aliases:
  - "/2018/01/21/java-enterprise-and-microservices-meet-microprofile/"
ShowToc: true
TocOpen: false
---

# Java Enterprise and Microservices – meet Microprofile!

It seems that just recently majority of server-side development was done  with some flavor of Enterprise Java. Who can forget J2EE, or JEE, writing all these JSP, JSF and Struts applications. It also feels that over the past few years there is less and less happening in that space. New projects are regularly picking alternative technologies and release and  the release of JEE 8 did not have the same impact as Spring Boot or Microservices in general. Microprofile is an attempt to change that. Microprofile is the Enterprise Java answer to Microservices.![](images/microprofile.png?resize=714%2C252&ssl=1)

### What exactly is Microprofile?

I will start by quoting the Microprofile website (<http://microprofile.io>) directly:

> The MicroProfile is a baseline platform definition that optimizes Enterprise Java for a microservices architecture and delivers application portability across multiple MicroProfile runtimes.

That roughly translates to: *“Microprofile is a Java Enterprise subset suitable for building microservices.”*  Sounds great- plenty of Java developers have vast Java Enterprise experience that could be reused in more microservices-oriented framework. The official website elaborates by adding that the initial baseline is  JAX-RS + CDI + JSON-P. As a fan of CDI beans that sounds like a good start to me. This is also not meant to be the whole extent of Microprofile. Because it is not Oracle controlled, it is not strictly limited to using technologies from the Java Enterprise portfolio. The idea here is to combine them with other open-source projects.

This leads to another important point about Microprofile. It is controlled by Eclipse foundation- that means community control and innovation. Microprofile is free to innovate and experiment much faster than Java Enterprise ever was with JCP and JSR process. In my opinion, this is good, as we will have the best of both worlds. Very solid foundation in terms of proven Java EE technologies, coupled with heavy community involvement and freedom to move forward faster.

### Can you already use Microprofile?

The answer is yes! Microprofile version 1.3 was released in January 2018. Eclipse published even some samples on their Github profile. Here I would like to take a closer look at their [microprofile-sample-cannonical](https://github.com/eclipse/microprofile-samples/tree/master/microprofile-sample-canonical) which is a simple sample of a Rest microservice.

So the main application class goes as follows:

```

/*
 * Copyright (C) 2016, 2017 Antonio Goncalves and others.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.
 *
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.eclipse.microprofile.sample.canonical.rest;

import javax.enterprise.context.ApplicationScoped;
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;

@ApplicationPath("/")
@ApplicationScoped
public class RestApplication extends Application {
}

```

and we have the Rest controller:

```

/*
 * Copyright (C) 2016, 2017 Antonio Goncalves and others.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.
 *
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.eclipse.microprofile.sample.canonical.rest;

import javax.enterprise.context.RequestScoped;
import javax.inject.Inject;
import javax.json.Json;
import javax.json.JsonArrayBuilder;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.eclipse.microprofile.sample.canonical.utils.QLogger;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.Logger;

@Path("/")
@RequestScoped
public class TopCDsEndpoint {

    @Inject
    @QLogger
    private Logger logger;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public String getTopCDs() {

        final JsonArrayBuilder array = Json.createArrayBuilder();
        final List&lt;Integer&gt; randomCDs = getRandomNumbers();
        for (final Integer randomCD : randomCDs) {
            array.add(Json.createObjectBuilder().add("id", randomCD));
        }
        return array.build().toString();
    }

    private List&lt;Integer&gt; getRandomNumbers() {
        final List&lt;Integer&gt; randomCDs = new ArrayList&lt;&gt;();
        final Random r = new Random();
        randomCDs.add(r.nextInt(100) + 1101);
        randomCDs.add(r.nextInt(100) + 1101);
        randomCDs.add(r.nextInt(100) + 1101);
        randomCDs.add(r.nextInt(100) + 1101);
        randomCDs.add(r.nextInt(100) + 1101);

        logger.info("Top CDs are " + randomCDs);

        return randomCDs;
    }
}

```

So far this looks great. You can see that there is no much code needed here and the whole application resembles Spring Boot or Dropwizard. Now let’s look at the dependencies…

```

<?xml version="1.0" encoding="UTF-8"?>

<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.eclipse.microprofile.sample</groupId>
        <artifactId>parent</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>

    <artifactId>canonical</artifactId>
    <packaging>${packaging.type}</packaging>
    <name>Microprofile Samples :: Canonical</name>

    <dependencies>
        
        <dependency>
            <groupId>org.jboss.logging</groupId>
            <artifactId>jboss-logging</artifactId>
        </dependency>
        
        <dependency>
            <groupId>javax</groupId>
            <artifactId>javaee-api</artifactId>
        </dependency>
        
        <dependency>
            <groupId>net.javacrumbs.json-unit</groupId>
            <artifactId>json-unit-fluent</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </dependency>
        <dependency>
            <groupId>org.jboss.resteasy</groupId>
            <artifactId>resteasy-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.arquillian.universe</groupId>
            <artifactId>arquillian-junit</artifactId>
            <type>pom</type>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
        </dependency>
    </dependencies>

    <build>
        <finalName>microprofile-sample-canonical</finalName>
    </build>

    <profiles>
        <profile>
            <id>wildfly-swarm</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.wildfly.swarm</groupId>
                        <artifactId>wildfly-swarm-plugin</artifactId>
                    </plugin>
                </plugins>
            </build>
        </profile>
        <profile>
            <id>hammock</id>
            <dependencies>
                <dependency>
                    <groupId>ws.ament.hammock</groupId>
                    <artifactId>dist-microprofile</artifactId>
                </dependency>
                <dependency>
                    <groupId>ws.ament.hammock</groupId>
                    <artifactId>test-arquillian</artifactId>
                    <scope>test</scope>
                </dependency>
                <dependency>
                    <groupId>org.jboss.arquillian.container</groupId>
                    <artifactId>arquillian-weld-embedded</artifactId>
                    <scope>test</scope>
                </dependency>
            </dependencies>
        </profile>
    </profiles>
</project>

```

Being exposed to Spring Boot, the number of dependencies here seems quite large in comparison. This is not necessarily bad, but opinionated frameworks with their ease of development are gaining more and more traction. Perhaps Microprofile in the future could provide a bit more guidance in which libraries are recommended or necessary to get some basics running.

One interesting thing is the use of WildFly Swarm. With this, we gain something similar to embedded Tomcat that is found in Spring Boot. It is added here as a Maven plugin- closer and more seamless integration would be most welcome!

### What is the future of Microprofile?

At the time of writing, Microprofile just released version 1.3. Currently, that includes:

- JAX-RS 2.0
- CDI 1.2
- JSON-P 1.0
- Config 1.1 (slight update to Config 1.0)
- Fault Tolerance 1.0
- JWT Propagation 1.0
- Health Metrics 1.0
- Health Check 1.0
- MicroProfile OpenTracing 1.0
- MicroProfile OpenAPI 1.0
- MicroProfile Type-safe Rest Client 1.0
- MicroProfile Metrics 1.1
- MicroProfile Config 1.2

Given that the version 1.0 was released on 17th September 2016 (announcement [here](https://microprofile.io/blog/2016/09/microprofile-at-javaone)) this is very impressive list of features. The features that the team will focus on now are:

- JSON-B 1.0
- CDI 2.0
- JSON-P 1.1
- JAX-RS 2.1
- Improving development documentation

There is a lot of exciting stuff and innovation here. Especially with JSON-B (that you should read about, as it may change the way we write Java to Json: <http://json-b.net/>) and with CDI 2.0 as they bring plenty of new features to already very good CDI Beans.

### My final thoughts

It feels that Microprofile will bring a much-needed breath of fresh air onto Java Enterprise development. At the moment the team is moving at a very high speed and there are ample opportunities to cooperate with them and influence, just check on: <https://microprofile.io>. One thing I really would like to see is a closer integration with Application Server, as this was one of the features that made Spring Boot and Dropwizard so popular. WildFly Swarm is great, but not sure how easily you can configure it with Microprofile itself. Maybe there is a chance for better integration than Maven plugin?

The future of Enterprise Java is looking exciting once again!
