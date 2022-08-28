import json
import requests
from confing import keys

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(guote: str, base: str, amount: str):

        if guote == base:
            raise APIException(f'Невозможно перевести одинаковые: {base}')
        try:
            guote_ticker = keys[guote]
        except KeyError:
            raise APIException(f'Не удалось обрботать валюту: {guote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработаь валюту: {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработаь валюту: {amount}')
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={guote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base