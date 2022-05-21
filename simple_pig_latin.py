""" https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python """

def pig_it(text):
    lst_text = list(text.split())
    for i in range(len(lst_text)):
        if lst_text[i] not in ['!', '?', ',', '.']:
            lst_text[i] += lst_text[i][0]
            lst_text[i] = lst_text[i][1::] + 'ay'
    return ' '.join(lst_text)

print(pig_it('Pig latin is cool !'))