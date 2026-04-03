---
title: "Helping your team - Start using pull request"
date: 2018-01-15T00:00:00Z
draft: false
description: "You should be using pull requests. This blog post contains guidance and advice on helping your team by introducing them to pull requests"
categories: ["Building teams"]
cover:
  image: "images/pulling-line.jpg"
  alt: "Helping your team - Start using pull request"
aliases:
  - "/2018/01/15/helping-your-team-start-using-pull-request/"
ShowToc: true
TocOpen: false
---For these teams already using pull requests (or merge requests as they are sometimes known), this advice seems trivial. For the teams that do not use them- it may not be so simple. Let me explain why you need and how to get started.

![](images/pulling-line.jpg)

### What is a Pull Request

Pull requests is effectively a request to get your code merged with the rest of the source code. If you are using git via Github, Bitbucket, Gitlab- you have an automatic support for them. If you are using something else, maybe even different version control system than git- you may need to do some research for an equivalent process.

### What do you get from Pull Request

The main benefit of doing a Pull Request is an organized, dedicated place for doing code reviews. Hopefully, you are already convinced that code reviews are important. I have seen people claiming that they are doing code reviews manually, or via some other process, but I have never seen anything as effective and simple as the Pull Request method. If you disagree and have something better let me know in the comments! I would love to know!

The other great benefit is improved history of the project. We all know that commits can have less than ideal messages and sometimes the big picture from a single commit is hard to see. What you get with a Pull Request is all the related commits put together with an overarching review and hopefully a decent explanation of the ultimate goal that they serve.

Pull Request also can serve as a quality gate before integrating developers code with the main code of the project. I’m talking here about the build and automated testing being started on the creation of a Pull Request. The benefits are quick to manifest themselves with much more stable codebase.

### Fears before introducing Pull Requests

I have seen the pull requests adoption a few times and there are often concerns raised. I will try to calm down the most common fears here:

- **This is a new process that will waste time:**I have never seen project takes more time and move slower after pull requests were introduced. Maybe at first it sounds tricky, but I found that virtually all developers quickly adopt it as their second nature. It is really quick and simple.
- **People will just end up blocking each other with conflicting changes:**This may happen, but it is either a problem that already exists in the team or misuse of the Pull Request process. If you have multiple people editing the exact same parts of the system- you are bound to have conflicts, Pull Requests just make them visible. You need to divide work better or explore ideas such as pair programming. If this really was not the case you may have developers creating gigantic 1000+ lines Pull Requests. This is not ideal, these should be small enough to be realistically reviewed and understood (of course there always can be a rare exception).
- **We already do code review and what is the point anyway?:**This is answered in the first part of the article!

### Summary and next steps

I hope that you have been convinced of the amazing utility that Pull Requests bring! I can’t recommend using them enough. If you want to get started you may want to:

- See how to deal with pull requests in your environment of choice:
  - Github: <https://help.github.com/articles/creating-a-pull-request/>
  - Bitbucket: <https://www.atlassian.com/git/tutorials/making-a-pull-request>
  - Gitlab: <https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html>
  - Anything else – should be easy to google that!
- Adopt some workflow with your pull requests. I recommend:
  - Gitflow, neatly explained here: <https://danielkummer.github.io/git-flow-cheatsheet/>
  - Github feature flow as explained here: <https://guides.github.com/introduction/flow/>
- Have a meeting with your team about giving it a go and try using them for a month or so. I don’t think you will be coming back!

Good luck with your pull requests!
