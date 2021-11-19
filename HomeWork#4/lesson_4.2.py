import requests
from decimal import *


def currency_rates(cur):
    cur = cur.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if cur not in response:
        return None

    rub = response[response.find('<Value>', response.find(cur)) + 7:response.find('</Value>', response.find(cur))]
    return f"{Decimal(rub.replace(',', '.'))}"


print(currency_rates('AUD'))
print(currency_rates('BYN'))
print(currency_rates('JPY'))
print(currency_rates('SEK'))
