#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)

