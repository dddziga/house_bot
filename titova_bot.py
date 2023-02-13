import telebot;
bot = telebot.TeleBot('5621421229:AAFVOZhyaMASCKlM-TzLY42GyayaxGhPia8');

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Hi gay')
    elif message.text == "/help":
     bot.send_message(message.from_user.id, "Напиши привет")
    else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)