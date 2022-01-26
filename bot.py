#!/bin/python3

import sqlite3
import telebot
from telebot import types
import time

from webdav3.client import Client

options = {
 'webdav_hostname': "http://10.7.0.1/nextcloud/remote.php/dav/files/user/",
 'webdav_login':    "USER",
 'webdav_password': "PASSWORD"
}

client = Client(options)
files1 = client.list('music/Telegram')

bot = telebot.TeleBot("123546:qwertyuiop1234567890....")

file = open('weather', 'r')
w = file.read()
file1 = open('i', 'r')
p = file1.read()
e = 'Доброго утра! Бро, проснись и пой! \n \nСейчас на Краснодаре ' + str(w) + '. ' + 'И ' + str(p) + '.\nПродуктивного дня!'
#Вместо 12345678 нужно вписать свой id в telegram
bot.send_message(12345678, e)
file.close()
file1.close()

@bot.message_handler(commands=['p'])
def send_message(message):
    chat_id = message.chat.id
    file = open('probki', 'r')
    i = file.read()
    e = 'Короче, сейчас ' + str(i)
    print(e)
    bot.send_message(chat_id, e)
    file.close()

@bot.message_handler(commands=['w'])
def send_message(message):
    chat_id = message.chat.id
    file = open('weather', 'r')
    w = file.read()
    e = 'Бро, сейчас ' + str(w) + '. Хорошего тебе дня, будь здоров'
    print(e)
    bot.send_message(chat_id, e)
    file.close()

@bot.message_handler(commands=['news'])
def send_message(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    bot.send_message(chat_id, "Новости с Хабр:")
   
    conn = sqlite3.connect("habrbot.db")
    cursor = conn.cursor()

    for values in cursor.execute('''SELECT NAME,LINK_STR FROM habrbot ORDER BY rowid DESC LIMIT 15'''):
       bot.send_message(chat_id, ': \n'.join(values))

@bot.message_handler(content_types=['audio'])
def handle_docs_photo(message):
    bot.reply_to(message, "Ок, я тебя понял. Сейчас направлю на твой сервер")
    try:
        #Введите свой чат id, можно посмотреть в специальных ботах
        chat_id = 1234567

        #Качаем музыку на машину на которой крутиться бот
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = '/media/dt/' + message.audio.file_name;
        print(src)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
                    

        client.upload_sync(remote_path = 'music/Telegram/' + message.audio.file_name, local_path= src)
        bot.reply_to(message, "Я загрузил, бро" )
    except Exception as e:
        bot.reply_to(message, e)

bot.polling()
