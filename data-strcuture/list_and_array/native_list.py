import array
import string
import random
from memory_profiler import profile


def make_random_key(key_len=10):
    random_key_factor = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(random_key_factor) for _ in range(key_len))


@profile
def list_memory():
    list1 = list()
    for ch in make_random_key(1000000):
        list1.append(ch)

    print(list1.count('s'))
    print(list1.count('u'))
    print(list1.count('p'))


def list_sample():
    # list are very flexible and can hold completely heterogeneous, arbitrary data,
    # and they can be appended to very efficiently, in amortized constant time.

    # If you need to shrink and grow your array time-efficiently and without hassle,
    # they are the way to go. But they use a lot more space than C arrays.

    li = list()
    li.append(10)
    li.append('a')
    li.append([1,2,3,])
    print(li)

    li.remove(10)
    print(li.pop())
    print(li)

    li.insert(li.index('a'), 'c')
    print(li)


if __name__ == "__main__":
    list_memory()
    #list_sample()
