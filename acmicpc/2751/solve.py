# -*- coding: utf-8 -*-
def read_data_to_list(input_list, input_count):
    for n in range(input_count):
        input_list.append(int(input()))


def quicksort(alist):
    quicksort_helper(alist, 0, len(alist)-1)


def quicksort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quicksort_helper(alist, first, splitpoint-1)
        quicksort_helper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark+1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark-1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


if __name__ == '__main__':
    input_list = list()
    input_len = int(input())

    read_data_to_list(input_list, input_len)
    quicksort(input_list)
    for p in input_list:
        print(p)
