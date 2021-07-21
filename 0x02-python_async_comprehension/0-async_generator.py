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
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)