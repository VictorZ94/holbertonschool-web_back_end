#!/usr/bin/env python3
""" complex type-annotated to Any
"""
from typing import Any, TypeVar, Union, Mapping


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
