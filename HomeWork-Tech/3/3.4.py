#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2.Написать функцию, которая принимает 3 аргумента - числа, 
найти среди них два максимальных, вывести в консоль
"""

def maxi(x1, x2, x3):
    l = [x1, x2, x3]
    min_num = int(x1)
    for i in l:
        if int(i) < int(x1):
            min_num = i
    l.remove(min_num)
    return l

a = input('Enter 1st num: ')
b = input('Enter 2nd num: ')
c = input('Enter 3rd num: ')

print(maxi(a, b, c))
