# -*- coding: utf-8 -*-
import cProfile
import pstats
import sys


def read_data_to_list(input_list, input_count):
    for n in range(input_count):
        input_list.append(int(input()))
    return input_list


def sort_select(input_list):
    list_len = len(input_list)

    # O(n*n)
    for n in range(list_len):
        min_idx = n
        for i in range(n, list_len):
            # find index of min value
            if input_list[min_idx] > input_list[i]:
                min_idx = i

        # swap value
        if n != min_idx:
            input_list[min_idx], input_list[n] = input_list[n], input_list[min_idx]


def sort_insertion(input_list):
    list_len = len(input_list)

    # O(n*n)
    for start_idx in range(1, list_len):
        access_idx = start_idx-1
        key = input_list[start_idx]

        while access_idx >= 0:

            # compare value that start index and access index
            if input_list[access_idx] < key:
                # pop and insert value
                input_list.insert(access_idx+1, input_list.pop(start_idx))
                break

            # last comapre value
            if access_idx == 0 and input_list[0] > key:
                # pop and insert value
                input_list.insert(access_idx, input_list.pop(start_idx))
                break

            access_idx -= 1


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
    sort_select(input_list)

    for n in range(input_len):
        print(input_list[n])

    if is_profile_mode:
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats()

