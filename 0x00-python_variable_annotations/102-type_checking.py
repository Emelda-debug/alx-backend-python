
#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code
and apply any necessary changes
"""
from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    the function attempts to zoom in on a list-like element(represented as a tuple in this case)
    by duplicating its elements

    Arguments:
        lst: Tuple - The input list-like element. While it's
        declared as a Tuple, the function seems
        to work with any iterable sequence (like lists).
        factor: int = 2 (Optional) - The zoom factor, an
        integer specifying how many times to duplicate
        each element. Defaults to 2.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
