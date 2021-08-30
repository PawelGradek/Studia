import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.DiGraph()

random.seed(15726346)
edges = []
for i in range(1, 26):
    a = random.randrange(6, 12)
    b = random.randrange(8, 12)
    # if i < 16:
    for j in range(a):
        edges.append((f'{i}', f'{random.randrange(i, 26)}'))
    # krawedzie.append(('15', '18'))
    # krawedzie.append(('14', '19'))
    # krawedzie.append(('12', '22'))
    # krawedzie.append(('18', '21'))
    #
    # if i >= 16 and i < 24:
    #     for j in range(nie_padly_w_5_loso):
    #         krawedzie.append((f'{i}', f'{random.randrange(i+1, 25)}'))

G.add_edges_from(edges)

print(G.nodes())
print(G.edges())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='y')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True)

plt.show()