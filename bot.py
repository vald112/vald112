#!/bin/python3

import sqlite3
import telebot
from telebot import types
import time
from webdav3.client import Client

options = {
 'webdav_hostname': "http://10.9.0.2/nextcloud/remote.php/dav/files/user/",
 'webdav_login':    "USER",
 'webdav_password': "PASSWORD"
}

client = Client(options)
files1 = client.list('Музыка/Telegram')

bot = telebot.TeleBot("TOKEN")
conn = sqlite3.connect("/media/nextcloud/projects/tgbot/habrbot.db")
cursor = conn.cursor()

for num in cursor.execute(f'SELECT id FROM habrbot ORDER BY rowid DESC LIMIT 1'):
    num = int(num[0])
    #print(type(num))
    #print(num)

lastId = int()
@bot.message_handler(content_types = ['text'])
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=0.5)
    news  =  types.KeyboardButton('Новости') 
    weather  =  types.KeyboardButton('Погода в Краснодаре')

    if message.text == 'Погода' or message.text == 'погода' or message.text == 'Погода в Краснодаре':
        chat_id = message.chat.id
        file = open('/media/nextcloud/projects/tgbot/weather', 'r')
        w = file.read()
        e = 'Бро, сейчас ' + str(w) + '. Хорошего тебе дня, будь здоров'
        print(e)
        bot.send_message(chat_id, e)
        file.close()
    elif message.text == '/start':
        chat_id = message.chat.id
        #markup = types.ReplyKeyboardRemove(selective=False)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(news, weather)
        bot.send_message(chat_id, 'Дароу, Бро, скорее жмакай на интересующий тебя пункт )))', reply_markup=markup)
 
    elif message.text == 'Новости' or message.text == 'новости' or message.text == 'К последней новости':
        global num
        global lastId
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        last  =  types.KeyboardButton('Назад') 
        next  =  types.KeyboardButton('Вперед')
        stop = types.KeyboardButton('Хватит новостей')
        start = types.KeyboardButton('К последней новости')
        markup.row(last, next) 
        markup.row(start, stop)
        

        chat_id = message.chat.id
        bot.send_message(chat_id, "Новости на сегодня:", reply_markup=markup)
   
        conn = sqlite3.connect("/media/nextcloud/projects/tgbot/habrbot.db")
        cursor = conn.cursor()
        
        for values in cursor.execute('''SELECT NAME,LINK_STR FROM habrbot ORDER BY rowid DESC LIMIT 1'''):
            print(values)
            bot.send_message(chat_id, ': \n'.join(values))
        def lastID():
            global lastId
            global num
            for num in cursor.execute(f'SELECT id FROM habrbot ORDER BY rowid DESC LIMIT 1'):
                num = int(num[0])
                lastId = num
                print(type(num))
                print(num)
                print(type(lastId))
                print(lastId)
        lastID()

    elif message.text == 'Вперед' or message.text == '▶️':
        #global num
        num = num - 1
        print(num)
        conn = sqlite3.connect("/media/nextcloud/projects/tgbot/habrbot.db")
        cursor = conn.cursor()
        chat_id = message.chat.id
            
        #bot.send_message(chat_id, "Новости на сегодня:")
        for values in cursor.execute(f'SELECT NAME,LINK_STR FROM habrbot WHERE id={num}'):
             print(values)
             bot.send_message(chat_id, ': \n'.join(values))
       
    elif message.text == 'Назад':
        global lastId
        chat_id = message.chat.id
        if num > lastId:
            bot.send_message(chat_id, "Это последняя новость")
        elif num < lastId:
            num = num + 1
            print(num)
            conn = sqlite3.connect("/media/nextcloud/projects/tgbot/habrbot.db")
            cursor = conn.cursor()
            chat_id = message.chat.id
            
            for values in cursor.execute(f'SELECT NAME,LINK_STR FROM habrbot WHERE id={num}'):
                print(values)
                bot.send_message(chat_id, ': \n'.join(values))
        else:
            bot.send_message(chat_id, 'Это последняя новость')           
        
    elif message.text == 'Хватит новостей':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(news, weather)
        bot.send_message(chat_id, 'Ок, бро. А я пока отдохну )))', reply_markup=markup)

    elif message.text == 'Красава' or message.text == 'красава':
        bot.reply_to(message, "Я в курсе, бро )))")
    elif message.text == 'Красавчик' or message.text == 'красавчик':
        bot.reply_to(message, 'Ты мне льстишь...')
    else:
        bot.reply_to(message, "Сам понял, что сказал???")

@bot.message_handler(content_types=['audio'])
def handle_docs_photo(message):
    bot.reply_to(message, "Ок, я тебя понял. Сейчас направлю на твой сервер")
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = '/media/nextcloud/dt/' + message.audio.file_name;
        print(src)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
                    
        client.upload_sync(remote_path = 'Музыка/Telegram/' + message.audio.file_name, local_path= src)
        bot.reply_to(message, "Я загрузил, бро" )
    except Exception as e:
        bot.reply_to(message, e)

bot.polling(none_stop=True)
