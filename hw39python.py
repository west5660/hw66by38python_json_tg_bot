
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def film():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    print('start proga')
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    print('open firefox')

    driver.get('https://www.imdb.com/trailers/?ref_=hm_hp_sm')
    pog1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[1]/a').text
    pog2 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[1]/div[3]').text
    pog3 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[2]/a').text
    pog4 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[2]/div[3]').text
    pog5 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[3]/a').text
    pog6 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[3]/div[3]').text
    pog7 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[4]/a').text
    pog8 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[4]/div[3]').text

    pogoda = f"{pog1}\n{pog2}\n{pog3}\n{pog4}\n{pog5}\n{pog6}\n{pog7}\n{pog8}"
    print(pogoda)
    driver.close()
    print('finish')
    return pogoda

film()

