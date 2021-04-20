from selenium import webdriver
from time import sleep

def main():
    url = get_url()
    real, new = browser()
    real_user_agent(url, real)
    real.close()
    sleep(5)
    print()
    new_agent(url, new)
    new.close()
    new.quit()


def get_url():
    # Перехожу на сайт для получения user-agent.
    url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

    return url

def browser():
    # Создаю браузер.
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=whatever you want")
    driver_real_agent = webdriver.Chrome()
    driver_new_agent = webdriver.Chrome(options=options)

    return driver_real_agent, driver_new_agent

def real_user_agent(url, driver):
    # Реальный user-agent.

    # Перехожу на сайт.
    driver.get(url=url)
    # Ищу на сайте user-agent.
    my_user_agent = driver.find_element_by_xpath(
        '//*[@id="detected_value"]/a')

    print('Мой user-agent:')
    print(my_user_agent.text)


def new_agent(url, driver):
    # Реальный user-agent.

    # Перехожу на сайт.
    driver.get(url=url)
    # Ищу на сайте user-agent.
    my_user_agent = driver.find_element_by_xpath(
        '//*[@id="detected_value"]/a')

    print('Новый user-agent:')
    print(my_user_agent.text)

if __name__ == '__main__':
    main()