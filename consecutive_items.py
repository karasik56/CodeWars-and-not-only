""" https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python """


def consecutive(arr, a, b):
    lst = []
    for count, value in enumerate(arr):
        if value == a or value == b:
            lst.append(count)
    if abs(abs(lst[0]) - abs(lst[1])) == 1:
        return True
    return False


print(consecutive([1, 3, 5, 7], 3, 1))
