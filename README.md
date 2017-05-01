# Decorators and descriptors decoded

## Description

Python developers use decorators and descriptors on a daily basis, but many don't understand them well enough to create (or debug) them. Decorators are widely deployed in popular Python Web frameworks. Descriptors are the key to the database mappers used with those frameworks, but under the covers they play an even more crucial role in Python as the device that turns plain functions into bound methods, setting the value of the `self` argument. This tutorial is a gentle introduction these important Python features, using a test-driven presentation and exercises.

Decorators without closures are presented first, highlighting the difference between _run time_ and _import time_ that is crucial when meta-programming. We then get a firm grounding on closures and how they are implemented in Python, before moving to higher order function decorators.

Coverage of descriptors starts with a close look at Python's `property` built-in function and dynamic attribute look up. We then implement some ORM-like field validation descriptors, encounter a usability problem, and leverage a class decorator to solve the issue. A metaclass appears briefly at the very end to make the solution transparent to our library users, while making the library maintainers life more _interesting_.


## Audience

This tutorial is aimed at intermediate Python programmers. Participants should have a few months of frequent, if not daily, Python practice. Browse the official Python Tutorial to see if you have basic blanks to fill.

After the tutorial, engaged participants should be able to create their own basic but useful decorators and descriptors, and know where to look for tools and resources to tackle more advanced implementations of those features.

## Outline

Note: 15' break between topics 3 and 4 (85' after session start)

0. Overview [5' total]
	* [1'] What we'll see 
   	* [2'] Review: functions as objects
	* [2'] Function introspection
1. Introducing decorators [25' total]
	* [1'] What happens when: _import time_ versus _run time_
	* [10'] __EXERCISE__: code evaluation order
	* [5'] Registration decorators: the simplest kind
	* [9'] Case study: function-based __Strategy__ pattern
2. Closures [25' total] 
	* [2'] How Python decides variable scopes in the absence of declarations
	* [5'] The `global` and `nonlocal` declarations
	* [8'] Practical applications of closures
	* [10'] __EXERCISE__: a higher-order function to compute a running average
3. Behavior-changing decorators [30' total] 
	* [5'] Decorators in the standard library
	* [5'] Implementing a simple decorator
	* [10'] __EXERCISE__: enhancing the stopwatch decorator
	* [5'] Parametrized decorators
	* [5'] Introduction to class-based decorators
	* __EXERCISE__: refactoring from nested functions to class-based
4. Properties [30' total] 
	* [2'] Protected attributes
	* [4'] A simple property
	* [2'] Full signature of the `property` built-in
	* [10'] __EXERCISE__: property for attribute validation
	* [2'] Properties overriding instance attributes
	* [10'] A property factory
5. Descriptors [30' total]
	* [8'] A descriptor for attribute validation
	* [10'] __EXERCISE__: debugging a descriptor
	* [8'] The value storage problem
	* [3'] Overriding and non-overriding descriptors
	* [1'] Methods as descriptors
6. Putting it all together [20' total]
	* [1'] Making decorators aware of their assigned attributes
	* [9'] Decorator-based API for the validating descriptors
	* [10'] Metaclass-based API for the validating descriptors

