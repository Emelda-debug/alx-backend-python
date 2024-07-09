#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension four times
in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine to execute async_comprehension 4 times in parallel using asyncio.gather"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    total_execution_time = time.perf_counter() - start_time
    return total_execution_time
