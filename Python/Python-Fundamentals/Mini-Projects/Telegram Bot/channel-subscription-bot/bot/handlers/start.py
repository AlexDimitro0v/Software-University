from datetime import datetime, timezone

from aiogram import types

from ..utils.format import format_timestamp
from .. import dp, db, cfg

bot = dp.bot
CHANNEL_ID = cfg['channel_id']


@dp.message_handler(commands="start")
async def command_start(m: types.Message):
    await answer_keyboard(m)
    await answer_plans(m)


@dp.message_handler(regexp=r'^Plans$')
async def button_plans(m: types.Message):
    await answer_plans(m)


@dp.message_handler(regexp=r'^Status$')
async def button_status(m: types.Message):
    user_id = m.from_user.id
    expire_date = await db.get_membership_expire_date(user_id)
    utcnow = int(datetime.now(tz=timezone.utc).timestamp())
    if expire_date is None:
        text = "You don't have any active subscriptions at the moment."
    elif expire_date >= utcnow:
        text = "Your membership will be expired at: <code>{}</code>".format(
            await format_timestamp(expire_date)
        )
    elif expire_date < utcnow:
        text = "Your membership expired at: <code>{}</code>".format(
            await format_timestamp(expire_date)
        )
    await m.answer(text)


async def answer_keyboard(m):
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Plans', 'Status']
    reply_markup.row(*(types.KeyboardButton(text) for text in buttons))
    await m.answer(f"Hi {m.from_user.first_name}",
                   reply_markup=reply_markup)


async def answer_plans(m):
    text = """\
𝗜𝗻-𝗣𝗹𝗮𝘆 𝗭𝗼𝗻𝗲 𝗣𝗿𝗲𝗺𝗶𝘂𝗺

The aim of the premium group is to provide high-quality inplays and challenges 🚂.

Don't Hesitate, Join Today!"""
    reply_markup = types.InlineKeyboardMarkup(row_width=3)
    reply_markup.add(
        types.InlineKeyboardButton('Sunday Pass, $5.99',
                                   callback_data="purchase_1")
    )
    await m.answer(text, reply_markup=reply_markup)
