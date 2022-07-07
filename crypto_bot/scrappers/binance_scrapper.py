from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from crypto_bot.db import BinanceLab


class BinanceScrapper:
    """Класс для скрапинга BinanceLab"""

    link = 'https://labs.binance.com/'

    @staticmethod
    def get_soup(link_l):
        try:
            response = requests.get(link_l)
            if response.status_code == 200:
                print('Successfully connected, response code is 200')
                soup = BeautifulSoup(response.text, 'lxml')
                return soup
            else:
                print('Response code is different than 200. Response code: ', response.status_code)
        except Exception as e:
            print('error occured: ', e)

    def scrap(self, conn) -> Optional[List[str]]:
        """Распарсить и вернуть мессаджи"""
        soup = self.get_soup(self.link)
        parsed_projects = []
        if soup:
            for text in soup.find_all('a', class_='team col-lg-4 col-sm-6 mb-5'):
                url = text.get('href')

                if not BinanceLab(conn).check_entry(url):
                    project_names = text.find_all('h4')
                    if project_names:
                        for project in project_names:
                            project_name = project.text
                            BinanceLab(conn).write_entry(url, project_name)
                            parsed_projects.append((url, project_name))
                    else:
                        project_name = 'Project name not found'
                        BinanceLab(conn).write_entry(url, project_name)
                        parsed_projects.append((url, project_name))

            return [f"URL: {project[0]} \r\nProject: {project[1]}" for project in parsed_projects]
        return None
