

if __name__ == "__main__":
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