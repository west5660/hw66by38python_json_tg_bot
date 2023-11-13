from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def novosti():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    print('start proga')
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    print('open firefox')

    driver.get('https://dzen.ru/news?issue_tld=ru')
    pog1 = driver.find_element(By.XPATH, '//*[@id="neo-page"]/div/div/div/div[2]/div[2]/div[2]/div/section[1]/div/div[1]/div/div/div[2]/h2/a').text
    pog2 = driver.find_element(By.XPATH, '//*[@id="neo-page"]/div/div/div/div[2]/div[2]/div[2]/div/section[1]/div/div[2]/div/div/div[1]/div/h2').text


    pogoda = f"{pog1}\n{pog2}\n"
    print(pogoda)
    driver.close()
    print('finish')
    return pogoda

novosti()

