import asyncio
import logging

from aiogram import Bot, Dispatcher, types, filters

from app.settings import app_settings

bot = Bot(app_settings.telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(filters.Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")


@dp.message_handler(filters.Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Тут будет помощь")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
