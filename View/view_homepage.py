from View import online_page

import kivy
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.textfield.textfield import MDTextField


class HomeApp(MDApp):
    def __init__(self):
        super().__init__()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.path_kv: str = "View\HomePage.kv"
        self.img_source: str = None
        self.screen: kivy.uix.screenmanager.ScreenManager = None

    def action_content(self, instance_navigation_rail, instance_navigation_rail_item) -> None:
        match instance_navigation_rail_item.text:
            case "Online":
                search = MDTextField(icon_left="magnify", mode="round", _icon_right_color="white")
                self.root.ids.content.clear_widgets()
                self.root.ids.content.add_widget(search)
                online_page.Albums(self.root.ids.content).create_box_albums()
            case _:
                self.root.ids.content.clear_widgets()

    def build(self):
        self.img_source: str = 'https://ru.hitmotop.com/covers/a/95e/323/371376.jpg'
        self.screen = Builder.load_file(self.path_kv)
        return Builder.load_file(self.path_kv)


def run_view() -> None:
    HomeApp().run()
