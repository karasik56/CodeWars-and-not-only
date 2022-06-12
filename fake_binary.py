"""https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python"""

def fake_bin(x):
    return ''.join([str(0) if int(i) < 5 else str(1) for i in x])


print(fake_bin("45385593107843568"))