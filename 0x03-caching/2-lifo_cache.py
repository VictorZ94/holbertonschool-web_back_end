#!/usr/bin/env python3
""" Implement a caching system
    cache replacement algorithm - LIFO
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherit from BaseCaching and is a caching system
    Args:
        BaseCaching (Father class): Implement methods
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if self.cache_data.get(key):
                self.cache_data.pop(key)
            self.cache_data.update({key: item})

        len_cache = len(self.cache_data)
        if len_cache > BaseCaching.MAX_ITEMS:
            index_dict = {i: j for i, j in enumerate(self.cache_data)}
            print(f"DISCARD: {index_dict.get(3)}")
            self.cache_data.pop(index_dict.get(3))

    def get(self, key):
        """Obtain a value from dict by key
        """
        if key is not None:
            value = self.cache_data.get(key)
            if value is None:
                return None
            return value
        else:
            return None
