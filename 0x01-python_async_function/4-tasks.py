#!/usr/bin/env python3
"""
Altering code from task3 into a new function task_wait_n
"""
import asyncio
from typing import List

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function task_wait_n    """
    task_list = [get(max_delay) for x in range(n)]
    stop_task = [await task for task in asyncio.as_completed(task_list)]
    return stop_task
