import websocket
import json


def on_message(ws, message):
    values = json.loads(message)['values']
    y = int(values[1])
    if y>2:
        print("d")
    elif y<-2:
        print("a")

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

