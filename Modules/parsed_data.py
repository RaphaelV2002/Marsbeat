from dataclasses import dataclass


@dataclass
class Album:
    title: str = None
    img: str = None
    url: str = None

    def __post_init__(self):
        if self.img:
            self.img = "https:" + self.img.replace("background-image: url('", "").replace("')", "")


@dataclass
class Track:
    title: str = None
    author: str = None
    img: str = None
    url: str = None
