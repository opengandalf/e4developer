---
title: "AWS IAM - Looking at some of the more advanced features"
date: 2019-07-28T00:00:00Z
draft: false
description: "AWS Identity and Access Management (IAM) is one of the most important services available in AWS. Most people know that you can create user accounts and assign…"
categories: ["AWS", "DevOps"]
cover:
  image: "images/aws-iam.jpg"
  alt: "AWS IAM - Looking at some of the more advanced features"
aliases:
  - /aws-iam-looking-at-some-of-the-more-advanced-features/
  - "/2019/07/28/aws-iam-looking-at-some-of-the-more-advanced-features/"
ShowToc: true
TocOpen: false
---AWS Identity and Access Management (IAM) is one of the most important services available in AWS. Most people know that you can create user accounts and assign permissions (policies). In this blog post, I will look at a few more advanced features of the AWS IAM.

## AWS policies can have conditions

AWS policies can have conditions. That means that you can apply a policy that would only work in a specific time window. This can be for example next Wednesday between 1 pm and 4 pm if you expect a user to need specific permission around this time. In general, you can use these conditions to grant and revoke permissions to do things at specific dates and times.

An example policy condition that gives access in a specific time window will look as follows:

```

"Condition" :  {
      "DateGreaterThan" : {
         "aws:CurrentTime" : "2019-07-31T13:00:00Z"
       },
      "DateLessThan": {
         "aws:CurrentTime" : "2019-07-13T16:00:00Z"
       }
}

```

Of course, if it was only about dates and times it would not be very exciting, you can also set the conditions around things such as:

- Usernames
- Source IPs
- SSL being used (to ensure only secure requests are respected)
- Tag keys (to further customise conditions)
- And some more as described here: <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html>

It is important to be aware of these possibilities, as setting tight access control is the best way of avoiding your account being damaged, or compromised.

Another significant benefit of these conditions is reducing the manual workload of granting and revoking permissions when you know the access need in advance.

## AWS policies can be dynamic

Imagine a scenario when you want to give IAM users *“home directories”* in S3. If you are not aware of AWS dynamic policies it may look like you need to create everyone a policy with something like:

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": ["s3:ListBucket"],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::homes"],
      "Condition": {"StringLike": {"s3:prefix": ["Bartosz/*"]}}
    },
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::homes/Bartosz/*"]
    }
  ]
}

```

The good news is that AWS will let you create a policy like this:

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": ["s3:ListBucket"],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::homes"],
      "Condition": {"StringLike": {"s3:prefix": ["${aws:username}/*"]}}
    },
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::homes/${aws:username}/*"]
    }
  ]
}

```

That is much more maintainable, as it can be then saved as a managed policy and given to all the users that need it.

The same variables that you have seen used in conditions, can be generally used for making policies dynamic. Again, if you want to read some more official documentation on the topic, have a look here: <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html>

## Using separate AWS accounts is sometimes the right thing to do

One thing that confused me when I started using AWS in the real-world project was the idea of having multiple AWS accounts for different things. I assumed that given such a powerful IAM solution, we should use one account as much as possible. Wrong!

There are good reasons for using separate AWS accounts when there is a need for that. For example, is perfectly ok to have a separate development account and a production account to make the separation between resources as strong as possible.

You may want to have administrators on one account that have root-level access that you wouldn’t want to give that access on another account. It also makes sense when you have multiple strictly separate departments in your company.

I don’t want to go in-depth on every scenario here, as there are many. The point I want to make- if you feel like you may need another AWS account for something you could be right! Don’t necessarily reject the idea because we have a powerful IAM solution in AWS.

## AWS roles can work better than accounts and policies

Ok, so you have multiple accounts in your organisation now, but you would like to share some resources between them. One way would be to use bucket policies. This sounds easy enough, but there is a problem. When an S3 object is created, the account that owns the bucket does not own the object. This is often not what you want.

In this and many other scenarios, the solution is to use AWS cross-account role. With this, you give an IAM user from another account a role that they can assume in your account. That will let you manage the permissions from IAM and retain ownership of the objects without resolving to hacks such as requiring explicit permission grants in IAM policies.

This may sound a bit complicated, but again the most important here is the general message. Creating IAM roles that can be assumed across accounts is often the most maintainable, safe and easy way to deal with sharing resources across accounts.

## Summary

AWS IAM is a very powerful IAM solution. In order to manage a non-trivial AWS account properly, you should familiarise yourself with it in depth. On the other hand, you may already be proficient in IAM, but there could be features that you may not be aware of, that would make your life much easier.

No matter if you are just starting, or if you are an experienced AWS user, it is worth refreshing your AWS IAM knowledge now and then! I will leave you with a link to the official documentation: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>

Let me know if you have a favourite AWS IAM feature that you rely on.
