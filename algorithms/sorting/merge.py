# -*- coding: utf-8 -*-
import cProfile
import pstats
import sys


def read_data_to_list(input_list, input_count):
    for n in range(input_count):
        input_list.append(int(input()))


def merge_sort(alist):
    if len(alist) <= 1:
        return

    mid = len(alist)//2
    left_half = alist[:mid]
    right_half = alist[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_iter=0
    right_iter=0
    alist_iter=0

    while left_iter < len(left_half) and right_iter < len(right_half):
        if left_half[left_iter] < right_half[right_iter]:
            alist[alist_iter]=left_half[left_iter]
            left_iter=left_iter+1
        else:
            alist[alist_iter]=right_half[right_iter]
            right_iter=right_iter+1
        alist_iter=alist_iter+1

    while left_iter < len(left_half):
        alist[alist_iter]=left_half[left_iter]
        left_iter=left_iter+1
        alist_iter=alist_iter+1

    while right_iter < len(right_half):
        alist[alist_iter]=right_half[right_iter]
        right_iter=right_iter+1
        alist_iter=alist_iter+1


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
    merge_sort(input_list)
    for p in input_list:
        print(p)

    if is_profile_mode:
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats()
