class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return f"{self.name} : {self.description}\n{self.value}"


class Gold(Item):
	def __init__(self, amount):
		sefl.amount = amount
		super().__init__(name = 'Gold',
						description = f'{self.amount} round shiny coins of Gold',
						value = self.amount)