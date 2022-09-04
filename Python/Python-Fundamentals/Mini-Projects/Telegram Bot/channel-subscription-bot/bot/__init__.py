from pathlib import Path

from aiogram import Bot, Dispatcher

from .utils.db import Database
from config import cfg

BOT_TOKEN = cfg['bot_token']
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
db = Database(Path(__file__).parent.parent / "data.db")
