CREATE SCHEMA IF NOT EXISTS crypto_bot_schema;

CREATE TABLE crypto_bot_schema.chat_ids(
chat_id   INTEGER
);

CREATE TABLE crypto_bot_schema.binance_lab(
project   VARCHAR,
url   VARCHAR
);

ALTER TABLE crypto_bot_schema.binance_lab ALTER COLUMN url TYPE text USING url::text;
ALTER TABLE crypto_bot_schema.binance_lab ALTER COLUMN project TYPE text USING project::text;