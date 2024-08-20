#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)  # Frequency dictionary
        self.usage_order = OrderedDict()   # Order of usage for LRU behavior in ties

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If key is already in cache, update the value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            # If cache is full, we need to remove the LFU item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the key(s) with the lowest frequency
                min_freq = min(self.frequency.values())
                candidates = [k for k, freq in self.frequency.items() if freq == min_freq]

                # Use LRU to select the key to discard among the candidates
                if len(candidates) > 1:
                    lru_key = next(k for k in self.usage_order if k in candidates)
                else:
                    lru_key = candidates[0]

                # Remove the LFU (or LRU among ties) item
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.usage_order[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new key to cache
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and usage order
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

