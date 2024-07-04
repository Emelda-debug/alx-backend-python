#!/usr/bin/python3
""" Augments the following code with the correct duck-typed annotations
# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    Args:
        lst: A list of elements (type unknown).

    Returns:
        The first element of the list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
