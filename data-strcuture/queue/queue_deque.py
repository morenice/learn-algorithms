"""
Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

New in version 2.4.

If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end. Bounded length deques provide functionality similar to the tail filter in Unix. They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

Changed in version 2.6: Added maxlen parameter.
"""
import collections


def deque_perf():
    dequeue = collections.deque()

    for i in range(300000):
        dequeue.append(i)

    for i in range(300000):
        dequeue.popleft()


def deque_sample():
    dequeue = collections.deque()

    print('set 1 to queue')
    dequeue.append(1)
    print('set \"abc\" to queue')
    dequeue.append('abc')
    print('set list to queue')
    dequeue.append([1,2,3])

    print('get from queue')
    print(dequeue.popleft())
    print('queue size {0}'.format(len(dequeue)))

    print('get from queue')
    print(dequeue.popleft())
    print('queue size {0}'.format(len(dequeue)))

    print('get from queue')
    print(dequeue.popleft())
    print('queue size {0}'.format(len(dequeue)))

    try:
        print(dequeue.popleft())
    except IndexError:
        # empty queue
        print('queue is empty')


if __name__ == "__main__":
    #deque_sample()
    deque_perf()
