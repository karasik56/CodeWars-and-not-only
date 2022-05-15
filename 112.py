def main():
    default_list = []
    while True:
        experiment_data = int(input())
        if experiment_data == 000:
            print('Ввод закончен')
            break
        else:
            default_list.append(experiment_data)
    if len(default_list) <= 4:
        print('Данных слишком мало, введите больше 4 значений')
    print(default_list)
    without_max_and_min(default_list)
    return default_list


def without_max_and_min(default_list):
    new_list = []
    default_list.sort()
    for i in default_list:
        new_list.append(i)
    del new_list[0:len(default_list)+1:len(default_list)-1]
    #del new_list[-1]
    print(new_list)





main()