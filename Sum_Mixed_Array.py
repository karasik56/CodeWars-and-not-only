"""https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python"""


def sum_mix(arr):
    return sum(list(map(int, arr)))


print(sum_mix([9, 3, '7', '3']))