#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, 
иначе - к нижнему
"""

def letter_case(my_string, case=True):
    if case == True:
        a = my_string.lower()
    elif case == False:
        a = my_string.upper()
    return a

print(letter_case('KJHsjkhKJdkjHWWODKksd', False))
