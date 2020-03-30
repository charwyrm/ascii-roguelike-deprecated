from __init__ import *
from line import Line
class Panel(object):
	def __init__(self, h, v, p, is_entry = False):
		self.h_size = h
		self.v_size = v
		self.p = p
		self.e = is_entry
		self.content = []

		for i in range(0, self.v_size):
			self.content.append(Line(self.h_size))

		self.empty = self.content

	def Build(self, index, join_char='', spaced=True):
		if self.e:
			return f'{join_char}'.join(self.content[index].get_text())+'_'+' '*(self.h_size - len(self.content[index].text)-1)
		else:
			return f'{join_char}'.join(self.content[index].get_text())+' '*(self.h_size - len(self.content[index].text))
			
	def Clear(self):
		self.content = self.empty

	def Add_Char(self, index, char):
		return self.content[index].add_char(char)

	def Add_String(self, string):
		self.content.insert(0, Line(self.h_size))
		self.content[0].text = string.split()
		if len(self.content) > 5:
			del(self.content[5:])

	def Set(self, index, chars):
		self.content[index].set_text = chars
