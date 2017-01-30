# -*- coding: utf-8 -*-


def read_data_to_list(input_list, input_count):
    for n in range(input_count):
        input_list.append(int(input()))
    return input_list


def sort_select(input_list):
    list_len = len(input_list)

    for n in range(list_len):
        min_idx = n
        for i in range(n, list_len):
            # find index of min value
            if input_list[min_idx] > input_list[i]:
                min_idx = i

        # exchange value
        if n != min_idx:
            input_list[min_idx], input_list[n] = input_list[n], input_list[min_idx]


if __name__ == '__main__':
    input_list = list()
    input_len = int(input())

    read_data_to_list(input_list, input_len)
    sort_select(input_list)

    for n in range(input_len):
        print(input_list[n])