current_list = []
while True:
    char = str(input())
    if char == '':
        print('Ввод закончен')
        break
    else:
        current_list.append(int(char))
print(current_list)
for i in current_list:
    if i<0:
        print(i)
for i in current_list:
    if i==0:
        print(i)
for i in current_list:
    if i>0:
        print(i)