total_money = []
sum_total_money = 0
while True:
    money = (input())
    if money == '':
        print('Ввод закончен')
        break
    else:
        total_money.append(money)
for i in total_money:
    sum_total_money += float(i)
print(sum_total_money)



