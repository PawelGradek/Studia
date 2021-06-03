import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(15726)

edges = [(1, 2), (2, 4), (5, 3), (8, 5), (3, 6), (4, 7), (4, 8), (5, 9), (6, 9), (7, 10), (7, 11),
        (7, 12), (8, 13), (9, 13), (10, 15), (11, 15), (12, 14), (13, 14), (14, 15), (15, 17), (16, 19),
        (17, 16), (19, 22), (18, 20), (15, 18), (20, 23), (22, 23), (23, 24), (15, 22), (18, 23),(24, 25), (23,25)]

G = nx.DiGraph()
G.add_edges_from(edges)
print(G.nodes())
print(G.edges())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='y')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True)

plt.show()