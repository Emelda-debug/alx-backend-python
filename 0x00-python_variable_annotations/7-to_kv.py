#!/usr/bin/env python3
"""
type-annotated function to_kv that takes a string k 
and an int OR float v and returns a tuple. 
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function that returns a tuple with the string k and square of v  """
    return (k, v ** 2)
