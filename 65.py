def convert_c_to_f():
    for t in range(0,101,10):
        fahr = (( t * (9/5))+32)
        print(f'Температура по Цельсию {t}, Температура по Фаренгейту {fahr}')


convert_c_to_f()