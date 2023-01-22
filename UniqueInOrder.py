#  https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    new_list = []
    for i in sequence:
        if len(new_list) == 0:
            new_list.append(i)
        if len(new_list) and new_list[-1] != i:
            new_list.append(i)
    return new_list


lst = [1, 2, 2, 3, 4, 4, 4, 4, 5]
print(unique_in_order(lst))
