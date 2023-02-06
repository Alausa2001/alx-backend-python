#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.

Write a function task_wait_random that takes an integer max_delay and
returns a asyncio.Task
"""
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """returns a task object"""
    task = create_task(wait_random(max_delay))
    return task

