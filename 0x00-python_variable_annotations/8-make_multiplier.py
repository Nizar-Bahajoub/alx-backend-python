#!/usr/bin/env python3
"""Takes a float and returns a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
