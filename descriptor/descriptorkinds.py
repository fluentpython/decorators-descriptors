

"""
Non-overriding descriptor (a.k.a. shadowable descriptor):

    >>> o = Model()
    >>> o.nonover  # doctest: +ELLIPSIS
    --> NonOverriding.__get__ invoked
    'value of an attribute in instance <descriptorkinds.Model object at 0x...>'
    >>> Model.nonover  # doctest: +ELLIPSIS
    --> NonOverriding.__get__ invoked
    <descriptorkinds.NonOverriding object at 0x...>

A non-overriding descriptor can be shadowed by assigning to an instance:

    >>> o.nonover = 7
    >>> o.nonover
    7

Overriding descriptor (a.k.a. enforced descriptor):

    >>> o.over  # doctest: +ELLIPSIS
    --> Overriding.__get__ invoked
    'value of an attribute in instance <descriptorkinds.Model object at 0x...>'
    >>> Model.over  # doctest: +ELLIPSIS
    --> Overriding.__get__ invoked
    <descriptorkinds.Overriding object at 0x...>

An overriding descriptor cannot be shadowed by assigning to an instance:

    >>> o.over = 7
    --> Overriding.__set__ invoked
    >>> o.over  # doctest: +ELLIPSIS
    --> Overriding.__get__ invoked
    'value of an attribute in instance <descriptorkinds.Model object at 0x...>'

Methods are non-overriding descriptors:

    >>> o.spam  # doctest: +ELLIPSIS
    <bound method Model.spam of <descriptorkinds.Model object at 0x...>>
    >>> Model.spam  # doctest: +ELLIPSIS
    <function Model.spam at 0x...>
    >>> o.spam()
    'result of calling .spam()'
    >>> o.spam = 7
    >>> o.spam

"""


class NonOverriding:
    def __get__(self, instance, cls):
        print('--> NonOverriding.__get__ invoked')
        if instance is None:
            return self
        else:
            return 'value of an attribute in instance %r' % instance


class Overriding:
    def __get__(self, instance, cls):
        print('--> Overriding.__get__ invoked')
        if instance is None:
            return self
        else:
            return 'value of an attribute in instance %r' % instance

    def __set__(self, instance, value):
        print('--> Overriding.__set__ invoked')


class Model:
    nonover = NonOverriding()
    over = Overriding()

    def spam(self):
        return 'result of calling .spam()'
