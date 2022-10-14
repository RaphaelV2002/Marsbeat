import os
import multiprocessing as mp

from View import online_page, selected_genres
from Modules import databases_service

import kivy
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.textfield.textfield import MDTextField
from kivymd.uix.spinner.spinner import MDSpinner


class HomeApp(MDApp):
    def __init__(self):
        super().__init__()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.path_kv: str = "View/Templates/HomePage.kv"
        self.img_source: str = None
        self.screen: kivy.uix.screenmanager.ScreenManager = None

    def action_content(self, instance_navigation_rail, instance_navigation_rail_item) -> None:
        # modify the interface so that it does not hang when selecting content
        mp.set_start_method('spawn')
        q = mp.Queue()
        p = mp.Process(target=selected_genres.Genres(self.root.ids.content).create_box_selected())
        if os.path.isfile("user_config.db") is False:
            databases_service.Config().create_tables()
        match instance_navigation_rail_item.text:
            case "Online":
                self.root.ids.content.clear_widgets()
                load = MDSpinner(
                    size_hint=(.5, .5),
                    pos_hint={'center_x': .5, 'center_y': .5},
                    active=True,
                    palette=[
                        [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
                        [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
                        [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
                        [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
                    ]
                )
                self.root.ids.content.add_widget(load)
                print(q.get())
                p.start()
                # self.content = self.root.ids.content
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
