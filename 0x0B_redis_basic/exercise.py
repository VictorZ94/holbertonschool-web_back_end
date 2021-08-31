#!/usr/bin/env python3
""" Getting started using redis
"""
import redis
from typing import Any
import uuid


class Cache:

    def __init__(self):
        """ Create first instace of redis and
        clean all db with flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """ create the first key-value pair into db

        Args:
            data (Any): data can be a str, bytes, int or float.

        Returns:
            str: Uniq identifier ID
        """
        ID = str(uuid.uuid4())
        self._redis.mset({ID: data})
        return ID
