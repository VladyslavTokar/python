#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l_div7 = []
l_not_div7 = []

for i in range(1, 100 + 1):
    if i % 7 == 0:
        l_div7.append(i)
    else:
        l_not_div7.append(i)

print('List div to 7: ', l_div7)
print('List NOT div to 7: ', l_not_div7)
