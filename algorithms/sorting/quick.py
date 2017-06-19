# -*- coding: utf-8 -*-
import cProfile
import pstats
import sys


def read_data_to_list(input_list, input_count):
    for n in range(input_count):
        input_list.append(int(input()))


def quicksort(alist):
    __quicksort(alist, 0, len(alist)-1)


def __quicksort(alist, first, last):
    if first < last:
        split_point = __quick_partition(alist, first, last)
        __quicksort(alist, first, split_point-1)
        __quicksort(alist, split_point+1, last)


def __quick_partition(alist, first, last):
    pivot_value = alist[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark = leftmark+1

        while alist[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark-1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


if __name__ == '__main__':
    is_profile_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == "profile":
        is_profile_mode = True

    if is_profile_mode:
        pr = cProfile.Profile()
        pr.enable()

    input_list = list()
    input_len = int(input())

    read_data_to_list(input_list, input_len)
    quicksort(input_list)
    for p in input_list:
        print(p)

    if is_profile_mode:
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats()
