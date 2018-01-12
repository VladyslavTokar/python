#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = ['a', 24, 'to-delete', 'None', None, 'to-delete', 3, 'to-delete', 15, 64, ]
for i in l:
    if i == 'to-delete':
        l.remove(i)
#l.remove('to-delete')
print(l)