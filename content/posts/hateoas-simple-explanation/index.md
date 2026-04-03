---
title: "HATEOAS - a simple explanation | E4developer"
date: 2018-02-16T00:00:00Z
draft: false
description: "HATEOAS - Hypermedia as the Engine of Application State. Simple explanation what it is, why should you use it and common misconceptions."
categories: ["Architecture", "Orchestration"]
cover:
  image: "images/cropped-e4-dev-twitter.png"
  alt: "HATEOAS - a simple explanation | E4developer"
aliases:
  - "/2018/02/16/hateoas-simple-explanation/"
ShowToc: true
TocOpen: false
---

# HATEOAS – a simple explanation

HATEOAS – Hypermedia as the Engine of Application State, a name long enough to intimidate and confuse. Behind this complicated name we have a rather simple and elegant idea. In this blog post, I explain what HATEOAS is and how it can be practically used to build more stable systems.

HATEOAS is a way of designing a REST API. More precisely it is a specific constraint of a REST architecture. It can be summed up with:

> API that guides the client through its usage.

Rephrasing it for clarity with some extra details:

> API that describes in its responses how it can be used. By providing URLs to other allowed actions.

Lets look at an example. Assuming that you have a REST service that provides different *products*descriptions; think about some e-commerce website. If you get a JSON response with a *product* from that website, and if it was using HATEOAS it could look something like that:

```

{
    "productId": "123",
    "productName": "Super Microwave",
    "description": "The best microwave in the world. Fact."
    "links": [{
        "rel": "self",
        "href": "http://localhost:8080/super-shop/api/products/123"
    }, {
        "rel": "details",
        "href": "http://localhost:8080/super-shop/api/products/123/details"
    }, {
        "rel": "addToCart",
        "href": "http://localhost:8080/super-shop/api/addToCart/123"
    }]
}

```

Here, you can see a few *links* added. In this implementation (inspired by [Spring HATEOAS](http://projects.spring.io/spring-hateoas/)) you have two fields:

- **rel** – stands for ‘relationship’ and explains how the link relates to the object that you requested for. `self` – meaning, this is the link to the object, `details`– this could be a more detailed information available, `addToCart`– that would be a way of adding this *product* to a shopping cart.
- **href** – a complete URL that shows how the action can be performed

This should be clear now, but there is a bit more to HATEOAS. As the name means Hypermedia as the Engine of Application State, there should be some relation to that response and the application state. Imagine now that there was a product that was not available for purchase. The hypothetical response could look like:

```

{
    "productId": "345",
    "productName": "The Philosophers Stone",
    "description": "Transforms anything into gold"
    "links": [{
        "rel": "self",
        "href": "http://localhost:8080/super-shop/api/products/345"
    }, {
        "rel": "details",
        "href": "http://localhost:8080/super-shop/api/products/345/details"
    }]
}

```

Great stuff- *The Philosophers Stone*, but there is no link to `addToCart`, maybe the item sold out, or is not for sale- either way, this action is not available. The client of the REST service discovers that fact by not having the link available to carry out the action. The application discloses its state via Hypermedia… Hypermedia becomes the engine that drives the Application State… Hypermedia as the Engine of Application State – HATEOAS.

With this simple explanation, let’s consider some implications of using HATEOAS and look at some misconceptions:

### HATEOAS reduces the configuration needed

One thing that is great about HATEOAS is that it will reduce the need for configuring URL endpoints. All these URLs telling you how to look up product details? How to add a product to the shopping cart? You don’t need them hardcoded or in some configuration files. They are supplied by the application. If you really want to have something in your config files, you could place the `rel`– relationships there. In any application of reasonable complexity, you are likely to have dozens if not hundreds different REST API calls. This makes that benefit a very real one.

> HATEOAS can drastically reduce the amount of brittle configuration.

### HATEOAS promotes loose coupling

It can be a considerable challenge to build an application based on REST services in such a way that changing API is easy. HATEOAS does not make it trivial (as you still can’t easily remove or change `rel's`) but makes it better than the status quo. You can change your URLs and their structure with relative ease- that is something.

### HATEOAS is not magic- you still need to know the API to code the interactions

When reading about HATEOS you will see the discoverable API aspect highlighted quite a lot. You should really understand it at a conceptual level. The API is discoverable, but this is more relevant to a lack of hardcoded URLs rather than the services somehow figuring out which `rel's` they should interact with. The one aspect of this discoverability that is worth highlighting is that it makes understanding API by the developers programming the interactions easier. This sort of active documentation adds lots of value.

### Is there library support for HATEOAS?

There are a few libraries that help with HATEOAS in the Java space. The popular ones include:

- [Spring HATEOAS](http://projects.spring.io/spring-hateoas/) – the standard way of doing HATEOAS with Spring- waiting for the version 1.0 at the time of writing. Since I am a Spring aficionado, this is what I would recommend
- [Jersey](https://jersey.github.io/) – being the reference implementation of JAX-RS provides HATEOAS support
- [VRaptor](http://www.vraptor.org/) – if you enjoy CDI beans, this MVC framework provides HATEOAS support explored by ZeroTurnaround in their [blog post from 2014](https://zeroturnaround.com/rebellabs/beyond-rest-how-to-build-a-hateoas-api-in-java-with-spring-mvc-jersey-jax-rs-and-vraptor/)

### Should I use HATEOAS for my next project?

This is really for you to decide. As you can see it is a nice idea that improves important parts of the system. Loose Coupling and [Open/Close principle](https://en.wikipedia.org/wiki/Open/closed_principle) are core system qualities worth the effort. On the other hand, it does add overhead and if you are building rather trivial, unlikely to change the system- the complications may outweigh the benefits. Hopefully, with a good understanding of the idea, you can make the best decision for your project.
