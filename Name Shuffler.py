def name_shuffler(str_):
    new_lst = str_.split()[::-1]
    return ' '.join(new_lst)



print(name_shuffler('john McClane'))