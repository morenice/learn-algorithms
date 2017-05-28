import collections


class Cache(object):
    def get(self, key):
        raise NotImplementedError

    def set(self, key, *value):
        raise NotImplementedError


class LRUCache(Cache):
    """LRU Cache (Least Recently Used)
    _cache : write key/value
    _queue : write key for recently used
    """
    def __init__(self, max_cache_count=30):
        self._max_count = max_cache_count
        self._cache = dict()
        self._queue = collections.deque()

    def set(self, key, *value):
        """set key/value cache data"""
        if not value or not key:
            return False

        if len(value) == 1:
            value = value[0]

        if key not in self._cache:
            if len(self._cache) >= self._max_count:
                # remove least recently used data
                del(self._cache[self._queue.pop()])

            self._cache[key] = value
            self._queue.appendleft(key)
            return True

        self._cache[key] = value
        self._queue.remove(key)
        self._queue.appendleft(key)
        return True

    def get(self, key):
        if key not in self._cache:
            raise KeyError

        self._queue.remove(key)
        self._queue.appendleft(key)
        return self._cache[key]


if __name__ == "__main__":
    cache = LRUCache(3)

    # set example
    cache.set("key1", 10)
    cache.set("key2", "test")
    cache.set("key3", ["a","b","c"])
    print(cache._queue)
    print(cache._cache)

    cache.set("key4", "value")
    print(cache._queue)
    print(cache._cache)

    cache.set("key5", "value")
    print(cache._queue)
    print(cache._cache)

    # get example
    print(cache.get("key3"))
    print(cache._queue)
    print(cache._cache)
