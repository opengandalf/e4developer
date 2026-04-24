---
title: "Please, stop writing so many “for loops” in Java!"
date: 2018-09-15T00:00:00Z
draft: false
description: "In this blog post, I want to take you back to basics and talk about Java for loops. To be honest, I am writing this blog post partially for myself…"
categories: ["Algorithms", "Java"]
cover:
  image: "images/loops.jpg"
  alt: "Please, stop writing so many “for loops” in Java!"
aliases:
  - "/2018/09/15/please-stop-writing-so-many-for-loops-in-java/"
  - "/please-stop-writing-so-many-for-loops-in-java/"
ShowToc: true
TocOpen: false
---In this blog post, I want to take you back to basics and talk about Java *for loops*. To be honest, I am writing this blog post partially for myself, as this is something that I am myself too often guilty of. Since Java 8, we don’t have to write so many *for loops* in Java! I hope this blog post will make your code nicer to read and quicker to write.

## What do you need a for loop for?

Broadly speaking there are two categories of tasks performed by for loops:

- **Iterating over collections**
- **Running algorithms**

For algorithms, a for loop may be appropriate. Have a look at this algorithm checking if a number is a power of three:

```

double number = 81;
for(; number > 1; number /=3);
return number == 1;

```

*For loop* is an appropriate construct here. This is a very simple example and as you can imagine, things can get much trickier with more difficult algorithms.

For most developers, in their day to day work, this is a minority of cases. Most of the time, we use *for loops* to iterate over collections. Let’s look at some examples of that code.

## Iterating over collections in Java

Let’s take a List<String> that contains some values.

```

List<String> heroes = new ArrayList<>();
heroes.add("SuperPerson");
heroes.add("WonderGirl");
heroes.add("LemurMan");
heroes.add("TimesTenDeveloper");
heroes.add("PandaFace");
heroes.add("CobraKid");
heroes.add("TShapedTeamMember");

```

There are many ways to iterate over it. Let’s start with the rather archaic *Iterator* approach:

```

Iterator<String> heroesIterator = heroes.iterator();
while (heroesIterator.hasNext()) {
    System.out.println(heroesIterator.next());
}

```

That looks really heavy weight. This kind of code gives Java its somewhat deserved reputation for verbosity.

Another try, this time with a classical indexed *for loops*:

```

for(int i = 0; i < heroes.size(); i++){
    System.out.println(heroes.get(i));
}

```

Well, this is a bit simpler to follow, but since Java 5 we have *for each loop* at our disposal:

```

for(String hero : heroes){
    System.out.println(hero);
}

```

This is where the most developers get stuck. This construct is so familiar and easy to follow, that most of us don’t bother to think about anything better. Java 8 is been available for a while though…

With Java 8 we can use a forEach function, making it very obvious what we are doing:

```

heroes.forEach(hero -> System.out.println(hero));

```

We can simplify it even further:

```

heroes.forEach(System.out::println);

```

I really like this, as it is very obvious that we are not running an algorithm with possibly a dynamic number of steps- we are just iterating over the elements of an array.

To be honest, I wish Java would allow us to also pass an index more easily with that style. Unfortunately, at the moment this is not possible:

```

//not legal Java!!!
heroes.forEach((hero , i) -> System.out.println(hero +" at "+i));

```

And if you want to keep using that style while accessing the index, you may need to resolve to less pretty:

```

IntStream.range(0, heroes.size())
        .forEach(i -> System.out.println(heroes.get(i) +" at "+i));

```

## Where to go next? Use Java Streams

Once you stop writing so many *for loops* in Java and *forEach* becomes a second nature, you should look at Streams in Java.

With a similar syntax, you can, for example, easily choose all heroes beginning with a letter ‘T’:

```

heroes.stream().filter(hero -> hero.startsWith("T"))
        .forEach(System.out::println);

```

This gives you the famous *“TimesTenDeveloper”* and the *“TShapedTeamMember”*.

## Summary

Stop writing so many *for loops*. Once you do, the Java 8 Streams will come as a natural step and your code will be easier to read and faster to write. What is not too like? Good luck!
