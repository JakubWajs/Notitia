
import numpy as np
import requests as rq
from bs4 import BeautifulSoup as bs

class scrap:
    id = []
    numbers = []
    soup = ''

    def __init__(self):
        self.html_import()
        self.scraping()
        print(self.numbers)

    def html_import(self):
        html_doc = rq.get('https://www.lotto.pl/lotto/wyniki-i-wygrane')
        self.soup = bs(html_doc, 'html.parser')


    def scraping(self):
        numb = self.soup.find_all(class_="scoreline-item circle")
        x = len(numb)/6

        for i in numb:
            self.numbers.append(int(i))
            
        self.numbers = np.array_split(self.numbers, x)

        #<div data-v-4593a923="" class="d-md-none special-mobile-box"> 
        #  <p data-v-4593a923="" class="resu1lt-item__name">Lotto</p> 
        #     <div data-v-4593a923="" class="result-item__number-box"><p data-v-4593a923="" class="white-number-box__sign white-number-box__sign--mobile">Nr losowania:</p> 
        #        <p data-v-4593a923="" class="result-item__number"> 6544 </p></div></div> <p data-v-4593a923="" class="result-item__name d-none d-md-block">Lotto</p> <div data-v-4593a923="" class="result-item__number-box d-none d-md-flex"><p data-v-4593a923="" class="white-number-box__sign white-number-box__sign--mobile d-md-none">Nr losowania:</p> <p data-v-4593a923="" class="result-item__number">6544</p></div> <div data-v-4593a923="" class="result-item__balls-box"><div data-v-4593a923="" class="scoreline-item circle">
        #                                        3
        #                                    </div><div data-v-4593a923="" class="scoreline-item circle">
        #                                        4
        #                                    </div><div data-v-4593a923="" class="scoreline-item circle">
        #                                        24
        #                                    </div><div data-v-4593a923="" class="scoreline-item circle">
        #                                        27
        #                                    </div><div data-v-4593a923="" class="scoreline-item circle">
        #                                        28
        #                                    </div><div data-v-4593a923="" class="scoreline-item circle">
        #                                        48
        #                                    </div> </div> <!----> <!---->