import serial
import pydirectinput 
import serial.tools.list_ports
import time

s = list(serial.tools.list_ports.comports())
inpstring = ""
for index , e in enumerate(s):
    inpstring = inpstring + str(index) + " "+ str(e.description) + "\n"

inp = int(input(inpstring+">>> "))

arduino = serial.Serial(s[inp].name,115200,timeout=.1)

pydirectinput.PAUSE = 0

keysDown = {}   #list of currently pressed keys


def keyDown(key):               #what to do if key pressed. takes value from handleJoyStickAsArrowKeys
    keysDown[key] = True        #adds key to KeysDown list
    pydirectinput.keyDown(key)  #runs pydirectinput using key from (argument)
    #print('Down: ', key)       #remove '#' from print to test data stream


def keyUp(key):                     #what to do if key released. takes value from handleJoyStickAsArrowKeys
    if key in keysDown:
        del (keysDown[key])         #remove key from KeysDown
        pydirectinput.keyUp(key)    #runs pydirectinput using key from (argument)
        #print('Up: ', key)         #remove '#' from print to test data stream

def handlekeys(x):      #note that the x and y directions are swapped due to the way I orient my thumbstick
    if x == 'w':          #0 is up on joystick
        keyDown('up')   #add up key to keyDown (argument)
        keyUp('down')   #add down key to keyUp (argument), as you can't press up and down together
    elif x == 's':        #2 is down on joystick
        keyDown('down')
        keyUp('up')
    else:               #1 is neutral on joystick
        keyUp('up')
        keyUp('down') 
time.sleep(2)
while True:
    rawdata = arduino.readline()
    try:
        data = str(rawdata.decode('utf-8'))
        data = data.replace('\n',"")
        data = data.replace('\r',"")
        if data == 's' or data == 'w':
            print(data)
            handlekeys(data)
    except UnicodeDecodeError as e:
        print(rawdata)
