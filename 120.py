total_word = []
while True:
    word = input()
    if word == '':
        print('Ввод закончен')
        break
    else:
        total_word.append(word)
if len(total_word) == 1:
    print(f'{total_word[0]}')
elif len(total_word) == 2:
    print(f'{total_word[0]} и {total_word[1]}')
elif len(total_word) >2:
    for i in len(total_word)-2:
        print(f'{total_word[0]}, {total_word[1]} и {total_word[2]}')

