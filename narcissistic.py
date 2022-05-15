def narcissistic(value):
    value_lst = list(''.join(str(value)))
    sum_char = 0
    for i in value_lst:
        sum_char += int(i)**len(value_lst)
    if sum_char == value:
        return True
    return False




print(narcissistic(371))