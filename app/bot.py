"""Bot for telegram MMORPG."""

import logging

from aiogram import Bot, Dispatcher, filters
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from app.buttons import DEV, HELP
from app.settings import app_settings

bot = Bot(app_settings.telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(filters.Command('start'))
async def cmd_start(message: Message) -> None:
    """
    Handle the '/start' command.

    Args:
        message (Message): The incoming message object.
    """
    button_help = KeyboardButton(text=HELP)
    button_dev = KeyboardButton(text=DEV)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help, button_dev)

    await message.answer('Добро пожаловать! Выберите функцию: ', reply_markup=keyboard)


@dp.message_handler(filters.Text(contains=HELP) | filters.Command('help'))
async def cmd_help(message: Message) -> None:
    """
    Handle the '/help' command.

    Args:
        message (Message): The incoming message object.
    """
    await message.answer(app_settings.manual)


@dp.message_handler(filters.Text(contains=DEV))
async def button_dev(message: Message) -> None:
    """
    Handle the message, which contain 'DEV'.

    Args:
        message (Message): The incoming message object.
    """
    await message.answer(DEV)


async def main() -> None:
    """Run the main event loop for the bot."""
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
