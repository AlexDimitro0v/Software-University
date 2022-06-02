# https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs


def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print(required_arg)

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args:    # If args is not empty.
        print(f"args: {args}")

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs:  # If kwargs is not empty.
        print(f"kwargs: {kwargs}")


"""
>>> func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() takes at least 1 argument (0 given)
"""


func("required argument")
# required argument

print('----------------------------------------------')
func("required argument", 1, 2, '3')
# required argument
# (1, 2, '3')

print('----------------------------------------------')
func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")
# required argument
# (1, 2, '3')
# {'keyword2': 'foo', 'keyword1': 4}

# NOTE: You can also use both in the same function definition but *args must occur before **kwargs.

print('----------------------------------------------')


# Note: positional arguments must come before keyword arguments
def f(*args, **kwargs):
    print(args)
    print(kwargs)


f()
