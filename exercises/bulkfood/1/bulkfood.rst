========
Scenario
========

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import LineItem
	>>> raisins = LineItem('Golden raisins', 5, 2.48)
	>>> raisins.description, raisins.weight, raisins.price
	('Golden raisins', 5, 2.48)
	>>> raisins.subtotal()
	12.4


Current implementation
======================

.. literalinclude:: bulkfood.py
   :linenos:


The problem
===========

The ``LineItem`` attributes are not validated, leading to trouble::

	>>> raisins.weight = -10
	>>> raisins.subtotal()
	-24.8

Now the customer will be credited with that amount...
