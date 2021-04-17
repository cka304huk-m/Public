from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def main():
    url = get_url()
    driver = browser()
    real_user_agent(url, driver)
    driver.close()
    driver.quit()


def get_url():
    # Перехожу на сайт для получения user-agent.
    url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

    return url

def browser():
    # Создаю браузер.
    driver = webdriver.Chrome()

    return driver

def real_user_agent(url, driver):
    # Реальный user-agent.

    # Перехожу на сайт.
    driver.get(url=url)
    # Ищу на сайте user-agent.
    my_user_agent = driver.find_element_by_xpath(
        '//*[@id="detected_value"]/a')

    print('Мой user-agent:')
    print(my_user_agent.text)

if __name__ == '__main__':
    main()