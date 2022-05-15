def list_input_sort():
    new_list = []
    while True:
        char = int(input())
        if char == 0:
            print("Вы ввели ноль первым или закончили ввод данных")
            break
        else:
            new_list.append(char)
    new_list.sort(reverse=True)
    print(new_list)


list_input_sort()

# тут же и задача №111
