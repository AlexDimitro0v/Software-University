import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)


def markup_inline():
    markup = ReplyKeyboardMarkup()
    print(markup)
    markup.row_width = 2
    markup.row("Plans", "Status")
    return markup


@bot.callback_query_handler(func=lambda message: True)
def callback_query(message):
    bot.answer_callback_query(message.id, "Hello")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    new_line = '\n'
    welcome_message = f"Hey {message.from_user.first_name}!"
    information = "𝗜𝗻-𝗣𝗹𝗮𝘆 𝗭𝗼𝗻𝗲 𝗣𝗿𝗲𝗺𝗶𝘂𝗺" + new_line * 2 + "The aim of the premium group is to provide high-quality inplays and challenges 🚂." + new_line * 2 + "Don't Hesitate, Join Today!"
    bot.send_message(message.chat.id, welcome_message)
    bot.send_message(message.chat.id,
                     information, reply_markup=markup_inline())


# keep_alive.keep_alive()
bot.infinity_polling()
