======
Step 5
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

Now ``weight`` and ``price`` are managed by instances of the ``Quantity``
descriptor, which does not accept negative values::

	>>> raisins.weight = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0
	>>> raisins.price = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

The values of ``price`` and ``weight`` are stored in each ``LineItem``
instance in attributes named by the descriptor class. These attributes
look like ``_quantity_«N»``::

	>>> dir(raisins) #doctest: +ELLIPSIS
	[...'_LineItem__price', '_LineItem__weight', ..., 'price', ..., 'weight']

In the ``LineItem`` class, the ``weight`` descriptor is declared first,
so we know its value is stored in the ``_quantity_0`` attribute::

	>>> raisins.weight
	5
	>>> raisins._LineItem__weight
	5
