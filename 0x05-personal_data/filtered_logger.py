#!/usr/bin/env python3
""" log message obfuscated
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Log formatter
        """
        return self.filter_datum(self.fields,
                                 self.REDACTION,
                                 super(RedactingFormatter,
                                       self).format(record),
                                 self.SEPARATOR)

    def filter_datum(self, fields: List[str], redaction: str,
                     message: str, separator: str) -> str:
        """return string obfuscated
        """
        for field in fields:
            message = re.sub(f"{field}=.*?{separator}",
                             f"{field}={redaction}{separator}", message)
        return message
