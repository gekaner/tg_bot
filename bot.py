# bot.py
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN, TEXT


TOKEN = BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: Message):
    await message.answer(TEXT)

@dp.message_handler()
async def save_message(message: Message):
    await message.answer(TEXT)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
