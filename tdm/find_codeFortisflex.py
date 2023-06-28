from bs4 import BeautifulSoup
import requests

def find_fortisflexCode(search):
    url = f'https://fortisflex.ru/search/search_do/?search_string={search}'
    page_0 = requests.get(url)
    soup_0 = BeautifulSoup(page_0.text, "lxml")

    product = soup_0.find('div',
                            class_='col-lg-6 col-md-6 col-sm-12 search_list').find('a')['href']
    product = f'https://fortisflex.ru{product}'

    page_1 = requests.get(product)
    soup_1 = BeautifulSoup(page_1.text, "lxml")
    productCode = soup_1.find('div', class_='col-lg-4 col-md-4 col-sm-12 logistic').findAll('li')[2].text[41:]

    return productCode
