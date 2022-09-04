from datetime import datetime, timezone

from aiogram.types.user import User


async def format_name(user: User) -> str:
    return " ".join([
        str(user.id),
        f"@{user.username}" if user.username else '',
        user.first_name,
        user.last_name or ''
    ]).strip()


async def format_timestamp(date: int) -> str:
    return (
        datetime
        .fromtimestamp(date, tz=timezone.utc)
        .strftime("%F %T (UTC)")
    )
