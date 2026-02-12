from aiogram import types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💎 TON")],
            [KeyboardButton(text="₿ BTC")],
            [KeyboardButton(text="Ξ ETH")],
        ],
        resize_keyboard=True
    )
    await message.answer("Вибери криптовалюту:", reply_markup=keyboard)


def register_start(dp):
    dp.message.register(start_handler, Command("start"))
