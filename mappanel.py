from __init__ import *
from panel import Panel
from line import Line

from map import Map

class MapPanel(Panel):
	def __init__(self, h, v, m, p, isLocal):
		super().__init__(h, v, p)
		self.tile_map = m
		self.isLocal = isLocal
		if self.isLocal:
			self.px, self.py = self.p.local_x, self.p.local_y
		else:
			self.px, self.py = self.p.global_x, self.p.global_y
		 
		self.Refresh(self.px, self.py)

	def Refresh(self, px, py):
		
		self.content = []
		for i in range(0, self.v_size):
			self.content.append(Line(self.h_size))
			
		xpos, ypos = 0, 0
		
		for y in self.tile_map.m:
			for x in y:
				if xpos == px and ypos == py:
					self.content[ypos].add_char(f"{c.Get_Color(self.p.fg_color, self.p.bg_color)}@{c.Get_Color('light gray')}")
				else:
					self.content[ypos].add_char(f"{c.Get_Color(x.fg_color, x.bg_color)}{x.symbol}{c.Get_Color('light gray')}")
				xpos +=1
			xpos = 0
			ypos += 1
			
	def MBuild(self, index, join_char=''):
		
		if self.isLocal:
			self.px, self.py = self.p.local_x, self.p.local_y
		else:
			self.px, self.py = self.p.global_x, self.p.global_y
			
		self.Refresh(self.px, self.py)
		longest = 0
		index-=1
		for i in self.content:
			if len(i.text) > longest:
				longest = len(i.text)
				
		for i in self.content:
			i.text += ' '*(longest - len(i.text))
	 	
		
		if longest % 2 == 0:
			return (' '*int((self.h_size - longest)/2)+
			f'{join_char}'.join(self.content[index].get_text())+
			' '*int((self.h_size - longest)/2+1))
			
		else:
			return (' '*int((self.h_size - len(self.content[index].text))/2)+
			f'{join_char}'.join(self.content[index].get_text())+
			' '*int((self.h_size- len(self.content[index].text))/2))
