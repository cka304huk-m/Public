from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

class FindCode:
    """Поиск штрих кода на сайте производителя
    по артикулу из накладной."""

    def __init__(self, search):
        self.__search = search

    def reqBs4(self, url):
        """Переход по ссылке и получение с него данных"""
        ua = UserAgent()    # Антибот
        page = requests.get(url, ua.random)
        soup = BeautifulSoup(page.text, "lxml")

        return soup

    def find_tdm(self):
        url = f'https://tdme.ru/search?q={self.__search}&analog=0&page=1'
        product = self.reqBs4(url).find('a',
                              class_='c-card h-full flex flex-col transition duration-300 block bg-white border-gray-300 hover:shadow-2xl overflow-hidden')[
            'href']
        product = f'https://tdme.ru{product}'

        productCode = self.reqBs4(product).findAll('td',
                                     class_='lg:w-1/3 lg:w-auto py-4 lg:px-6 text-xs break-all lg:break-normal lg:text-sm text-gray-700')[
            10].text.strip()

        return productCode

    def find_fortisflex(self):
        url = f'https://fortisflex.ru/search/search_do/?search_string={self.__search}'

        product = self.reqBs4(url).find('div',
                              class_='col-lg-6 col-md-6 col-sm-12 search_list').find('a')['href']
        product = f'https://fortisflex.ru{product}'

        productCode = self.reqBs4(product).find('div', class_='col-lg-4 col-md-4 col-sm-12 logistic').findAll('li')[2].text[41:]

        return productCode

    def edit_month(self, month):
        if month == 'января':
            digMonth = '01'
        elif month == 'февраля':
            digMonth = '02'
        elif month == 'марта':
            digMonth = '03'
        elif month == 'апреля':
            digMonth = '04'
        elif month == 'мая':
            digMonth = '05'
        elif month == 'июня':
            digMonth = '06'
        elif month == 'июля':
            digMonth = '07'
        elif month == 'августа':
            digMonth = '08'
        elif month == 'сентября':
            digMonth = '09'
        elif month == 'октября':
            digMonth = '10'
        elif month == 'ноября':
            digMonth = '11'
        elif month == 'декабря':
            digMonth = '12'
        return digMonth

FC = FindCode('test')