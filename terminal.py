import subprocess
import curses
import os
import platform

def run(command):
	return subprocess.run(command.split(), shell=True, capture_output=True).stdout.decode()

def main(stdscr):
	if platform.system() == 'Windows':
		stdscr.addstr(f"Microsoft Windows [Version {platform.version()}]\n(c) Microsoft Corporation. All rights reserved.\n\n")
	prev_command = []
	s= " "
	d_com = []
	y = 3
	while True:
		command = ""
		stat = f"[{os.getlogin()}@{platform.node()}]-[{os.getcwd()}]$ "
		x = len(stat)
		stdscr.addstr(y,0,stat)
		while True:
			key = stdscr.getkey()
			if key == "KEY_UP" and prev_command!=[]:
				d_com.append(command)
				command = prev_command.pop()
				stdscr.addstr(y,x,command)

			elif key == "KEY_DOWN" and d_com!=[]:
				command = d_com.pop()
				stdscr.addstr(y,x,command)

			elif key == "KEY_LEFT":
				stdscr.addstr("left")
			elif key == "KEY_RIGHT":
				stdscr.addstr("right")
			elif key in ("KEY_BACKSPACE", '\b', "\x7f"):
				command = command[0:len(command)-1:]
				stdscr.addstr(y,x,command)

			elif ord(key) == 10:
				prev_command.append(command)
				res = run(command)
				# stdscr.addstr("\n")
				# y+=1
				break
			else:
				command = command+key
				stdscr.addstr(key)
			# stdscr.addstr(y,x,command)
			stdscr.refresh()
		y+=1
		
		


		
	# get pc name ,directory name,git status if any.
	# get input then pass the input to the run(command) above
	# then display the returned value.

curses.wrapper(main)