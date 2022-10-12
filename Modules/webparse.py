import requests
from bs4 import BeautifulSoup

from Modules.parsed_data import Album


class WebParse:
    def __init__(self):
        self.url: str = "https://ru.hitmotop.com/"

    def parse_albums(self) -> list:
        request = requests.get(self.url + 'albums')
        data: list = []
        soup = BeautifulSoup(request.content, 'html.parser')
        j: int = 0
        for i in soup.find_all('li', class_='album-item'):
            j += 1
            data.append(Album(title=' '.join(i.find('span', class_='album-title').text.replace('\n', '').split()),
                              img=i.find('span', class_='album-image').get('style'),
                              url=self.url + i.find('a').get('href')))
            if j == 5:
                break
        return data

    def parse_genre(self) -> list:
        request = requests.get(self.url + 'genres')
        data: list = []
        soup = BeautifulSoup(request.content, 'html.parser')
        for i in soup.find_all('li', class_='album-item'):
            data.append(Album(title=i.find('span', class_='album-title').text,
                              img=i.find('span', class_='album-image').get('style'),
                              url="https://ru.hitmotop.com" + i.find('a', class_='album-link').get('href')
                              )
                        )
        return data

    def parse_tracks(self) -> list:
        ...
