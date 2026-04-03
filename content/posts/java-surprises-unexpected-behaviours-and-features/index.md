---
title: "Java surprises - Unexpected behaviours and features"
date: 2018-10-28T00:00:00Z
draft: false
description: "Java is a very mature programming language – in fact, it is over 21 years old, so if it was a person it could drink even in the USA! With age comes wisdom…"
categories: ["Java"]
cover:
  image: "images/java-surprises.jpg"
  alt: "Java surprises - Unexpected behaviours and features"
aliases:
  - "/2018/10/28/java-surprises-unexpected-behaviours-and-features/"
ShowToc: true
TocOpen: false
---Java is a very mature programming language – in fact, it is over 21 years old, so if it was a person it could drink even in the USA! With age comes wisdom, but also with age comes quirkiness… at least sometimes. In this article, I will look at some of the more surprising and unexpected behavior and features of the language.

Here we go, in no particular order, a collection of Java surprises to amuse you and impress your friends!

## Java has goto and const keywords

While Java does not have *goto* it does reserve it as a keyword. The same is true for *const*. All it means is that you can’t name your variables using these names:

```

int goto = 0;
int const = 0;

```

is both illegal and won’t compile!

## Formatting numbers with \_

Java lets you use the *\_* character for padding out your numbers. Hence, you can write numeric values like this:

```

int thousand = 1_000;
double bigValue = 1_000_000.456_555;
long thisIsSilly = 3______4__3;

```

## Double.MIN\_VALUE is not what many assume

So, *Double.MAX\_VALUE* works pretty much as expected, giving you the value of: *1.7976931348623157E308*. What do you think *Double.MIN\_VALUE* gives you then? *4.9E-324*! Ok, for a start- this value is greater than 0!

*Double.MIN\_VALUE* returns the smallest Double value that is greater than 0. If you want the smallest Double value, you need to go with: *-Double.MAX\_VALUE*. They really could name these things a bit better. I wonder how many bugs this caused!

## Fun with Integer equality

Speaking of bugs… Let me show you something really disturbing:

```

Integer ten = Integer.parseInt("10");
System.out.println(ten == Integer.valueOf(10));
//this is true

Integer thousand = Integer.parseInt("1000");
System.out.println(thousand == Integer.valueOf(1000));
//this is false

```

Turns our that *Integer* objects are cached for values from -128 to 127. This means that when operating in this range, the *==* comparison will mostly work correctly. When going above it though- all bets are off!

Imaging, you could even write unit tests and all is good, as long as you are not using big enough numbers. This can cause serious bugs, so just to be safe- a reminder: When working with objects always, use *.equals()* rather than relying on *==* equality, unless you know for sure this is the right thing to do.

## Reflection lets you do (almost) anything

This should not come as a surprise, but with reflection, you can override final values (most of the time) and access private fields… But not always.

When writing my [How to write horrible Java]({{< ref "/posts/how-to-write-horrible-java" >}}) I found a case where overwriting final values does not work as expected. Constants in Java, when final will get inlined and even though your code will seem to have worked- no value will change. Magic (check [my article]({{< ref "/posts/how-to-write-horrible-java" >}}) for details and this [Stack Overflow answer](https://stackoverflow.com/questions/1615163/modifying-final-fields-in-java/2107976#2107976)).

Here is the code for overwriting finals if you insist:

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

```

## Did you know we have labels in Java?

Ok, we depart the naughty land and we are back in the good old correct Java. Did you know that we have labels for our loops? Have a look:

```

outerLoop:
while (true) {
    System.out.println("I'm the outer loop");
    while(true){
        System.out.println("I am the inner loop");
        break outerLoop;
    }
}

```

Using labels lets you *continue* or *break* a specific loop when dealing with nested loops… Kind of like *goto* would in a different language.

This let’s write a very suspicious looking code that compiles fine:

```

int i = 3;

http://www.e4developer.com
while(i > 0){
    System.out.println("http://www.e4developer.com");
    i--;
}

```

It compiles and works fine since it is simply a loop labeled *http:* with a comment attached to it. Makes for an interesting puzzle for those not familiar with labels!

## Enums are classes

Ok, you probably know about that, but it bears repeating. Enums are special classes that have a limited number of instances. That means that enums can:

- Implement interfaces
- Have constructors
- Implement different methods

I wrote an article for Scott Logic blog called [Java Enums – how to use them smarter](https://blog.scottlogic.com/2016/07/28/java-enums-how-to-use-them-smarter.html) where I show some other neat usage ideas.

## For loops are quite flexible

The standard for loop, I am sure that you used them more times than you can remember:

```

for(int i = 0; i < 100; i++){
    //...
}

```

Did you know that all parts are optional? You don’t need to initialize a variable, you don’t need a conditional stop and you don’t need to increment anything… If you omit everything you end up with an interesting syntax for an infinite loop:

```

for(;;){
    //Infinite loop!
}

```

## Java has initializers… Mentioning just in case…

Ok, this is a fairly popular feature, yet I still meet experienced Java developers who are not really aware that it exists. In Java, you can write blocks of code that run either on the class load (static initializers) or just before the constructor (standard initializers). It goes like this.

Normal initializer:

```

int sum = 0;
{
    for(int i = 0; i < 1; i++){
        sum += 1;
    }
}

```

Static initializer:

```

static double value = 0;
static {
    
    for(int i = 0; i < 1; i++){
        value += 1;
    }
}

```

Just remember to put these blocks inside the class, but not inside any methods or a constructor.

## Double braces initialization of collections

While on the topic of initializing things, I will show you a surprising way to initialize collections in Java:

```

Map<String, String> map = new HashMap<String, String>() {{
    put("it", "really");
    put("works", "!");
}};

Set<String> set = new HashSet<String>() {{
    add("It");
    add("works");
    add("with");
    add("other");
    add("collections");
    add("too");
}};

```

It is called double brace initialization in Java and I have never seen it used by anyone… Is it because hardly anyone knows about it?

…after publishing this article many readers were quick to let me know that this is a dangerous feature that should be avoided! Use the helpers methods like *List.of()* instead.

## Final value initialization can be postponed

It is a small thing, but some people assume that you have to initialize final values as you declare them. This is not the case. You just need to make sure that you initialize them only once. Check this valid code:

```

final int a;              
if(someCondition){        
    a = 1;                
} else {                  
    a = 2;                
}                         
System.out.println(a);   

```

This can get quite tricky when we mix in initializer blocks and other constructs.

## Joint union for extending generics

Despite a suspicious implementation (type erasure), generics are still quite powerful in Java. I was surprised that we are allowed to be very specific about the type of Generic we require. Have a look at this example:

```

public class SomeClass<T extends ClassA & InterfaceB & InterfaceC> 
{}

```

It can be quite useful when you are fussy about your T!

## Do you have more?

I hope you enjoyed my selection of Java trivia and curiosities. If you know other surprising features and behaviors that are worth sharing, be sure to let me know in the comments or on [Twitter](https://twitter.com/e4developer)!
