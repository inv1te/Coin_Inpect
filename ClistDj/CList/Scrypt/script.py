import time

from art import *
from binance.client import Client
import json
import requests
from fake_useragent import UserAgent

api_key = "o2nxoIU69ksiOLtbpxKxdSEujQ6oP8ckjs0NYnCTxl4WIv8f6jEhh49Jtauyh9YT"
api_secret = "MuQlxiEJzjUjABVdEBOVAA9tCA7Qc3Ybp3bHy8JgMcCGsC9UlNnhCCq5W1aa32cs"

CURRENCIES_by = ['BTC', 'ETH', 'BNB', 'USDC', 'XRP', 'SOL', 'BUSD', 'UST', ]
CURRENCIES_to = ["USD"]

client = Client(api_key, api_secret)


class Binance_crypto:
    def get_inf0_and_currency(first_curr_array, sec_curr):
        data_Bin = []
        info = client.get_all_tickers()
        tprint('CRYPTOS')
        tprint('TOXA')
        tprint('MuNcH')
        tprint('KPyTOII')
        for i in first_curr_array:
            value = i + sec_curr+'T'
            for elem in info:
                if elem.get('symbol') == value:
                    data_Bin.append({
                        "market": "Binance",
                        "symbol": elem.get("symbol"),
                        'price': round(float(elem.get("price")),4)
                    })
        with open("res.json", 'w') as file:
            json.dump(data_Bin, file, ensure_ascii=False, indent=4)
        return data_Bin

class FTX_crypto:
    def get_inf0_and_currency(first_curr_array, sec_curr):
        data_FTX = []
        API_URL = 'https://ftx.com/api/markets'
        response = requests.get(API_URL).json().get('result')
        with open("res_x.json", 'w') as file:
            json.dump(response, file, ensure_ascii=False, indent=4)
        for elem in first_curr_array:
            value = elem+'/'+sec_curr
            for i in response:
                if i.get('name') == value:
                    data_FTX.append({
                        "market": "FTX",
                        "symbol": elem+sec_curr,
                        'price': i.get("price"),
                        'change1h': round(i.get("change1h"), 4),
                        'change24h': round(i.get("change24h"), 4),
                        'priceMax24h': round(i.get('priceHigh24h')),
                        'priceMin24h': round(i.get('priceLow24h'))
                    })
        with open("res_2.json", 'w') as file:
            json.dump(data_FTX, file, ensure_ascii=False, indent=4)
        return data_FTX

class Kraken_crypto:
    def get_inf0_and_currency(first_curr_array, sec_curr):
        data_Kraken = []

        for i in first_curr_array:
            value = i + sec_curr
            resp = requests.get("https://api.kraken.com/0/public/Ticker?pair="+value)

            if resp.json().get('error') == []:
                res = resp.json().get('result')
                info = res.get(list(res.keys())[0])
                data_Kraken.append({
                    'market': "Kraken",
                    'symbol': value,
                    'price': float(info.get('c')[0]),
                    'priceMax24h': float(info.get('h')[1]),
                    'priceMin24h': float(info.get('l')[1])
                })
            else:
                data_Kraken.append({
                    'error:': resp.json().get('error')
                })

        with open("res_3.json", 'w') as file:
            json.dump(data_Kraken, file, ensure_ascii=False, indent=4)
        return data_Kraken
class KuCoin:
    def get_inf0_and_currency(first_curr_array, sec_curr):
        data_ku = []
        API_URL = "https://api.kucoin.com/api/v1/market/allTickers"
        resp = requests.get(API_URL)
        if sec_curr[-1] != 'T' and sec_curr[:3] == 'USD':
            sec_curr = sec_curr + 'T'
        for elem in first_curr_array:
            value = elem + "-" + sec_curr
            for i in resp.json().get('data').get('ticker'):
                if i.get('symbol') == value:
                    data_ku.append({
                        'market': "KuCoin",
                        'symbol': elem+sec_curr,
                        'price': float(i.get('sell')),
                        "change24h": float(i.get('changeRate')),
                        'priceMax24h': float(i.get('high')),
                        'priceMin24h': float(i.get('low'))
                    })
        with open("res_4.json", 'w') as file:
            json.dump(data_ku, file, ensure_ascii=False, indent=4)
        return data_ku

class Gate_Io:
    def defget_inf0_and_currency(first_curr_array, sec_curr):
        data_gate = []
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        API_URL = "https://api.gateio.ws/api/v4/spot/tickers"
        resp = requests.request('GET', API_URL, headers=headers)
        for elem in first_curr_array:
            value = elem+"_"+sec_curr
            for i in resp.json():
                if i.get('currency_pair') == value:
                    data_gate.append({
                        'market': "Gate_Io",
                        'symbol': elem + sec_curr,
                        'price': float(i.get('last')),
                        'priceMax24h': float(i.get('high_24h')),
                        'priceMin24h': float(i.get('low_24h'))
                    })
        with open("res_5.json", 'w') as file:
            json.dump(data_gate, file, ensure_ascii=False, indent=4)
        return data_gate

def main():
    Bin = Binance_crypto.get_inf0_and_currency(CURRENCIES_by, CURRENCIES_to[0])
    FTX = FTX_crypto.get_inf0_and_currency(CURRENCIES_by, CURRENCIES_to[0])
    Kraken = Kraken_crypto.get_inf0_and_currency(CURRENCIES_by, CURRENCIES_to[0])
    KuC = KuCoin.get_inf0_and_currency(CURRENCIES_by, CURRENCIES_to[0])
    Gate = Gate_Io.defget_inf0_and_currency(CURRENCIES_by, CURRENCIES_to[0])
    Markets = [Bin, FTX, KuC, Kraken, Gate]

    print('[!] File .json saved successfully [!]')


if __name__ == "__main__":
    main()
