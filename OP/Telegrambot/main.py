import asyncio
from aiogram import Bot, Dispatcher

from config.config import TOKEN
from handlers.handlers import register_handlers


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    print("Bot is running...")
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
