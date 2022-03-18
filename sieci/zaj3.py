# Sieć złożona składa się z krajów kontynentu Afryka, które posługują się tym samym językiem rdzennym afryki
import networkx as nx
# import pandas as pd
# import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

filename = 'afryka' # źródło: https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_Afryki
lines = [line.split(':') for line in open(filename, 'r')]
connections_list = []
for line in lines:
    key = line[0].strip()
    for elem in line[1].split(','):
        connections_list.append((key, elem.strip()))

connections_dict = defaultdict(set)
for (elem1, elem2) in connections_list:
    connections_dict[elem1].add(elem2)
    connections_dict[elem2].add(elem1)

G = nx.Graph()
G.add_edges_from(connections_list)
G.nodes(data=True)



print('Stopień sieci wynosi (liczba wierzchołków):', G.number_of_nodes())
print('Rozmiar sieci wynosi (liczba krawędzi):', G.number_of_edges())
print('Czy siec jest spójna:', nx.is_connected(G))
print('Stopnie sieci:', nx.degree(G)) # ilość krawędzi dla poszczególnych źródeł
print('Gęstość sieci', nx.density(G)) # Gęstość wynosi 0 dla wykresu bez krawędzi i 1 dla całego wykresu.
print('Bliskość sieci', nx.closeness_centrality(G)) # Oblicz centralność bliskości węzłów.
print('Średnica sieci', nx.diameter(G)) # średnica-maksymalny mimośród w grafie (maksymalna odległość wierzchołka grafu od innych wierzchołków.)
for i in nx.connected_components(G):
    print('Składowa spójna', i)
print('Czy sieć jest k-spójna dla k=4', nx.is_k_edge_connected(G,
                                                               4))  # Czy nie można odłączyć grafu usuwając mniej niż k krawędzi? Jeśli tak, to G jest połączone krawędzią k.
print('Spójności krawędziowa sieci', nx.edge_connectivity(G)) #  jest równa minimalnej liczbie krawędzi, które muszą zostać usunięte, aby rozłączyć sieć G lub uczynić ją trywialną.
print('Spójność wierzchołkowa sieci', nx.node_connectivity(G)) #  jest równa minimalnej liczbie węzłów, które muszą zostać usunięte, aby rozłączyć sieć G lub uczynić ją trywialną.


 # ZADANIE
# wybrać wskaźniki nie wszystkie ze strony networx ->kliki
# 1.analiza klik w mojej małej sieci
# 2.analiza klik w sieci losowej
# -wybór generatora sieci\ generator sieci w networx
# -plan eksperymentu
# -rozmiar sieci Zwraca wszystkie kliki w grafie nieskierowanym.
# -gęstość sieci
# -wskaźniki związane z analizą
# wnioski\ jak ktoś zwiększał gęstośc sieci to jego wskaźnik wzrósł

# Ad1
# wskaźnik find_cliques(G)- Zwraca wszystkie maksymalne kliki w grafie nieskierowanym.
print('Maksymalna lista klik w sieci G', list(nx.find_cliques(G)))
# wskaźnik graph_clique_number(G[, kliki]) - Zwraca liczbę największej kliki wykresu.
print('Wielkość największej kliki w sieci G', nx.graph_clique_number(G, cliques=None))
# graph_number_of_cliques(G[, kliki])- Zwraca liczbę maksymalnych klik na wykresie.
print('Maksymalna liczba klik w sieci G', nx.graph_number_of_cliques(G, cliques=None))

# wnioski: Wielkość największej kliki wynosi 7 a stopień sieci wynosi 26 z tego wynika że około 1/4 wierzchołków jest w bezpośrednim połączeniu ze sobą