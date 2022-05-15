def own_divisor(x):
    my_list = []
    sum_list = 0
    for i in range(1, x):
        if x % i == 0:
            my_list.append(i)
    for k in my_list:
        sum_list += k
    if sum_list == x:
        print(x)
        return x




def main():
    for j in range(1, 10000):
        own_divisor(j)




main()



