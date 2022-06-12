"""https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python"""


def vowel_indices(word):
    index_list = []
    for k, v in enumerate(word.lower(), start=1):
        if v in ['a', 'e', 'i', 'o', 'u', 'y']:
            index_list.append(k)
    return index_list


print(vowel_indices("apple"))
