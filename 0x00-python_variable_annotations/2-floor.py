#!/usr/bin/env python3
from math import floor as round_up

"""
Write a type-annotated function floor which takes a float n as
argument and returns the floor of the float
"""

def floor(n: float) -> int:
    """returns the floor a float"""
    return round_up(n)
