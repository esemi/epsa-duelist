import asyncio
import logging

from aiogram import Bot, Dispatcher, filters, types
from settings import app_settings
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(app_settings.telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):

    button_help = KeyboardButton(text="❓ Помощь", callback_data='help')
    button_dev = KeyboardButton(text="⚙️ В разработкеe", callback_data='dev')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help, button_dev)

    await message.answer("Добро пожаловать! Выберите фунуцию: ", reply_markup=keyboard)

@dp.message_handler(filters.Command('help'))
async def cmd_help(message: types.Message) -> None:
    await message.answer('https://teletype.in/@w.a.i/alpha_bot_manual')

@dp.message_handler(filters.Text(contains='❓ Помощь'))
async def button_help(message: types.Message) -> None:
    await message.answer('https://teletype.in/@w.a.i/alpha_bot_manual')

@dp.message_handler(filters.Text(contains='⚙️ В разработке'))
async def button_help(message: types.Message) -> None:
    await message.answer('⚙️')

@dp.callback_query_handler(lambda c: c.data == "help" or c.data == "dev")
async def send_callback(callback: types.CallbackQuery):
    await callback.message.answer("Вы нажали кнопку!")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())