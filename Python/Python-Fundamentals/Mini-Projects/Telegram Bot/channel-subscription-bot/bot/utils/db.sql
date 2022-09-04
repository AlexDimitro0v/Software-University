-- sqlite3 data.db <bot/utils/db.sql

CREATE TABLE IF NOT EXISTS membership (
    user_id INTEGER UNSIGNED NOT NULL,
    user_name TEXT NOT NULL,
    channel_id INTEGER SIGNED NOT NULL,
    expire_date INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY (user_id, channel_id)
);

CREATE TABLE IF NOT EXISTS invite_links (
    invite_link TEXT PRIMARY KEY,
    expire_date INTEGER UNSIGNED NOT NULL,
    user_id INTEGER SIGNED NOT NULL,
    channel_id INTEGER UNSIGNED NOT NULL
);
