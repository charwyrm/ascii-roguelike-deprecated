from __init__ import *
class CommandHandler():
	def __init__(self, p, gm, lm):
		self.player = p
		self.global_map = gm
		self.local_map = lm

	def ProcessCommand(self, command):
		if command == None:
			return None
		else:
			tokens = "".join(command).split(' ')
			if tokens[0] == "say":
				return self.cSay(tokens[1:])
			if tokens[0] == "look":
				if len(tokens) > 1:
					return self.cLook(tokens[1:])
				else:
					return self.cLook(['h'])
			else:
				return [f"Command \"{' '.join(tokens)}\" not recognised."]
				
	def ProcessKeyPress(self, key_char):
		if key_char == None:
			return None
		else:
			if key_char in ['w', 'a', 's', 'd']:
				return self.kGo(key_char)
			else:
				return None

	def cSay(self, tokens):
		return [f"{self.player.name} said: \"{' '.join(tokens)}\""]
		
	def cLook(self, tokens):
		
		if tokens[0] == 'n' or tokens[0] == "north":
			if 0 < self.player.local_y:
				return tw.fill(f"You look north and see a {self.local_map[self.player.local_y-1][self.player.local_x].name}. It's {self.local_map[self.player.local_y-1][self.player.local_x].description}").split('\n')
		
		elif tokens[0] == 's' or tokens[0] == "south":
			if self.player.local_y < len(self.local_map)-1:
				return tw.fill(f"You look south and see a {self.local_map[self.player.local_y+1][self.player.local_x].name}. It's {self.local_map[self.player.local_y+1][self.player.local_x].description}").split('\n')
		
		elif tokens[0] == 'w' or tokens[0] == "west":
			if 0 < self.player.local_x:
				return tw.fill(f"You look west and see a {self.local_map[self.player.local_y][self.player.local_x-1].name}. It's {self.local_map[self.player.local_y][self.player.local_x-1].description}").split('\n')

		elif tokens[0] == 'e' or tokens[0] == "east":
			if self.player.local_x < len(self.local_map[0])-1:
				return tw.fill(f"You look east and see a {self.local_map[self.player.local_y][self.player.local_x+1].name}. It's {self.local_map[self.player.local_y][self.player.local_x+1].description}").split('\n')		

		elif tokens[0] == 'h' or tokens[0] == "here":
			if self.player.local_x < len(self.local_map[0])-1:
				return tw.fill(f"You look below your feet and see a {self.local_map[self.player.local_y][self.player.local_x].name}. It's {self.local_map[self.player.local_y][self.player.local_x].description}").split('\n')		

		else:
			return None
	
	def kGo(self, key_char):
		
		if key_char == "w":
			if 0 < self.player.local_y:
				if self.local_map[self.player.local_y-1][self.player.local_x].isPassable:
					self.player.local_y -= 1
				
		elif key_char == "s":
			if self.player.local_y < len(self.local_map)-1:
				if self.local_map[self.player.local_y+1][self.player.local_x].isPassable:
					self.player.local_y += 1
				
		elif key_char == "a":
			if 0 < self.player.local_x:
				if self.local_map[self.player.local_y][self.player.local_x-1].isPassable:
					self.player.local_x -= 1	
				
		elif key_char == "d":
			if self.player.local_x < len(self.local_map[0])-1:
				if self.local_map[self.player.local_y][self.player.local_x+1].isPassable:
					self.player.local_x += 1
		return None
		
