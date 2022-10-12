from Modules import webparse

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.label import MDLabel, MDIcon


class Albums:

    def __init__(self, box_content):
        self.content_block = box_content
        self.len_rows: int = 1
        self.path_template: str = "View/Templates/"

    def create_box_genre(self):
        # the selection method needs to be changed
        # directly from the parser, the process takes a very long time
        list_genre: list = webparse.WebParse().parse_genre()
        root = Builder.load_file(self.path_template + 'Scroll_Y.kv')
        genre = Builder.load_file(self.path_template + 'Header.kv')
        for _list in list_genre:
            if _list.url:
                content = MDBoxLayout(orientation="vertical",
                                      adaptive_width=True,
                                      adaptive_height=True)
                if not _list.img:
                    content.add_widget(MDIcon(icon="image-off-outline"))
                else:
                    content.add_widget(FitImage(source=_list.img))
                content.add_widget(MDLabel(text=_list.title, halign="center", theme_text_color="Primary"))
                root.ids.horizontal_grid.add_widget(content)
        self.content_block.add_widget(genre)
        self.content_block.add_widget(root)
