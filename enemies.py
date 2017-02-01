class Enemy(object):
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0


class Rogue(Enemy):
	def __init__(self):
		super().__init__(name = 'Rogue', hp = 20, damage = 5)
