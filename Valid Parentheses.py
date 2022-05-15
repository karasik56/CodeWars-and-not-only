def valid_parentheses(string):
    count_left = 0
    count_right = 0
    for i in string:
        if count_right > count_left:
            return False
        elif i == '(':
            count_left += 1
        elif i == ')':
            count_right += 1
    if count_right == count_left:
        return True
    else:
        return False


print(valid_parentheses('hi(hi)()'))