import time

from crypto_bot.scrapper_bot import ScrapperBot
from crypto_bot.scrappers.binance_scrapper import BinanceScrapper


if __name__ == '__main__':

    scrapper_bot = ScrapperBot()
    scrapper_bot.run()

    b_scrapper = BinanceScrapper()

    while True:
        messages = b_scrapper.scrap(conn=scrapper_bot.conn)
        if messages:
            scrapper_bot.send_messages(messages)
        time.sleep(15)
