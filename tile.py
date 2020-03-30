from __init__ import *
class Tile():
	def __init__(self, x, y, ID, m):
		self.x = x
		self.y = y
		self.ID = ID
		self.m = m

		if self.ID == 'W':
			self.name = "wooden Wall"
			self.symbol = ' '
			self.fg_color = "yellow"
			self.bg_color = "dark yellow"			

			self.description = "a wooden wall made of bound logs, stripped of bark, with a waxy sheen."
			self.isPassable = False
			self.type = 'wall'
		
		elif self.ID == 'S':
			self.name = "stone Wall"
			self.symbol = ' '
			self.fg_color = "light gray"
			self.bg_color = "dark gray"
			self.description = "a rough wall made of carved stone, abrasive and cold to the touch."
			self.isPassable = False
			self.type = 'wall'
			
		elif self.ID == 's':
			self.name = "cobbled stone floor"
			self.symbol = '%'
			self.fg_color = "dark gray"
			self.bg_color = "black"
			self.description = "a cobbled floor made of jumbled stones, packed together with a clay mortar"
			self.isPassable = True
			self.type = 'floor'
			
		elif self.ID == 'b':
			self.name = "stone brick floor"
			
			if (x+(y%2)) % 2:
				self.symbol = '┬'
			else:
				self.symbol = '┴'
				
			self.fg_color = "dark gray"
			self.bg_color = "black"
			self.description = "a slabbed floor made of cut stone, packed together with a clay mortar"
			self.isPassable = True
			self.type = 'floor'
			
		elif self.ID == 'w':
			self.name = "wooden plank floor"
			self.symbol = '='
			self.fg_color = "dark yellow"
			self.bg_color = "black"
			self.description = "a planked floor made of cut wood, nailed together in a haphazard fashion."
			self.isPassable = True
			self.type = 'floor'
			
		elif self.ID == 'd':
			self.name = "door"
			self.symbol = ']'
			self.fg_color = "black"
			self.bg_color = "dark yellow"
			self.description = "a rustic wooden door, ajar, leaving a glimpse of the next room."
			self.isPassable = True
			self.type = 'decoration'
			
		elif self.ID == 'g':
			self.name = "grassy floor"
			self.symbol = random.choice(['"','\'', ';',':','.',','])
			self.fg_color = "dark green"
			self.bg_color = "black"
			self.description = "a patch of tufty meadow grass."
			self.isPassable = True
			self.type = 'decoration'
			
		elif self.ID == 'c':
			self.name = "chair"
			self.symbol = 'n'
			self.fg_color = "dark yellow"
			self.bg_color = "black"
			self.description = "a simple wooden stool. It's a little splintery..."
			self.isPassable = True
			self.type = 'decoration'
		
		elif self.ID == 'h':
			self.name = "chest"
			self.symbol = '±'
			self.fg_color = "dark yellow"
			self.bg_color = "black"
			self.description = "a rustic wooden chest, banded with iron."
			self.isPassable = False
			self.type = 'decoration'
			
		elif self.ID == 'T':
			self.name = "table"
			self.symbol = 'π'
			self.fg_color = "dark yellow"
			self.bg_color = "black"
			self.description = "a simple wooden table. It's top is weathered and stained with a carpenters' wax."
			self.isPassable = False
			self.type = 'decoration'
			
		elif self.ID == 'f':
			self.name = "flower"
			self.symbol = '¤'
			self.fg_color = random.choice(["magenta",'cyan','yellow','white', 'red'])
			self.bg_color = "black"
			mood = random.choice(['happy', 'contemplative', 'wistful', 'nostalgic', "like you're forgetting something whilst"])
			self.description = f"a little {self.fg_color} flower. You feel {mood} looking at it."
			self.isPassable = True
			self.type = 'decoration'
		
		elif self.ID == 'l':
			self.symbol = '~'
			self.name = "lava"
			self.bg_color = "red"
			self.fg_color = "dark red"
			if y > 0:
				if self.m[y-1][x].name != "lava":
					self.symbol = '▄'
					self.bg_color = "dark red"

			self.description = "a pit of lava, uncomfortably hot to even stand near to."
			self.isPassable = False
			self.type = 'pit'
			
		elif self.ID == 'u':
			self.symbol = '~'
			self.name = "water"
			self.bg_color = "cyan"
			self.fg_color = "white"
			if y > 0:
				if self.m[y-1][x].name != "water":
					self.symbol = '▄'
					self.bg_color = "dark cyan"
					self.fg_color = "dark cyan"

			self.description = "a pool of water, relaxing to stand next to."
			self.isPassable = False
			self.type = 'pit'
			
		else:
			self.ID == ' '
			self.name = "void"
			self.symbol = ' '
			self.fg_color = "black"
			self.bg_color = "black"
			self.description = "staring back."
			self.isPassable = False
			self.type = 'pit'

	def Shade(self, m):
		if self.ID == 'W':	
			if self.y < len(m)-1:
				if self.m[self.y+1][self.x].isPassable or self.m[self.y+1][self.x].type != 'wall':
					self.symbol = '▀'
				else:
					self.symbol = '█'
			else:
				self.symbol = '▀'
				
		if self.ID == 'S':	
			if self.y < len(m)-1:
				if self.m[self.y+1][self.x].isPassable or self.m[self.y+1][self.x].type != 'wall':
					self.symbol = '▀'
				else:
					self.symbol = '█'
			else:
				self.symbol = '▀'
			
