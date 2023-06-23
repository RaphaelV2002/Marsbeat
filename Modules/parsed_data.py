from dataclasses import dataclass
import requests


@dataclass
class Album:
    title: str = None
    img: str = None
    url: str = None

    def __post_init__(self):
        # add an insert to the table
        # or delete this file altogether
        self.url = self.url.replace('https://ru.hitmotop.com//', 'https://ru.hitmotop.com/')
        if requests.get(self.url).status_code == 200:
            if self.img:
                self.img = "https:" + self.img.replace("background-image: url('", "").replace("')", "")
                try:
                    requests.get(self.img)
                except requests.exceptions.InvalidURL:
                    self.img = self.img.replace("https:/", "https://ru.hitmotop.com/")
                if requests.get(self.img).status_code == 404:
                    self.img = None
        else:
            self.url = None

@dataclass
class Genre:
    title: str = None
    url: str = None

    def __post_init__(self):
        # add an insert to the table
        # or delete this file altogether
        self.url = self.url.replace('https://ru.hitmotop.com//', 'https://ru.hitmotop.com/')

@dataclass
class Track:
    title: str = None
    author: str = None
    img: str = None
    url: str = None
