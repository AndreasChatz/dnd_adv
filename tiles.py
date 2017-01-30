import items, enemies

class MapTile(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()

class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You find yourself in a cave with a flickering torch on the wall.
		You can make out four paths, each equally as dark and foreboding.
		"""
	def modify_player(self, player):
		# Room has no action on player
		pass


class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		self.add_loot(player)


class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print(f"Enemy does {self.enemy.damage} damage. You have {the_player.hp} HP remaining.")

class EmptyCavePath(MapTile):
	def intro_text(self):
		return """
		Another unremarkable part of the cave. You must forge onwards.
		"""

	def modify_player(self):
		pass

class  RogueRoom(EnemyRoom):
	"""docstring for  RogueRoom"""
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Rogue())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A rogue jumps in front of you!
			"""
		else:
			return """
			The corpse of a rogue rots on the ground.
			"""

class FindDaggerRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Dagger())

	def intro_text(self):
		return """
		You notice something shiny in the corner.
		It's a dagger! You pick it up.
		"""
		