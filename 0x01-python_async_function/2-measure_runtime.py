#!/usr/bin/env python3
"""
measure_time, that takes argument n and max_delay then
measures total execution for wait_n(n, max_delay)
Returns total_time / n float
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure_time and
    return float total_time / n
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop_time: float = time.perf_counter - start_time
    return stop_time / n
