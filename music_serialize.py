'''
1. С помощью модулей json и pickle сериализовать данный словарь
 в json и в байты, вывести результаты в терминал.
 Записать результаты в файлы group.json, group.pickle соответственно.
  В файле group.json указать кодировку utf-8.
'''
import json,pickle

my_fav_band ={
    'name':'сектор_газа',
    'tracks':['Еду бабу выручать','Колхозный панк'],
    'albums':[{'name':'Ядрена вошь', 'year':'1990'},{'name':'Восставшие из ада', 'year':'2000'}]}

with open('band.dat','wb')as f:
    pickle.dump(my_fav_band, f)

print ('Записано pickle')

import json

with open('band.json', 'w', encoding='utf-8') as f:
    json.dump(my_fav_band,f)

print ('Записано json')