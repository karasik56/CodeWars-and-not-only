from math import *
n = 10
x = 0
for i in range(1, n + 1):
    x += 1 / i
    y = x - log(n)
print(y)