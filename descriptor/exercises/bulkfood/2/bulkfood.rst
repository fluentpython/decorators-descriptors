======
Step 2
======

LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import LineItem
	>>> raisins = LineItem('Golden raisins', 5, 2.48)
	>>> raisins.description, raisins.get_weight(), raisins.price
	('Golden raisins', 5, 2.48)
	>>> raisins.subtotal()
	12.4

Now the weight is a protected attribute, and its setter method verifies that
the value is greater than 0::

	>>> raisins.set_weight(-10)
	Traceback (most recent call last):
		...
	ValueError: value must be > 0
