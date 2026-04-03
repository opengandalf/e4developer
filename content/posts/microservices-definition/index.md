---
title: "Microservices Definition | E4developer"
date: 2018-07-02T00:00:00Z
draft: false
description: "Are you really building microservices? What are microservices? There seems to be a constant disagreement on what constitutes microservices systems and what…"
categories: ["Architecture", "Microservices"]
cover:
  image: "images/definition.jpg"
  alt: "Microservices Definition | E4developer"
aliases:
  - "/2018/07/02/microservices-definition/"
ShowToc: true
TocOpen: false
---

# Microservices Definition

![](images/definition.jpg)

Are you really building microservices? What are microservices? There seems to be a constant disagreement on what constitutes microservices systems and what simply makes a “distributed monolith”. In this article, I will go back to basics and look at what’s at the core of what microservices really are.

Before giving my own opinion on the microservices definition and helping to answer you the question *“are we really building microservices?”* let’s quickly review what *the greats* have to say on that topic.

## Martin Fowler and James Lewis on Microservices

Despite Martin Fowler’s fame, he is not the only one who coined these definitions. James Lewis is credited for a lot of this work… He even puts an interesting tagline [on his twitter page](https://twitter.com/boicy):

> (…) blame me for Microservices
>
> James Lewis

Jokes aside, let’s see what these pioneers have to say on the definition of microservices.

There is the [seminal article titled Microservices](https://www.martinfowler.com/articles/microservices.html) where Martin Fowler and James Lews dissect the term. I strongly recommend you read it if you have not before. Rather than giving a simple definition, the authors mention the following list of characteristics that microservices exhibit:

**Microservices Architecture Characteristics**

- The primary way of a microservices system componentization is via services
- Services are organized around business capabilities
- They are used for building products more often than delivering projects. That indicates some DevOps ideas- teams that build microservices, usually run them as well.
- Preference of smart endpoints and dumb pipes
- Decentralized governance – a higher degree of technological freedom
- Decentralized data management – microservices owning their own data
- Automated infrastructure – another sign of a close marriage between DevOps and microservices
- Designed for failure – scalability from resiliency
- Exhibit evolutionary characteristics

I am just reiterating what was said in the enlighting [Microservices](https://www.martinfowler.com/articles/microservices.html)article (really, you should read it). The point here is that these characteristics do not form a simple and rigid definition.

What we can gather from here that Microservices Architecture is a style. In most cases, architects and developers decide to pursue the microservices approach and then end up somewhere on the spectrum.

When going for Microservices Architecture you may achieve different levels of maturity. I have even attempted to create a [Microservices Maturity Quiz](https://www.e4developer.com/2018/06/12/microservices-maturity-quiz/) that tries to highlight some useful technologies.

## Sam Newman and “Principles of Microservices”

Another person that greatly contributed to the popularity of microservices is Sam Newman. His book “Building Microservices” ([I reviewed it here](https://www.e4developer.com/2018/01/24/starting-with-microservices-read-building-microservices/)) is one of the most popular on the topic.

Rather than focus on the book, I would want to bring an absolutely phenomenal talk about Microservices delivered by Sam, titled “Principles of Microservices”. Wonders of the Internet and generosity of the NDC Conferences, you can watch the talk in its entirety here… And believe me, it is worth it!

What do we learn about Microservices from Sam here? We actually have a working Microservices definition:

> Small **Autonomous** services that **work together**, modeled around a **business domain**
>
> Microservices Definition – Sam Newman

This is great! A concise definition that encompasses the key things about Microservices.

If this is what Microservices are, why is this talk over 50 minutes long? That’s because there is the definition, and then there are principles. Sam identifies these principles as:

**Microservices Principles**

- Being Modelled Around Business Domain
- Culture of Automation
- Hiding Implementation Details
- Decentralizing all the things
- Independent Deployment
- Consumer First
- Isolating Failure
- Being Highly Observable

Do you notice anything? The Microservices Principles here are very similar to the characteristics of microservices architecture as described by Martin Fowler and James Lewis!

## So are you using microservices?

The answer to this question is simple. *Are you attempting to build small and autonomous services that are modelled around business domains?*If you answer yes, then you are working with microservices.

You would think that’s a great news… Yes, it is great in some ways, but that also means that you are attempting something really difficult. Make sure that you review the **Principles of Microservices** as presented by Sam Newman and avoid [Common Microservices Tech Debt](https://www.e4developer.com/2018/02/11/common-technical-debt-in-microservices/).

People will always argue about what makes a Microservices Architecture. I would advise everyone to focus on what makes a good Microservcies Architecture. You can start with principles, but since they were only formulated in 2015, there is still a lot of room for change in the future.

## Conclusion

I hope this article gives you a clear idea of how you can define microservices:

> Small **Autonomous** services that **work together**, modelled around a **business domain**
>
> Microservices Definition – Sam Newman

More importantly, I hope that with reading this, you will agree with me that understanding what makes good microservices architecture is more important!
