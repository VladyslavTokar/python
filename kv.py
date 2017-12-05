#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def solve(AA, BB, CC):
    D = BB*BB - 4.0*AA*CC
    if D >= 0:
        X1 = ( -BB - math.sqrt(D) ) / ( 2.0 * AA )
        X2 = ( -BB + math.sqrt(D) ) / ( 2.0 * AA )
        return [ X1, X2]
    else:
        return []

A = float(input('(type1)a: ')) 
B = float(input('(type5)b: '))
C = float(input('(type6)c: '))

R = solve(A, B, C )
print(R)

print('END') 