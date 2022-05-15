def find_it(seq):
    my_dict = {}
    for i in seq:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for k, v in my_dict.items():
        if v % 2 != 0:
            return k
    return None


print(find_it([0, 1, 0, 1, 0]))
