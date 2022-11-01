from Modules import webparse, filemanager

from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.uix.scrollview import ScrollView


class Genres:
    def __init__(self, box_content):
        self.content_block = box_content

    def create_box_selected(self):
        # self.content_block.clear_widgets()
        list_genre: list = None
        while list_genre is None:
            list_genre = webparse.WebParse().parse_genre()
        genres = GridLayout(cols=4, spacing=15, size_hint=(.1, None))
        scroll = ScrollView(size_hint=(1, 1))
        print(list_genre)
        for _list in list_genre:
            if _list.url is not None:
                content = MDBoxLayout(orientation="vertical",
                                      adaptive_width=True,
                                      adaptive_height=True)
                if not _list.img:
                    content.add_widget(MDIcon(icon="image-off-outline", pos_hint={'center_x': .5, 'center_y': .5}))
                else:
                    content.add_widget(FitImage(source=_list.img))
                content.add_widget(MDLabel(text=_list.title, halign="center", theme_text_color="Primary"))
                genres.add_widget(content)
        scroll.add_widget(genres)
        self.content_block.add_widget(MDLabel(text='Selected please favorite genres', halign="center", theme_text_color="Primary"))
        self.content_block.add_widget(scroll)


class Selected_Path:
    def __init__(self, box_content):
        self.box = box_content

    def create_button(self):
        con = MDBoxLayout(size_hint_x=None, pos_hint={"center_x": 0.4})
        but = MDRoundFlatIconButton(text="Select path from database", icon="folder", pos_hint={"center_y": 0.5})
        but.bind(on_press=lambda a: filemanager.Selected_directory(self.box).file_manager_open())
        con.add_widget(but)
        self.box.add_widget(con)
