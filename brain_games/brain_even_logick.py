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





		 

	 
	 
	 
	 
	 
	 
	 
