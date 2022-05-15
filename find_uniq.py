'''https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python'''


def find_uniq(arr):
    my_dict = {}
    for i in arr:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for key, value in my_dict.items():
        if value == 1:
            return key


print(find_uniq([1, 1, 1, 1, 5, 1, 1]))
