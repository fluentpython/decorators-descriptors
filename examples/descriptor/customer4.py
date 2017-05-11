"""
A client with name and e-mail:

    >>> jack = Customer('John Robinson', 'jack@rob.org')
    >>> jack.full_email()
    'John Robinson <jack@rob.org>'

A client cannot be created with a blank e-mail:

    >>> joe = Customer('Joseph Blow', '')
    Traceback (most recent call last):
      ...
    ValueError: 'NonBlank' must not be empty
    >>> joe = Customer('Joseph Blow', 'joe@blow.up')
    >>> joe.full_email()
    'Joseph Blow <joe@blow.up>'

Assigning a blank e-mail later is not allowed either:

    >>> joe.email = ''
    Traceback (most recent call last):
      ...
    ValueError: 'NonBlank' must not be empty

`NonBlank` fields must also be strings:

    >>> dummy = Customer('Buster', 99)
    Traceback (most recent call last):
      ...
    TypeError: 'NonBlank' must be of type 'str'

The `NonBlank` field values are stored in specially named
`Customer` instance attributes:

    >>> for key, value in sorted(jack.__dict__.items()):
    ...     print('{:>10} : {!r}'.format(key, value))
    NonBlank_0 : 'John Robinson'
    NonBlank_1 : 'jack@rob.org'
      fidelity : 0

"""


class NonBlank:
    field_count = 0

    def __init__(self):
        cls = self.__class__
        self.storage_name = '%s_%s' % (cls.__name__, cls.field_count)
        cls.field_count += 1

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("'NonBlank' must be of type 'str'")
        elif len(value) == 0:
            raise ValueError("'NonBlank' must not be empty")
        instance.__dict__[self.storage_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)


class Customer:

    name = NonBlank()
    email = NonBlank()

    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    def full_email(self):
        return '{0} <{1}>'.format(self.name, self.email)
