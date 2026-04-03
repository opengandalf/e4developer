---
title: "Introducing JSON-B with Spring Boot 2.0"
date: 2018-03-04T00:00:00Z
draft: false
description: "JSON Binding (JSON-B) is the new Java EE standard for converting JSON messages to Java Objects and back. See how it can be used in Spring Boot 2.0 and how does it compare to Jackson and GSON that are already available for some time."
categories: ["Microservices", "Spring Boot"]
cover:
  image: "images/cropped-e4-dev-twitter.png"
  alt: "Introducing JSON-B with Spring Boot 2.0"
aliases:
  - "/2018/03/04/introducing-json-b-with-spring-boot-2-0/"
ShowToc: true
TocOpen: false
---JSON Binding (JSON-B) is the new Java EE specification for converting JSON messages to Java Objects and back. JSON is used everywhere and so far we had two main ways of dealing with JSON conversion in Java- using either Jackson or GSON. With the introduction of JSON-B, we have a standard way of handling this conversion. In this article, we will see how Spring Boot 2.0 supports JSON-B, how easy it is to use it and how does it compare with the other options.

If you want to know more about JSON-B itself, you can visit the [official website](http://json-b.net/index.html) or read the four parts [Getting started with the JSON API](https://www.ibm.com/developerworks/java/library/j-javaee8-json-binding-1/index.html) by IBM. I found the [fourth part comparing JSON-B, Jackson, and GSON](https://www.ibm.com/developerworks/java/library/j-javaee8-json-binding-4/index.html) very interesting. Now it is time to see JSON-B in action!

### Converting Java Objects to JSON with Spring Boot 2.0 and JSON-B

How do you get JSON-B to work with Spring Boot 2.0? It is very simple. You need to add the required Maven dependencies:

```

<dependency>
	<groupId>javax.json.bind</groupId>
	<artifactId>javax.json.bind-api</artifactId>
	<version>1.0</version>
</dependency>
<dependency>
	<groupId>org.eclipse</groupId>
	<artifactId>yasson</artifactId>
	<version>1.0</version>
</dependency>
<dependency>
	<groupId>org.glassfish</groupId>
	<artifactId>javax.json</artifactId>
	<version>1.1</version>
</dependency>

```

And you need to choose the `preffered-json-mapper` setting to make sure that JSON-B is chosen. You may get GSON or Jackson on the classpath and then you can’t be sure how the autoconfiguration will work without this setting:

```

spring.http.converters.preferred-json-mapper=jsonb

```

With that in place, we are going to write a simple Rest Controller and a simple Car Class, that will make use of the JSON-B conversion:

```

package com.e4developer.jsonbexample;

import org.springframework.web.bind.annotation.*;

import java.util.Calendar;
import java.util.Optional;

@RestController
public class SimpleController {

    private Car makeCar() {
        Car newCar = new Car();
        newCar.make = "e4Cars";
        newCar.model = "theSensible";
        newCar.bonusFeatures = Optional.empty();
        newCar.price = 6000;
        newCar.productionDate = new Calendar.Builder().setDate(2018, 3, 3).build();
        return newCar;
    }

    @GetMapping("/car")
    public Car car() {
        Car newCar = makeCar();
        return newCar;
    }
}

```

```

package com.e4developer.jsonbexample;

import java.util.Calendar;
import java.util.Objects;
import java.util.Optional;

public class Car {
    public String make;
    public String model;
    public int price;
    public Calendar productionDate;
    public Optional<String> bonusFeatures;

    @Override
    public String toString() {
        return "Car{" +
                "make='" + make + '\'' +
                ", model='" + model + '\'' +
                ", price=" + price +
                ", productionDate=" + productionDate +
                ", bonusFeatures=" + bonusFeatures +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Car car = (Car) o;
        return price == car.price &&
                Objects.equals(make, car.make) &&
                Objects.equals(model, car.model) &&
                Objects.equals(productionDate, car.productionDate) &&
                Objects.equals(bonusFeatures, car.bonusFeatures);
    }

    @Override
    public int hashCode() {
        return Objects.hash(make, model, price, productionDate, bonusFeatures);
    }
}

```

Now let’s see how the response from that endpoint looks like:

```

{
    "make": "e4Cars",
    "model": "theSensible",
    "price": 6000,
    "productionDate": "2018-04-03T00:00:00+01:00[Europe/London]"
}

```

It is worth noting a few things. Treatment of the `Calendar` is specific to JSON-B specification and so is the simple disappearing of the missing `Optional`. I think the treatment of these two concepts is quite clean here.

The equivalent response with GSON would be:

```

{
    "make": "e4Cars",
    "model": "theSensible",
    "price": 6000,
    "productionDate": {
        "year": 2018,
        "month": 3,
        "dayOfMonth": 3,
        "hourOfDay": 0,
        "minute": 0,
        "second": 0
    },
    "bonusFeatures": {}
}

```

Note the different treatment of the `Calendar` and the quite peculiar thing that happens to `Optional`. It is not quite `null`, but not quite an Object either.

And with Jackson:

```

{
    "make": "e4Cars",
    "model": "theSensible",
    "price": 6000,
    "productionDate": "2018-04-02T23:00:00.000+0000",
    "bonusFeatures": null
}

```

Again, the `Calendar` is treated differently and the treatment of `Optional` at least can be seen as sensible- it is clearly a `null`.

If you are interested in a more detailed comparison between JSON-B, GSON, and Jackson standards, I once again recommend [the IBM article dealing with the subject](https://www.ibm.com/developerworks/java/library/j-javaee8-json-binding-4/index.html).

I showed you these three different examples to really make a point here. There is a lot of value from an official standard that deals with converting Java to JSON. Of course, JavaEE championed standards were not always successful. The original EJBs were mostly a disaster (sorry if you liked them, but sadly they did not catch on). CDI beans were much better (although they did not get enough traction in my opinion). JPA was on the other hand very successful and it is still very popular.

I strongly believe that the JSR 367 (this is Java Specification Requests for JSON-B) is here to stay and will bring a lot of good to the JVM ecosystem. I think we all want a more united and more seamless JSON development experience in the Java world.

We will see now how these different libraries deal with JSON to Java conversion.

### Converting JSON to Java Objects

It is important for a converter to be able to convert both ways between Java Object and JSON without changing the object itself. With the new standard, I wanted to see how well it handles this task.

We will use the original `Car` Object, get the JSON from JSON-B, GSON, and Jackson and then feed it back with a POST to see how the recreated Object looks like. We will check the equality to the Original Object and inspect any potential changes in the payload when returned once again.

For that I wrote a simple Controller endpoint:

```

    @PostMapping("/sendCar")
    public Car sendCar(@RequestBody Car car){
        System.out.println("original car: "+makeCar());
        System.out.println("transformed car: "+car.toString());
        System.out.println("Is the car the same? "+ car.equals(makeCar()));
        return car;
    }

```

##### Conversion with JSON-B

JSON-B passes the simple test of returning the same JSON text that it is sent.

**JSON-B fails the equality check**! It turns out that JSON-B assigns a naked `null` rather than the Optional value to the field when it is not present in the JSON! This is very disappointing, as it may cause unexpected bugs. To be clear what happens is:

1. JSON-B deals with `Optional.empty()` by not including it in the JSON response.
2. When JSON parsed into Java Object does not have a value for an `Optional<>` field it assings it `null` rather than `Optional.empty()`
3. This breaks the idea of `Optional`

This is disappointing enough that I hope it will change in the future iterations of the standard.

##### Conversion with GSON

GSON passes the simple test of returning the same JSON text that it is sent.

GSON also passes the equality check! It correctly deals with the `Optional` and the `Calendar` cases.

##### Conversion with JACKSON

Jackson passes the simple test of returning the same JSON text that it is sent.

**Jackson fails the equality check!**While Jackson is correctly handling the `Optional` case it fails to deal with the `Calendar` correctly. It loses the Zone information (in my case London/Europe) and changes it to UTC. This simplification can cause unexpected bugs in different systems.

### Conclusion

I believe that JSON-B is a great idea for a new standard. JSON became so important that having Java community agree on a good way of dealing with it can be very helpful.

It is apparent that dealing with JSON to Java and back is not as trivial as it may seem. As demonstrated here, these conversions may end up causing some unexpected side effects. Personally, I would like JSON-B to be more like GSON- perhaps sacrifice human readability for a clear back to back conversion.

No matter which converter you chose, Spring Boot 2.0 makes it easy to use. I am looking forward to JSON-B entering the field as the third worthy contender for your JSON converter of choice.

The code used for this article is available on [my Github account](https://github.com/bjedrzejewski/jsonb-example).
