from threading import Thread
from typing import Any
import requests
from bs4 import BeautifulSoup, ResultSet
import os
from Modules.parsed_data import Album, Genre
from multiprocessing.pool import ThreadPool


class WebParse:
    def __init__(self):
        self.url: str = "https://ru2.hitmo.top/"
        self.data: list = []

    def parse_albums(self) -> list:
        request = requests.get(self.url + 'albums')
        soup = BeautifulSoup(request.content, 'html.parser')
        obs = soup.find_all('li', class_='cover_item')
        pool = ThreadPool(processes=len(obs))
        for i in obs:
            pool.apply_async(self._in_data_album, i)
        while len(self.data) != len(obs):
            print('sleep')
        print(self.data)

    def _in_data_album(self, obj):
        self.data.append(Album(title=' '.join(obj.find('span', class_='title cover_title').text.replace('\n', '').split()),
                               img=obj.find('img', class_='cover_img').get('style'),
                               url=self.url + obj.find('a').get('href')))
        return self.data
    
    def _in_data_genre(self, obj):
        self.data.append(Genre(title=' '.join(obj.find('a').text.replace('\n', '').split()),
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
        obs = soup.find_all('li', class_='widget_itemLink')
        pool = ThreadPool(processes=len(obs))
        for i in obs:
            pool.apply_async(self._in_data_genre, (i,))
        while len(self.data) != len(obs):
            if len(self.data) == len(obs):
                pool.terminate()
                return self.data

    def parse_track(self) -> list:
        self.music_dir ="Music/"
        self.music_files = os.listdir(self.music_dir)
        self.track_list = [x for x in self.music_files if x.endswith(('mp3'))]
        self.data=self.track_list
        return self.data
