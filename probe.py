# def gen():
#     cnt = 0
#     while cnt < 10:
#         yield cnt
#         cnt+=1
#
# a = gen()
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(gen())
#
# def for_gen():
#     while True:
#         try:
#             print(next(a))
#         except StopIteration:
#             pass
# b = for_gen()
# print(b)

def my_func(position, default=1, *args, keyword, **kwargs):
    return len(args)


print(my_func(1, 2, 3, 4, 5, keyword=2))
