from __init__ import *
from tile import Tile
class Map():
	def __init__(self, s):
		self.Build_Map(s)

	def Build_Map(self, s):
		xpos = 0
		ypos = 0
		temp_map = []
		for _list in s:
			temp_list=[]
			for _id in _list:
				temp_list.append(Tile(xpos, ypos, _id, temp_map))
				xpos+=1
			xpos = 0
			ypos += 1
			temp_map.append(temp_list)
		self.m = temp_map
		for l in self.m:
			for t in l:
				t.Shade(self.m)
