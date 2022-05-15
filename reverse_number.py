def reverse_number(n):
    if n < 0:
        return int(float(str(n*(-1))[::-1])) * (-1)
    return int(float(str(n)[::-1]))


print(reverse_number(-123))