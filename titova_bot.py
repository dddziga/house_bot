import telebot;
bot = telebot.TeleBot('5621421229:AAFVOZhyaMASCKlM-TzLY42GyayaxGhPia8');

import re

from nomera import BotDB
BotDB = BotDB('titova29.db')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Узнать номер телефона')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, нажми кнопку "Узнать номер телефона"', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Узнать номер телефона':
        bot.send_message(message.chat.id, 'Введите номер авто в формате А000АА, А000АА00 или А000АА000')
    elif message.text == 'Стоп':
        bot.send_message(message.chat.id, 'Нажмите кнопку ниже')
    elif message.text == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif re.match(r'[А-Я]\d{3}[А-Я]{2}\d.+', message.text):
        try: 
            bot.send_message(message.chat.id, 'Номер телефона: '+str(BotDB.avto_exists(message.text)[0][0]))
        except Exception as e:
            bot.send_message(message.chat.id, 'Номер не найден, чтобы добавить номер авто - напишите @dddziga')
    elif re.match(r'[А-Я]\d{3}[А-Я]{2}', message.text):
        try: 
            bot.send_message(message.chat.id, 'Номер телефона: '+str(BotDB.avto_exists(message.text)[0][0]))
        except Exception as e:
            bot.send_message(message.chat.id, 'Номер не найден, чтобы добавить номер авто - напишите @dddziga')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй еще раз')

bot.polling()