import functools
import json


data = dict()


@functools.lru_cache(maxsize=10000)
def get_value(key):
    return data[key]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        items = json.loads(f.read())

        for item in items:
            try:
                value = get_value(item[0])
            except KeyError:
                data[item[0]] = item[1]
                value = item[1]

    print(get_value.cache_info())
