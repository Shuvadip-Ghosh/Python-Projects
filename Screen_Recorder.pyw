import tkinter
from tkinter import ttk
from tkinter.constants import HORIZONTAL, X
import threading
import datetime
import threading
import wave
import pyaudio
from pyautogui import size as Screen_resolution
import cv2
import numpy as np
from PIL import ImageGrab, Image,ImageTk
import os
import time
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

class ScreenRecorder():
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        self.gui_done = False
        self.recorder_running = False
        self.running = True
        self.camera = False
        self.camera_position = "down-right"
        self.resolution = Screen_resolution()
        self.fps = 20
        gui_thread = threading.Thread(target=self.gui_loop)
        gui_thread.start()
        self.screen = threading.Thread(target=self.screen_recorder,daemon=True)
        self.screen.start()

    def start_or_stop(self,op):
       if op == 1 and self.recorder_running==False:
            self.voice = threading.Thread(target=self.voice_recorder)
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            self.file_name = os.path.join(os.environ["USERPROFILE"], "Videos", "Captures", f"Screen-Recording-{time_stamp}")
            self.capture_video = cv2.VideoWriter(self.file_name+".mp4", fourcc, self.fps, (self.resolution.width, self.resolution.height))
            self.recorder_running = True
            self.voice.start()
            self.message_label.configure(text="Video Recording is on.")
       elif op == 1 and self.recorder_running:
           self.message_label.configure(text="Video Recording is currently on.")
       elif op ==0 and self.recorder_running:
           self.recorder_running = False
           self.capture_video.release()
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
        self.wid = int(self.resolution.width * 0.55)
        self.hei = int(self.resolution.height * 0.55)

        self.win = tkinter.Tk()
        self.win.title("Screen Recorder")
        self.win.geometry(f"{self.wid}x{self.hei}")
        self.win.minsize(self.wid,self.hei)
        self.win.maxsize(self.wid,self.hei)
        self.win.configure(bg="#3B3938",padx=10,pady=10)

        self.image_frame = tkinter.Frame(self.win,bg="#3B3938")
        self.image_frame.pack(side="top",fill=X)

        self.button_frame = tkinter.Frame(self.win,bg="black",highlightbackground="#3B3938", highlightthickness=2)
        self.button_frame.pack(fill=X)

        self.button_frame_right = tkinter.Frame(self.button_frame,bg="black",highlightbackground="#3B3938", highlightthickness=2)
        self.button_frame_right.pack(side="right")

        self.button_frame_left = tkinter.Frame(self.button_frame,bg="black",highlightbackground="#3B3938", highlightthickness=2)
        self.button_frame_left.pack(side="left",anchor="nw")

        self.image_label = tkinter.Label(self.image_frame,bg="#3B3938")
        self.image_label.pack(side="top")

        self.start_rec = tkinter.Button(self.button_frame_right,bg="#3B3938",command=lambda: self.start_or_stop(1),text="Start Recording")
        self.start_rec.configure(height=2,fg="white")
        self.start_rec.pack(pady=4)
        self.stop_rec = tkinter.Button(self.button_frame_right,bg="#3B3938",command=lambda: self.start_or_stop(0),text="Stop Recording")
        self.stop_rec.configure(height=2,fg="white")
        self.stop_rec.pack(pady=4)

        self.rec_cam = tkinter.Button(self.button_frame_left,bg="#3B3938",command=lambda: self.start_or_stop(2),text="Record camera")
        self.rec_cam.configure(height=2,fg="white")
        self.rec_cam.pack(pady=4)

        self.save_vid_progress = ttk.Progressbar(self.win,orient=HORIZONTAL,length=760,mode="indeterminate")
        self.save_vid_progress.pack(side="left")

        self.message_label = tkinter.Label(self.win,fg="white",bg="black",width=40,text="No New Message")
        self.message_label.pack(side="right")

        self.gui_done=True
        self.win.mainloop()

    def screen_recorder(self):
        width,height = self.resolution.width,self.resolution.height

        while True:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            img_np = np.array(img)
            self.img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            if self.camera:
                _, frame = self.webcam.read()
                frame = cv2.resize(frame,(213,160)) # the ratio width:height :: 4:3
                fr_height, fr_width, _= frame.shape
                vi_height = height-fr_height
                vi_width = width-fr_width
                if "top-left" in self.camera_position:
                    self.img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height,0:fr_width,:]
                elif "top-right" in self.camera_position:
                    self.img_final[0:fr_height, vi_width:width, :] = frame[0:fr_height,0:fr_width,:]
                elif "down-left" in self.camera_position:
                    self.img_final[vi_height:height, 0:fr_width, :] = frame[0:fr_height,0:fr_width,:]
                elif "down-right" in self.camera_position:
                    self.img_final[vi_height:height, vi_width:width, :] = frame[0:fr_height, 0:fr_width, :]

            img_final_bc = self.img_final        
            img_resized = cv2.resize(img_final_bc, (650,387))
            img_resized = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
            imgTk=ImageTk.PhotoImage(image=Image.fromarray(img_resized))
            self.image_label['image'] = imgTk

            if self.recorder_running:
                self.capture_video.write(self.img_final)


    def voice_recorder(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format= pyaudio.paInt16,channels = 1,rate = 44100,
                            input=True,frames_per_buffer = 1024)
        frames = []
        while True:
            data = self.stream.read(1024)
            frames.append(data)
            if not self.recorder_running:
                break
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        sound_file = wave.open(f"{self.file_name}.wav","wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
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
            print("videoclip.duration: ",videoclip.duration)

            speed_factor = videoclip.duration / audioclip.duration  
            # videoclip = videoclip.fx(lambda clip: clip.set_duration(audioclip.duration))
            videoclip = videoclip.set_audio(audioclip)
            videoclip.write_videofile(f"{self.file_name}nf.mp4", codec="libx264", audio_codec="aac")
            videoclip.close()
            audioclip.close()

            # os.remove(f"{self.file_name}.mp4")
            # os.remove(f"{self.file_name}.wav")
            # os.rename(f"{self.file_name}nf.mp4", f"{self.file_name}.mp4")
            self.message_label.configure(text="Video saved")
        except Exception as e :
            self.message_label.configure(text="Error Saving Video")
            print(e)
        self.save_vid_progress.stop()


screen_recorder = ScreenRecorder()
