---
title: "Java 9 to 12 - all the language modifications"
date: 2019-03-26T00:00:00Z
draft: false
description: "We have all had quite a lot of time to get familiar with Java 8 and all the amazing features that it provided us with. Since then quite a lot have happened…"
categories: ["Java"]
cover:
  image: "images/java-9-12.jpg"
  alt: "Java 9 to 12 - all the language modifications"
aliases:
  - "/2019/03/26/java-9-to-12-all-the-language-modifications/"
  - "/java-9-to-12-all-the-language-modifications/"
ShowToc: true
TocOpen: false
---We have all had quite a lot of time to get familiar with Java 8 and all the amazing features that it provided us with. Since then quite a lot have happened, with the release of Java 9, 10, 11 and this month 12 it is hard to stay on top of all the language changes happening! In here I will **focus exclusively on the changes to the language** leaving library changes to other writers.

It is important to know the new APIs and libraries introduced, but knowing how to read the language is vital. This will also make this blog post within a reasonable scope- after all, really a lot changed from Java 8 to Java 12! Without further ado- let’s begin, version by version!

## Java 9 – Project Jigsaw and the rise of Modules

The headline feature of Java 9 was the **introduction of Modules** (Project Jigsaw). At the top level of the project, you can define a *module-info.java* file that looks something like this:

```

module com.e4developer.modules.tricks {
    requires com.e4developer.modules.secret.sauce;
    exports com.e4developer.modules.tricks.trade;
}

```

And this will let you modularise your application better. If you are interested in this concept, you probably need quite a lot more than this short paragraph, but this should give you an idea.

Java 9 also introduced **private methods in interfaces**. This makes writing lengthy default interface methods somewhat more pleasant, but then again- you should be careful with this in the first place… Interface default methods should be used primarily for ensuring backwards compatibility of your APIs. Here you have a trivial example:

```

private interface:

public interface Spaceship {

    default void keepTalking(){
        System.out.println(makeText());
    }

    default void keepShouting(){
        System.out.println(makeText().toUpperCase());
    }

    /**
     * Be careful with private methods in interfaces.
     * Main place for implementation is inside classes.
     * @return
     */
    private String makeText(){
        String message = "hey there!";
        while(message.length() < 1000)
            message += message;

        return message;
    }
}

```

We can **use a diamond operator with anonymous inner classes** making this legal:

```

SuperCalculator<Integer> superCalculator 
    = new SuperCalculator() { //implementation
    };

```

And try with resources does not need a variable explicitly declared in the statement. This slightly improves the style:

```

FinalResource finalResource= new MyFinalResource();
try (finalResource) {
    // use finalResource
}

```

## Java 10 – introducing “var”‘

Java 10 focused mostly on adding and removing APIs, so it reads rather easily… There is only one large language change- **adding local-variable type inference – aka. “var” keyword**. With this you can make some of your code have a somewhat more *modern* feel and look to it:

```

var myABC= List.of("a", "b", "c");
var numbers= List.of(1, 2, 3);

for (var letter : myABC) {
    System.out.println(letter);
}

for (var i= 0; i< 100; i++){
    System.out.println(i);
}

```

## Java 11 – “var” support in lambdas

Java 11 introduced full *var* support into lambdas. Previously you could write this:

```

(Integer a, Integer b) -> a + b

```

Now, this is also allowed:

```

(var a, var b) -> a + b

```

Language-wise, everything stays the same.

## Java 12 – the new switch statement

Java 12 brings us the new, much-improved syntax for the switch statement. I will use an [example from the official documentation](https://openjdk.java.net/jeps/325) here. Consider the following switch statement:

```

switch (day) {
    case MONDAY:
    case FRIDAY:
    case SUNDAY:
        System.out.println(6);
        break;
    case TUESDAY:
        System.out.println(7);
        break;
    case THURSDAY:
    case SATURDAY:
        System.out.println(8);
        break;
    case WEDNESDAY:
        System.out.println(9);
        break;
}

```

With Java 12 you can write it in a much cleaner way:

```

switch (day) {
    case MONDAY, FRIDAY, SUNDAY -> System.out.println(6);
    case TUESDAY                -> System.out.println(7);
    case THURSDAY, SATURDAY     -> System.out.println(8);
    case WEDNESDAY              -> System.out.println(9);
}

```

I think this is a nice addition to the language. We were meant to receive raw String literals in Java 12 but that was dropped from the release… Worry not Java 13 is just around the corner!

## Final thoughts

With the new release cadence of Java features it is challenging to be aware of everything that is changing. The reality is that most changes are API and libraries related and do not affect the fundamental way that Java is written.  Don’t despair, it is still possible to stay up to date with the new language features and to write good clean Java!
