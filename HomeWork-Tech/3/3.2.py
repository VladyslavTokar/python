#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, 
который хочет посмотреть. 
Если все хорошо - пишите объект в консоль. 
Если нет - обработайте возмозможные ошибки и скажите ему, что не так
"""

my_list = [1, 4, 3, 'ds', None, 'k', [1, 2, 3], '2']
user_in = input('Enter num: ')

try:
    print(my_list[int(user_in)])
except IndexError:
	print('Try another num!')
except ValueError:
	print('Enter a num!')