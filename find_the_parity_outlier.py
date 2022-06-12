"""https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python"""


def find_outlier(integers):
    even_list = list(filter(lambda x: x % 2 == 0, integers))
    odd_list = list(filter(lambda x: x % 2 != 0, integers))
    return even_list[0] if len(even_list) == 1 else odd_list[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))
