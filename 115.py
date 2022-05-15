def own_divisor(x):
    my_list = []
    for i in range(1, x):
        if x % i == 0:
            my_list.append(i)
    return my_list

