---
title: "Having just the right amount of technical debt"
date: 2018-11-21T00:00:00Z
draft: false
description: "Today I want to talk to you about technical debt. This is a topic that comes up a lot and often generates some emotions. Developers often want to have a minimal…"
categories: ["Architecture", "Building teams", "Microservices"]
cover:
  image: "images/tech-debt.jpg"
  alt: "Having just the right amount of technical debt"
aliases:
  - "/2018/11/21/having-just-the-right-amount-of-technical-debt/"
ShowToc: true
TocOpen: false
---![](images/tech-debt.jpg)

Today I want to talk to you about technical debt. This is a topic that comes up a lot and often generates some emotions. Developers often want to have a minimal amount of technical debt. Some will go through great efforts to eliminate any technical debt they see. Let me tell you what I think about it all.

## Different type of technical debt

First of all, it is a bit simplistic to just classify all technical debt as the same thing. I have read a few attempts at classifying it- [Types of Technical Debt](https://agilemichaeldougherty.wordpress.com/2015/07/24/types-of-technical-debt/) by Agile Mike and [There are 3 main types of technical debt. Here’s how to manage them.](https://hackernoon.com/there-are-3-main-types-of-technical-debt-heres-how-to-manage-them-4a3328a4c50c) FirstMark make for interesting reading.

The aforementioned articles focus on looking how the debt came to be: *“was it deliberate?”*, *“was it because of lack knowledge?”* or perhaps *“did something change?”*. There is more to it and if you are interested, you can read the mentioned articles. In here I want to focus on a bit different classification. We are going to ask – **“What is this technical debt doing to my system?”**

**Potential bugs** – Some tech debt is often a source of potential bugs. Haphazardly handled multithreading issues, data transformation algorithms that take generous assumptions about the data quality etc. This kind of debt often manifests itself when bugs are *detected* and graduates to the level of a system failure that needs to be fixed.

**Potential security issues** – How many times did you take a shortcut when dealing with security concerns? I hope the answer is not many! I often see these potential security issues referred to as tech debt. On whoever side you land in this argument, I am sure that you will agree that it is different than your *standard* technical debt.

**Development impediments** – This is what most commonly is classified as technical debt. Things that make the development of the system more difficult than it could be. Here we can talk about the planned technical debt, accidental technical debt etc.

**Operational impediments** – In the modern large-scale system development (microservices and the like), we often have blurred lines between what is operations/infrastructure code and what is *the traditional* system source code. Some decision (for example, how the configuration is handled etc.) can be a technical debt hitting both the operation and the development of the system.

**Code aesthetics problems** – These are other classical tech debt issues, but the ones that do not directly make the development of the system much harder. Slightly wrong names patterns not used properly in code that has not been changed in a long time and it works correctly etc. The sort of tech debt that you need to look for to find.

I don’t want to tell you which technical debt is the most important to you. It depends on your system and your goals. It could be the security aspect or the operational aspect. What is probably always true is that some type of technical debt will cost you a lot, while others will be of lower priority.

With this classification and different *pricing* in mind let’s look at the metaphor once again.

## The technical debt metaphor

I really like the technical debt metaphor. It is linked to financial debt on which you need to pay interest as it accumulates… What I really like is that we can take this metaphor a bit further.

Different technical debt has different interests. Like in the financial world, not all debt is created equal. You want to pay off the highest interest debt first. This underlines the importance of knowing which debt matters for your system the most.

It is healthy to take on some debt. As you may know, most companies in the world have certain levels of debt, and this is considered healthy. You can use debt to fuel your growth (just don’t overdo it). In a software system, if you have absolutely zero technical debt, you can argue that you have spent too much making future development easier (which at one point will stop).

Like in the world of finance and companies, managing technical debt is a challenging and non-trivial task.

## Finding time to fix technical debt

What do you do when your product owner (or your manager) gives you no time to fix any of your technical debt? Depending on your level of control of what you are working on, the blame could be on your side!

If you are fixing the technical debt, you should reasonably expect rewards of these kinds:

- More time saved from fixing the technical debt, than it took to fix it (otherwise why do it?)
- Prevent bugs from happening that would take more time to fix (look at the point above)
- Prevent security incidents that could have a serious ramification (highly system dependent, you need to judge here)
- Save time on operations and maintaining the system (greater than the investment in fixing the debt)
- Feeling good about yourself and the codebase (this is also important!)

So, how do you know what is worth doing? It comes down to experience and some educated guesswork- who said it was easy?

If you can deliver more by doing a bit of tech debt fixing, you can arm yourself in some estimates and good arguments and you can win back the time from your product owner/manager. If they don’t need to know that level of details- do what delivers them working and maintainable system in the fastest way- that includes fixing some tech debt!

## The sensible approach

What is the sensible approach then? It depends, but I can give you some guidance:

- Make sure to classify your tech debt into the high-interest and low-interest one
- Prioritize tech debt that is quick to fix and gives good pay-off
- Work on tech debt in the most active areas of the code – the pay-off will be greater
- Don’t aim for the 100%, you won’t be doing the system a favour

Is it ever a good idea to completely stop working on new features to work on some tech debt? If the maths says that you will deliver faster and higher quality overall, it is the right call (give than you can pull it off with your management). LinkedIn did something like that with their project InVersion described in [When Your Tech Debt Comes Due](https://www.linkedin.com/pulse/when-your-tech-debt-comes-due-kevin-scott/) by their CTO Kevin Scott, definitely give it a read!

## Summary

I hope this article will make you reflect a bit more on the subtleties of managing tech debt in your project. If you like to discuss it, you can [catch me on twitter](https://twitter.com/e4developer). If you would like to read more about tech debt, I also wrote an article about[Common Technical Debt in Microservices]({{< ref "/posts/common-technical-debt-in-microservices" >}}).
