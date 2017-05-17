class Quantity(object):

    def __get__(self, instance, owner):
        return getattr(instance, self.target_name)

    def __set__(self, instance, value):
        if not hasattr(self, 'target_name'):
            self.set_target_names(instance)
        if value > 0:
            setattr(instance, self.target_name, value)
        else:
            raise ValueError('value must be > 0')

    def set_target_names(self, instance, owner=None):
        owner = owner if owner else instance.__class__
        for key, attr in owner.__dict__.items():
            if hasattr(attr, 'set_target_names'):
                setattr(attr, 'target_name', '_%s__%s' % (owner.__name__, key))

class LineItem(object):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
