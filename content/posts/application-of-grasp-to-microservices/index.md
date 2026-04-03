---
title: "Application of GRASP to Microservices | E4developer"
date: 2018-02-13T00:00:00Z
draft: false
description: "GRASP stands for General responsibility assignment software patterns. See how this OOP patterns apply to microservices development and design."
categories: ["Architecture", "Microservices"]
cover:
  image: "images/cropped-e4-dev-twitter.png"
  alt: "Application of GRASP to Microservices | E4developer"
aliases:
  - "/2018/02/13/application-of-grasp-to-microservices/"
ShowToc: true
TocOpen: false
---

# Application of GRASP to Microservices

GRASP stands for General responsibility assignment software patterns. You might have heard of it before, or you might not. Either way, you might not have thought about how these principles can potentially help when deciding your responsibilities assignments in a microservices architecture. Craig Larman in his book [Applying UML and Patterns](http://amzn.to/2EykJaH) said that the *“desert island skill”*, the most important skill to have in Object Oriented Analysis/Design would be: *“to skillfully assign responsibilities to software objects”.*I think there is some truth to this when thinking about the most important microservices skill as well. Lets look at GRASP through the prism of microservices.

GRASP principles/patterns are here to help us build better Object Oriented systems. The main goals of Object Oriented systems are:

- **Modularity**
- **Reusability**

If we think what we are usually trying to achieve with our microservices- these goals are very similar. We want a modular system with components that are loosely coupled and stand well on their own. These are well established patterns and principles that come from 40+ years of industry experience of building Object Oriented systems that stood the test of time. Given that, we should see if we can find some universal truths there that can help us deal with our design problems. I think I made my case here and we can start looking at the 9 patterns and how they can help us reason about microservices:

# The Nine GRASP principles/patterns:

### Information Expert

**Question**: What is a general principle of object design and responsibility assignment?

**Answer**: Assign a responsibility to the **information expert**– the class that has the information necessary to fulfill the responsibility.

**Application to Microservices**: This is quite a key pattern for OOA/D and it translates really well to the world of microservices. When we want to assign some responsibility, we should look which microservice already owns the data necessary. That will make everything easier. If we don’t need to worry about moving data around, then our job becomes easier. If it turns our that there are always multiple services required to gather the data to do anything- maybe that’s a sign that the microservices were not divided logically? This is one of the first thing you should think about when assigning responsibility to microservices.

### Controller

**Question**: What first object beyond the UI layer receives and coordinates system operation?

**Answer**: Assign the responsibility to an object representing one of these choices:

- Represents the overall system, a root object, a device that the software is running within, or a major subsystem (these are all variations of a *façade controller*)
- Represents a use case scenario within which the system operation occurs (a use-case or session controller)

**Application to Microservices**: The *façade controller*is the relevant one here. This is UI specific, but I think very relevant to microservices. It is really about dealing with a system completely external to the microservices architecture that you have some control over. If you are dealing with UI- yes you should have a Controller that the rest of the system hides behind. If there is some other arbitrary interface interacting with your system- you want to hide your system behind a *Controller* as well. It is all about hiding the system details and exposing a static interface. This is why we have Ingress in Kubernetes and Zuul in Spring Cloud (in the [Netflix](https://cloud.spring.io/spring-cloud-netflix/) part).

### **Low Coupling** (evaluative)

**Question**: How to reduce impact of change?

**Answer**: Assign responsibilities so that (unnecessary) coupling remains low. Use this principle to evaluate alternatives.

**Application to Microservices**: This is one of the main goals and hallmarks of good software/system design. Low coupling should drive most of our design decisions. Because if it does not, if you do not care for it, there is a large risk that you will end up with a *distributed monolith*. A system that pretends to be microservices, but has no benefits of a microservices system and all the difficulties and challenges. Low coupling can be viewed as one of a key measures of successful microservices implementation.

### **High Cohesion** (evaluative)

**Question**: How to keep objects focused, understandable, manageable, and as a side-effect, support Low Coupling?

**Answer**: Assign responsibilities so that cohesion remains high. Use this to evaluate alternatives.

**Application to Microservices**: This is another key characteristic of a successful microservices architecture. I have read multiple blog posts criticizing microservices and choreography in general stating that there is just too much overhead with the communication! If you have so much overhead that your system starts to become unusable- your cohesion may be a bit too low. It often seems great to make these services really *micro*, but if we split them along wrong lines, if we split something that is meant to be together, we end up with extremely chatty services. If you have couple services that can’t seem to get anything done on their own- you may consider making them into a single service. I have written about this problem in my [common technical debt in microservices](http://e4developer.com/2018/02/11/common-technical-debt-in-microservices/) blog post.

### **Polymorphism**

**Question**: Who is responsible when behaviour varies by type?

**Answer**: When related alternatives or behaviours vary by type (class), assign responsibilities for the behaviour- using polymorphic operations- to the types for which the behaviour varies.

**Application to Microservices**: At first this does not seem to relate to microservices in any obvious way. But if you think about what Polymorphism is- it is providing a single interface to entities of a different type. But, how do you achieve polymorphism in your architecture? You want to get a different behavior depending on the type of object that you are dealing with. You want to make a call, but you want it to be handled differently depending on what that call is, without actually knowing how it resolves, without knowing which service picks it up. I think this is an excellent illustration of the value that **Messaging/reactive services** can bring. You publish the message, depending on the type of that message, different microservices may pick it up, filter it and do what is necessary, without the caller knowing

### Creator

**Question**: Who creates? (use of Factory does not exclude creator)

**Answer**: Assign class B the responsibility to create an instance of class A if one of these is true:

- B contains A
- B aggregates A
- B has the initializing data for A
- B records A
- B closely uses A

**Application to Microservices**: Here the connection is again not as clear as in some of the other patterns. This pattern talks specifically about creating instances of a class. How does that translate? In OOA/D classes usually correspond closely to objects in the domain model. In microservices, if you follow Domain Driven Design (or often just a common sense) you may also see these one to one relationship between domain objects and data stored in a specific microservice. This microservice that owns that data becomes the *“golden source”*of this information. You can think of it as the *Creator* of this object representation, when it instantiates it either as JSON Object, a message or in some other way. This does not hold as neatly, but the spirit of the pattern still makes sense. The service responsible for the data instantiation, the service, that owns the data, should be the one that fulfills some of the criteria mentioned… With the criteria: “*B records A”* being self fulfilling in this case.

### **Pure Fabrication**

**Question**: Who is responsible when you are desperate, and do not want to violate high cohesion and low coupling?

**Answer**: Assign a high cohesive set of responsibilities to an artefact or convenience “behaviour” class that does not represent a problem domain concept- something made up, in order to support high cohesion, low coupling, and reuse.

**Application to Microservices**: In similar fashion to the OOA/D, this is the voice of a pragmatism. If for some reason, you need to create a service that does not really correspond closely with your domain, you have a permission to do just that. Of course, you have the permission if this helps you achieved high cohesion, low coupling, reuse- all noble goals. Plenty of the supporting services, such as message brokers, cache providers, request-routers do not correspond to the domain model, but help the system achieve these good characteristics. This is the permission to use them.

### **Indirection**

**Question**: How to assign responsibilities to avoid direct coupling?

**Answer**: Assign responsibility to an intermediate object to mediate between other components or services, so that they are not directly coupled.

**Application to Microservices**: This principle relates to microservices very directly. It can be translate as- if your services are coupled, use another component in between to decouple them. This sounds like a job for a message queue! Of course you could argue that an API gateway fulfills a similar goal. With a message broker that coupling is even loser as the only known thing between the services is location of the broker and expected message format/channel. Adding and removing services to the interaction can be pretty seamless. It is worth thinking about this next time we integrate our services.

### **Protected Variations**

**Question**: How to assign responsibilities to objects, subsystems, and systems so that the variations or instability in these elements do not have an undesirable impact on other elements?

**Answer**: Identify points of predicted variations or instability; assign responsibilities to create a stable “interface” around them.

**Application to Microservices**: This is absolutely key to any software design effort. Protecting variation is what we are trying to achieve when designing APIs, when thinking about our domain model, when writing the services themselves. This is a key principle for OOA/D, microservices and good software engineering in general. So, how does is specifically relates to microservices?:

- Stable APIs that do not need to change
- Using message queues as a preferred mode of communication- easy to add another services
- Data model that is open for extension, but closed for change
- Core services having limited responsibilities so they do not grow beyond their logical scope

You could say that the whole microservices pattern come from the idea of Protected Variations. You can actually finish writing a microservice and have it be stable despite everything else changing in the system. This is not quite the case with a monolith, as it is the system- it always changes.

# Conclusion

Some of the GRASP principles relate to microservices more clearly than others. Overall, these are founded in solid Software Engineering practices, so no surprise here that they are relevant. What did surprise me however, was reflecting on these principles and realizing **how strongly they seem to favor choreography as a preferred mode of integration**. Indirection, Polymorphism, Protected Variation- the ideas expressed by these patterns/principles are very much aligned with the goals of Choreographed microservices architecture.
