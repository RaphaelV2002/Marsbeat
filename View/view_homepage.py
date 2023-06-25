# -*- coding: utf-8 -*-

import random
import yaml
import os
os.environ['KIVY_AUDIO'] = 'ffpyplayer' 
from View import selected_genres
import kivy
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
import datetime
import time
start = time.time()


class HomeApp(MDApp):
    def __init__(self):
        super().__init__()
        with open("Configs/user_config.yaml", encoding="utf-8") as conf:
            yaml_conf = yaml.safe_load(conf)
        self.theme_cls.theme_style = yaml_conf['theme_style']
        self.theme_cls.primary_palette = yaml_conf['primary_palette']
        self.path_kv: str = "View/Templates/HomePage.kv"
        self.img_source: str = None
        self.screen: kivy.uix.screenmanager.ScreenManager = None
        self.path_db = yaml_conf['path_db']
        self.loads = False

    def action_content(self, instance_navigation_rail, instance_navigation_rail_item) -> None:
        match instance_navigation_rail_item.text:
            case "Online":
                if self.loads is False:
                    self.root.ids.content.clear_widgets()
                    #self.loads = selected_genres.Genres(self.root.ids.content).create_box_selected()
            case _:
                self.root.ids.content.clear_widgets()
                self.loads = False

    def build(self):
        self.pos_sound=0
        #self.img_source: str = 'https://ru.hitmotop.com/covers/a/95e/323/371376.jpg'
        self.music_dir ="Music/"
        self.music_files = os.listdir(self.music_dir)
        self.track_list = [x for x in self.music_files if x.endswith(('mp3'))]
        self.track_count = len(self.track_list)
        self.number_track = 0
        self.track_title = self.track_list[self.number_track]    
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir,self.track_title))
        self.screen = Builder.load_file(self.path_kv)
        return Builder.load_file(self.path_kv)
    def back(self,obj)-> None:
        self.sound.stop()
        #self.sound.unload()
        if self.number_track!=0:
            self.number_track=self.number_track-1
            self.track_title = self.track_list[self.number_track]
        print(self.number_track)
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir,self.track_title))
        self.change()
        self.sound.play()
    def skip(self,obj)-> None:
        self.sound.stop()
        #self.sound.unload()
        if self.number_track!=self.track_count-1:
            self.number_track=self.number_track+1
            self.track_title = self.track_list[self.number_track]
        print(self.number_track)
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir,self.track_title))
        self.change()
        self.sound.play()
    def change(self):
        self.root.ids.slider.max = self.sound.length
        self.root.ids.track_title.text = self.track_title.replace(".mp3","")
        self.root.ids.length_track.text = time.strftime("%M:%S", time.gmtime(self.sound.length))
            
    def play_pause(self,obj)-> None:
        if self.sound.state == "stop":
            self.root.ids.play_pause.icon = "pause"
            self.change()
            self.sound.play()
            time.sleep(0.0000000001)
            print("Play:" ,self.pos_sound)
            self.sound.seek(self.pos_sound)
        else:
            self.root.ids.play_pause.icon = "play"
            self.pos_sound = self.sound.get_pos()
            print("Pause:" ,self.pos_sound)
            self.sound.stop()


def run_view() -> None:
    HomeApp().run()
