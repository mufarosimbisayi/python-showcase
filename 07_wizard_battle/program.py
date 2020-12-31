print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import random
import time
from actors import Creature, Wizard, Dragon

def game_loop():
	creatures = [
		Creature("Toad", 1),
		Creature("Tiger", 12),
		Dragon("Dragon", 50),
		Wizard("Evil Wizard", 800)
	]

	hero = Wizard("Gandalf", 75)

	while True:
		active_creature = random.choice(creatures)
		print("A level {} {} appears from the dark and foggy forest...".format(
			active_creature.level, active_creature.name
		))
		print()
		action = input("Do you [a]ttack, [r]un away or [l]ook around? ")
	
		if action == 'a':
			victory = hero.attack(active_creature)
			if victory:
				print("The hero {} is victorious and the {} has been vanquished ...".format(
					hero.name, active_creature.name
				))
				creatures.remove(active_creature)
			else:
				print("{} has lost the battle and has to take some time to recover ...".format(
					hero.name
				))
				time.sleep(5)
				print("{} is revitalised and back for action ...".format(hero.name))
		elif action == 'r':
			hero.runs(active_creature)
		elif action == 'l':
			hero.looks_around(creatures)
		else:
			print("Exit status triggered ... goodbye!")
			break
		print()

		if not creatures:
			print("You have defeated all the creatures. Congrats!!")

def main():
	game_loop()

if __name__ == '__main__':
	main()
