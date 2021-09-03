#!/usr/bin/env python3
""" Getting started using redis
"""
import redis
from typing import Union, Optional
import uuid


class Cache:

    def __init__(self):
        """ Create first instace of redis and
        clean all db with flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ create the first key-value pair into db

        Args:
            data (Any): data can be a str, bytes, int or float.

        Returns:
            str: Uniq identifier ID
        """
        ID = str(uuid.uuid4())
        self._redis.mset({ID: data})
        return ID

    def get(self, key: str, fn: Optional[callable] = None) \
            -> Union[str, bytes, int, float]:
        if fn:
            value = self._redis.get(key)
            return value.decode('utf-8')

    def get_str(self, key: str) -> str:
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        v = self._redis.get(key)
        try:
            c = int(v.decode("utf-8"))
        except Exception:
            v = 0
        return v
