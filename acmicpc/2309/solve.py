# -*- coding: utf-8 -*-
import sys


def find_dwarf_for_princess(dwarf_height_list):
    total_sum = 0
    except_idx1 = except_idx2 = 0
    total_len = len(dwarf_height_list)

    for i in range(total_len):
        total_sum += dwarf_height_list[i]

    for i in range(0, total_len-1):
        for j in range(1, total_len):
            if i == j:
                continue

            if total_sum - dwarf_height_list[i] - dwarf_height_list[j] == 100:
                except_idx1 = i
                except_idx2 = j
                break

    new_dwarf_height_list = list()
    for i in range(total_len):
        if i == except_idx1 or i == except_idx2:
            continue

        new_dwarf_height_list.append(dwarf_height_list[i])

    new_dwarf_height_list.sort()
    return new_dwarf_height_list


if __name__ == '__main__':
    total_dwarf = 9
    dwarf_height_list = list()
    for n in range(total_dwarf):
        dwarf_height_list.append(int(input()))

    new_dwarf_list = find_dwarf_for_princess(dwarf_height_list)
    for dwarf in new_dwarf_list:
        print(dwarf)
