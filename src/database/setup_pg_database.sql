CREATE TABLE IF NOT EXISTS users (
    id                  SERIAL PRIMARY KEY,
    discord_id          BIGINT NOT NULL,
    balance             BIGINT DEFAULT 300,
    last_hourly_bonus   TIMESTAMP DEFAULT NOW() - INTERVAL '1 HOUR',
    last_daily_bonus    TIMESTAMP DEFAULT NOW() - INTERVAL '1 DAY',

    UNIQUE(discord_id)
)
