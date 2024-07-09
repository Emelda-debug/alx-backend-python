#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no arguments
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers
"""

import random
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """ coroutine to collect 10 random numbers then return them"""
    return [x async for x in async_generator()]
