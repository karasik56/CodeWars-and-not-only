""" https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python """


def high_and_low(numbers):
    return f'{max(list(map(int, numbers.split())))} {min(list(map(int, numbers.split())))}'


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
