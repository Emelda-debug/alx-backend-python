#!/usr/bin/env python3
""" async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay
"""
import random
import asyncio
from typing import List


wait_random = __import__(0 - basic_async_syntax.py).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async routine  that takes in 2 int arguments"""
    delay_time: List[float] = []
    all_tasks: List = []

    for _ in range(n):
        all_tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((all_tasks)):
        delay_time = await task
        delay_time.append(delay_time)

    return delay_time