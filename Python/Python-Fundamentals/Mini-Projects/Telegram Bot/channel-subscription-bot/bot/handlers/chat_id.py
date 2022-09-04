from aiogram import types

from .. import dp


@dp.message_handler(commands='id')
@dp.channel_post_handler(regexp=r'^\/id$')
async def command_id(m: types.Message):
    await m.answer(f"<b>Chat ID</b>: <code>{m.chat.id}</code>")
