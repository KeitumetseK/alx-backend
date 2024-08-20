#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.cache_keys.pop()
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]
            self.cache_data[key] = item
            self.cache_keys.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)

