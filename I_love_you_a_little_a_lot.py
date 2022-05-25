"""https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python"""


def how_much_i_love_you(nb_petals):
    my_dict = {
        1: "I love you",
        2: "a little",
        3: "a lot",
        4: "passionately",
        5: "madly",
        6: "not at all"
    }
    res = nb_petals % len(my_dict)
    return my_dict[res] if res != 0 else my_dict[6]

print(how_much_i_love_you(6))
