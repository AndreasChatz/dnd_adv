from player import Player

class Actions(object):
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.name = name
		self.hotkey = hotkey
		self.kwargs = kwargs

	def __str__(self):
		return f"{self.hotkey}: {self.name}"


class MoveNorth(Actions):
	def __init__(self):
		super().__init__(method = Player.move_north, name = 'Move north', hotkey = 'n')


class MoveSouth(Actions):
	def __init__(self):
		super().__init__(method = Player.move_south, name = 'Move south', hotkey = 's')

class MoveEast(Actions):
	def __init__(self):
		super().__init__(method = Player.move_east, name = 'Move east', hotkey = 'e')

class MoveWest(Actions):
	def __init__(self):
		super().__init__(method = Player.move_west, name = 'Move west', hotkey = 'w')
		
class ViewInventory(Actions):
	"""Prints the player's inventory"""
	def __init__(self):
		super().__init__(method = Player.print_inventory, name = 'View inventory', hotkey = 'i')

class Attack(Actions):
	def __init__(self, enemy):
		super().__init__(method = Player.attack, name = 'Attack', hotkey = 'a', enemy = enemy)

class Flee(Actions):
	def __init__(self, tile):
		super().__init__(method = Player.flee, name = 'Flee', hotkey = 'f', tile = tile)