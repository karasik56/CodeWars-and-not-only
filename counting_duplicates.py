"""https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python"""


def duplicate_count(text):
    my_dict = {}
    count = 0
    for i in text.lower():
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for k, v in my_dict.items():
        if v > 1:
            count += 1
    return count




print(duplicate_count("Indivisibilities"))