def square_or_square_root(arr):
    new_lst = []
    for i in arr:
        if (i**0.5) % 1 == 0:
            new_lst.append(int(i**0.5))
        else:
            new_lst.append(i**2)
    return new_lst




print(square_or_square_root([4, 3, 9, 7, 2, 1]))
