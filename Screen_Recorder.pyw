import tkinter
from tkinter import ttk
from tkinter.constants import HORIZONTAL, X
import threading
import datetime
import threading
import wave
import pyaudio
from win32api import GetSystemMetrics
import cv2
import numpy as np
from PIL import ImageGrab, Image,ImageTk
import os
import time
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import CompositeAudioClip

class ScreenRecorder():
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        self.gui_done = False
        gui_thread = threading.Thread(target=self.gui_loop)
        self.recorder_running = False
        self.running = True
        self.camera = False
        self.camera_position = "down-right"
        gui_thread.start()


    def start_or_stop(self,op):
       if op == 1 and self.recorder_running==False:
            self.screen = threading.Thread(target=self.screen_recorder)
            self.voice = threading.Thread(target=self.voice_recorder)
            self.recorder_running = True
            self.screen.start()
            self.voice.start()
            self.message_label.configure(text="Video Recording is on.")
       elif op == 1 and self.recorder_running:
           self.message_label.configure(text="Video Recording is on.")
       elif op ==0 and self.recorder_running:
           self.recorder_running = False
           self.message_label.configure(text="Video Recording off.....")
       elif op ==0 and not self.recorder_running:
           self.message_label.configure(text="Video Recording is already off.")
       elif op ==2 and not self.camera:
           self.camera = True
           self.rec_cam.configure(text="Camera recording on")
       elif op ==2 and self.camera:
           self.camera=False
           self.rec_cam.configure(text="Camera recording off")



    def gui_loop(self):
        self.wid = 1044
        self.hei = 540
        self.win = tkinter.Tk()
        self.win.title("Screen Recorder")
        self.win.geometry(f"{self.wid}x{self.hei}")
        self.win.minsize(self.wid,self.hei)
        self.win.maxsize(self.wid,self.hei)
        self.win.configure(bg="black")

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab")
        self.s.configure("TButton")

        self.tabs = ttk.Notebook(self.win)
        self.tabs.pack(fill="both",expand=True)

        self.tab1 = ttk.Frame(self.tabs,width=600,height=100)
        self.tab2 = ttk.Frame(self.tabs,width=600,height=100)

        self.tabs.add(self.tab1,text="Screen Recording")
        self.tabs.add(self.tab2,text="Settings")

        self.image_frame = tkinter.Frame(self.tab1,bg="#3B3938")
        self.image_frame.pack(side="top",fill=X)

        self.button_frame = tkinter.Frame(self.tab1,bg="black",highlightbackground="#3B3938", highlightthickness=2)
        self.button_frame.pack(fill=X)

        self.button_frame_right = tkinter.Frame(self.button_frame,bg="black",highlightbackground="#3B3938", highlightthickness=2)
        self.button_frame_right.pack(side="right")

        self.button_frame_left = tkinter.Frame(self.button_frame,bg="black",highlightbackground="#3B3938", highlightthickness=2)
        self.button_frame_left.pack(side="left",anchor="nw")

        self.image_label = tkinter.Label(self.image_frame,bg="#3B3938")
        self.image_label.pack(side="top")

        self.image_label_bc = tkinter.Label(self.image_frame,height=24,bg="black",width=93)
        self.image_label_bc.pack(side="top")

        self.start_rec = tkinter.Button(self.button_frame_right,bg="#3B3938",command=lambda: self.start_or_stop(1),text="Start Recording")
        self.start_rec.configure(height=2,fg="white")
        self.start_rec.pack(pady=4)
        self.stop_rec = tkinter.Button(self.button_frame_right,bg="#3B3938",command=lambda: self.start_or_stop(0),text="Stop Recording")
        self.stop_rec.configure(height=2,fg="white")
        self.stop_rec.pack(pady=4)

        self.rec_cam = tkinter.Button(self.button_frame_left,bg="#3B3938",command=lambda: self.start_or_stop(2),text="Record camera")
        self.rec_cam.configure(height=2,fg="white")
        self.rec_cam.pack(pady=4)
        # self.rec_aud = tkinter.Button(self.button_frame_left,bg="#3B3938",text=" Record Audio ")
        # self.rec_aud.configure(height=2,fg="white")
        # self.rec_aud.pack(pady=4)

        self.save_vid_progress = ttk.Progressbar(self.tab1,orient=HORIZONTAL,length=760,mode="indeterminate")
        self.save_vid_progress.pack(side="left")

        self.message_label = tkinter.Label(self.tab1,fg="white",bg="black",width=40,text="No New Message")
        self.message_label.pack(side="right")

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
        self.image_label_bc.destroy()
        self.image_label.configure(bg="black")
        while True:
            if self.recorder_running == False:
                break

            if self.camera:
                img = ImageGrab.grab(bbox=(0, 0, width, height))
                img_np = np.array(img)
                img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                _, frame = self.webcam.read()
                frame = cv2.resize(frame,(213,160)) # the ratio width:height :: 4:3
                fr_height, fr_width, _= frame.shape
                vi_height = height-fr_height
                vi_width = width-fr_width
                if "top-left" in self.camera_position:
                    img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height,0:fr_width,:]
                elif "top-right" in self.camera_position:
                    img_final[0:fr_height, vi_width:width, :] = frame[0:fr_height,0:fr_width,:]
                elif "down-left" in self.camera_position:
                    img_final[vi_height:height, 0:fr_width, :] = frame[0:fr_height,0:fr_width,:]
                elif "down-right" in self.camera_position:
                    img_final[vi_height:height, vi_width:width, :] = frame[0:fr_height, 0:fr_width, :]
            else:
                img = ImageGrab.grab(bbox=(0, 0, width, height))
                img_np = np.array(img)
                img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

            img_final_bc = img_final
            capture_video.write(img_final)
            img_resized = cv2.resize(img_final_bc, (650,387))
            img_resized = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
            imgTk=ImageTk.PhotoImage(image=Image.fromarray(img_resized))
            self.image_label['image'] = imgTk


        self.image_label.configure(image='',bg="#3B3938")
        self.image_label_bc = tkinter.Label(self.image_frame,height=24,bg="black",width=93)
        self.image_label_bc.pack(side="top")
        # print(f"{fr_width} {fr_height}")
        print("done Screen")

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
        print("voice")
        self.save_vid = threading.Thread(target=self.save)
        self.save_vid.start()

    def save(self):
        self.save_vid_progress.start(20)
        self.message_label.configure(text="Saving Video")
        try:
            videoclip = VideoFileClip(f"{self.file_name}.mp4")
            audioclip = AudioFileClip(f"{self.file_name}.wav")

            videoclip = videoclip.set_audio(audioclip)
            videoclip.write_videofile("new_filename.mp4")
            videoclip.close()
            audioclip.close()

            os.remove(f"{self.file_name}.mp4")
            os.remove(f"{self.file_name}.wav")
            os.rename("new_filename.mp4", f"{self.file_name}.mp4")
            self.message_label.configure(text="Video saved")
        except Exception as e :
            self.message_label.configure(text="Error Saving Video")
            print(e)
        self.save_vid_progress.stop()




screen_recorder = ScreenRecorder()
