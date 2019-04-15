#2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

'''
def max_ch():
    a=(int(input('Введите число:')))
    b=(int(input('И ещё разок')))
    c=(int(input('Последний раз')))
    list=[a,b,c]
    print (max(list))

max_ch(
'''

def max_ch():
    list=[]
    for i in range (3):
        chislo = int (input())
        list.append(chislo)
    print (max(list))

max_ch()