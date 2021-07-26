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
        
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = list(self.cache_data)[-2]
            print('DISCARD:', last)
            self.cache_data.pop(last)

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
