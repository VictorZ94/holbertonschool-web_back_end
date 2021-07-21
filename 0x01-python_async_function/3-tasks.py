#!/usr/bin/env python3
"""function that measures the total execution time for wait_n(n, max_delay)
"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        Any: Task Asyncio
    """
    return asyncio.Task(wait_random(max_delay))
