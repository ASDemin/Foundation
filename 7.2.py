'''
2. Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
1. Элемент кратен 3,
2. Элемент положительный,
3. Элемент не кратен 4.

    Примечание: Список с целыми числами создайте вручную в начале файла.
    Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

'''

print(list)
import random

list=[random.randint(-30,30) for i in range(1,20)]
result1=[number for number in list if number%3==0]
result2=[number for number in list if number>0]
result3=[number for number in list if number%4!=0]
print(result1)
#print(result2)
#print(result3)
