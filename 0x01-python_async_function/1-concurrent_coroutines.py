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
    task_list = [asyncio.create_task(wait_random(max_delay)) for x in range(n)]
    completion = [await task for task in asyncio.as_completed(task_list)]
    return completion
