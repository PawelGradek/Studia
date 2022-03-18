import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import json
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np


file_1o = open('dane_o_filmach.json', "r", encoding="utf-8")
oceny = json.load(file_1o)
file_1o.close()

oceny_filmow = oceny["oceny_filmow"]
liczba_glosow = oceny["liczba_glosow"]
print('liczba glosow', liczba_glosow)

print(len(oceny_filmow))
print(len(liczba_glosow))

filename = 'filmy'
lines = [line.split(':') for line in open(filename, 'r', encoding="utf-8")]
print("lines:",len(lines))
connections_list = []
for line in lines:
    print(line,"line")
    key = line[0].strip()
    print(key,'key')
    for elem in line[1].split(','):
        print(elem,'elem')
        connections_list.append((key, elem.strip()))
        print((key, elem.strip()),'()')

connections_dict = defaultdict(set)
for (elem1, elem2) in connections_list:
    connections_dict[elem1].add(elem2)
    connections_dict[elem2].add(elem1)


G = nx.Graph()
G.add_edges_from(connections_list)
G.nodes(data=True)

pos=nx.spring_layout(G)
val_map  = {}


for i in range(len(oceny_filmow)):
    val_map[f'{oceny_filmow[i][0]}'] = oceny_filmow[i][1]

# zbior_ocen = []
# for i in val_map.values():
#     zbior_ocen.append(i)
# zbior_ocen = set(zbior_ocen)
# print(zbior_ocen)
#
# ColorLegend = {}
#
# for i in zbior_ocen:
#     ColorLegend[f'ocena {i}'] = i
# print(ColorLegend)

print(val_map)
values = [val_map.get(node, 0) for node in G.nodes()]

# jet = cm = plt.get_cmap('jet')
# cNorm  = colors.Normalize(vmin=0, vmax=max(values))
# scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
#
# f = plt.figure(1)
# ax = f.add_subplot(1,1,1)
# for label in ColorLegend:
#     ax.plot([0],[0],color=scalarMap.to_rgba(ColorLegend[label]),label=label)

plt.figure(figsize=(10, 10))
nx.draw_kamada_kawai(G, with_labels=True,  cmap=plt.get_cmap('jet'), node_color=values, font_size=6, node_size=[liczba_glosow[v][1] for v in range(len(liczba_glosow))])
# nx.draw_networkx(G,pos, cmap = jet, vmin=0, vmax= max(values),node_color=values,with_labels=True,ax=ax)
# nx.draw_networkx(G,pos, cmap = jet, vmin=0, vmax= max(values),node_color=values,with_labels=True,ax=ax)
# nx.draw_kamada_kawai(G, cmap = jet, vmin=0, vmax= max(values),node_color=values,with_labels=True, ax=ax, font_size=6, node_size=[liczba_glosow[v][1] for v in range(len(liczba_glosow))])
# plt.axis('off')
# f.set_facecolor('w')
# plt.legend()
# f.tight_layout()

plt.show()