from threading import Thread
from typing import Any

import requests
from bs4 import BeautifulSoup, ResultSet

from Modules.parsed_data import Album
from multiprocessing.pool import ThreadPool


class WebParse:
    def __init__(self):
        self.url: str = "https://ru.hitmotop.com/"
        self.data: list = []

    def parse_albums(self) -> list:
        request = requests.get(self.url + 'albums')
        soup = BeautifulSoup(request.content, 'html.parser')
        obs = soup.find_all('li', class_='album-item')
        pool = ThreadPool(processes=len(obs))
        for i in obs:
            pool.apply_async(self._in_data_classes, i)
        while len(self.data) != len(obs):
            print('sleep')
        print(self.data)

    def _in_data_classes(self, obj):
        self.data.append(Album(title=' '.join(obj.find('span', class_='album-title').text.replace('\n', '').split()),
                               img=obj.find('span', class_='album-image').get('style'),
                               url=self.url + obj.find('a').get('href')))
        return self.data

    def get_num_values(self, category: str) -> int:
        request = requests.get(self.url + category)
        soup = BeautifulSoup(request.content, 'html.parser')
        obs: ResultSet[Any] = soup.find_all('li', class_='album-item')
        return len(obs)

    def parse_genre(self) -> list:
        request = requests.get(self.url + 'genres')
        soup = BeautifulSoup(request.content, 'html.parser')
        obs = soup.find_all('li', class_='album-item')
        pool = ThreadPool(processes=len(obs))
        for i in obs:
            pool.apply_async(self._in_data_classes, (i,))
        while len(self.data) != len(obs):
            if len(self.data) == len(obs):
                pool.terminate()
                return self.data

    def parse_tracks(self) -> list:
        ...
