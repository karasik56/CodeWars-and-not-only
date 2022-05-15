def same_case(a, b):
    if a.islower() and b.islower() or a.isupper() and b.isupper():
        return 1
    elif (a.islower() or b.islower()) and (a.isupper() or b.isupper()):
        return 0
    else:
        return -1


print(same_case('/n', 'V'))