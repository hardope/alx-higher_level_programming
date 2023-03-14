A test to for adding two inteter

Import Python module + collections
>>> import sys
>>> sys.path.insert(1, '../')
>>> lib = __import__("0-add_integer")
>>> add_integer = lib.add_integer

# Normal addition test
>>> add_integer(0)
98
>>> add_integer(-1)
97
>>> add_integer(10.5)
108

# Type Errors
>>> add_integer(10+5j)
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer([])
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer({})
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer(set())
Traceback (most recent call last):
...
TypeError: a must be an integer

>>> add_integer("")
Traceback (most recent call last):
...
TypeError: a must be an integer

# Two input addition type errors
>>> add_integer(10, 10+5j)
Traceback (most recent call last):
...
TypeError: b must be an integer
>>> add_integer(10, [])
Traceback (most recent call last):
...
TypeError: b must be an integer
>>> add_integer(10, {})
Traceback (most recent call last):
...
TypeError: b must be an integer
>>> add_integer(10, set())
Traceback (most recent call last):
...
TypeError: b must be an integer

>>> add_integer(10, "")
Traceback (most recent call last):
...
TypeError: b must be an integer
