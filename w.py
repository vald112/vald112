#!/bin/python3

import requests
from bs4 import BeautifulSoup as bs


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'}

urlp = 'https://yandex.ru/pogoda/maps/nowcast?utm_campaign=informer&utm_content=main_informer&utm_term=nowcast_link&utm_medium=web&utm_source=home&lat=45.03547&lon=38.975313&le_Lightning=1&ll=38.975313_45.035470&z=9'

p = requests.get(urlp)
w = bs(p.text, "lxml")
#print(w)
for weather in w.find_all('div', class_='weather-maps-fact__temp'):
    today = weather.find('span', class_='temp__value temp__value_with-unit').text.strip()
    today = str(today) + ' °C'
    print('Температура сейчас', today)

for opis in w.find_all('div', class_='weather-maps-fact'):
    opis = opis.find('div', class_='weather-maps-fact__nowcast-alert').text.strip()
    print(opis)

result = str(today) + ' ' + str(opis)

file = open('weather', 'w')
file.write(result)
file.close()

