def string_clean(s):
    """
    Function will return the cleaned string
    """
    digits = '0123456789'
    new_list = []
    for i in s:
        if i in '0123456789':
            continue
        else:
            new_list.append(i)
    new_str = ''.join(new_list)
    return new_str

s = "v123456789v"

print(string_clean(s))