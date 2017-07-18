def queue_perf():
    queue = list()

    for i in range(300000):
        queue.append(i)

    for i in range(300000):
        queue.pop(0)


def queue_sample():
    queue = list()

    #
    # get/set queue
    print('set 1 to queue')
    queue.append(1)
    print('set \"abc\" to queue')
    queue.append('abc')
    print('set list to queue')
    queue.append([1,2,3])

    print('get from queue')
    print(queue.pop(0))
    print('queue size {0}'.format(len(queue)))

    print('get from queue')
    print(queue.pop(0))
    print('queue size {0}'.format(len(queue)))

    print('get from queue')
    print(queue.pop(0))
    print('queue size {0}'.format(len(queue)))

    try:
        print(queue.pop(0))
    except IndexError:
        # empty queue
        print('queue is empty')


if __name__ == "__main__":
    #queue_sample()
    queue_perf()
