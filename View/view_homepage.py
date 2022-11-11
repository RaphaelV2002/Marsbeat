# -*- coding: utf-8 -*-

import yaml

from View import selected_genres

import kivy
from kivy.lang import Builder

from kivymd.app import MDApp

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
                    self.loads = selected_genres.Genres(self.root.ids.content).create_box_selected()
            case _:
                self.root.ids.content.clear_widgets()
                self.loads = False

    def build(self):
        self.img_source: str = 'https://ru.hitmotop.com/covers/a/95e/323/371376.jpg'
        self.screen = Builder.load_file(self.path_kv)
        return Builder.load_file(self.path_kv)


def run_view() -> None:
    HomeApp().run()
