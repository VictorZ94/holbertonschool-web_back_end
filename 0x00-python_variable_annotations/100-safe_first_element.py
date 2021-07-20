#!/usr/bin/env python3
""" complex type-annotated to Any
"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any, None]:
    """ complex type-annotated to Any
    """
    if lst:
        return lst[0]
    else:
        return None
