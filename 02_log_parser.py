# -*- coding: utf-8 -*-
from pprint import pprint
# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

#
class Log_parser:
    def open_text_file(self, text_file):
        file = []
        with open('events.txt', 'r') as text_file:
            for line in text_file:
                if 'NOK' in line:
                    file.append(line[:17]+']')
            self.write_new_file(file)

            #pprint(file)

    def write_new_file(self, file):
        new_file = set()
        counter = 1
        with open('events_new.txt', 'a') as new_text_file:
            for i in file:
                if i not in new_file:
                    new_file.add(f'{i} = {file.count(i)}')
            new_file_list = sorted(list(new_file))
            for k in new_file_list:
                new_text_file.write(k+'\n')
        pprint(new_file_list)
            #pprint(new_file)



   # def write_new_text(self, file):



a = Log_parser()
a.open_text_file('events.txt')








# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
