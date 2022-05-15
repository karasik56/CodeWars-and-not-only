""" https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python """
def duplicate_encode(word):
    my_dict = {}
    my_list = []
    for i in word.lower():
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for k in word.lower():
        if my_dict[k] == 1:
            my_list.append('(')
        else:
            my_list.append(')')
    return ''.join(my_list)







print(duplicate_encode('Success'))