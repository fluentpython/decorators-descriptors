class NonBlank:

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("%r must be of type 'str'" % self.storage_name)
        elif len(value) == 0:
            raise ValueError("%r must not be empty" % self.storage_name)
        instance.__dict__[self.storage_name] = value


def named_fields(cls):
    for name, attr in cls.__dict__.items():
        if isinstance(attr, NonBlank):
            attr.storage_name = name
    return cls
