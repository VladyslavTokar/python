#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 

counter_total_answers = 0
counter_of_write_answers = 0

language = input('1. What language do we learn?: ')
if language == 'Python' or language == 'python':
    print('Yes, we learn ' + language)
    counter_of_write_answers += 1
else:
    print('No, we learn ' + 'Python')
counter_total_answers +=1

type_after_division = input('2. What number type we get after division? (1-int; 2-float; 3-complex)? ')
if type_after_division == '2' or type_after_division == '2-float' or type_after_division == 'float':
    print('Yes, it\'s float')
    counter_of_write_answers += 1
else:
    print('No, it\'s float')
counter_total_answers +=1

symbols_in_variables = input('3. What symbols can we use to name variables? (1-latin,all spec,numbers; 2-latin,only "_",numbers; 3-latin,numbers) ')
if symbols_in_variables == '2':
    print('Yes')
    counter_of_write_answers += 1
else:
    print('No, we can use "latin,only "_",numbers"')
counter_total_answers +=1

name_len = input('4. What len of your name? ')
name = input('Please enter your name: ')
if int(name_len) == len(name):
    print('Yes, your name {} has {} symbols'.format(name, name_len))
    counter_of_write_answers += 1
else:
    print('No, your name {} has {} symbols'.format(name, name_len))
counter_total_answers +=1

print('5. What booling type do you know: 1-True; 2-None; 3-False; 4-Var? (Need two answers)')
first_answer = input('Enter first answer: ')
second_answer = input('Enter second answer: ')
if first_answer == '1' and second_answer == '3':
    print('Yes')
    counter_of_write_answers += 1
else:
    print('No, There are "True" and "False"')
counter_total_answers +=1

coding_utf8 = input('6. Does python understand UTF-8 coding? (yes/no) ')
if coding_utf8 == 'yes' or coding_utf8 == 'y':
    print(True)
    counter_of_write_answers += 1
else:
    print(False)
counter_total_answers +=1

print('7. Enter two numbers for check human comparison:')
number_one = input('Number One: ') 
number_two = input('Number Two: ')
user_answer = input('Is {} greater then {}? (yes/no): '.format(number_one, number_two))
comparison = int(number_one) > int(number_two)
if user_answer == 'yes':
    if comparison == bool(True):
        print('Correct')
        counter_of_write_answers += 1
    else:
        print('Not correct')
elif user_answer == 'no':
    if comparison == bool(False):
        print('Correct')
        counter_of_write_answers += 1
    else:
        print('Not correct')
counter_total_answers +=1

print('8. Has your name a some letter?')
letter = input('Enter some letter: ')
name = input('Enter your name: ')
if letter in name:
    print(letter + 'is in your name')
    counter_of_write_answers += 1
else:
    print('There is no letter ' + letter + ' in your name')
counter_total_answers +=1

print('Total answers is: ' + str(counter_total_answers))
print('Correct answers is: ' + str(counter_of_write_answers))