"""https://www.codewars.com/kata/55a5c82cd8e9baa49000004c"""


def divisible_count(x, y, k):
    lst = [i for i in range(x, y + 1) if i % k == 0]
    return len(lst)


print(divisible_count(6, 11, 2))
# вариант рабочий, но медленный