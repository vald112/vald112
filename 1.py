#!/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import sqlite3

db = sqlite3.connect("habrbot.db")
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS habrbot (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    LINK_STR TEXT,
    OPIS TEXT
)""")
db.commit()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://habr.com/ru/all'
url1 = 'https://habr.com'
i = 1

r = requests.get(url, headers = headers)
soup = bs(r.text, "lxml")

name_list = []
link_list = []

for name  in soup.find_all('div', class_='tm-article-snippet'):
    name_str = name.find('a', class_='tm-article-snippet__title-link').text.strip()
    name_list.append(name_str)
    name_list.reverse()
#    print(name_list)

for link  in soup.find_all('div', class_='tm-article-snippet'):
    link_str = link.find('a', class_='tm-article-snippet__title-link').get('href')
    nt = ''.join([url1,link_str])
    link_list.append(nt)
    link_list.reverse()
#    print(link_list)

while i < len(link_list):
    name1 = name_list[i]
    link2 = link_list[i]

    cur.execute("""INSERT INTO habrbot (NAME, LINK_STR) VALUES (?, ?);""", (name1, link2))
    db.commit()
    print("Добавлено " + str(i))
    i = i + 1

