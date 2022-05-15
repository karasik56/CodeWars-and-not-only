def positive_sum(arr):
    sum = 0
    if arr is False:
        return 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

print(positive_sum([1,-2,3,4,5]))