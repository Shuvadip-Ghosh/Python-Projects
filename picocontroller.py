# get the device ready for hid device and install circuit python 
# and save this file as code.py on the pico.

import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keypressf = False
keypressb = False

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

forward = digitalio.DigitalInOut(board.GP18)
forward.direction = digitalio.Direction.INPUT
forward.pull = digitalio.Pull.DOWN

forward1 = digitalio.DigitalInOut(board.GP19)
forward1.direction = digitalio.Direction.INPUT
forward1.pull = digitalio.Pull.DOWN

backward = digitalio.DigitalInOut(board.GP20)
backward.direction = digitalio.Direction.INPUT
backward.pull = digitalio.Pull.DOWN

backward1 = digitalio.DigitalInOut(board.GP21)
backward1.direction = digitalio.Direction.INPUT
backward1.pull = digitalio.Pull.DOWN


while True:
    if forward1.value and keypressf== True:
        keyboard.release(Keycode.W)
        keypressf = False
    elif forward.value and forward1.value and keypressf== False:
        keyboard.press(Keycode.W)
        keypressf = True
    elif backward1.value and keypressb== True:
        keyboard.release(Keycode.S)
        keypressb = False
    elif backward.value and backward1.value and keypressb== False:
        keyboard.press(Keycode.S)
        keypressb = True
