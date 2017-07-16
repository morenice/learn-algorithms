

if __name__ == "__main__":
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
