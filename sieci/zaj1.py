import requests
from bs4 import BeautifulSoup
import json

file_1o = open('dane_o_filmach.json', "r", encoding="utf-8")
oceny = json.load(file_1o)
file_1o.close()

URL = 'https://www.filmweb.pl/films/search?orderBy=popularity&descending=true'

lista_filmow = []
oceny_filmow = []
liczba_glosow = []

# funkcja do pobierania potrzebnych danych ze strony Filmweb
# poniższa funkcja została zaimplementowana przy pomocy tutoriala znajdującego się pod linkiem: https://www.youtube.com/watch?v=CEOTrWowqfo
def parse_page(number):
    print('pracuje nad strona: ', number)
    page = requests.get(f'{URL}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')

    # rate - ocena danego filmu, count- liczba ocen społeczności danego filmu
    for film in bs.find_all('div', class_='filmPreviewHolder isSmall'):
        title = film.find('h2', class_='filmPreview__title').get_text()
        rate = film.find('span', class_='rateBox__rate').get_text()
        count = film.find('span', class_='rateBox__votes rateBox__votes--count').get_text()
        title = title.replace(":", "")
        title = title.replace(",", " ")
        rate = rate.replace(',', '.')
        rate = round(float(rate), 2)
        count = count.replace(' ', '')
        count = int(count.strip())

        lista_filmow.append([title, count])
        oceny_filmow.append([title, rate])
        liczba_glosow.append([title, int(round((count/1000), 0))])


for page in range(1, 13):
    parse_page(page)

filmy = {}

# dodajemy do słownika filmy które mają podobną liczbę ocen społeczności
for i in range(len(lista_filmow)):
    filmy[lista_filmow[i][0]] = []
    for j in range(len(lista_filmow)):
        if i == j:
            continue
        else:
            if lista_filmow[j][1] - 5000 < lista_filmow[i][1] <= lista_filmow[j][1] + 5000:
                filmy[lista_filmow[i][0]].append(lista_filmow[j][0])


# otwieramy plik w trybie do zapisu
plik = open("filmy", 'w', encoding="utf-8")

lista_filmow_w_pliku = []
for i, j in zip(filmy.keys(), filmy.values()):
    j = set(j)
    if j != set():
        l = ''
        for k in j:
            l = l + f'{k}, '
        l = l[:-2]
        # każdy z obiektów po konwersji zapisujemy w nowej linii
        plik.write(f'{i}: {l}' + '\n')
    else:
        # usuwamy filmy które nie mają połączenia z innymi filmami o podobnej liczbie ocen społeczności
        tabu = []
        for k in range(len(oceny_filmow)):
            if oceny_filmow[k][0] == f'{i}':
                tabu.append(k)
        for t in tabu:
            del oceny_filmow[t]
            del liczba_glosow[t]

plik.close()

# zapisujemy dane_o_filmach.json i liczbę ocen społeczności filmów do pliku json o nazwie 'dane_o_filmach.json'
oceny["oceny_filmow"] = oceny_filmow
oceny["liczba_glosow"] = liczba_glosow
g = open("dane_o_filmach.json", "w", encoding="utf-8")
json.dump(oceny, g)
g.close()
