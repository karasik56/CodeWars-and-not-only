def square_digits(num):
    sum = []
    for i in str(num):
        sum.append(str(int(i)**2))
    sum_str = ''.join(sum)
    return sum_str





print(square_digits(9119))
