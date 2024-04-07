from secret_key import API_KEY
import requests
from requests import Session
from pprint import pprint as pp


class CoinMarketCap:
    # "https://coinmarketcap.com/api/documentation/v1/#"
    def __init__(self, token):
        self.api_url = "https://pro-api.coinmarketcap.com"
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_all_coins(self):
        url = self.api_url + "/v1/cryptocurrency/map"
        r = self.session.get(url)
        data = r.json()['data']

        return data


    def get_price(self, symbol):
        url = self.api_url + "/v2/cryptocurrency/quotes/latest"
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']

        return data


def main():
    cmc = CoinMarketCap(API_KEY)

    coin_symbol = input("Enter the crypto ticker symbol: ")
    pp(cmc.get_price(coin_symbol))



if __name__ == "__main__":
    main()
