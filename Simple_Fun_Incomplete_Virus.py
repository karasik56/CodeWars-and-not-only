"""https://www.codewars.com/kata/595467c63074e38ba4000063/train/python"""


def incomplete_virus(s):
    count = 0
    for i in range(1, int(s) + 1):
        a = set(''.join(str(i)))
        if a.issubset(['1', '0']) or a.issubset(['1']):
            print(i)
            count += 1
    return count


print(incomplete_virus('100'))
