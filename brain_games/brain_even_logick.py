import prompt
from random import randint

def game_logick():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello ' + name + '!')
	print('Anser "yes" if the number is even, otherwise answer "no".')
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
				
			
