import prompt
from random import randint
import random


def game_logick():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello ' + name + '!')
	print('Answer "yes" if the number is even, otherwise answer "no".')
	n = 0
	while n != 3:
		b = randint(0, 50)
		print(f'Question: ' + str(b))
		answer = prompt.string('Your answer: ')
		if (b % 2 == 0 and answer == 'yes') or (b % 2 != 0 and answer == 'no'):
			print('Correct!')
			n += 1
		elif b % 2 == 0 and answer != 'yes':
			print(answer +  " is wrong answer ;(. Correct answer was 'yes'.\nLet's try again " + name + '!')
			break
		elif b % 2 != 0 and answer != 'no':
			print(answer + " is wrong answer ;(. Correct answer was 'no'.\nLet's try again " + name + '!')
			break
	if n == 3:
		print('Congratulations ' + name + '!')

				
def game_calc():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello ' + name + '!')
	print('What is the result of the expression?')
	n = 0
	while n != 3:
		a = randint(0, 50)
		b = randint(0, 50)
		c = random.choice(['+', '-', '*'])
		print('Question: ' + str(a) + ' ' + c + ' ' + str(b))
		if c == '+':
			answer_logic = a + b
		elif c == '-':
			answer_logic = a - b
		elif c == '*':
			answer_logic = a * b
		answer = prompt.string('Your answer: ')
		if int(answer) == answer_logic:
			print('Correct')
			n += 1
		elif int(answer_logic) != answer:
			print(answer + " is wrong answer ;(. Correct answer was " + str(answer_logic) + ".\nLet's try again " + name + '!')
			break
	if n == 3:
		print('Congratulations ' + name + '!')


def game_grd():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello ' + name + '!')
	print('Find the greatest common divisor of given numbers.')
	n = 0
	while n != 3:
		a = randint(0, 100)
		b = randint(0, 100)
		print('Question ' + str(a) + ' ' + str(b))
		while a != b:
			if a > b:
				a = a - b
			else:
				b = b - a
		answer = prompt.string('Your answer: ')
		if int(answer) == a:
			print('Correct!')
			n += 1
		elif int(answer) != a:
			print(answer + " is wrong answer ;(. Correct answer was " + str(a) + ".\nLet's try again " + name + '!')
			break
	if n == 3:
		print('Congratulations ' + name + '!')


def func_progression():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello ' + name + '!')
	print('What number is missing in the progression?')
	n = 0
	while n != 3:
		result = []
		step = randint(2, 5)
		for i in range(randint(10, 15), randint(60, 70), step):
			result.append(i)
		random_position = randint(0, 5)
		right_answer = result[random_position]
		result[random_position] = '..'
		result_str = ' '.join(map(str, result))
		result_str = result_str[0:30]
		print('Question: ' + result_str)
		answer = prompt.string('Your answer: ')
		if answer == str(right_answer):
			print('Correct!')
			n += 1
		elif answer != str(right_answer):
			print(answer + " is wrong answer ;(. Correct answer was " + str(right_answer) + ".\nLet's try again " + name + '!')
			break
	if n == 3:
		print('Congratulations ' + name + '!')


def func_simple_numbers():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello ' + name + '!')
	print('Answer "yes" if given number is prime. Otherwise answer "no".')
	n = 0
	number_prime = 0
	while n!= 3:
		number = randint(0, 100)
		print('Question: ' + str(number))
		answer = prompt.string('Your answer: ')
		for i in range(2, number + 1):
			if number % i == 0:
				break
			else:	
				number_prime = 1
		if number_prime == 1:
			if answer =='yes':
				print('Correct!')
				n += 1
			elif answer != 'yes':
				print(answer + " is wrong answer ;(. Correct answer was 'yes' .\nLet's try again " + name + '!')		
				break
		else:
			if answer =='no':
				print('Correct!')
				n += 1
			elif answer != 'no':
				print(answer + " is wrong answer ;(. Correct answer was 'no' .\nLet's try again " + name + '!')		
				break					
	if n == 3:
		print('Congratulations ' + name + '!')
