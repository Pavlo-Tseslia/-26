import telebot
from config.config import TELEGRAM_BOT_TOKEN
from handlers.start import register_handlers

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("❌ Помилка: TELEGRAM_BOT_TOKEN не знайдено у .env")
        return

    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

    register_handlers(bot)

    print("✅ Бот запущений. Очікую повідомлень...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
