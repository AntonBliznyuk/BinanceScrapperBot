import psycopg2
from telegram import Update, Bot
from telegram.ext import CallbackContext, Updater, CommandHandler

from crypto_bot.db import UserIds

TOKEN = '5523089120:AAHxposdv_TCrXN7OypNfbSKjaJH18Cn1As'



class ScrapperBot:
    """Класс реализующий логику бота"""

    def __init__(self):
        self.telegram_bot = Bot(TOKEN)
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=postgres host=pg_db")

    def start(self, update: Update, context: CallbackContext) -> None:
        """Sends explanation on how to use the crypto_bot."""
        update.message.reply_text(f'Hi! Remember you {update.message.chat_id}')
        UserIds(self.conn).add_user(user_id=update.message.chat_id)

    def run(self) -> None:
        """Run crypto_bot."""
        updater = Updater(TOKEN)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.start))

        updater.start_polling()

    def send_messages(self, messages):
        """Send message to subscribers"""
        chat_ids = UserIds(self.conn).get_users()
        if chat_ids:
            for chat_id in chat_ids:
                print(f'{chat_id[0]} from {chat_ids}')
                for message in messages:
                    self.telegram_bot.send_message(chat_id=chat_id[0], text=message)
