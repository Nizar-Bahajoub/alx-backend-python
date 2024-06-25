#!/usr/bin/env python3
"""Function that returns a tuple of the given arguments
"""
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return an annotated Tuple
    """
    return (k, v ** 2)
