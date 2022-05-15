'''https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python'''

def to_jaden_case(string):
    lst = list(string.split())
    result = [i.capitalize() for i in lst]
    return ' '.join(result)




print(to_jaden_case("How can mirrors be real if our eyes aren't real"))