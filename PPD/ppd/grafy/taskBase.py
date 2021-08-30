import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


g = nx.Graph()
random.seed(15726)
zadania = []
for i in range(0, 24):
    zadania.append([])
    zadania[i].append(i+1)
    zadania[i].append(random.randint(1, 7))
    zadania[i].append(random.randint(1, 7))
    g.add_node(i+1)
print(np.array(zadania))


# krawedzie = [(1,2),(1,3), (2,4), (2,5), (3,6), (4,7), (4,8), (5,9), (6,9), (7,10), (7,11), (7,12), (8,13), (9,13), (10,15), (11,15), (12,14), (13,14), (14,15) ]
# g.add_edges_from(krawedzie)
# nx.draw(g,  with_labels=True, node_color='yellow')
# plt.show()



