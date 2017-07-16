import array

def array_sample():
    # array.array is useful when you need a homogeneous C array of data for reasons other than doing math.
    # single type data array.

    print(array.typecodes)
    array1 = array.array('u', 'new string')

    print(array1)
    print(array1.count('s'))
    array1.fromunicode(' append string')

    print(array1)


if __name__ == "__main__":
    array_sample()
