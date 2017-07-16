import array

# TODO : memory_profiler
def compare_list_array():
    mylist = []
    for i in range(1,100000):
        mylist.append(i)

    myarray = array.array('i')
    for i in range(1,100000):
        myarray.append(i)


if __name__ == "__main__":
    compare_list_array()
