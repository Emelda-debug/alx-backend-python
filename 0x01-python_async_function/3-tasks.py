#!/usr/bin/env python3
"""
function task_wait_random that takes integer
argument max_delay and returns an asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes in argument max_delay and returns async.Task
    """
    return asyncio.create_task(wait_random(max_delay))
