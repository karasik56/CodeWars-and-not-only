def move_zeros(array):
    start_len_array = len(array)
    while 0 in array:
        array.remove(0)
    end_len_array = len(array)
    array.extend([0]*(start_len_array-end_len_array))
    return array






print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
