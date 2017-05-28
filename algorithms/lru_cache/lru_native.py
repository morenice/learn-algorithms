import functools
import urllib


@functools.lru_cache(maxsize=32)
def get_pep(num):
    '''Retrieve text of a Python Enhancement Proposal'''
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        #print('called %s' % (get_pep.__name__))
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except Exception as ex:
        return 'Not Found' + str(ex)


@functools.lru_cache(maxsize=None)
def fib(n):
    #print('called %s' % (fib.__name__))
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    # example1
    for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))

    print(get_pep.cache_info())
    print('='*40)

    # example2
    result = [fib(n) for n in range(16)]
    print(result)
    print(fib.cache_info())
