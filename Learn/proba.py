import json
# {"liczba_iteracji":  [],  "wartosci_blędu_w_poszczegolnych_iteracjach":  [], "koncowe_wartosci_wag":  [],  "wyniki_dzialania_dla_zbioru_testujacego":  []}
import os
# Pobieranie ścieżki do bieżącego katalogu
sciezka = os.getcwd()
# Pobranie listy pliku we wskazanym katalogu
katalogi_i_pliki = os.listdir(sciezka)
# Wydruk listy plików
print(katalogi_i_pliki)
i =len(katalogi_i_pliki)+1


with open(f'wyniki{i}.json','w') as f:
    f.write('{}')
f.close()

file_1 = open(f'wyniki{i}.json', "r")
data = json.load(file_1)
file_1.close()

data["liczba_iteracji"] = []
data["wartosci_bledu_w_poszczegolnych_iteracjach"] = []
data["koncowe_wartosci_wag"] = []
data["wyniki_dzialania_dla_zbioru_testujacego"] = []
g = open(f"wyniki{i}.json", "w")
json.dump(data, g)
g.close()

# data = json.load(f)

# data['liczba_iteracji'] = 78
#
#
# f = open('zbior_testujacy', "r")
# data_2 = json.load(f)
# f.close()
# for i in data_2['zbior_testujacy']:
#     for j in i[-4:-3]:
#         print(j+2000000)
#
# g = open("wyniki_symulacji", "w")
# json.dump(data, g)
# g.close()
