class NonBlank:

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("%r must be of type 'str'" % self.storage_name)
        elif len(value) == 0:
            raise ValueError("%r must not be empty" % self.storage_name)
        instance.__dict__[self.storage_name] = value


class ModelMeta(type):

    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)

        for name, attr in dic.items():
            if isinstance(attr, NonBlank):
                attr.storage_name = name


class Model(metaclass=ModelMeta):
    """Inherit from this class to use NonBlank"""
