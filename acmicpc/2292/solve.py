# -*- coding: utf-8 -*-
def get_pass_room_count_honeycomb(position):
    """
    1-depth room count : 1 (0-1)
    2-depth room count : 6 (2-7)
    3-depth romm count : 12 (8-19)
    4-depth romm count : 18 (20-37)
    N-depth room count : 6*(N-1) (2+(6*(N-2), 1+(6*N-1))
    """
    if position == 1:
        return 1

    count = 2
    left_edge = 2
    right_edge = 7

    while True:
        if position >= left_edge and position <= right_edge:
            return count

        left_edge += (count-1)*6
        right_edge += count*6
        count += 1

        if left_edge > 1000000000:
            break

    return -1


if __name__ == '__main__':
    position = input()
    print("%d" % get_pass_room_count_honeycomb(int(position)))
