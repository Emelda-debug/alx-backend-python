#!/usr/bin/env python3
""" Annotating the below function's parameters and return
values with the appropriate types"""

from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ since in duck typing there is less regard for data types,
    We also know this function returns i and the length of
    i by looping, therefore
    """
    return [(i, len(i)) for i in lst]
