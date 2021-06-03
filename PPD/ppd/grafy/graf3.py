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
    # edges.append(('15', '18'))
    # edges.append(('14', '19'))
    # edges.append(('12', '22'))
    # edges.append(('18', '21'))
    #
    # if i >= 16 and i < 24:
    #     for j in range(b):
    #         edges.append((f'{i}', f'{random.randrange(i+1, 25)}'))

G.add_edges_from(edges)

print(G.nodes())
print(G.edges())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='y')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True)

plt.show()