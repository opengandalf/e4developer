---
title: "Spring Data - Microservices Data Companion"
date: 2018-05-05T00:00:00Z
draft: false
description: "Spring Data is one of the flagship projects of the Spring ecosystem. If you need to work with data- be it SQL, non-SQL, using map-reduce or other…"
categories: ["Microservices", "Spring Boot"]
cover:
  image: "images/spring-data.jpg"
  alt: "Spring Data - Microservices Data Companion"
aliases:
  - "/2018/05/05/spring-data-microservices-data-companion/"
ShowToc: true
TocOpen: false
---![](images/spring-data.jpg)

Spring Data is one of the flagship projects of the Spring ecosystem. If you need to work with data- be it SQL, non-SQL, using map-reduce or other, Spring Data most likely has you covered. In this article, I will introduce the Spring Data project and explain how it makes writing microservices easier.

Working with data is at the core of software development. This *data* can be in different forms:

- Relational / SQL Database
- NoSQL Database
- Graph Databases (like Neo4j)
- LDAP records
- Distributed cache technologies (Redis)
- Other technologies and variations of the above

How great would it be to have a single technology that you could rely on when dealing with any of the above? Well, it is your lucky day- **Spring Data can help you with all these and more**!

## Overview of Spring Data

Spring Data is an umbrella project. It contains multiple different projects that will help you to integrate with any of the aforementioned data sources.

The project provides a common way of building these integrations. The [official project site](http://projects.spring.io/spring-data/) states:

> Spring Data’s mission is to provide a familiar and consistent, Spring-based programming model for data access while still retaining the special traits of the underlying data store.

Before going into details, let’s see what makes Spring Data particularly useful for microservices architectures.

## Why is Spring Data good for microservices?

**Seamless integration with Spring Boot** – This is itself is a killer feature. Knowing how popular Spring Boot is, having the project integrate with it well will make any developers life easier.

**A large number of technologies supported** – Because of all the different technologies that are supported, using Spring Data brings familiarity to often complicated and not commonly known technologies. Different microservices often interact with different databases in unique ways.

**Focus on usability and brevity** – One of the big principles behind microservices is being micro… We don’t want to have an overwhelming configuration to deal with each time we build a new service. Spring Data coupled with Spring Boot really helps here.

I have written an [article](http://blog.scottlogic.com/2016/11/22/spring-boot-and-mongodb.html) in 2016 for Scott Logic showcasing how easy it makes working with MongoDB. In a workshop I ran, I was able to get all the integration up and running with live coding under 45 minutes while explaining every step!

## Common Integrations

To really understand why Spring Data is so useful, here are a few examples of how easily we can integrate with Spring Boot, Data, and a few popular database technologies.

### Spring Data and MongoDB

MongoDB is a very popular database. Let’s see how easy is to have Spring Data work with it.

We start by adding the required dependency to POM:

```

<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>

```

Now we can define the class representing data that we want to store. Let’s create a *Product* class:

```

public class Product {

    @Id
    public String id;

    public String name;
    public String description;

    public Product () {}

    public Product (String name, String description) {
        this.name = name;
        this.description= description;
    }
}

```

With Spring Data *Repositories* you can define additional methods for retrieving and working with objects:

```

public interface ProductRepository extends MongoRepository<Product, String> {

    public List<Product> findByName(String name);

}

```

This repository can later be used in the following fashion:

```

@Autowired
private ProductRepository repository;

//Listing all products
repository.findAll();
//Finding products by name
repository.findByName(someName);
//Saving products
repository.save(product);

```

The connection details can be easily configured as necessary in the usual Spring Boot way.

### Spring Data and MySQL

MySQL, being a very popular SQL database, will serve as our example for the *common integration number two.*

```

<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
	<groupId>mysql</groupId>
	<artifactId>mysql-connector-java</artifactId>
</dependency>

```

The Class changes only slightly from the MongoDB example, to accommodate the JPA specific *@Entity* and *@GeneratedValue* annotation.

```

@Entity
public class Product {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    public String id;

    public String name;
    public String description;

    public Product () {}

    public Product (String name, String description) {
        this.name = name;
        this.description= description;
    }

}

```

The MySQL repository will extend the interface *CrudRepository*rather than *MongoRepository*. *MongoRepository*is a specialization of *CrudRepository.*

```

public interface ProductRepository extends CrudRepository<Product , Long> {

}

```

**Using this MySQL based repository is pretty much identical to the way we used the MongoDB one**. This is one of the great benefits of Spring Data in action!

```

@Autowired
private ProductRepository productRepository;

productRepository.findAll();
productRepository.save(someProduct);

```

You can configure the connectivity to the MySQL database with Spring Boot properties.

### Common Integration Summary and Further Reading

MongoDB and MySQL served here as examples for the point I am trying to make. You can use SQL and NoSQL databases in very similar fashion with Spring Data. The familiarity Spring Data brings really helps developers to become *database agnostic.*

You can find further details on working with MongoDB and MySQL here:

- [Accessing Data with MongoDB](https://spring.io/guides/gs/accessing-data-mongodb/) by Spring.io
- [Accessing Data with MySQL](https://spring.io/guides/gs/accessing-data-mysql/) by Spring.io

## Familiar syntax with unfamiliar technologies

One of the big benefits of using Spring Data is how well different and innovative technologies get integrated with the project. It makes learning new things feel familiar. Let’s have a look at Neo4J as an example.

### Spring Data and Neo4j

This time we require a single dependency:

```

<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-neo4j</artifactId>
</dependency>

```

Defining entities is quite different because the concepts from Neo4j are slightly different to those in more traditional databases.

```

@NodeEntity
public class Product {

    @Id
    @GeneratedValue
    public String id;

    public String name;
    public String description;

    public Product () {}

    public Product (String name, String description) {
        this.name = name;
        this.description= description;
    }

    @Relationship(type = "COMPATIBLE", direction = Relationship.UNDIRECTED)
    public Set<Product> compatibleProducts;

    public void compatibleWith(Product product) {
        if (compatibleProducts == null) {
            compatibleProducts = new HashSet<>();
        }
        compatibleProducts.add(product);
    }
}

```

From this point onward things get extremely similar. You define *CrudRepository*the same you would do it for MySQL and you can interact with the repository through the same interface. The configuration is handled by setting Spring Boot properties.

Overall, using Neo4j with Spring Data feels very close to using it with any other database. This is a common theme with Spring Data. While you can rely on the specializations that different data technologies bring, what can be done in a common way is done in a common way.

## Summary

Using Spring Data bring multiple benefits to your project. You get the ease of development and a multitude of well-supported integrations. If you are already using Spring Boot, I don’t see why you would not make use of Spring Data. If you are not using Spring Boot, Spring Data gives yet another reason to start!
