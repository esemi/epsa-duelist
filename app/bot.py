"""Bot for telegram MMORPG."""

import asyncio
import logging

from aiogram import Bot, Dispatcher, filters, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup as RKM
from app.settings import app_settings
from app.buttons import help, dev
bot = Bot(app_settings.telegram_token)
dp = Dispatcher(bot)

KB = KeyboardButton
KBM = RKM

@dp.message_handler(filters.Command('start'))
async def cmd_start(message: types.Message) -> None:
    button_help = KB(text=help)
    button_dev = KB(text=dev)
    keyboard = RKM(resize_keyboard=True).add(button_help, button_dev)

    await message.answer("Добро пожаловать! Выберите фунуцию: ", reply_markup=keyboard)

@dp.message_handler(filters.Command('help') | filters.Text(contains=help))
async def cmd_help(message: types.Message) -> None:
    await message.answer(app_settings.manual)

@dp.message_handler(filters.Text(contains=dev))
async def button_dev(message: types.Message) -> None:
    await message.answer(dev)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == 'main':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
