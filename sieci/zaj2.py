import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import json
import matplotlib.colors as colors
import matplotlib.cm as cmx

file_1o = open('dane_o_filmach.json', "r", encoding="utf-8")
oceny = json.load(file_1o)
file_1o.close()

oceny_filmow = oceny["oceny_filmow"]
liczba_glosow = oceny["liczba_glosow"]


# poniżej tworzymy liste połączoną w której znajdują się filmy które będą połączone ze sobą w sieci,
# podobnej implementacji dokonywaliśmy na zajęciach laboratoryjnych
filename = 'filmy'
lines = [line.split(':') for line in open(filename, 'r', encoding="utf-8")]
connections_list = []
for line in lines:
    key = line[0].strip()
    for elem in line[1].split(','):
        connections_list.append((key, elem.strip()))

# poniżej tworzymy słownik w którym znajdują się filmy które będą połączone ze sobą w sieci
connections_dict = defaultdict(set)
for (elem1, elem2) in connections_list:
    connections_dict[elem1].add(elem2)
    connections_dict[elem2].add(elem1)


# następnie korzystając z pakietu networkx tworzymy sieć
G = nx.Graph()
G.add_edges_from(connections_list)
G.nodes(data=True)

pos = nx.spring_layout(G)
val_map = {}

# dodajemy kolor wezlow zalezny od oceny filmu
for i in range(len(oceny_filmow)):
    val_map[f'{oceny_filmow[i][0]}'] = oceny_filmow[i][1]

zbior_ocen = []
for i in val_map.values():
    zbior_ocen.append(i)
zbior_ocen = set(zbior_ocen)

zbior_ocen2 = []
for i in zbior_ocen:
    zbior_ocen2.append(i)
zbior_ocen2.sort()
zbior_ocen2.reverse()

ColorLegend = {}

for i in zbior_ocen2:
    ColorLegend[f'{i}'] = i


values = [val_map.get(node, 0) for node in G.nodes()]

# normalizujemy wartości tak aby były w jednym kolorze lecz w róznych barwach dla poszczególnych ocen
# poniższy kod był wzorowany na przykładzie który znajduje się na stronie: https://stackoverflow.com/questions/22992009/legend-in-python-networkx
jet = cm = plt.get_cmap('jet')
cNorm = colors.Normalize(vmin=0, vmax=max(values))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

f = plt.figure(1)
ax = f.add_subplot(1, 1, 1)
for label in ColorLegend:
    ax.plot([0], [0], color=scalarMap.to_rgba(ColorLegend[label]), label=label)


# przypisanie wielkości węzłom zgodnej z liczbą ocen
liczba_glosow2 = []
for node in G:
    for i in liczba_glosow:
        if node == i[0]:
            liczba_glosow2.append(i[1])

# wcelu wizualizacji sieci użyłem dwóch metod z pakietu networkx: kamada kawai oraz circular
# nx.draw_kamada_kawai(G, cmap=jet, vmin=0, vmax=max(values), node_color=values, with_labels=True, ax=ax, font_size=6, node_size=[liczba_glosow[v][1] for v in range(len(liczba_glosow))])
nx.draw_circular(G, cmap=jet, vmin=0, vmax=max(values), node_color=values, with_labels=True, ax=ax, font_size=6, node_size=[liczba_glosow2[v] for v in range(len(liczba_glosow2))])

plt.axis('off')
f.set_facecolor('w')
plt.legend(title='Oceny')
f.tight_layout()

plt.show()
print('Liczba filmów: ', len(oceny_filmow))

# Ad1
# wskaźnik find_cliques(G)- Zwraca wszystkie maksymalne kliki w grafie nieskierowanym.
x = list(nx.find_cliques(G))

l = 0

list_of_cliques = []
rate_in_cliques = []
for i in x:
    if len(i) > 3:
        l += 1
        list_of_cliques.append(i)


for i in list_of_cliques:
    list_of_rate_cliques = []
    for j in i:
        for k in oceny_filmow:
            if j == k[0]:
                list_of_rate_cliques.append(k[1])
    rate_in_cliques.append(list_of_rate_cliques)

list_cliques_with_rate = []
for i in range(len(list_of_cliques)):
    secondary_list = []
    for j in range(len(list_of_cliques[i])):
        secondary_list.append([list_of_cliques[i][j], rate_in_cliques[i][j]])
    list_cliques_with_rate.append(secondary_list)

print('rate in cliques',rate_in_cliques)
for i in range(len(rate_in_cliques)):
    minimum = min(rate_in_cliques[i])
    maximum = max(rate_in_cliques[i])
    if round((maximum - minimum),3) <= 0.4:
        print(f'klika {i + 1}: {list_cliques_with_rate[i]}\n spełnia założenia')
    if round((maximum - minimum),3) > 0.4:
        print(f'klika {i+1}: {list_cliques_with_rate[i]}\n  nie spełnia założeń')

