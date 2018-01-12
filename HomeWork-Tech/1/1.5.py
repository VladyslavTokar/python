#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 

print('Check the multiplicity by 5')

user_num1 = int(input('Enter first number: '))
user_num2 = int(input('Enter second number: '))

for i in range(user_num1, user_num2 + 1):
    if i % 5 == 0:
        print(i)


