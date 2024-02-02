import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
API_TOKEN = open('token.txt').readline()  # Замените на свой токен бота
# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик всех входящих текстовых сообщений
@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    await message.answer(message.text)

async def on_startup(dp):
    logging.info("Бот запущен и готов к работе!")

async def on_shutdown(dp):
    logging.info("Бот остановлен!")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)