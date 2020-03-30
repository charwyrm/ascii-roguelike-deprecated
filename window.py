from __init__ import *
from map import Map
from panel import Panel
from mappanel import MapPanel

class Window():
	def __init__(self, p):

		self.p = p

		self.p1 = MapPanel(63, 15,
		Map([
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','f','g','f','u','u','u','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','S','S','S','S','S','S','g','g','g','W','W','W','W','W','g','g','b','b','b','b','b','b','b','b','g','g','g','f','g','g','g','g','f','g','f','g','u','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','b','h','b','h','b','S','g','g','g','W','h','w','w','W','g','g','b','b','b','b','b','c','b','b','g','g','f','g','g','g','f','g','g','g','g','g','g','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','b','b','b','b','b','S','g','g','g','W','w','w','w','d','g','g','b','b','b','b','c','T','c','b','g','g','g','g','f','g','g','g','f','g','g','g','f','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','b','b','b','b','b','d','s','s','g','W','w','w','w','W','g','g','b','b','b','b','b','c','b','b','g','g','g','g','g','f','g','g','S','S','S','S','S','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','b','b','b','b','b','S','g','s','g','W','W','w','W','W','g','g','b','b','b','b','b','b','b','b','g','g','g','f','g','g','g','b','S','b','b','g','S','g','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','b','b','b','b','b','S','g','s','g','g','W','d','W','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','b','h','g','S','g','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','S','S','S','S','S','S','S','g','s','g','W','W','s','W','W','g','S','S','d','S','S','g','g','g','g','g','g','g','g','g','f','g','b','d','b','b','b','S','b','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','g','W','s','s','s','W','S','S','s','s','s','S','g','g','g','g','g','g','g','g','g','g','g','g','S','b','g','g','S','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','d','s','s','s','s','d','s','s','s','s','S','g','g','g','g','g','g','g','g','g','g','g','g','S','b','g','g','S','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','W','s','s','s','W','S','S','s','s','s','S','g','g','g','g','g','g','g','g','g','g','g','g','S','S','S','S','S','u','u','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','W','W','W','W','W','g','S','S','S','S','S','g','g','g','g','g','g','g','g','g','g','g','g','g','g','b','b','g','f','g','u'],
		['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','f','g','g','f','g','g','g','g','u','u']
		
		]), p, True)

		self.p2 = Panel(15, 6, p)

		self.p3 = MapPanel(15, 9,
		Map([
		[1,2,1,2,1],
		[0,0,2,0,0],
		[1,2,1,0,0],
		[0,0,2,0,0],
		[1,2,1,2,1]
		]), p, False)

		self.p4 = Panel(78, 5, p)
		self.p5 = Panel(77, 1, p, False)

	def Print(self):
		self.scaffold = f"""
╔═<Local Map>═══════════════════════════════════════════════════╤═<Stats>═══════╗
║{self.p1.MBuild(0)}│{self.p2.Build(4)[0:15]}║
║{self.p1.MBuild(1)}│{self.p2.Build(3)[0:15]}║
║{self.p1.MBuild(2)}│{self.p2.Build(2)[0:15]}║
║{self.p1.MBuild(3)}│{self.p2.Build(1)[0:15]}║
║{self.p1.MBuild(4)}│{self.p2.Build(0)[0:15]}║
║{self.p1.MBuild(5)}├─<World Map>───╢
║{self.p1.MBuild(6)}│{self.p3.MBuild(0)}║
║{self.p1.MBuild(7)}│{self.p3.MBuild(1)}║
║{self.p1.MBuild(8)}│{self.p3.MBuild(2)}║
║{self.p1.MBuild(9)}│{self.p3.MBuild(3)}║
║{self.p1.MBuild(10)}│{self.p3.MBuild(4)}║
║{self.p1.MBuild(11)}│{self.p3.MBuild(5)}║
║{self.p1.MBuild(12)}│{self.p3.MBuild(6)}║
║{self.p1.MBuild(13)}│{self.p3.MBuild(7)}║
║{self.p1.MBuild(14)}│{self.p3.MBuild(8)}║
╟─<Output>──────────────────────────────────────────────────────┴───────────────╢
║ {self.p4.Build(4, ' ')[0:78]}║
║ {self.p4.Build(3, ' ')[0:78]}║
║ {self.p4.Build(2, ' ')[0:78]}║
║ {self.p4.Build(1, ' ')[0:78]}║
║ {self.p4.Build(0, ' ')[0:78]}║
╟─<Input>───────────────────────────────────────────────────────────────────────╢
║> {self.p5.Build(0)[max(0, len(self.p5.content[0].get_text())-77):max(77, (len(self.p5.content[0].get_text())))]}║
╚═══════════════════════════════════════════════════════════════════════════════╝"""
		print(self.scaffold, end='')
