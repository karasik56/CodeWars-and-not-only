'''https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python'''


def persistence(n):
    if n < 10:
        return 0
    n_str = str(n)
    val = 1
    for i in n_str:
        val = val * int(i)
    return 1 + persistence(val)


print(persistence(999))
