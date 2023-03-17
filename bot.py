import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open ('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
         if  message.text == 'привет':
             bot.send_message(message.chat.id, 'Оу,здравствуй😁')
         elif message.text == 'рандомное число':
             bot.send_message(message.chat.id, str(random.randint(0,10000)))
         elif message.text == 'еще':
             bot.send_message(message.chat.id, str(random.randint(0,10000)))
         elif message.text == 'пока':
             bot.send_message(message.chat.id, 'до встречи👋')
         elif message.text == 'как дела?':
             bot.send_message(message.chat.id, 'Отлично,как сам?😉')
         elif message.text == 'включи таймер Pomodoro':
             bot.send_message(message.chat.id, 'прости, я не знаю как его включить,потому что я его не сделал 😭')
         else:
             bot.send_message(message.chat.id, 'Я не знаю что ответить 🤷‍♂️')


# RUN
bot.polling(none_stop=True)