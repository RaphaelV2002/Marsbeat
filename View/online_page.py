from Modules import webparse

from kivy.lang import Builder


class Albums:

    def __init__(self, box_content):
        self.content_block = box_content
        self.len_rows: int = 1

    def create_box_albums(self):
        result = webparse.WebParse().parse()
        root = Builder.load_file('View\Scroll_Y.kv')
        for r in result:
            content = Builder.load_file('View\AlbumsBox.kv')
            content.ids.img.source = r.img
            content.ids.title.text = r.title
            root.ids.horizontal_grid.add_widget(content)
        self.content_block.add_widget(root)
