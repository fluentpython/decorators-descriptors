class Quantity(object):
    instance_counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__.lower()
        self.attr_name = '_%s_%s' % (prefix, cls.instance_counter)
        cls.instance_counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.attr_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem(object):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
