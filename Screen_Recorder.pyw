import tkinter
import threading
import os
import datetime
import threading
import wave
import pyaudio
from plyer import notification
from win32api import GetSystemMetrics
import cv2
import numpy as np
from PIL import ImageGrab, Image,ImageTk
import os
import time
from moviepy.editor import *


 
class ScreenRecorder():
    def __init__(self):
        self.gui_done = False
        gui_thread = threading.Thread(target=self.gui_loop)
        self.recorder_running = False
        self.running = True
        gui_thread.start()

    
    def start_or_stop(self,op):
        if op == 1 and self.recorder_running==False :
            self.screen = threading.Thread(target=self.screen_recorder)
            self.voice = threading.Thread(target=self.voice_recorder)
            self.recorder_running = True
            self.screen.start()
            self.voice.start()
        elif op == 1 and self.recorder_running:
            print("Already running")
        elif op ==0 and self.recorder_running:
            self.recorder_running = False
                
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.title("Screen Recorder")
        self.win.geometry("700x500")
        self.win.configure(bg="black")
        
        self.image_label = tkinter.Label(self.win, bg="black")
        self.image_label.pack(side="right")
        
        self.start_rec = tkinter.Button(self.win,command=lambda: self.start_or_stop(1),text="Start Recording")
        self.start_rec.pack(side="left")
        self.stop_rec = tkinter.Button(self.win,command=lambda: self.start_or_stop(0),text="Stop Recording")
        self.stop_rec.pack(side="left") 
        
        self.gui_done=True
        self.win.mainloop()
        
    def screen_recorder(self):
        tame_stab = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        self.file_name = f'Screen Recording {tame_stab}' 
        # self.file_name = f'Screen Recording' 
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
       
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        capture_video = cv2.VideoWriter(self.file_name+".mp4", fourcc, 14.5, (width, height))

        while True:
            if self.recorder_running == False:
                break
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_final_bc = img_final
            capture_video.write(img_final)
            img_resized = cv2.resize(img_final_bc, (500,300))
            img_resized = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
            imgTk=ImageTk.PhotoImage(image=Image.fromarray(img_resized))
            self.image_label['image'] = imgTk
    

    def voice_recorder(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format= pyaudio.paInt16,channels = 1,rate = 44100,
                            input=True,frames_per_buffer = 1024)
        frames = []
        while True:
            data = stream.read(1024)
            frames.append(data)
            if not self.screen.is_alive():
                break
        stream.stop_stream()
        stream.close()
        audio.terminate()

        sound_file = wave.open(f"{self.file_name}.wav","wb")
        sound_file.setnchannels(1) 
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
        
        
        videoclip = VideoFileClip(f"{self.file_name}.mp4")
        audioclip = AudioFileClip(f"{self.file_name}.wav")
            
        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        videoclip.write_videofile("new_filename.mp4")
        
        os.remove(f"{self.file_name}.mp4")
        os.remove(f"{self.file_name}.wav")
        os.rename("new_filename.mp4", f"{self.file_name}.mp4")

        


screen_recorder = ScreenRecorder()

