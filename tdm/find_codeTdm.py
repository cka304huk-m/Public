from bs4 import BeautifulSoup
import requests

def find_tdmCode(search):
    url = f'https://tdme.ru/search?q={search}&analog=0&page=1'
    page_0 = requests.get(url)
    soup_0 = BeautifulSoup(page_0.text, "lxml")
    product = soup_0.find('a',
                            class_='c-card h-full flex flex-col transition duration-300 block bg-white border-gray-300 hover:shadow-2xl overflow-hidden')['href']
    product = f'https://tdme.ru{product}'

    page_1 = requests.get(product)
    soup_1 = BeautifulSoup(page_1.text, "lxml")
    productCode = soup_1.findAll('td', class_='lg:w-1/3 lg:w-auto py-4 lg:px-6 text-xs break-all lg:break-normal lg:text-sm text-gray-700')[10].text.strip()

    return productCode