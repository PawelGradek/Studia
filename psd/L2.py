import requests
from requests.exceptions import HTTPError
from time import sleep


adress_url = 'https://bitbay.net/API/Public/'

def get_data(currency1, category, format):
    try:
        response = requests.get(f'{adress_url}/{currency1}/{category}.{format}')
        response.raise_for_status() #zwraca obiekt HTTPError, jeśli podczas procesu wystąpił błąd, jeśli nie znaleziono adresu url kod 404
        return response
    except HTTPError as http_error:#"Wystąpił błąd HTTP, jeśli np. nie znalezionoby podanego adresu url
        print(f'Error! Operation failed:{http_error}')
    except Exception as error:
        print(f'Error! Operation failed:{error}')

def show_data(currency1, category, format, n=3):
    response1 = get_data(currency1, category, format)
    response2 = response1.json()
    bids = response2['bids']
    for i in range(n):
        print(f'{currency1} USD', bids[i])


def calculate_data(currency2, category, format):
    response3 = get_data(currency2, category, format)
    response4 = response3.json()
    bids_price = response4['bids'][0][1]
    asks_price = response4['asks'][0][1]
    result = round((1 - (asks_price - bids_price) / bids_price) * 100, 2)
    print(f'{currency2} : {result} % ')


def show_all_data():
    print('Purchase price')
    show_data('BTC/USD', 'orderbook', 'json')
    show_data('LTC/USD', 'orderbook', 'json')
    show_data('DASH/USD', 'orderbook', 'json')


def discreate_data_stream():
    print('The difference between buying and selling:')
    while True:
        calculate_data('BTC/USD', 'orderbook', 'json')
        calculate_data('LTC/USD', 'orderbook', 'json')
        calculate_data('DASH/USD', 'orderbook', 'json')
        sleep(5)


if __name__ == "__main__":
    print('The difference between buying and selling:')
    discreate_data_stream()
    #show_all_data
