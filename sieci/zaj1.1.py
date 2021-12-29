import networkx as nx
import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

# Ad 2

# dense_gnm_random_graph(n, m[, ziarno])- Zwraca wykres losowy G, gdzie: n liczba węzłów, m- liczba krawędzi
# przy czym n odpowiada za rozmiar sieci a m za gęstość sieci

G1 = nx.gnm_random_graph(10, 20, seed=None, directed=False)
G1 = nx.Graph()
G1.add_edges_from(connections_list)
G1.nodes(data=True)
nx.draw_spring(G1,with_labels=True)
plt.show()