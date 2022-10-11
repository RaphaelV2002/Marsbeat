from Modules import webparse

from kivy.lang import Builder


class Albums:

    def __init__(self, box_content):
        self.content_block = box_content
        self.len_rows: int = 1
        self.path_template: str = "View/Templates/"

    def create_box_albums(self):
        list_albums: list = webparse.WebParse().parse_albums()
        root = Builder.load_file(self.path_template + 'Scroll_Y.kv')
        for _list in list_albums:
            content = Builder.load_file(self.path_template + 'AlbumsBox.kv')
            content.ids.img.source = _list.img
            content.ids.title.text = _list.title
            root.ids.horizontal_grid.add_widget(content)
        self.content_block.add_widget(root)
