import requests
import bs4

import re
from pytz import timezone
from datetime import datetime

spaces = re.compile(r"\s+")


def sanitize(string):
    strings = string.strip(" \n\xa0").replace("/", " e ").lower()

    for s in strings.split("\n"):
        yield spaces.sub(" ", s)


def _parse(content, weekday):
    soup = bs4.BeautifulSoup(content, "lxml")
    table = soup.find("div", class_="content clearfix").find("table")

    rows = table.find_all("tr")

    today = rows[weekday + 1].find_all("td")[2:]

    for entry in today:
        items = sanitize(entry.text)

        for s in items:
            if s != '' and not s.isspace():
                yield s


def parse(*args):
    return list(_parse(*args))


def ru(weekday=None):
    resp = requests.get("http://ru.ufsc.br/ru/")

    if weekday is None:
        weekday = datetime.now(timezone("America/Sao_Paulo")).weekday()

    if not resp.ok:
        return []

    return parse(resp.content, weekday)
