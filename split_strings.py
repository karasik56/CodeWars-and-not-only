'''https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python'''
def solution(s):
    new_list = []
    temp_str = ''
    if len(s) % 2 != 0:
        s = s + '_'
    for i in s:
        temp_str += i
        if len(temp_str) == 2:
            new_list.append(temp_str)
            temp_str = ''
    return new_list








print(solution('abcdefdhfghdgdfhhjhgjjg'))

