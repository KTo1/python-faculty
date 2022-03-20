
import requests
from datetime import datetime


def currency_rates(currency_code):
    api_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    # API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    result = dict()

    res = requests.get(api_url)

    if not res.status_code == 200:
        print('Could"t get data from service.')
        return None

    res_json = res.json()

    currency = res_json['Valute'].get(currency_code.upper())
    if currency is not None:
        result['code'] = currency["CharCode"]
        result['value'] = currency["Value"]
        result['date'] = datetime.fromisoformat(res_json['Date'])

        return result

    return None


currency_list = ['eUr', 'USd', 'USd1']

for currency_code in currency_list:

    currency = currency_rates(currency_code)
    if currency is not None:
        print(f'{currency["code"]}, {currency["value"]}, {currency["date"].date()}')
    else:
        print(f'{currency_code}: not found.')

