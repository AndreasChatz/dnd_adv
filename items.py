class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return f"{self.name}\nDescription: {self.description}\nValue: {self.value}"


class Gold(Item):
	def __init__(self, amount):
		self.amount = amount
		super().__init__(name = 'Gold',
			description = f'{self.amount} round shiny coins of Gold',
			value = self.amount)


class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return f'{self.name}\nDescription: {self.description}\nDamage: {self.damage}\nValue: {self.value}'


class Dagger(Weapon):
	def __init__(self):
		super().__init__(name = 'Dagger', 
			description = 'A small finesse weapon', 
			value = 2, 
			damage = 4)

class EpicDagger(Weapon):
	def __init__(self):
		super().__init__(name = 'Epic Dagger', 
			description = 'A small really sharp dagger', 
			value = 120, 
			damage = 14)

