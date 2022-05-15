'''https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python'''


def delete_nth(order, max_e):
    my_dict = {}
    order_revers = order[::-1]
    for i in order:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for k, v in my_dict.items():
        if v > max_e:
            for z in range(v-max_e):
                order_revers.remove(k)
    return order_revers[::-1]


print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))

# [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]
