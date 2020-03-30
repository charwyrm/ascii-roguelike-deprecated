from contextlib import contextmanager
import sys, os, random, textwrap
from msvcrt import getch as gch
os.system('mode con: cols=81 lines=25')
#sys.stdout.write(f"\033[38;5;7;48;5;59m")

tw = textwrap.TextWrapper(width=77)

class Color():
	def __init__(self):
		self.colors = {
		"black":30,
		"dark red":31,
		"dark green":32,
		"dark yellow":33,
		"dark blue":34,
		"dark magenta":35,
		"dark cyan":36,
		"light gray":37,
		"dark gray":90,
		"red":91,
		"green":92,
		"yellow":93,
		"blue":94,
		"magenta":95,
		"cyan":96,
		"white":97,
		}
	
	def Get_Color(self, fg_color, bg_color="black"):
		return f"\033[{self.colors[bg_color]+10};{self.colors[fg_color]}m"

	def Set_Color(self, fg_color, bg_color):
		sys.stdout.write(f"\033[{self.colors[bg_color]+10};{self.colors[fg_color]}m")

	def Random_Color(self):
		sys.stdout.write(f"\033[{random.choice([91, 92, 93, 94, 95, 96])+10};{random.choice([31, 32, 33, 34, 35, 36])}m")
		
	def Reset_Color(self):
		sys.stdout.write(f"\033[0;37m")
		return""
	
	def Refresh_Color(self):
		print("")
		os.system('cls')

c = Color()
def intro():
		c.Set_Color("white", "cyan")
		for i in range(0, 81*5):
			if i > 324:
				print(random.choice([' ','░']), end='')
			elif i >162:
				print(random.choice([' ','░','▒','▓']), end='')
			else:
				print(random.choice([' ','░','▒','▓','█']), end='')

		c.Set_Color("light gray", "cyan")
		for i in range(0, 81*1):
			print(' ', end='')

		for i in range(0, 81*1):
			if i%2 == 0:
				print('▄', end='')
			else:
				print(" ",end='')

		c.Set_Color("dark gray", "light gray")
		for i in range(0, 81*10):
			if i%2 == 0:
				print('┬', end='')
			else:
				print("┴",end='')

		c.Set_Color("dark green", "green")
		for i in range(0, 162):
			if i > 80:
				print('▒', end='')
			else:
				print(' ', end='')

		c.Set_Color("green", "dark green")
		for i in range(0, 486):
			print(random.choice([',', '\'']), end='')
		input()
		c.Reset_Color()

#intro()
