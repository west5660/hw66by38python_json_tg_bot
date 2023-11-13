from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def getpogoda():
    from selenium.webdriver.firefox.options import Options
    options = Options()  # Создаем экземпляр класса Options

    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    print('start proga')
    driver = webdriver.Edge()
    driver.maximize_window()
    print('open firefox')
    options.add_argument('-headless')
    driver.get('https://yandex.ru/pogoda/pskov')
    pog1 = driver.find_element(By.XPATH, '//*[@id="content_left"]/div[2]/div[1]/div[4]')
    pog2 = driver.find_element(By.XPATH, '//*[@id="content_left"]/div[2]/div[1]/div[6]')
    pogoda = (pog1.text + '\n' + pog2.text).split('\n')

    prognoz = 'Погода: ' + pogoda[0] + ' ' + pogoda[1] + '\nВетер: ' + pogoda[4]
    print(prognoz)
    driver.close()
    print('finish')
    return prognoz
