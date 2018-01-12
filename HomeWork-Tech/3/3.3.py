#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1.Написать функцию, которая принимает на вход два аргумента. 
Если аргументы больше нуля, возвращаем их сумму. 
Если оба меньше - разность. Если знаки разные - возвращаем 0
"""

def aref_arg(x1, x2):
    if x1 > 0 and x2 > 0:
        return (x1 + x2)
    elif x1 < 0 and x2 < 0:
        return (x1 - x2)
    elif (x1 < 0 and x2 > 0) or (x1 > 0 and x2 < 0):
        return 0

a = float(input('Enter 1st num: '))
b = float(input('Enter 2nd num  '))

print(aref_arg(a, b))