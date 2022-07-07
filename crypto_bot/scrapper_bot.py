import psycopg2
from telegram import Update, Bot
from telegram.ext import CallbackContext, Updater, CommandHandler

from crypto_bot.db import UserIds

TOKEN = '5180562566:AAHY__ggw-1UUGO6ffJ0Cg2Qp1tssOpVYWY'  # s
# TOKEN = '5115822882:AAGZflRWZ1xRSkmIMFPGI-3qcRDwfzF6slU'  # j


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
        # Create the Updater and pass it your crypto_bot's token.
        updater = Updater(TOKEN)

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        # on different commands - answer in Telegram
        dispatcher.add_handler(CommandHandler("start", self.start))

        # Start the Bot
        updater.start_polling()
        # updater.idle()

    def send_messages(self, messages):
        """Send message to subscribers"""
        chat_ids = UserIds(self.conn).get_users()
        if chat_ids:
            for chat_id in chat_ids:
                print(f'{chat_id[0]} from {chat_ids}')
                for message in messages:
                    self.telegram_bot.send_message(chat_id=chat_id[0], text=message)
