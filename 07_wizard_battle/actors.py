import random

class Creature:
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def muster_defense_or_attack(self):
		return random.randint(1, 12) * self.level


class Dragon(Creature):
	def __init__(self, name, level, scaliness=15, breathes_fire=True):
		super().__init__(name, level)
		self.scaliness = scaliness
		self.breathes_fire = breathes_fire

	def muster_defense_or_attack(self):
		base_roll = super().muster_defense_or_attack()
		scale_modifier = self.scaliness / 10
		fire_modifier = 1.5 if self.breathes_fire else 1

		return base_roll * scale_modifier * fire_modifier


class Wizard(Creature):
	def attack(self, creature):
		print("The hero {} attacks the level {} {} ...".format(
			self.name, creature.level, creature.name
		))

		hero_roll = super().muster_defense_or_attack()
		creature_roll = creature.muster_defense_or_attack()

		print("{} musters an attack worth {} points ...".format(
			self.name, hero_roll
		))
		print("The {} musters a defense worth {} points ...".format(
			creature.name, creature_roll
		))

		if hero_roll > creature_roll:
			return True
		else:
			return False

	def runs(self, creature):
		print("The hero {} runs like a coward from a level {} {} ...".format(
			self.name, creature.name, creature.level
		))

	def looks_around(self, creatures):
		print("The hero {} looks around and sees:".format(self.name))
		for creature in creatures:
			print("A level {} {}".format(creature.level, creature.name))
