import logging
from importlib import import_module

from aiogram.utils.executor import Executor

from . import dp, db


async def on_startup(dispatcher):
    await db.start()


def run_bot():
    runner = Executor(dp, skip_updates=True)
    handlers = ('start', 'chat_id', 'owner', 'purchase')
    for handler in handlers:
        logging.info("loading handler: %s", handler)
        import_module(f".{handler}", 'bot.handlers')
    runner.on_startup(on_startup)
    runner.start_polling()
