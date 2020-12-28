print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import random

random_number = random.randint(0, 100)


while 1:
	guessed_number = int(input('Guess a number between 0 and 100: '))
	if guessed_number < random_number:
		print("Sorry {} is lower than my number.".format(guessed_number))
	elif guessed_number > random_number:
		print("Sorry {} is higher than my number.".format(guessed_number))
	else:
		print("Yes, you got it. The number was {}.".format(guessed_number))
		break
