#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_int_sort(l):
    new_l = []
    for i in l:
        try:
            int(i)
        except:
            print('ValueError')
        else:
            new_l.append(i)
    new_l.sort()
    print(new_l)

list_int_sort([4, 'e', 6, 90, 3, 7, 4, 2])