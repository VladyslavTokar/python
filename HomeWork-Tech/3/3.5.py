#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
3.Написать функцию, которая принимает два аргумента. 
Первый - список чисел, второй - булевый флаг. 
Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, 
если флаг отрицателен - возвращаем новый список с четными числами из входного списка
"""

def even_odd(x1, x2):
    my_list = []
    if x2 == True:
        for i in x1:
            if int(i) % 2 != 0:
                my_list.append(i)
    elif x2 == False:
        for i in x1:
            if int(i) % 2 == 0:
                my_list.append(i)

    return my_list

a = [1, 2, 5, 3, 4, 7, 8, 11, 13, 6, 10, 60, 154, 3542]
#b = input('Enter True/False for even/odd: ')
print(even_odd(a, False))