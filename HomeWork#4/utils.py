import requests
from decimal import *
from datetime import datetime


def currency_rates(cur):
    cur = cur.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if cur not in response:
        return None

    rub = response[response.find('<Value>', response.find(cur)) + 7:response.find('</Value>', response.find(cur))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"
