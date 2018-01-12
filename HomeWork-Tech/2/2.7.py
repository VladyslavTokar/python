#!/usr/bin/env python3
# -*- coding: utf-8 -*-

matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 11],
    [8, 10, 12],    
]
a = []
b = []
c = []
for row in matrix:
    print(row)
for col in matrix:
    a.append(col[0])
    b.append(col[1])
    c.append(col[2])

print(a) 
print(b)
print(c)
