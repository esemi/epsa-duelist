"""Bot for telegram MMORPG."""

import asyncio
import logging

from aiogram import Bot, Dispatcher, filters, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.buttons import DEV, HELP
from app.settings import app_settings

bot = Bot(app_settings.telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(filters.Command('start'))
async def cmd_start(message: types.Message) -> None:
    button_help = KeyboardButton(text=HELP)
    button_dev = KeyboardButton(text=DEV)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help, button_dev)

    await message.answer("Добро пожаловать! Выберите фунуцию: ", reply_markup=keyboard)

@dp.message_handler(filters.Command('help'),filters.Text(contains=HELP))
async def cmd_help(message: types.Message) -> None:
    await message.answer(app_settings.manual)

@dp.message_handler(filters.Text(contains=DEV))
async def button_dev(message: types.Message) -> None:
    await message.answer(DEV)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
