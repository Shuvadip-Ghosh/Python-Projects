import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def load_text():
    lines = ["The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How quickly daft jumping zebras vex.",
    "Jinxed wizards pluck ivy from the big quilt.",
    "The five boxing wizards jump quickly.",
    "Bright vixens jump; dozy fowl quack.",
    "We promptly judged antique ivory buckles for the next prize.",
    "Crazy Fredrick bought many very exquisite opal jewels.",
    "The job requires extra pluck and zeal from every young wage earner.",
    "System.out.println();",
    "Scanner sc = new Scanner(System.in);",
    "public void main(){}"]
    return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)
	while True:
        try:
		    wpm_test(stdscr)
        except:
            continue
		stdscr.addstr(2, 0, "You completed the text!\nPress Esc to quit or\nPress any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)