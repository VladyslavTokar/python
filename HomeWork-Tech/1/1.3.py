#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 

print('Super simple calculator')
num1 = input('Enter first number: ')
action = input('Enter action (+/-): ')
num2 = input('Enter second number: ')
if action == '+':
    result = int(num1) + int(num2)
elif action == '-':
    result = int(num1) - int(num2)
print('The result is: ' + str(result))