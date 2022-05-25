"""https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/train/python"""
import string


def bingo(array):
    bingo_set = set()
    for k, v in enumerate(string.ascii_uppercase, start=1):
        if v in 'BINGO':
            bingo_set.add(k)
    if bingo_set.issubset(array):
        return 'WIN'
    return 'LOSE'


print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]))
