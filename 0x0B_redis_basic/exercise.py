#!/usr/bin/env python3
""" Getting started using redis
"""
import redis
from functools import wraps
from typing import Union, Optional, Callable
import uuid


def count_calls(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history
    Args:
        method (typing.Callable):
    Returns:
        typing.Callable:
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + "outputs", output)

        return output
    return wrapper


def replay(fn: Callable):
    """replay
    Args:
        fn (typing.Callable): display the history of calls
    """
    r = redis.Redis()
    fn_name = fn.__qualname__
    n_calls = r.get(fn_name)
    try:
        n_calls = n_calls.decode("utf-8")
    except Exception:
        n_calls = 0
    print(f'{fn_name} was called {n_calls} times:')

    inputs = r.lrange(fn_name + ":inputs", 0, -1)
    outputs = r.lrange(fn_name + ":outputs", 0, -1)

    for ins, outs in zip(inputs, outputs):
        try:
            ins = ins.decode("utf-8")
        except Exception:
            ins = ""
        try:
            outs = outs.decode("utf-8")
        except Exception:
            outs = ""

        print(f'{fn_name}(*{ins}) -> {outs}')


class Cache:

    def __init__(self):
        """ Create first instace of redis and
        clean all db with flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
