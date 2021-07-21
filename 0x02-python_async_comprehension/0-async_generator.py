#!/usr/bin/env python3
""" coroutine async generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    Yields:
        [type]: [description]
    """
    n: int = 10
    for i in range(n):
        yield random.uniform(0, n)
        await asyncio.sleep(1)
