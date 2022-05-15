a = ['a', 'b', 'c']
b = ['good']
text = 'ffghgfhgfh adc ggd good c'

def filter_bad_word():
    text_list = text.split()
    print(text_list)
    for i in b:
        if i in text_list:
            black_list(text_list)
            return text_list
        else:
            continue
    print('Провал')
    return 'Провал'


def black_list(text_list):
    for k in a:
        if k in text_list:
            print('Есть стоп слово')
            return 'Есть стоп слово'
        else:
            continue
    print('Успех')
    return 'Успех'





filter_bad_word()