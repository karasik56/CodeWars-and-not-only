def is_pangram(s):
    my_dict = {}
    for i in s.lower():
        if i.isalpha() and i not in my_dict:
            my_dict[i] = 1
        elif i.isalpha() and i in my_dict:
            my_dict[i] += 1
    if len(my_dict) == 26:
        return True
    return False


print(is_pangram('The quick, brown fox jumps over the lazy dog!'))