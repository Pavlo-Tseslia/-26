import os
from dotenv import load_dotenv
import telebot

load_dotenv(r"C:\Users\pasha\PyCharmMiscProject\OP\.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не знайдено у файлі .env")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

def main():
    print("Бот запущений.")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
