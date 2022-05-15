user_data = []
#char = int(input())
mid = 0
while True:
    char = int(input())
    if char == 0:
        print("Вы ввели ноль первым или закончили ввод данных")
        break
    else:
        user_data.append(char)
for i in user_data:
    mid +=i
total = mid/len(user_data)
print(total)

