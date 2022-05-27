"""https://www.codewars.com/kata/5aa736a455f906981800360d/train/python"""


def feast(beast, dish):
    return True if beast[0]+beast[-1] == dish[0]+dish[-1] else False

print(feast("great blue heron", "garlic naan"))

