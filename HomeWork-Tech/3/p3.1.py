#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def num_mul(*nums):
    mul = 1
    for i in nums:
        mul *= i
    return mul

a = num_mul(1, 4, 7, 6)
print(a)