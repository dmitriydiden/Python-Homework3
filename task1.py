#Задача №1 Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

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

print("Ввудите число от 0-9:", end=" ")
number = input()
def number_search(ls, x, y):
    count = 0
    for i in range(0, x):
        if ls[i] == y:
            count=1
    if count==1:
        print(ls, 'Число', y, 'встречается в списке')
    else:
        print(ls, 'Число', y, 'не встречается в списке')
number_search(list, n, number)