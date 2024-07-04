#!/usr/bin/env python3
"""
Annotating the below function's parameters and return
values with the appropriate types
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function that returns an element and len(element) """
    return [(i, len(i)) for i in lst]
