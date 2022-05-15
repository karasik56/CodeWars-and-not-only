'''https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python'''

def sort_array(source_array):
    odd_dict = {}
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            odd_dict[i] = source_array[i]
    for k in list(odd_dict.keys())[::-1]:
        del source_array[k]
    source_array = sorted(source_array)
    for i, n in odd_dict.items():
        source_array.insert(i, n)
    return source_array




print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))