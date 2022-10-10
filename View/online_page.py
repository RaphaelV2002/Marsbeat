from Modules import webparse

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation

class Albums:
    def __init__(self, box_content):
        self.content_block = box_content

    def create_box_albums(self):
        result = webparse.WebParse().parse()
        layout = BoxLayout(spacing=10, size_hint_x=None)
        for r in result:
            content = Builder.load_file('View\AlbumsBox.kv')
            content.ids.img.source = r.img
            content.ids.title.text = r.title
            layout.add_widget(content)
        self.content_block.add_widget(layout)
        # content = MDBoxLayout(orientation="horizontal", spacing=10)
        # j: int = 0
        # for r in result:
        #     j += 1
        #     box = MDBoxLayout(orientation="vertical", md_bg_color=(1, 0, 0, 1), adaptive_width=True, pos_hint={"top": 1})
        #     img = FitImage(source=r.img)
        #     label = MDLabel(text=r.title, halign='center')
        #     box.add_widget(img)
        #     box.add_widget(label)
        #     content.add_widget(box)
        #     if j == 3:
        #         self.content_block.add_widget(content)
        #         self.content_block.add_widget(MDBoxLayout(md_bg_color=(0, 1, 0, 1)))
        #         self.content_block.add_widget(MDBoxLayout(md_bg_color=(0, 0, 1, 1)))
        #         break
