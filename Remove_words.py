"""https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python"""


def remove(s):
    new_list = []
    list_s = s.split()
    for i in list_s:
        if len(i) > 3 :
            new_list.append(i)
    return ' '.join(new_list)



print(remove('!Hi! ! !Hi!'))