#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = int(input('Enter num: '))

try:
    if num % 2 == 0:
        raise ValueError('Num multiplicity 2')
    elif num < 0:
        raise TypeError('Num less then 0')
    elif num > 10:
        raise IndexError('Num grate then 10')
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)
#my git chng
