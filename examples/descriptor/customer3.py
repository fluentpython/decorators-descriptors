"""
A client with name and e-mail:

    >>> jack = Customer('John Robinson', 'jack@rob.org')
    >>> jack.full_email()
    'John Robinson <jack@rob.org>'

A client cannot be created with a blank e-mail:

    >>> joe = Customer('Joseph Blow', '')
    Traceback (most recent call last):
      ...
    ValueError: 'email' must not be empty
    >>> joe = Customer('Joseph Blow', 'joe@blow.up')
    >>> joe.full_email()
    'Joseph Blow <joe@blow.up>'

Assigning a blank e-mail later is not allowed either:

    >>> joe.email = ''
    Traceback (most recent call last):
      ...
    ValueError: 'email' must not be empty

`NonBlank` fields must also be strings:

    >>> dummy = Customer('Buster', 99)
    Traceback (most recent call last):
      ...
    TypeError: 'email' must be of type 'str'

"""


class NonBlank:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("%r must be of type 'str'" % self.storage_name)
        elif len(value) == 0:
            raise ValueError('%r must not be empty' % self.storage_name)
        instance.__dict__[self.storage_name] = value


class Customer:

    name = NonBlank('name')
    email = NonBlank('email')

    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    def full_email(self):
        return '{0} <{1}>'.format(self.name, self.email)
