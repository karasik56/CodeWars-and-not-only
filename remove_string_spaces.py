"""https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python"""

def no_space(x):
    return ''.join([i for i in x if i != ' '])


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))