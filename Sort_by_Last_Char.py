"""https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/train/python"""

def last(s):
    sorted_list_of_last_char = sorted([i[::-1] for i in s.split()])
    return [i[::-1] for i in sorted_list_of_last_char]


print(last("man i need a taxi up to ubud"))