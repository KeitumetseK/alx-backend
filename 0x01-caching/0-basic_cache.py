# 0-basic_cache.py

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching """
    def put(self, key, item):
        """ Assigns to the dictionary self.cache_data the item value for the key key """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
       

