import collections


def stack_perf():
    stack = collections.deque()
    for i in range(300000):
        stack.append(i)

    for i in range(300000):
        stack.pop()


def stack_sample():
    stack = collections.deque()

    #
    # push/pop stack
    print('push 1 to stack')
    stack.append(1)
    print('push \"abc\" to stack')
    stack.append('abc')
    print('push list to stack')
    stack.append([1,2,3])

    print('pop from stack')
    print(stack.pop())
    print('stack size {0}'.format(len(stack)))

    print('pop from stack')
    print(stack.pop())
    print('stack size {0}'.format(len(stack)))

    print('pop from stack')
    print(stack.pop())
    print('stack size {0}'.format(len(stack)))


if __name__ == "__main__":
    #stack_sample()
    stack_perf()
