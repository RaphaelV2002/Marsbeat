# -*- coding: utf-8 -*-

import yaml

from View import selected_genres

import kivy
from kivy.lang import Builder

from kivymd.app import MDApp


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

    def action_content(self, instance_navigation_rail, instance_navigation_rail_item) -> None:
        # modify the interface so that it does not hang when selecting content
        match instance_navigation_rail_item.text:
            case "Online":
                self.root.ids.content.clear_widgets()
                if self.path_db:
                    selected_genres.Selected_Path(self.root.ids.content).create_button()
                # if databases_service.Config().cur.execute("SELECT COUNT(*) FROM  GENRES").fetchone()[0] == 0:
                #     selected_genres.Genres(self.root.ids.content).create_box_selected()
                # else:
                #     search = MDTextField(icon_left="magnify", mode="round", _icon_right_color="white")
                #     self.root.ids.content.clear_widgets()
                #     self.root.ids.content.add_widget(search)
                #     online_page.Albums(self.root.ids.content).create_box_genre()
            case _:
                self.root.ids.content.clear_widgets()

    def build(self):
        self.img_source: str = 'https://ru.hitmotop.com/covers/a/95e/323/371376.jpg'
        self.screen = Builder.load_file(self.path_kv)
        return Builder.load_file(self.path_kv)


def run_view() -> None:
    HomeApp().run()
