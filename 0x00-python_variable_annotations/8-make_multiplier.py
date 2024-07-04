#!/usr/bin/env python3
"""  type-annotated function make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ this function takes a float argument and returns a function
    that gives the product of multiplier and a number
    i.e. this function callable takes a float and returns a float
    Args:
        multiplier- argument number to be multiplied with of type float
    Returns:
        the product of multiplier and a number
    """
    def inner_function(num: float) -> float:
        return num * multiplier
    return inner_function
