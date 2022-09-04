import logging
from datetime import datetime, timezone

from aiogram import types
from aiogram.types.message import ContentTypes

from ..utils.format import format_name
from .. import dp, db, cfg

bot = dp.bot
PAYMENTS_PROVIDER_TOKEN = cfg['stripe_token']
CHANNEL_ID = cfg['channel_id']
LOG_CHAT_ID = cfg['log_chat_id']


@dp.callback_query_handler(text='purchase_1')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_id = query.from_user.id
    expire_date = await db.get_membership_expire_date(user_id)
    utcnow = int(datetime.now(tz=timezone.utc).timestamp())
    if expire_date is not None and utcnow < expire_date:
        await query.answer("Your membership is not expired yet")
        return
    if user_id != query.message.chat.id:
        return
    title = '𝟭-𝗗𝗮𝘆 𝗦𝘂𝗻𝗱𝗮𝘆 𝗣𝗮𝘀𝘀'
    description = """\
Your benefits:
✅𝗜𝗻-𝗣𝗹𝗮𝘆 𝗭𝗼𝗻𝗲 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 - 𝗜𝗻𝗽𝗹𝗮𝘆 𝗕𝗲𝘁𝘀 (with suggested stake)
✅𝗜𝗻-𝗣𝗹𝗮𝘆 𝗭𝗼𝗻𝗲 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 - 𝗖𝗵𝗮𝘁 (access to the channel)

Price: €𝟱.𝟵𝟵
Billing method: 𝟭 𝗱𝗮𝘆
Billing mode: 𝗼𝗻𝗲 𝘁𝗶𝗺𝗲"""
    prices = [types.LabeledPrice(label='𝟭-𝗗𝗮𝘆 𝗦𝘂𝗻𝗱𝗮𝘆 𝗣𝗮𝘀𝘀', amount=599)]
    await bot.send_invoice(user_id,
                           title=title,
                           description=description,
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='eur',
                           prices=prices,
                           start_parameter='one-day-sunday-pass',
                           payload='SUNDAY PASS')


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    error_message = "Something went wrong, try to pay again in a few minutes"
    await bot.answer_pre_checkout_query(pre_checkout_query.id,
                                        ok=True,
                                        error_message=error_message)


@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(m: types.Message):
    try:
        user = m.from_user
        total_amount = m.successful_payment.total_amount / 100
        currency = m.successful_payment.currency
        invite_link, expire_date = await update_membership(user)
        assert None not in (invite_link, expire_date)
        expire_date_readable = f"{expire_date} (UTC)"
        text = (
            f"Received payment: {total_amount} {currency}\n\n"
            f"Join the channel: <b>{invite_link}</b>\n\n"
            "Note that the link could only be used once "
            f"and it will expire at <code>{expire_date_readable}</code>"
        )
        if LOG_CHAT_ID is not None:
            log_text = (
                "<b>Invite Link</b>: <code>{}</code>\n"
                "<b>Expire Date</b>: <code>{}</code>\n"
                "<b>User Info</b>: {}\n"
                "<b>User Mention</b>: {}"
            ).format(
                invite_link,
                expire_date_readable,
                await format_name(user),
                user.mention
            )
            await bot.send_message(LOG_CHAT_ID, log_text)
    except AssertionError:
        text = (
            "Failed to update membership, "
            "contact admin: <b>@admin_username</b>"
        )
    except Exception as e:
        text = (
            f"<b>ERROR</b>: {e}\n\n"
            "Failed to update membership, "
            "contact admin: <b>@admin_username</b>"
        )
    await bot.send_message(m.chat.id, text)


async def update_membership(user):
    expire_date = (
        int(datetime.now(tz=timezone.utc).timestamp())
        + 60 * 60 * 24  # one day in seconds
    )
    name = (
        f"VIP: {user.id} @{user.username} {user.first_name} {user.last_name}"
    )[:32].strip()
    chat_invite_link = await bot.create_chat_invite_link(
        CHANNEL_ID,
        expire_date=expire_date,
        member_limit=1,
        name=name
    )
    invite_link = chat_invite_link.invite_link
    expire_date = chat_invite_link.expire_date
    await db.save_invite_link(invite_link, expire_date, user.id)
    logging.info("%s (%s): %s",
                 invite_link,
                 expire_date,
                 await format_name(user))
    await db.update_membership(user, 60 * 60 * 24)
    return (invite_link, expire_date)
