# bot.py
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN


TOKEN = BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# SQLite инициализация
conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    text TEXT
)
""")
conn.commit()

@dp.message_handler(commands=["start"])
async def start_cmd(message: Message):
    await message.reply("Привет! Напиши мне что-нибудь, я сохраню это в базу данных.")

@dp.message_handler()
async def save_message(message: Message):
    cursor.execute("INSERT INTO messages (user_id, text) VALUES (?, ?)", (message.from_user.id, message.text))
    conn.commit()
    await message.reply("Сообщение сохранено!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
