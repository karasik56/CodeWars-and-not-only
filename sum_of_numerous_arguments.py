"""https://www.codewars.com/kata/55c5b03f8c28da9a51000045/train/python"""


def find_sum(*args):
    if len(args) == 0:
        return 0
    elif min(args) < 0:
        return -1
    else:
        return sum(args)


print(find_sum())
