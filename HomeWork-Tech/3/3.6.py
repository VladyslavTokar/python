#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1.Написать функцию, которая принимает любое количество аргументов чисел. 
Среди них она находит максимальное и минимальное. И возвращает оба
"""

def min_max(*numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return (min_num, max_num)

print(min_max(6, 3, 5, 43, 37, 34, 1024, 23, 2, 35, 436, 64, 53, 24))
