#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
3.Написать функцию, которая принимает любое количество позиционных аргументов - строк 
и один парматер по-умолчанию glue, который равен ':'. 
Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. 
Для соединения между любых двух строк вставлять glue
"""

def glue_fun(*strings, glue=':'):
    l = []
    for i in strings:
        if len(i) > 3:
            l.append(i)
    s = glue.join(l)
    return s

print(glue_fun('dadd', 'asdasd', 'fd', 'dfsdfss', 'd'))