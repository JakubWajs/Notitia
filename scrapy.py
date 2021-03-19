
import numpy as np
import requests as rq
from bs4 import BeautifulSoup as bs


class node:
    id = 0
    numbers = [0]

    def __init__(self):
        self.id = 0
        self.numbers = [0]

    def __init__(self, id, numbers):
        self.id = id
        self.numbers = numbers
        self.printer()

    def __get__(self, id, scrap):                                                   #will it be needed?
        return self.id

    def __get__(self, numbers, scrap):
        return self.numbers

    def printer(self):
        print('id: ', self.id, '\n', self.numbers)


class scrap(node):
    soup = ''
    id = [0]
    numbers = [0]
    nodes = node(id, numbers)


    def __init__(self):
        self.import_html()
        self.scraping()
        self.node_init()
        print(self.nodes)

    def import_html(self):
        url = 'https://www.lotto.pl/lotto/wyniki-i-wygrane'
        html = rq.get(url).text
        self.soup = bs(html, 'html.parser')

    def scraping(self):  
        id_number = self.soup.find_all(class_="result-item__number")
        numb = self.soup.find_all(class_="scoreline-item circle")

        for i in id_number:
            self.id.append(int(i.string))

        for i in numb:
            self.numbers.append(int(i.string))

        x = len(numb) / 6
        self.numbers = np.array_split(self.numbers, x)

    def node_init(self):

        for i in range(len(self.id)):
            self.nodes.append(node(self.id[i], self.numbers[i]))

