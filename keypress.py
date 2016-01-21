#!/usr/bin/env python 
## Play sounds on keypresses in Linux
## Originally by Sayan "Riju" Chakrabarti (sayanriju) 
## http://rants.sayanriju.co.cc/script-to-make-tick-tick-sound-on-keypres
 
from Xlib.display import Display 
import threading
import os 
import time
import Xlib

notes=[440,494,523,587,659,698,784]
 
ZERO,SHIFT,ALT,CTL=[],[],[],[] 
for i in range(0,32): 
	ZERO.append(0) 
	if i==6: 
		SHIFT.append(4) 
	else: 
		SHIFT.append(0) 
	if i==4: 
		CTL.append(32) 
	else: 
		CTL.append(0) 
	if i==8: 
		ALT.append(1) 
	else: 
		ALT.append(0) 
		 
ignorelist=[ZERO,ALT,SHIFT,CTL] 
# ignorelist=[ZERO]

class KeyPress(threading.Thread):
	def run(self):
		os.system("aplay sounds/key01.wav")

def main(): 
	disp = Display()
	screen = disp.screen()
	w = screen.root.create_window(0, 0, 100, 100, 1,
		screen.root_depth,
		event_mask = Xlib.X.KeyPressMask)
	w.map()
	
	while True:
		event = disp.next_event()
		if event.type != Xlib.X.KeyPress:
			continue
		
		keymap = disp.query_keymap() 
		if keymap not in ignorelist: 
			KeyPress().start()
			time.sleep(0.08)
 
if __name__ == '__main__': 
	main() 
