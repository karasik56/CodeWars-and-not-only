def polindrom(n):
    if n == n[::-1]:
        print('Полиндром')
    else:
        print('Не полиндром')

n = 'anna'
polindrom(n)