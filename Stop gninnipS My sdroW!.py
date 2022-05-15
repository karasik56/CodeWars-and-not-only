def spin_words(sentence):
    old_list = sentence.split()
    new_list = []
    for i in old_list:
        if len(i) >= 5:
            new_list.append(i[::-1])
        else:
            new_list.append(i)
    return ' '.join(new_list)


print(spin_words('one words consist this and of string all the with spaces string'))