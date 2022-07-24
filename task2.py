'''
Задача №2 Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
'''
import random
import string

print("Введите количество строк в списке:", end=" ")
n = int(input())
list=[]
def criation_list(ls, x):
    for i in range(0, x):
        ls.insert(i, ''.join(random.choices(string.digits)))
        i+=1  
    print(ls)
    return(ls) 

criation_list(list, n)

print("Ввудите строку, позицию второго вхождения, которой вы хотите найти:", end=" ")
number = input()
def string_search(ls, x, y):
    count = 0
    for i in range(0, x):
        if ls[i] == y:
            count+=1
        if count == 2:
            print(ls, 'ищем:', y, 'ответ:', i)
            break
    if count!=2:
        print(ls, 'ищем:', y, 'ответ:', -1)

string_search(list, n, number)
