"""https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python"""
import re
def increment_string(strng):
    if strng == '':
        return '1'
    elif strng.isalpha():
        return strng + '1'
    else:
        new_list = re.split(r"\D", strng)
        digits = str(int(new_list[-1].split()[-1]) + 1)
        if new_list[-1][0] != '0':
            return ''.join(re.sub('[0-9]+', digits, strng))
        return ''.join(re.sub('[0-9]+', ('0'*(len(new_list[-1])-len(digits)))+digits, strng))




print(increment_string("foobar00099"))