'''https://www.codewars.com/kata/614ac445f13ead000f91b4d0/train/python'''

def solve(eq: str):
    res = eq.split('=')
    new_str = ''
    count = -1
    for i in res:
        count += 1
        if 'x' in i:
            new_str += i
            break
    new_str = new_str.replace('x', '0')
    if count == 0 and new_str != '- 0 ':
        return eval(res[1] + '+' + str(-eval(new_str)))
    if count == 1 and new_str != '- 0 ':
        return eval(str(eval(new_str)) + '-' + str(-eval(res[0])))
    if count == 0 and new_str == '- 0 ':
        return eval(res[1])*(-1)
    if count == 1 and new_str == '- 0 ':
        return eval(res[0])*(-1)


# print(solve('x + 1 = 9 - 2'))
# print(solve('2 + 1 = 9 - x'))
# print(solve('- 10 = x'))
print(solve('- x = - 1'))



