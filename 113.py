total_word = []
sorted_total_word = []
while True:
    word = input()
    if word == '':
        print('Ввод закончен')
        break
    else:
        total_word.append(word)
    for i in total_word:
        if i not in sorted_total_word:
            sorted_total_word.append(i)
print(sorted_total_word)
