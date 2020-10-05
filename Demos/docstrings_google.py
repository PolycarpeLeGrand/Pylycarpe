"""Example of Google style docstrings

This module demonstrates how to do Google style docstrings
Properly documenting projects is generally considered as the polite thing to do

Examples:
    Example or Examples sections are used for examples!
    For examples, see: https://www.sphinx-doc.org/en/2.0/usage/extensions/example_google.html
"""

module_var = 'heyyy!'
"""Inline documentation of a module variable"""

typed_module_var = 'wazup!'
"""str: Typed inline documentation of a module variable"""

multi_line_module_var = 'This requires a long explanation!'
"""Multi line documentation of a module variable

Some variables are very complicated and might require multiple lines of documentation
It is important to get the point across
"""


def one_line_docsting_funciton(param):
    """Returns the argument times two"""

    double = param * 2
    return double


def multi_line_docstring_function(param_0, param_1):
    """Takes two arguments and returns the sum

    This is a very complicated function
    On a side note, notice that we leave a blank line after docstring strings

    Args:
        param_0: the first param
        param_1: the second param

    Returns: the sum of the two params

    """

    result = param_0 + param_1
    return result


def multi_line_docstring_generator(collection):
    """Boring generator

    Notice that we use Yields instead of Returns
    That is all i have to say about that

    Args:
        collection: a collection to generate from

    Yields: items from the collection

    """
    for item in collection:
        yield item

