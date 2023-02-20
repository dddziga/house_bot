import telebot;
bot = telebot.TeleBot('5621421229:AAFVOZhyaMASCKlM-TzLY42GyayaxGhPia8');

from nomera import BotDB
BotDB = BotDB('titova29.db')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Узнать номер телефона')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Узнать номер телефона':
        bot.send_message(message.chat.id, 'Введите номер авто в формате А000АА')
    elif message.text == 'Стоп':
        bot.send_message(message.chat.id, 'Нажмите кнопку ниже')
    elif message.text == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text == 'ясо субибу':
        bot.send_message(message.chat.id, str(BotDB.avto_exists('С091ТР')[0][0]))

bot.polling()