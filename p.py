#!/bin/python3

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'}

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
urlp = 'https://yandex.ru/maps/35/krasnodar/?l=trf%2Ctrfe&ll=38.975313%2C45.035470&z=13'
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(urlp)
#time.sleep(config,safe_delay)
#sleep(5)
html = driver.page_source
w = bs(html, 'html.parser')
print(w)

for red in w.find_all('div', class_='traffic-raw-icon _color_red'):
    now_1 = red.find('div', class_='traffic-raw-icon__text').text.strip()
    n1 = int(now_1)
    if n1 >= 6:
        now1 = 'Да ну нафиг!? Лучше на трамвай садись ' + str(n1) + ' баллов пробки'
        print(now1)
        file = open('probki', 'w')
        file.write(now1)
    else:
        print('Не красный уровень')

for yellow in w.find_all('div', class_='traffic-raw-icon _color_yellow'):
    now_2 = yellow.find('div', class_='traffic-raw-icon__text').text.strip()
    n2 = int(now_2)
    if 4 < n2 < 6:
        now2 = 'желтый уровень движения ' + str(n2) + ' баллов пробки. Так-то можно на траллике, но советую на трамвае ехать, если собираешься куда-то 😁'
        print(now2)
        file = open('probki', 'w')
        file.write(now2)
    elif n2 == 4:
        now2 = 'желтый уровень движения ' + str(n2) + ' балла пробок. Так-то можно на траллике, но советую на трамвае ехать, если собираешься куда-то'
        print(now2)
        file = open('probki', 'w')
        file.write(now2)
    else:
        print('Не желтый уровень')

for green in w.find_all('div', class_='traffic-raw-icon _color_green'):
    now_3 = green.find('div', class_='traffic-raw-icon__text').text.strip()
    n3 = int(now_3)
    if n3 == 1:
        now3 = 'можешь поехать на траллике или трамвае, ' + str(now_3) + ' балл пробок'
        print(now3)
        file = open('probki', 'w')
        file.write(now3)
    elif 1 < n3 < 4:
        now3 = 'можешь поехать на траллике или трамвае, ' + str(now_3) + ' балла пробок'
        print(now3)
        file = open('probki', 'w')
        file.write(now3)
    elif n3 >= 4:
        print('бл, я пошел по другому сценарию')
    elif n3 == 0:
        print('Пусто')
    else:
        now3 = 'можешь поехать на траллике или трамвае, ' + str(now_3) + ' баллов пробок'
        print(now3)
        file = open('probki', 'w')
        file.write(now3)
