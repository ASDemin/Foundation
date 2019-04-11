'''
2: Создать модуль music_deserialize.py. В этом модуле
открыть файлы group.json и group.pickle, прочитать из
них информацию. Получить объект — словарь из предыдущего задания.
'''

import json,pickle

with open ('band.json', 'r', encoding ='utf-8') as f:
    my_fav_band=json.load(f)

print(my_fav_band)
print(my_fav_band['tracks'])
print('_______________________________________________________________')

with open ('band.dat', 'rb') as f:
    my_f_b=pickle.load(f)
print(my_f_b)
print(my_f_b['name'])