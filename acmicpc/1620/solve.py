import bisect

import cProfile
import pstats


def create_pocketbook():
    return list()


def add_pocketbook(pocketbook, pocketmon):
    pocketbook.append(pocketmon)


def find_pocketbook_by_name(pocketbook, name):
    for i, pocket in enumerate(pocketbook):
        if pocket == name:
            return i+1
    return -1


def find_pocketbook(pocketbook, index):
    return pocketbook[index-1]


def create_bs_pocketbook():
    """ pocketbook for binary searching """
    return list()


def add_bs_pocketbook(bs_pocketbook, pocketmon):
    index = len(bs_pocketbook)
    bs_pocketbook.append((pocketmon, index))


def find_bs_pocketbook(bs_pocketbook, bs_keys, name):
    """ pocketbook for binary searching """
    bs_index = bisect.bisect_left(bs_keys, name)
    return (bs_pocketbook[bs_index][1] + 1)


def main_list():
    n, m = map(int, input().split())
    pocketbook = create_pocketbook()

    for i in range(0, n):
        pocketmon = input()
        add_pocketbook(pocketbook, pocketmon)

    for i in range(0, m):
        search_string = input()
        search_num = -1
        try:
            search_num = int(search_string)
        except:
            pass

        if search_num == -1:
            print(find_pocketbook_by_name(pocketbook, search_string))
        else:
            print(find_pocketbook(pocketbook, search_num))


def main_bisect():
    n, m = map(int, input().split())
    bs_pocketbook = create_bs_pocketbook()
    pocketbook = create_pocketbook()

    for i in range(0, n):
        pocketmon = input()
        add_bs_pocketbook(bs_pocketbook, pocketmon)
        add_pocketbook(pocketbook, pocketmon)

    bs_pocketbook.sort(key=lambda r: r[0])
    bs_keys = [p[0] for p in bs_pocketbook]

    for i in range(0, m):
        search_string = input()
        search_num = -1
        try:
            search_num = int(search_string)
        except:
            pass

        if search_num == -1:
            print(find_bs_pocketbook(bs_pocketbook, bs_keys, search_string))
        else:
            print(find_pocketbook(pocketbook, search_num))


def main_map():
    n, m = map(int, input().split())
    pocketbook = create_pocketbook()
    pocketbook_map = dict()

    for i in range(0, n):
        pocketmon = input()
        add_pocketbook(pocketbook, pocketmon)
        pocketbook_map[pocketmon] = i

    for i in range(0, m):
        search_string = input()
        search_num = -1
        try:
            search_num = int(search_string)
        except:
            pass

        if search_num == -1:
            print(pocketbook_map[search_string]+1)
        else:
            print(find_pocketbook(pocketbook, search_num))


if __name__ == '__main__':

    pr = cProfile.Profile()
    pr.enable()

    #main_list()
    #main_bisect()
    main_map()

    pr.disable()
    ps = pstats.Stats(pr).sort_stats('cumulative')
    ps.print_stats()
