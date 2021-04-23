# Programmatically Accessing Docstrings
def func():
    """This is a function that does nothing at all"""
    return
# The docstrings can be accessed using the __doc__ attribute
print(func.__doc__)
help(func)
def greet(name, greeting ="Hello"):
    """Print a greeting to the user `name`

    Optional parameter `greeting` can change what they're greeted with."""
    print("{} {}".format(greeting, name))
help(greet)
# Write Documentation using docstrings
def hello(name):
    """Greet someone.

    print a greeting("Hello") for the person with the given name."""
    print("Hello "+name)
class Greeter:
    """An object used to greet people.

    It contains multiple greeting functions for several languages and times of the day"""
#  Syntax Convention
#  PEP 257
#  One-line Docstrings
def hello():
    """Say hello to your friends."""
    print("Hello my friends!")
#  Multi-line Docstrings
def hello(name, language="en"):
    """Say hello to a person.

    Arguments:
    name: The name of the person
    language: The language in which the person should be greeted"""
    print(greeting[language]+" "+name)
#  Sphinx
def hello(name, language="en"):
    """Say hello to a person

    :param name: the name of the person
    :type name: str
    :param language: The language in which the person should be greeted
    :type language: str
    :return: a number
    :rtype: int
    """
    print(greeting[language]+" "+name)
    return 4
# Google Python Style Guide
def hello(name, language="en"):
    """Say hell to a person

    Args:
        name: the name of the person as string
        language: the language code string

    Returns:
        A number.
    """
    print(greeting[language]+" "+name)
    return 4