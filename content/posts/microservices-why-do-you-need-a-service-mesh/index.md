---
title: "Microservices - Why Do You Need A Service Mesh? | E4developer"
date: 2019-05-15T00:00:00Z
draft: false
description: "Working for consultancy, I already had a chance to build microservice based systems in large financial organisations as well as public sector ones."
categories: ["DevOps", "Microservices"]
cover:
  image: "images/service-mesh.jpg"
  alt: "Microservices - Why Do You Need A Service Mesh? | E4developer"
aliases:
  - "/2019/05/15/microservices-why-do-you-need-a-service-mesh/"
ShowToc: true
TocOpen: false
---

# Microservices – Why Do You Need A Service Mesh?

![](images/service-mesh.jpg)

Working for consultancy, I already had a chance to build microservice based systems in large financial organisations as well as public sector ones. When sharing my experience with other developers, there is one topic that often comes up- many people wished that they had a service mesh from the start! In this article, I will explain what a service mesh is and why is it so useful!

## Service mesh defined

A service mesh is a dedicated infrastructure layer that helps with managing your service to service communication. It is often implemented as a lightweight reverse-proxy using the sidecar pattern, deployed in a separate container. The two most popular implementations are currently [Istio](https://istio.io/) and [Linkerd](https://linkerd.io/) (which absorbed Conduit).

The common features that are provided by a service mesh include:

- **Controlling the traffic flow and API calls** making testing, upgrading and managing the system easier
- **Managing your authentication, authorization and encryption** which are vital for a secure, production-ready system
- **Providing rich tracing and monitoring**making debugging easier
- **Minimum performance overhead**Istio and Linkerd proxies are implemented in C++ and Rust respectively making them blazing fast

## Real microservices, real problems

Here I want to give you a selection of “battle stories” that would be much easier if the respective systems were using a service mesh:

- **Replacing an authorization layer across the project** – this system had a proof of concept style authorization layer that was later replaced with [Keycloak](https://www.keycloak.org/). This included changes to every single microservice and many shared libraries. This may not have been trivial in a service mesh, but having the authorization layer clearly separated from individual services would have resulted in much less work.
- **Introducing encryption everywhere** – in this scenario, suddenly came a requirement to introduce strong encryption for pretty much every single communication. With nothing like a service mesh in place, you can imagine how difficult and time consuming this was. In comparison, a service mesh would have solved that trivially.
- **Audit requirement for all API calls** – one thing is the ability to debug problems in a system, another is a requirement to audit all the API calls. Once you get the idea of what a service mesh is, this again seems like a perfect use-case that can be a pain if all microservices are deployed “vanilla” style.
- **Switching between databases** – maybe not as difficult in a standard architecture, but definitely not as clean and more invasive. In the case described here, it always required restarts of all microservices (re-deployments) in Kuberenetes. Think of the time wasted!

I could go on here, but I wanted to focus on real examples that did happen and made the team go- “if only we had a service mesh!”. So why did not we?

## Service mesh – the initial investment

Installing Istio or Linkerd is not particularly difficult. Especially when you are just starting to build your system. The problem is that when you are only starting, it may not be immediately obvious that you need a service mesh! Your system is still small and easy to work with, why add all that bloat?

This is where the experience comes in. Most of the developers I worked with or talked to are either on their first, or second large scale microservices project. Most people lack the practical experience to realise that service mesh is such an amazing pattern. If you are reading this- trust me! Your team will thank you if you convince them to spend just a little extra time adding it to your system.

I believe that in a few years service mesh will become an absolute bog-standard for all new microservice architectures. All we need is more time and experience in the community, hence- spread the word.

## But why not just use API Gateway between services?…

An interesting idea that I have encountered is using an API Gateway between microservices as an easy solution. **DO NOT USE API GATEWAY IN PLACE OF A SERVICE MESH**. I need to go all caps here, as this is a trap!

API Gateways look like a very similar offering, but they are much less integrated and often much to slow for a large microservices system. Some of my colleagues had an unfortunate experience of falling into this trap and then having to completely remove the “internal API Gateway”. To be honest, in the past I also thought it sounds like a good idea…

An “internal API Gateway” sounds like an easier thing to do, but it can have a dramatic performance and security impact on your system. Please save yourself a lot of time and pain and use a proper service mesh instead.

## Summary

The “service mesh” is a crucial microservices architecture pattern that you should know. If you are starting a new microservices project, consider including [Istio](https://istio.io) or [Linkerd](https://linkerd.io/) (or another service mesh) as a part of your system. If you are already running microservices, investigate how hard or easy would it be to add a service mesh. If you already have experience with a service mesh, let me know in the comments or share it on [Twitter](https://twitter.com/e4developer).
