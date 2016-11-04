import bisect


def create_pocketbook():
    return list()


def add_pocketbook(pocketbook, pocketmon):
    pocketbook.append(pocketmon)


def find_pocketbook(pocketbook, index):
    return pocketbook[index-1]


def create_bs_pocketbook(pocketbook):
    """ pocketbook for binary searching """
    bs_pocketbook = []
    for i, pocketmon in enumerate(pocketbook):
        bs_pocketbook.append((pocketmon, i))

    bs_pocketbook.sort(key=lambda r: r[0])
    bs_keys = [p[0] for p in bs_pocketbook]
    return bs_pocketbook, bs_keys


def find_bs_pocketbook(bs_pocketbook, bs_keys, name):
    """ pocketbook for binary searching """
    bs_index = bisect.bisect_left(bs_keys, name)
    return (bs_pocketbook[bs_index][1] + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    pocketbook = create_pocketbook()

    for i in range(0, n):
        pocketmon = input()
        add_pocketbook(pocketbook, pocketmon)

    bs_pocketbook, bs_keys = create_bs_pocketbook(pocketbook)

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
