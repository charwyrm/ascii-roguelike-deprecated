from __init__ import *
from window import Window
from player import Player
from commandhandler import CommandHandler
#(chr(ord(gch())))


p = Player(input(('\n'*11) + (' '*20) + 'Please enter the player character\'s name'+ ('\n'*12) + (' '*32) +'> '), 2, 3, 23, 4)
os.system('cls')
w = Window(p)
ch = CommandHandler(p, w.p3.tile_map.m, w.p1.tile_map.m)

is_command_being_entered = False
while True:
	w.p2.content[4].set_chars(f"({p.local_x}, {p.local_y})")
	w.Print() #Output
	is_command_being_entered = False
	t_char = chr(ord(gch())) # Input
	
	if t_char == '\r':
		is_command_being_entered = True
		w.p5.e = True
		
		
	while is_command_being_entered:
		w.Print()
		
		t_char = chr(ord(gch())) # Input
		returned_text = w.p5.Add_Char(0, t_char+"")
		if not returned_text == None:
			is_command_being_entered = False
			w.p5.e = False
			if len(returned_text) > 0:
				returned_text = (ch.ProcessCommand(returned_text))
				if not returned_text == None:
					for text in returned_text:
						w.p4.Add_String(text)
				
	returned_text = ch.ProcessKeyPress(t_char)
	if not returned_text == None:
		if len(returned_text) > 0:
			w.p4.Add_String(returned_text)
				
	#os.system('cls') # Clear Screen

