def create_pocketbook():
    return list()


def find_pocketbook_by_name(pocketbook, name):
    for i, pocket in enumerate(pocketbook):
        if pocket == name:
            return i+1
    return -1


def find_pocketbook_by_index(pocketbook, index):
    return pocketbook[index-1]


if __name__ == '__main__':
    input_data = input().split()
    n = int(input_data[0])
    m = int(input_data[1])

    pocketbook = create_pocketbook()

    for i in range(0, n):
        pocketmon = input()
        pocketbook.append(pocketmon)

    for i in range(0,m):
        search_string = input()
        search_num = -1
        try:
            search_num = int(search_string)
        except:
            pass

        if search_num == -1:
            print(find_pocketbook_by_name(pocketbook, search_string))
        else:
            print(find_pocketbook_by_index(pocketbook, search_num))
