"""https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python"""


def number(bus_stops):
    cnt_ent = 0
    cnt_ext = 0
    for i in bus_stops:
        cnt_ent += i[0]
        cnt_ext += i[1]
    return cnt_ent - cnt_ext


print(number([[10, 0], [3, 5], [5, 8]]))
