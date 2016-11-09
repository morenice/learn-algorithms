def find_fraction(index):
    # x and y : x/y
    x = y = 0
    cnt = 1

# values :  1/1   |  1/2     2/1  |   3/1    2/2   1/3   |   1/4    3/2    2/3
# (x,y)  : (0, 0) | (1, 0) (0, 1) | (0, 2) (1, 1) (2, 0) | (3, 0) (2, 1) (1, 2)
# index  :   1    |   2       3   |    4      5      6   |    7      8      9
    if index <= 1:
        return str(y+1) + '/' + str(x+1)

    # x,y index search
    while True:
        if y == 0:
            x += 1
            cnt += 1
            if cnt == index:
                return str(y+1) + '/' + str(x+1)

            while x != 0:
                x -= 1
                y += 1
                cnt += 1

                if cnt == index:
                    return str(y+1) + '/' + str(x+1)
        if x == 0:
            y += 1
            cnt += 1
            if cnt == index:
                return str(y+1) + '/' + str(x+1)

            while y != 0:
                y -= 1
                x += 1
                cnt += 1

                if cnt == index:
                    return str(y+1) + '/' + str(x+1)


if __name__ == '__main__':
    print(find_fraction(int(input())))
