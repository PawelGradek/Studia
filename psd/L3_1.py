import requests
from requests.exceptions import HTTPError
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation

adress_url = 'https://bitbay.net/API/Public/'

def get_data(currency1, currency2, category1, format1):
    try:
        response = requests.get(f'{adress_url}/{currency1}/{currency2}/{category1}.{format1}')
        response.raise_for_status()
    except HTTPError as http_error:
        print(f'Error! Operation failed:{http_error}')
    except Exception as error:
        print(f'Error! Operation failed:{error}')
    else:
        data = response.json()
        return data


def plot_data(_):
    values_y = [values_1_bid, values_1_ask, values_2_bid, values_2_ask, values_3_bid, values_3_ask]
    values_y[0].append(y1['bid'])
    values_y[1].append(y1['ask'])
    values_y[2].append(y2['bid'])
    values_y[3].append(y2['ask'])
    values_y[4].append(y3['bid'])
    values_y[5].append(y3['ask'])

    time = datetime.now()
    values_x.append(time.strftime('%H:%M:%ciag'))

    values_legend = ['bid1', 'ask1', 'bid2', 'ask2', 'bid3', 'ask3']
    plt.cla()#Wyczyść bieżące osie

    for i in values_y:
        plt.plot(values_x, i, label=values_legend[values_y.index(i)])

    # plt.xticks(values_x, rotation=20)
    # limits = []
    # for j in values_y:
    #     limits.append(min(j))
    #     limits.append(max(j))
    #
    # minimum = min(limits)
    # maximum = max(limits)
    # plt.ylim(minimum-1, maximum+1)

    plt.legend(loc='best', bbox_to_anchor=(0.5, 0.3, 0.5, 0.45))  # ustawienie legendy w ktorym miejscu
    plt.xlabel("Time")
    plt.ylabel("USD price")
    plt.title("Data graph")
    plt.subplots_adjust(bottom=0.2)  #wielkoś wykresu

if __name__ == "__main__":
    values_1_bid, values_1_ask = [], []
    values_2_bid, values_2_ask = [], []
    values_3_bid, values_3_ask = [], []
    y1 = get_data('BAT', 'USD', 'ticker', 'json')
    y2 = get_data('TRX', 'USD', 'ticker', 'json')
    y3 = get_data('LSK', 'USD', 'ticker', 'json')
    values_x = []

    plt.style.use('seaborn')
    animation = FuncAnimation(plt.gcf(), plot_data, interval=5000)# plt.gcf-- Jeśli aktualna figura nie istnieje, nowa jest tworzona za pomocą figure()
    plt.show()
    #opis funcAnimation
    #1pozycja- Obiekt figury używany do uzyskiwania potrzebnych zdarzeń, takich jak rysowanie lub zmiana rozmiaru.
    #2pozycja - Funkcja do wywołania w każdej klatce. Pierwszy argument będzie następną wartością w ramkach
    # Wszelkie dodatkowe argumenty pozycyjne można podać za pośrednictwem parametru fargs .
    #3pozycja- Opóźnienie między klatkami w milisekundach