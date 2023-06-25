import threading

from Modules import webparse, filemanager

from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.fitimage.fitimage import FitImage

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.label import Label
from kivymd.uix.button import MDRoundFlatIconButton, MDFlatButton
from kivy.uix.scrollview import ScrollView


class Playlists:
    def __init__(self, box_content):
        self.content_block = box_content

    def create_box_selected(self,callback) -> bool:
        # self.content_block.clear_widgets()
        #cols: int = ((Window.size[0] - 80) // 64)
        cols: int = 1
        spacing: float = (((Window.size[0] - 80) % 64) / 100)
        list_track: list = None
        while list_track is None:
            list_track: list = webparse.WebParse().parse_track()
        scroll = ScrollView(size_hint=(1, 1), do_scroll_y=True, do_scroll_x=False)
        playlists = GridLayout(cols=cols, spacing=spacing, size_hint=(None, None), width=500)
        playlists.bind(minimum_height=playlists.setter('height'))
        
        for _list in list_track:
            if _list is not None:
                content = MDBoxLayout(orientation="vertical",
                                      adaptive_width=True,
                                      adaptive_height=True)
                playlists.add_widget(content)
                print(_list)
                select=lambda x: callback(_list)
                self.track=MDFlatButton(text=_list, theme_text_color="Primary", md_bg_color="blue", on_release=select)
                playlists.add_widget(self.track)
                
        scroll.add_widget(playlists)
        self.content_block.add_widget(scroll)

        return True



