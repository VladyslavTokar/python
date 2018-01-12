#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_list = [1, 4, 3, 'ds', None, 'k', [1, 2, 3], '2']
user_in = input('Enter num: ')

try:
    print(my_list[int(user_in)])
except IndexError:
	print('Try another num!')
except ValueError:
	print('Enter a num!')