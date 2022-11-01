from multiprocessing.pool import Pool
from threading import Thread

from Modules import webparse

from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.spinner.spinner import MDSpinner


class Genres:

    def __init__(self, box_content):
        self.content_block = box_content
        self.path_template: str = "View/Templates/"
        self.content = MDBoxLayout(orientation="vertical",
                                   adaptive_width=True,
                                   adaptive_height=True)

    def loading(self):
        loading = MDSpinner(
            size_hint=(.5, .5),
            pos_hint={'x': .5, 'y': .5},
            active=True,
            palette=[
                [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
                [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
                [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
                [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
            ]
        )
        self.content.add_widget(loading)
        self.content_block.add_widget(self.content)

    def create_box_genre(self, data):
            print(data)
        # self.content.clear_widgets()
        # self.content_block.clear_widgets()
        # for _list in list_genre:
        #     if _list.url:
        #         if not _list.img:
        #             self.content.add_widget(MDIcon(icon="image-off-outline"))
        #         else:
        #             self.content.add_widget(FitImage(source=_list.img))
        #         self.content.add_widget(MDLabel(text=_list.title, halign="center", theme_text_color="Primary"))
        #         root.ids.horizontal_grid.add_widget(self.content)
        # self.content_block.add_widget(genre)
        # self.content_block.add_widget(root)
