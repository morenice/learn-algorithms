import array

if __name__ == "__main__":
    # single type array
    print(array.typecodes)
    array1 = array.array('u', 'new string')

    print(array1)
    print(array1.count('s'))
    array1.fromunicode(' append string')

    print(array1)