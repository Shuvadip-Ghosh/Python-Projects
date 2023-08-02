import websocket
import json
import pydirectinput
pydirectinput.PAUSE = 0


keysDown = {}   #list of currently pressed keys


def keyDown(key):               #what to do if key pressed. takes value from handleJoyStickAsArrowKeys
    keysDown[key] = True        #adds key to KeysDown list
    pydirectinput.keyDown(key)  #runs pydirectinput using key from (argument)
    #print('Down: ', key)       #remove '#' from print to test data stream


def keyUp(key):                     #what to do if key released. takes value from handleJoyStickAsArrowKeys
    if key in keysDown:
        del (keysDown[key])         #remove key from KeysDown
        pydirectinput.keyUp(key)  


def on_message(ws, message):
    values = json.loads(message)['values']
    y = int(values[1])
    print(y)
    if y>=3:
        keyDown('d')   #add up key to keyDown (argument)
        keyUp('a')
    elif y<=-3:
        keyDown('a')   #add up key to keyDown (argument)
        keyUp('d')
    else:
        keyUp('a')
        keyUp('d')      

def on_error(ws, error):
    print("error occurred")
    print(error)

def on_close(ws, close_code, reason):
    print("connection close")
    print("close code : ", close_code)
    print("reason : ", reason  )

def on_open(ws):
    print("connected")
    

def connect(url):
    ws = websocket.WebSocketApp(url,on_open=on_open,on_message=on_message,on_error=on_error,on_close=on_close)
    ws.run_forever()
 
 
connect("ws://10.0.0.2:8080/sensor/connect?type=android.sensor.accelerometer") 

