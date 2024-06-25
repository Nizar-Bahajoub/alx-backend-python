#!/usr/bin/env python3
"""Correcting Annotation
"""
from typing import Any, Iterable, Optional


# The types of the elements of the input are not know
def safe_first_element(lst: Iterable[Any]) -> Optional[Any]:
    """Correcting Annotaion
    """
    if lst:
        return lst[0]
    else:
        return None
