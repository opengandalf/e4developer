---
title: "How to write horrible Java"
date: 2018-05-13T00:00:00Z
draft: false
description: "I feel horrible today. I am sick- my throat hurts, my head is not working as it should. Hence, I decided I will tell you how to write horrible Java code."
categories: ["Career", "Java", "Personal"]
cover:
  image: "images/horrible-java.jpg"
  alt: "How to write horrible Java"
aliases:
  - "/2018/05/13/how-to-write-horrible-java/"
ShowToc: true
TocOpen: false
---![](images/horrible-java.jpg)

I feel horrible today. I am sick- my throat hurts, my head is not working as it should. Hence, I decided I will tell you how to write horrible Java code. If you are tired of all these beautiful patterns and best practices and you want to write something insane- read on. Maybe you like horror stories but in code- this may appeal to you!

If you are looking for advice on how to write good code- look elsewhere! Check my [review of *“Effective Java*“]({{< ref "/posts/effective-java-microservices-require-effective-java" >}}) and take it from there. Nothing nice is waiting for you in the following paragraphs… But if you are insisting on reading…

## Step 1 – Use Exceptions for everything

You know loops right? It is so easy to make an off by one error. When you are iterating a collection, it is easy to get this wrong…  Let’s see how we can use Java Exception handling to solve that issue and not worry at all about these pesky off-by-one errors!

```

public static void horribleIteration(String [] words){
    int i = 0;
    try {
        while(true){
            System.out.println(words[i]);
            i++;
        }
    } catch (IndexOutOfBoundsException e){
        //iteration complete
    }
}

```

## Step 2 – Don’t worry about access modifiers…

Access modifiers in Java… What a waste of time! Did you know that making something *private* is just a suggestion? If you want to edit it- go for it! Nothing is really stopping you (besides maybe lack of knowledge). If that’s the case, check out this amazing technique.

```

public static void readPrivate() throws NoSuchFieldException, IllegalAccessException {
    Field f = System.class.getDeclaredField("lineSeparator");
    f.setAccessible(true);
    String separator = (String) f.get(System.class);
    System.out.println("Line separator is " + separator + ".");
}

```

We are reading *lineSeparator* here, which well… is not that exciting. Changing that *lineSeparator* yields much more fun! Look what happens to *System.out.println* after we change lineSeparator in this code:

```

public static void readWritePrivate() throws NoSuchFieldException, IllegalAccessException {
    Field f = System.class.getDeclaredField("lineSeparator");
    f.setAccessible(true);
    String separator = (String) f.get(System.class);
    System.out.println("Line separator is " + separator + ".");

    f.set(System.class ,"!!!");
    System.out.println("Line one");
    System.out.println("Line two");
    System.out.println("Line three");
}

```

The output is:

```

Line separator is 
WARNING: All illegal access operations will be denied in a future release
.
Line one!!!Line two!!!Line three!!!

```

Looking good to me!

## Step 3 – Nothing is *really* final in Java…

Some developers think that they have said their final word by dropping the *final* keyword in front of a variable… The truth is- sometimes you really want to change a value of a *final* field. I am not here to judge (actually- read the title, maybe I am), so here is how to do it:

```

public static void notSoFinal() throws NoSuchFieldException, IllegalAccessException, InterruptedException {
    ExampleClass example = new ExampleClass(10);
    System.out.println("Final value was: "+ example.finalValue);
    Field f = example.getClass().getDeclaredField("finalValue");
    Field modifiersField = Field.class.getDeclaredField("modifiers");
    modifiersField.setAccessible(true);
    modifiersField.setInt(f, f.getModifiers() & ~Modifier.FINAL);
    f.setInt(example, 77);
    System.out.println("Final value was: "+ example.finalValue);
}

public static class ExampleClass {
    final int finalValue;

    public ExampleClass(int finalValue){
        this.finalValue = finalValue;
    }
}

```

Word of caution (*ha ha ha!*) this worked for me when supplying the final value in a constructor. If you have the final value set in the class, then it does not work. The code executes fine, but the value is not changed. Probably some compiler-level optimization spoiling all the fun!

## Step 4 – Use Java serialization. Just do it.

This one is simple. Serialize with Java. Have fun. Enjoy it.

Ok, I guess you want some justification. Last Friday I saw [Mark Reinhold](https://twitter.com/mreinhold) – Chief Architect of Java Platform say that they regret putting Serialization in Java. Apparently, around 1/3 security flaws in Java come from Serialization alone. Also, we are meant to use JSON, or databases or something like that… In my opinion, the guy doesn’t know what he is talking about!

Go ahead, rely on Java serialization.

## Step 5 – Use Object for everything

You know Classes right? Waste of time! Do you want to see a pinnacle of code reuse? There you go!

```

public static void printThings (List things){
    int i = 0;
    try {
        while(true){
            System.out.println(things.get(i));
            i++;
        }
    } catch (IndexOutOfBoundsException e){
        //iteration complete
    }
}

List superList = new ArrayList();
superList.add(7);
superList.add("word");
superList.add(true);
superList.add(System.class);
printThings(superList);

```

Can you believe we had that power for all this time? Also, bonus point for combining two patterns!

This is just the beginning of what you can do with Object. Remember if in doubt- use Object. You can always cast back if needed with this amazing pattern!

```

public static void printThingsUppercaseStrings (List things){
    int i = 0;
    try {
        while(true){
            Object o = things.get(i);
            System.out.println(o);
            if(o.getClass() == String.class){
                String so = (String) o;
                so = so.toUpperCase();
                System.out.println(so);
            }
            i++;
        }
    } catch (IndexOutOfBoundsException e){
        //iteration complete
    }
}

```

And this is type-safe. What a robust solution.

## Step 6 – Fully embrace the art of convenient programming

Did you know that Bill Gates prefers lazy developers? Bill actually said:

> “hire a lazy person to do a difficult job (…)because a lazy person will find an easy way to do it”

So with that glaring endorsement of Bill Gates, we can fully embrace our laziness. Are you ready? Here we go!

- **Never write tests, just don’t write bugs!**
- **Make everything public – convenient access!**
- **Favor global variables – you may need them!**
- **Prefer large interfaces to small specialized ones – the more methods you can use the better!**
- **Favor inheritance over composition (with default methods in interfaces it has never been easier)!**
- **Always use boxed primitives – they work as Objects as well (Step 5)!**
- **Use the shortest names possible for everything *(a,* *b, val* are great)!**

## Step 7 – Don’t learn anything new – you always know best

The most important quality a programmer can have is faith in himself. Ideally, a blind faith that she knows everything best and there is nothing more to learn!

With that in mind, make sure to never learn:

- **New libraries**
- **New languages**
- **New frameworks**

It will save you time! You should never learn anything new, as you are already the best.

### Disclaimer:

I am really sick. After reading these steps make sure to read the title again: *“How to write horrible Java”.* To close this article off, let’s remember this English phrase:

> Just because you can doesn’t mean you should
