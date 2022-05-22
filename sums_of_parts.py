"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python"""

# def parts_sums(ls):
#     res = []
#     while len(ls) != 0:
#         res.append(sum(ls))
#         ls.pop(0)
#     if len(ls) == 0:
#         res.append(0)
#     return res


def parts_sums(ls):
    val = sum(ls)
    res = [val]
    for i in ls:
        val = val - i
        res.append(val)
    return res







print(parts_sums([0, 1, 3, 6, 10]))