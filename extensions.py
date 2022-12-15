import json
import requests
from config import keys

class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        resp = json.loads(r.content)
        sum_price = resp[quote_ticker] * amount
        sum_price = round(sum_price, 3)
        text = f"Цена {amount} {base} в {quote} составит: {sum_price}"
        return text

