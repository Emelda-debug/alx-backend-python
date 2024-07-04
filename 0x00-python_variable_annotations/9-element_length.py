#!/usr/bin/python3
""" Annotating the below function's parameters and return
values with the appropriate types"""

from typing import Any, Tuple, List


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """ since in duck typing there is less regard for data types, we incoroporate any
    We also know this function returns i and the length of i by looping, therefore
     we know that result is a list, where our iterator will loop over the elements in our list
    Furthermore, we know that this will return any value for i because i can be anything eg. number,
    string etc  and int for len(i) be cause lenght will always return a number int. We also know that this list
     will include an int and a different data type hence why it is a tuple
    """
    return [(i, len(i)) for i in lst]
