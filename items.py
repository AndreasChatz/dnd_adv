class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return f"{self.name}\nDescription: {self.description}'\nValue: {self.value}"


class Gold(Item):
	def __init__(self, amount):
		sefl.amount = amount
		super().__init__(name = 'Gold',
						description = f'{self.amount} round shiny coins of Gold',
						value = self.amount)


class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super.__init__(name, description, value)

	def __str__(self):
		return f'{name}\nDescription: {description}\nDamage: {self.damage}',
				'\nValue: {self.value}'
