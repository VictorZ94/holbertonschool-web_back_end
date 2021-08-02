#!/usr/bin/env python3
"""[summary]
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: List[str],
                 separator: str) -> str:
    for i in fields:
        string = re.sub(f"{i}=[^=]*{separator}",
                        f"{i}={redaction}{separator}", message)
    return string
