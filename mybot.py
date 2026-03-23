import telebot
import os

# Token'ı Render'dan güvenli bir şekilde alacağız
API_TOKEN = os.getenv('BOT_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selam Ahmos! Render üzerinden canlı yayındayım. Hiç uyumam!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"aq(sendedin): {message.text}")

bot.infinity_polling()
