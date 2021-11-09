import datetime
import threading
import wave
import pyaudio
from plyer import notification
from win32api import GetSystemMetrics
import cv2
import numpy as np
from PIL import ImageGrab
import os
tame_stab = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{tame_stab}'

def send_notification(message):
    notification.notify(       
            title = "Screen Recorder",
            message=f"{message}" ,
            timeout=2
    )




def screen_recorder():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    capture_video = cv2.VideoWriter(file_name+".mp4", fourcc, 20.0, (width, height))

    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('My Screen Recorder', img_final)
        capture_video.write(img_final)
        if cv2.waitKey(10) == ord('q'):
            break
def voice_recorder():
    audio = pyaudio.PyAudio()
    stream = audio.open(format= pyaudio.paInt16,
                       channels = 1,
                       rate = 44100,
                       input=True,
                       frames_per_buffer = 1024)
    frames = []
    while True:
        data = stream.read(1024)
        frames.append(data)
        if screen.is_alive():
            continue
        else:
            break

        
    send_notification("Your video is getting ready.\nYou will be notified when it is ready")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open(f"{file_name}.wav","wb")
    sound_file.setnchannels(1) 
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
      
if __name__ == "__main__":
    screen = threading.Thread(target=screen_recorder)
    screen.start()
    voice_r = threading.Thread(target=voice_recorder)
    voice_r.start()
    voice_r.join()
      
    from moviepy.editor import *
    videoclip = VideoFileClip(f"{file_name}.mp4")
    audioclip = AudioFileClip(f"{file_name}.wav")
    
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("new_filename.mp4")
    
    os.remove(f"{file_name}.mp4")
    os.remove(f"{file_name}.wav")
    os.rename("new_filename.mp4", f"{file_name}.mp4")
    


    send_notification("Your video is ready\n enjoy!!!!!!")
    print("done")



