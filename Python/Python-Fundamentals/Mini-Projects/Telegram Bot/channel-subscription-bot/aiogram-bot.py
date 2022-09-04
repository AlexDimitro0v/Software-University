"""
aiogram-bot
"""
import logging

from aiogram import Bot, Dispatcher, executor, types

# Configuration
BOT_TOKEN = "5516198201:AAHuQXbA5FipOyD31SSz0tiH0U5RbVoE6uU"

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands="start")
    async def command_start(m: types.Message):
        await m.answer("Hi")

    executor.start_polling(dp, skip_updates=True)
