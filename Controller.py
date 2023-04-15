import serial
import pydirectinput 
import serial.tools.list_ports
import websocket
import json
import threading

class Controller:
    def __init__(self) -> None:
        s = list(serial.tools.list_ports.comports())
        inpstring = ""
        for index , e in enumerate(s):
            inpstring = inpstring + str(index) + " "+ str(e.description) + "\n"
        inp = int(input(inpstring+">>> "))
        self.arduino = serial.Serial(s[inp].name,115200,timeout=.1)
        pydirectinput.PAUSE = 0
        self.keysDown = {} 

        appconn = threading.Thread(target=self.connect)
        appconn.start()

        while True:
            rawdata = self.arduino.readline()
            try:
                data = str(rawdata.decode('utf-8'))
                data = data.replace('\n',"")
                data = data.replace('\r',"")
                if data == 's' or data == 'w':
                    print(data)
                    self.handlekeys(data)
            except UnicodeDecodeError as e:
                print(rawdata)


    def on_message(self, message):
        values = json.loads(message)['values']
        y = int(values[1])
        if y>2:
            self.keyDown('d')   #add up key to keyDown (argument)
            self.keyUp('a')
        elif y<-2:
            self.keyDown('a')   #add up key to keyDown (argument)
            self.keyUp('d')

    def on_error(self, error):
        print("error occurred")
        print(error)

    def on_close(self, close_code, reason):
        print("connection close")
        print("close code : ", close_code)
        print("reason : ", reason  )

    def on_open(self):
        print("connected")
        
    def connect(self):
        url = "ws://10.0.0.2:8080/sensor/connect?type=android.sensor.accelerometer"
        ws = websocket.WebSocketApp(url,on_open=self.on_open,on_message=self.on_message,on_error=self.on_error,on_close=self.on_close)
        ws.run_forever()
        
    
    def keyDown(self,key):               #what to do if key pressed. takes value from handleJoyStickAsArrowKeys
        self.keysDown[key] = True        #adds key to KeysDown list
        pydirectinput.keyDown(key)  #runs pydirectinput using key from (argument)     #remove '#' from print to test data stream

    def keyUp(self,key):                     #what to do if key released. takes value from handleJoyStickAsArrowKeys
        if key in self.keysDown:
            del (self.keysDown[key])         #remove key from KeysDown
            pydirectinput.keyUp(key)    #runs pydirectinput using key from (argument)
            #print('Up: ', key)         #remove '#' from print to test data stream

    def handlekeys(self,x):      #note that the x and y directions are swapped due to the way I orient my thumbstick
        if x == 'w':          #0 is up on joystick
            self.keyDown('up')   #add up key to keyDown (argument)
            self.keyUp('down')   #add down key to keyUp (argument), as you can't press up and down together
        elif x == 's':        #2 is down on joystick
            self.keyDown('down')
            self.keyUp('up')
        else:               #1 is neutral on joystick
            self.keyUp('up')
            self.keyUp('down') 
  