import array
import string
import random
from memory_profiler import profile


def make_random_key(key_len=10):
    random_key_factor = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(random_key_factor) for _ in range(key_len))


@profile
def array_memory():
    array1 = array.array('u')
    for ch in make_random_key(1000000):
        array1.fromunicode(ch)

    print(array1.count('s'))
    print(array1.count('u'))
    print(array1.count('p'))


def array_sample():
    """ single type data array.

    array.array is useful when you need a homogeneous C array of data for reasons other than doing math.
    """
    print(array.typecodes)
    array1 = array.array('u', 'asdfasdf')
    print(array1.count('s'))

    array1.fromunicode(' append string')
    print(array1)


if __name__ == "__main__":
    array_memory()
    #array_sample()
