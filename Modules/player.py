import datetime
import time
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
import os
os.environ['KIVY_AUDIO'] = 'ffpyplayer' 
import random
class Player(MDApp):
    def __init__(self):
        self.pos_sound=0
        self.music_dir ="Music/"
        self.music_files = os.listdir(self.music_dir)
        self.track_list = [x for x in self.music_files if x.endswith(('mp3'))]
        self.track_count = len(self.track_list)
        self.track_title = self.track_list[random.randrange(0,self.track_count)]
        print(5436)
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir,self.track_title)) 
    def play_pause(self)-> None:
        if self.sound.state == "stop":
            self.root.ids.play_pause.icon = "pause"
            self.root.ids.slider.max = self.sound.length
            self.root.ids.track_title.text = self.track_title.replace(".mp3","")
            self.root.ids.length_track.text = time.strftime("%M:%S", time.gmtime(self.sound.length))
            self.sound.play()
            time.sleep(0.0000000001)
            print("Play:" ,self.pos_sound)
            self.sound.seek(self.pos_sound)
        else:
            self.root.ids.play_pause.icon = "play"
            self.pos_sound = self.sound.get_pos()
            print("Pause:" ,self.pos_sound)
            self.sound.stop()