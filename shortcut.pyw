import pyautogui
from pynput.keyboard import Key, Listener
import datetime
import getpass

needed_keys = ["Key.ctrl_l","Key.shift","Key.up","Key.down","Key.print_screen"]
pressed_keys = []

def check():
    if pressed_keys.count("Key.ctrl_l") and pressed_keys.count("Key.shift") and pressed_keys.count("Key.up"):
        pyautogui.press("volumeup")
    if pressed_keys.count("Key.ctrl_l") and pressed_keys.count("Key.shift") and pressed_keys.count("Key.down"):
        pyautogui.press("volumedown")
    if pressed_keys.count("Key.print_screen"):
        time_stab = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')
        directory = f'C:\\Users\\{getpass.getuser()}\\Pictures\\Screenshot\\Screenshot-{time_stab}.png'
        img = pyautogui.screenshot(directory)
def on_press(Key):
    if str(Key) in needed_keys:
        pressed_keys.append(str(Key))
        check()
    else:
        pass

def on_release(key):
    try:
        # print(str(key))
        pressed_keys.remove(str(key))
    except:
        pass

with Listener(on_press = on_press,on_release = on_release) as listener:
    listener.join()
