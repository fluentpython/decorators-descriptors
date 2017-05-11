======
Step 3
======

LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import LineItem
	>>> raisins = LineItem('Golden raisins', 5, 2.48)
	>>> raisins.description, raisins.weight, raisins.price
	('Golden raisins', 5, 2.48)
	>>> raisins.subtotal()
	12.4

Now weight is a property, so we can refer to it simply as ``raisins.weight``,
but assignment is managed by a setter method::

	>>> raisins.weight = -10
	Traceback (most recent call last):
		...
	ValueError: value must be > 0
