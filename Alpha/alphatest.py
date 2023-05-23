import asyncio
import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я - основной бот")

@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("Тут будет помощь")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())