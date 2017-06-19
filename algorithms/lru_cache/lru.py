import collections
import json


class Cache(object):
    def get(self, key):
        raise NotImplementedError

    def set(self, key, *value):
        raise NotImplementedError


class LRUCache(Cache):
    """LRU Cache (Least Recently Used)
    _cache : write key/value
    """
    def __init__(self, max_cache_count=30):
        self._max_count = max_cache_count
        self._cache = collections.OrderedDict()

    def set(self, key, *value):
        """set key/value cache data"""
        if not key:
            raise KeyError

        if not value:
            raise ValueError

        if len(value) == 1:
            value = value[0]

        if key not in self._cache:
            if len(self._cache) >= self._max_count:
                self._cache.popitem()

        # insert or upate
        self._cache[key] = value
        self._cache.move_to_end(key, last=False)

    def get(self, key):
        if key not in self._cache:
            raise KeyError

        self._cache.move_to_end(key, last=False)
        return self._cache[key]


def sample():
    cache = LRUCache(3)

    # set example
    cache.set("key1", 10)
    cache.set("key2", "test")
    cache.set("key3", ["a","b","c"])
    print(cache._cache)

    cache.set("key4", "value")
    print(cache._cache)

    cache.set("key5", "value")
    print(cache._cache)

    # get example
    print(cache.get("key3"))
    print(cache._cache)


if __name__ == "__main__":
    cache = LRUCache(10000)

    with open("input.txt", "r") as f:
        items = json.loads(f.read())

        for item in items:
            try:
                value = cache.get(item[0])
            except KeyError:
                cache.set(item[0], item[1])
                value = item[1]
