def get_count(sentence):
    vowels = ['a', 'e', 'o', 'u', 'i']
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count


print(get_count("abracadabra"))