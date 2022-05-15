def digital_root(n):
    sum_numb = 0
    n_lst = list(''.join(str(n)))
    for i in n_lst:
        sum_numb += int(i)
    length = len(str(sum_numb))
    if length == 1:
        return sum_numb
    else:
        return digital_root(sum_numb)









print(digital_root(132189))