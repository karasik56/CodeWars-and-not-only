from random import randint
new_list = []
count = 10
if len(new_list)<=10:
    for i in range(1, count):
            a = randint(1,20)
            if a not in new_list:
                new_list.append(a)
new_list.sort()
print(new_list)

#решено через while. есть фото в телефоне