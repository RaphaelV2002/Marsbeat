import requests
from bs4 import BeautifulSoup

from Modules.parsed_data import Album


class WebParse:
    def __init__(self):
        self.request = requests.get("https://ru.hitmotop.com/albums")

    def parse(self):
        data: list = []
        soup = BeautifulSoup(self.request.content, 'html.parser')
        for i in soup.find_all('li', class_='album-item'):
            data.append(Album(title=' '.join(i.find('span', class_='album-title').text.replace('\n', '').split()),
                              img=i.find('span', class_='album-image').get('style'),
                              url='https://ru.hitmotop.com' + i.find('a').get('href')))
        return data
