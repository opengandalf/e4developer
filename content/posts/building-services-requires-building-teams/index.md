---
title: "Building services requires building teams"
date: 2018-02-20T00:00:00Z
draft: false
description: "Microservices are linked to the idea of independent teams. See how vital this idea is to the successful adoption of such highly decoupled architecture."
categories: ["Building teams", "DevOps", "Microservices"]
cover:
  image: "images/team.jpg"
  alt: "Building services requires building teams"
aliases:
  - "/2018/02/20/building-services-requires-building-teams/"
  - "/building-services-requires-building-teams/"
ShowToc: true
TocOpen: false
---When talking about microservices (or agile development), the idea of self-managed, independent teams often comes up. What is not emphasized enough is how vital this idea is to the successful adoption of such highly decoupled architecture. In this article, I will share my experiences about working with independent teams and being part of them.

Most successful projects that I was either part of, or had a pleasure of working with had one thing in common. They were delivered by either one or a multiple of high-performing, self-managed, independent teams. You may say: *every sizable project nowadays is delivered by a team!* I disagree, most medium and large projects are delivered by groups of people, but in many cases, I would not call them *teams*. In my opinion, it takes more than grouping a few people together and slapping a name on them to make a team…

### What is a team?

What is a team then? I will answer that in the context of software development of course. I define *a team* as: *“Team is a group of people, working together on a number of shared goals”*. Let’s unpack that sentence:

- **Group of people** – you don’t need any specific roles to make a team.  You need a group of people- so you need at least two people (although that would be a very small group).
- **Working together** – this is where many *“teams”* fail. Working together goes beyond just working in the same room, or on the same project. There needs to be collaboration. One person helping another. If someone is not an expert in a given technology, she should not be afraid to ask a teammate for help. If someone needs help, other members are stepping in. The work is done together, not alone.
- **Shared goals** – goals should be set at a team level. If there is some UI work to be done, it is not given directly to the UI expert, rather the team decides how to deal with that. Maybe there is another person that could do the task only with the minimal help of the single UI expert on the team? Finding the best way of doing the work is left to the team. Shared goals delivered by a group of people truly working together- this is how you spot a team.

### What is an independent team?

So what is an independent team? Of course, no-one is truly independent in most organizations, so lets narrow the description of what sort of independence we are talking about here.

We want teams that can deliver their goals with minimum dependencies on people outside of the team. The ultimate goals for most software development teams are working features and products in production. **Let’s see what things can stop the team from being independent**:

- Reliance on testing done outside of the team
- Reliance on separate teams deploying the service
- The design is done outside of the team
- Reliance on business knowledge not easily available to the team
- Inability to communicate with other teams to get their services integrated
- Any other person or process dependency stopping the team from delivering the work efficiently

I mentioned things that can block a team whose goal is to deliver features to production. There are different teams out there whose goals may be different. If your team is tasked with building automated testing for an already existing application, your dependencies can differ. If you work on the sort of software that is not deployed in production (i.e. software installed on end-user devices), dependencies would be different again.

### Ownership of a service

To achieve independence and general success in your microservices development, each microservice should be owned by a dedicated team. Microservices are small enough that they should be easily managed by one team. If there is more than one team owning a single microservice, these will impede their independence. Suddenly the teams (likely working on separate goals) are dependent on each other when making changes to the service.

### Can teams manage more than one service?

To be clear- each team can own multiple services. Once work is mostly finished on a given microservice, there is nothing stopping a team from taking ownership of another one. It is actually expected and completely normal for one team to own multiple microservices. The challenge for the team is keeping the microservices independent from each other. This is a technical topic that I explore in a [dedicated blog post]({{< ref "/posts/common-technical-debt-in-microservices" >}}).

### DevOps is a requirement, not an option

If you want to have truly high performing teams, the developers and operations have to really come together. Ideally, you would want your team to be responsible for deploying the services, but for many companies, this is not practical yet.

A potential solution is teaming up with the Operations closely enough that Developers end up being closely involved in the provisioning of the service. This has many benefits:

- Technical debt on both sides is made clear. Any challenges that operations are facing become transparent to the developers and become their challenges as well
- Problems with deployment can be investigated rapidly. Developers know the system better so that they can understand system errors quicker
- The service team becomes more independent, as they understand the deployment process better. They can get ahead of potential issues faced by operation
- Building communication channels that might not have existed before
- Many more- often specific to your own organization

DevOps is a culture rather than a specific process. Make sure that your company is adopting that culture, as this does not happen overnight.

### Structure of an independent team

There is much talk about the structure of independent teams. Should these include people traditionally involved in operations? Should they include manual testers?

In the best scenario, they should include anyone who spends the majority of their day working towards fulfilling the team’s goals (even though they may not be members of the team yet). This list includes but is not limited to:

- Testers
- Operations
- Architects
- Business Analyst
- Developers

The structure of the team promotes collaboration and working together. If there is a chance to get more people collaborating closely, it is a chance worth exploring.

### Roles that operate across multiple teams

There is a number of roles that can operate across different teams. Architects or business analysts for example. You can then think of your teams on two levels:

- **Service teams** – these are the teams that this article is mainly about. Teams delivering services, each service should belong to a single team
- **Project teams** – much larger, combining multiple service teams and people that may work across different service teams. One project team can contain multiple Service teams

Some companies do not have projects as such and there are teams that work on multiple projects… Well, in this case, we are dealing with different **specialized teams** (information security or enterprise architecture, are good examples) that have their own goals, potentially different than service teams. The key to building a successful working relationship with them is communication.

### Conway’s law in action – the importance of communication

You might have heard about Conway’s law before. Coined by Melvin Conway it goes like that:

> “organizations which design systems … are constrained to produce designs which are copies of the communication structures of these organizations.”

Now, imagine the kind of systems that are produced by multiple teams where the communication is broken… These are mostly the broken systems, failed projects. Nobody wants that!

How do you avoid broken communication- by actively promoting good communication! I don’t know what your role is in the project, but whatever it is you should be doing your bit. If you can, make sure that communication works well.

**Get a good chat program**. You need a program where you can have team channels and global channels. A few spring to mind: Slack, Microsoft Teams, HipChat. I have seen project transform in unbelievable ways by something as trivial as a good chat program being introduced.

**Get people to know each other**. If you are lucky enough to be collocated with another teams, make sure that people know each other and are not afraid to talk. You can do that by different presentations and activities in the office and you can do it outside of the office. Organizing cross-team lunches, after work drinks, integration activities go long way. If your teams are not co-located- do what you can. Video conferencing can help.

**Celebrate each other successes.**Amazing things happen when people share each other successes. You need a mindset that one teams success is also another teams success. You are in it together. Once people start seeing it this way, they will naturally start collaborating more.

There are more ways to foster good communication and they probably require their own blog post!

### Automation as a mean of achieving independence

Assuming that you have the team structures and communication solved-what more can be done to promote independence? I have noticed that one thing that helps a team become independent is automation.

Automation of testing, automation of deployment, automation of admin processes. The more things you can automate the less you need to rely on people. Often overworked people, that are not part of your team. Whenever your team relies on someone from outside of the team to do something- see if this can be automated to remove the dependency. Chances are that all parties involved will be happy.

### The importance of a long term vision

The last thing to mention is that there should be a long term vision/goal available to the team. It is great when the team is truly independent, but the team should never lose the sight of what the company is trying to achieve. Every team should be aware of why what they are delivering is important and how the future looks like. This will not only motivate the team, but also prevent them from making mistakes by taking a decision that may jeopardize the future goals of the project.

### Summary

Building teams is a large topic. There are whole books being written on the subject. I hope this article gives you an idea about the importance of having great teams and gives you some ideas where to look for improvements. Working as a part of high performing team is among the most rewarding experiences I had as a software developer. I hope you will have that experience too. If you are in a position to build such teams- make it happen. Great software is delivered by great teams.
