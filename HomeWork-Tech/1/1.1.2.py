#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 

print('9. Enter two numbers for computer comparison:')
number_one = int(input('Number One: '))
comparison_symbol = input('Enter comparison symbol ("<" or ">" or "="): ') 
number_two = int(input('Number Two: '))
if comparison_symbol == '=':
    if number_one == number_two:
        print(str(number_one) + ' eq ' + str(number_two))
    else:
        print(str(number_one) + ' not eq ' + str(number_two))
elif comparison_symbol == '<':
    if number_one < number_two:
        print(str(number_one) + ' less then ' + str(number_two))
    else:
        print(str(number_one) + ' not less then ' + str(number_two))
elif comparison_symbol == '>':
    if number_one > number_two:
        print(str(number_one) + ' grater then ' + str(number_two))
    else:
        print(str(number_one) + ' not grater then ' + str(number_two))
else:
    print('You enter wrong comparison symbol')