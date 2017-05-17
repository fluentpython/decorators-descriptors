class LineItem(object):

    def __init__(self, description, weight, price):
        self.description = description
        self.set_weight(weight)
        self.price = price

    def subtotal(self):
        return self.get_weight() * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
