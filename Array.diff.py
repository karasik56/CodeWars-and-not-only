def array_diff(a, b):
    new_list = []
    if a and b is False:
        return []
    for i in a:
        if i not in b:
            new_list.append(i)
    return new_list

print(array_diff([1, 2, 2, 2, 3], [2]))
