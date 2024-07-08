#!/usr/bin/env python3
""" async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay.
and will spawn wait_random n times with the specified max_delay. """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function to return a list of all the delays random float.
    """
    the_delays: List[float] = []
    delay_list: List[float] = []

    for x in range(n):
        the_delays.append(wait_random(max_delay))

    for y in asyncio.as_completed(the_delays):
        delay_list.append(await y)

    return delay_list
