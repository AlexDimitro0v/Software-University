import logging
import sqlite3
from io import BytesIO
from datetime import datetime, timezone
from typing import Tuple, Optional
from pathlib import Path

from config import cfg

CHANNEL_ID = cfg['channel_id']
LOG_CHAT_ID = cfg['log_chat_id']


class Database(object):
    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        self.users = tuple()

    async def create_table(self):
        logging.info("creating table")
        with open(Path(__file__).parent / "db.sql", 'r') as f:
            sql_script = f.read()
        self.cur.executescript(sql_script)
        self.con.commit()

    async def start(self):
        await self.create_table()
        await self.cache_users()

    async def backup_sql(self) -> Tuple[BytesIO, str]:
        backup = BytesIO()
        for line in self.con.iterdump():
            backup.write(('%s\n' % line).encode())
        utcnow = datetime.now(timezone.utc)
        backup.name = f"sqlite3-backup_{int(utcnow.timestamp())}.sql"
        info = (
            "\u2022 <b>Date</b>: <code>{date}</code>\n"
            "\u2022 <b>Statistics</b>: {num_users} users"
        ).format(
            date=utcnow.strftime('%F %T'),
            num_users=len(self.users)
        )
        return backup, info

    async def restore_sql(self, backup: BytesIO):
        query = "DROP TABLE IF EXISTS membership"
        self.cur.execute(query)
        query = backup.getvalue().decode('UTF-8')
        backup.close()
        self.cur.executescript(query)
        self.con.commit()

    async def cache_users(self):
        query = (
            "SELECT DISTINCT user_id FROM membership "
            f"WHERE channel_id={CHANNEL_ID} AND expire_date > strftime('%s')"
        )
        self.cur.execute(query)
        self.users = tuple(x[0] for x in self.cur.fetchall())
        logging.info("loaded %s users", len(self.users))

    async def save_invite_link(self,
                               invite_link: str,
                               expire_date: int,
                               user_id: int) -> bool:
        query = """INSERT INTO
invite_links (invite_link, expire_date, user_id, channel_id)
VALUES (?, ?, ?, ?)"""
        data = (invite_link, expire_date, user_id, CHANNEL_ID)
        self.cur.execute(query, data)
        self.con.commit()
        return bool(self.cur.fetchone())

    async def update_membership(self, user, duration: int):
        user_id = user.id
        user_name = "{} {} {}".format(
            f"@{user.username}" if user.username else '',
            user.first_name,
            user.last_name or ''
        ).strip()
        utcnow = int(datetime.now(tz=timezone.utc).timestamp())
        current_expire_date = await self.get_membership_expire_date(user_id)
        expire_date = max(utcnow, current_expire_date or 0) + duration
        query = """\
INSERT INTO membership (user_id, user_name, channel_id, expire_date)
VALUES (?, ?, ?, ?)
ON CONFLICT(user_id, channel_id) DO UPDATE SET expire_date=?"""
        data = (user_id, user_name, CHANNEL_ID, expire_date, expire_date)
        self.cur.execute(query, data)
        self.con.commit()
        return bool(self.cur.fetchone())

    async def get_membership_expire_date(self, user_id: int) -> Optional[int]:
        query = "SELECT expire_date FROM membership WHERE user_id=?"
        data = (user_id,)
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        return result[0] if result is not None else None

    async def delete_membership(self, user_id: int) -> bool:
        query = (
            "DELETE FROM membership "
            f"WHERE user_id=? AND channel_id={CHANNEL_ID}"
        )
        data = (user_id,)
        self.cur.execute(query, data)
        self.con.commit()
        return bool(self.cur.rowcount)

    async def clean_membership(self, bot) -> tuple:
        query = (
            "SELECT DISTINCT user_id, user_name FROM membership "
            f"WHERE channel_id={CHANNEL_ID} AND expire_date < strftime('%s')"
        )
        self.cur.execute(query)
        users = [x for x in self.cur.fetchall()]
        success = 0
        for user_id, user_name in users:
            try:
                until_date = int(datetime.now(tz=timezone.utc).timestamp()) \
                    + 60
                await bot.ban_chat_member(CHANNEL_ID,
                                          user_id,
                                          until_date=until_date)
                success += 1
            except Exception as e:
                logging.info("Exception: %s", e)
                text = (
                    "<b>ERROR</b>: failed to ban user from channel, "
                    f"{user_id} {user_name}: {e}"
                )
                if LOG_CHAT_ID is not None:
                    await bot.send_message(LOG_CHAT_ID, text)
            await self.delete_membership(user_id)
            logging.info("%s: %s", user_id, user_name)
            text = (
                "Remove User with Expired Membership: "
                f"<code>{user_id}</code> {user_name}"
            )
            if LOG_CHAT_ID is not None:
                await bot.send_message(LOG_CHAT_ID, text)
        return success, len(users)

    async def get_statistics(self) -> str:
        query = (
            "SELECT user_id, expire_date FROM membership "
            f"WHERE channel_id={CHANNEL_ID}"
        )
        self.cur.execute(query)
        users = [x for x in self.cur.fetchall()]
        utcnow = int(datetime.now(timezone.utc).timestamp())
        users_total = tuple([x[0] for x in users])
        users_expired = tuple([x[0] for x in users if x[1] < utcnow])
        return f"""<b>Membership Statistics</b>:

<b>Expired</b>: {len(users_expired)}
<b>Total</b>: {len(users_total)}
"""
