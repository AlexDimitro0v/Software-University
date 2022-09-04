import logging
from io import BytesIO

from aiogram import types

from .. import dp, db, cfg

OWNER = cfg['owner']


async def owner_only(m: types.Message):
    chat = m.chat
    return OWNER in (chat.id, chat.username)


# @dp.message_handler(lambda m: OWNER in (m.chat.id, m.chat.username),
@dp.message_handler(owner_only, regexp=r'^(\/database|Backup Database)$')
async def command_database(m: types.Message):
    if m_reply := m.reply_to_message:
        logging.info("restore database")
        backup = BytesIO()
        await m_reply.document.download(destination_file=backup)
        backup.seek(0)
        await db.restore_sql(backup)
        await m_reply.reply("Restored database")
    else:
        logging.info("backup database")
        backup, info = await db.backup_sql()
        # https://t.me/aiogram/23526?thread=23522
        backup.seek(0)
        await m.reply_document(types.InputFile(backup), caption=info)
        backup.close()


@dp.message_handler(owner_only, commands='admin')
async def command_admin(m: types.Message):
    text = "<b>The following actions are owner only</b>"
    reply_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Backup Database', 'Clean Membership']
    reply_markup.row(*(types.KeyboardButton(text) for text in buttons))
    buttons = ['Statistics', 'Help']
    reply_markup.row(*(types.KeyboardButton(text) for text in buttons))
    await m.answer(text, reply_markup=reply_markup)


@dp.message_handler(owner_only, regexp=r'^Clean Membership$')
async def button_clean_membership(m: types.Message):
    success, total = await db.clean_membership(dp.bot)
    text = (
        f"Found {total} expired membership, "
        f"removed {success} users from the channel"
    )
    await m.answer(text)


@dp.message_handler(owner_only, regexp=r'^Statistics$')
async def button_statistics(m: types.Message):
    text = await db.get_statistics()
    await m.answer(text)


@dp.message_handler(owner_only, regexp=r'^(\/help|Help)$')
async def button_help(m: types.Message):
    text = """
<b>Owner Commands</b>

\u2022 /id -- get chat ID
\u2022 /admin -- show admin panel
\u2022 /database -- (non-reply) backup database
\u2022 /database -- (reply to a .sql file) restore database
"""
    await m.answer(text)
