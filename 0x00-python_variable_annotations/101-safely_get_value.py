#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations to the function
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    this function retrieves a value from a dictionary in a safe manner.

    Parameters:
        dct: Mapping - This represents the input dictionary.The Mapping type from typing
        indicates that it can be any dictionary-like object (e.g., dict, OrderedDict, etc.).
        key: Any - The key to search for in the dictionary. It can be of
        any data type (string, integer, etc.).
        default: Union[T, None] = None (Optional) - defines a default value to
        return if the key is not found in the dictionary. The type T here is a placeholder
        for any specific type you might want to use. By default, it's set to None.
        Union[T, None] allows the default value to be either of type T or None.

    Returns:
        Union[Any, T]: The function returns either the value
        associated with the key in the dictionary (Any) or
        the provided default value (T).
    """
    if key in dct:
        return dct[key]
    else:
        return default
