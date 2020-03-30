from inventory import Inventory
class Player():
	def __init__(self, name, gx, gy, lx, ly):
		self.name = name
		self.global_x = gx # Global position is the room the player is in
		self.global_y = gy
		self.local_x = lx # Local position is the specific coordinate inside of a room the player is in
		self.local_y = ly
		self.fg_color = "white"
		self.bg_color = "magenta"
		self.inventory = Inventory(10)
	
	def TilewiseMove(self, vector):
		self.local_x += vector[0]
		self.local_y += vector[1]
	
	def RoomwiseMove(self, vector):
		self.global_x += vector[0]
		self.globaL_y += vector[1]
