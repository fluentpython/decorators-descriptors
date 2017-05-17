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


class Customer:

    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("'email' must be of type 'str'")
        elif len(value) == 0:
            raise ValueError("'email' must not be empty")
        self.__email = value

    def full_email(self):
        return '{0} <{1}>'.format(self.name, self.email)
