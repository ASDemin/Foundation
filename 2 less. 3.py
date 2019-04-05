name = input('Как Вас зовут?')
s_name = input('А фамилия?')
age = int(input('Сколько Вам лет?'))
weight = int(input('Сколько Вы весите?'))
if age < 30 and (weight > 50 or weight < 120):
    print('У Вас хорошее состояние.')
if age > 30 and (weight < 50 or weight > 120):
    print('Вам надо заняться собой!')
if age > 40 and (weight < 50 or weight > 120):
    print("Вам нужно обратиться к врачу!")
