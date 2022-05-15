def digitize(n):
    new_lst = []
    for i in str(n):
        new_lst.append(int(i))
    return new_lst[::-1]


a = 348597

print(digitize(a))