def sum_of_differences(arr):
    sort_arr = sorted(arr, reverse=True)
    res = 0
    if len(arr) < 2:
        return 0
    for i in range(len(arr)):
        try:
            res += sort_arr[i]-sort_arr[i+1]
        except Exception:
            break
    return res


print(sum_of_differences([1, 2, 10]))