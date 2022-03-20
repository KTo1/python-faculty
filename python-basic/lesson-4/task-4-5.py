
import utils
import sys


if len(sys.argv) == 2:
    currency = utils.currency_rates(sys.argv[1])
    if currency is not None:
        print(f'{currency["code"]}, {currency["value"]}, {currency["date"].date()}')
    else:
        print('Not found.')
else:
    print('Wrong arguments.')