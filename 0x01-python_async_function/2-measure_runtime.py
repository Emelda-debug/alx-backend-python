#!/usr/bin/env python3
"""
measure_time, that takes argument n and max_delay then
measures total execution for wait_n(n, max_delay)
Returns total_time / n float
"""
import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int= 10) -> float:
    """
    Function to measure_time and
    return float total_time / n
    """
    start_time:float = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time:float = time.time
    return (stop_time - start_time) / n
