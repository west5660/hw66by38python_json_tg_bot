from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def anekdot():
    from selenium.webdriver.firefox.options import Options
    options = Options()  # Создаем экземпляр класса Options

    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    print('start proga')
    driver = webdriver.Edge()
    driver.maximize_window()
    print('open firefox')
    # options.add_argument('-headless')
    driver.get('https://newostrie.ru/anec-random?ysclid=lkpi3iyk8p787862972')
    pog1 = driver.find_element(By.XPATH, '//*[@id="desktop_device_type"]/section/main/article/div[6]/div[1]/div[2]/div/div')
    pog2 = driver.find_element(By.XPATH, '//*[@id="desktop_device_type"]/section/main/article/div[6]/div[1]/div[2]/div/div')
    pogoda = (pog1.text + '\n' + pog2.text).split('\n')

    prognoz = pogoda
    print(prognoz)
    driver.close()
    print('finish')
    return prognoz

