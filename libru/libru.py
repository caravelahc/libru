import requests
import bs4

import re
from pytz import timezone
from datetime import datetime

spaces = re.compile('\s+')


def sanitize(string):
    return spaces.sub(' ', (string.strip(' \n\xa0')
                            .replace('\n', ' ')
                            .replace('/', ' e ')
                            .lower()))


def parse(content, weekday):
    soup = bs4.BeautifulSoup(content, 'lxml')
    table = soup.find('div', class_='content clearfix').find('table')

    rows = table.find_all('tr')

    today = [sanitize(entry.text)
             for entry in rows[weekday].find_all('td')[1:]]

    return today


def ru(weekday=None):
    resp = requests.get('http://ru.ufsc.br/ru/')

    if weekday is None:
        weekday = datetime.now(timezone('America/Sao_Paulo')).weekday()

    if not resp.ok:
        return []

    return parse(resp.content, weekday)
