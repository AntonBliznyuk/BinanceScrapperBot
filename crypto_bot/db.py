import os


def get_pg_credentials() -> dict:
    return dict(
        dbname=os.getenv('PG_DB_NAME', 'postgres'),
        user=os.getenv('PG_DB_USER', 'postgres'),
        password=os.getenv('PG_DB_PASSWORD', 'postgres'),
        host=os.getenv('PG_DB_HOST', 'pg_db')
    )


class DBBase:
    def __init__(self, conn):
        self.conn = conn


class UserIds(DBBase):
    """Класс для работы с таблицей user_ids"""

    def get_users(self) -> list:
        """Получить всех user_ids из БД"""
        sql = "SELECT DISTINCT chat_id FROM crypto_bot_schema.chat_ids;"
        with self.conn as conn:
            with conn.cursor() as curs:
                curs.execute(sql)
                chat_ids = curs.fetchall()
        return [chat_id for chat_id in chat_ids]

    def add_user(self, user_id: int):
        """Добавить user_id в БД"""
        sql = f"INSERT INTO crypto_bot_schema.chat_ids (chat_id) VALUES ({user_id});"
        with self.conn as conn:
            with conn.cursor() as curs:
                curs.execute(sql)


class BinanceLab(DBBase):
    """Класс для работы с таблицей binance_lab"""

    def check_entry(self, url) -> bool:
        """Проверить project в БД"""
        sql = f"SELECT project FROM crypto_bot_schema.binance_lab where url = '{url}';"
        with self.conn as conn:
            with conn.cursor() as curs:
                curs.execute(sql)
                entry = curs.fetchall()
        return bool(entry)

    def write_entry(self, url: str, project: str):
        """Добавить project в БД"""
        sql = f"INSERT INTO crypto_bot_schema.binance_lab (url, project) VALUES ('{url}', '{project}');"
        with self.conn as conn:
            with conn.cursor() as curs:
                curs.execute(sql)
