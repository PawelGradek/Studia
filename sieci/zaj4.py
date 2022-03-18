import networkx as nx
import numpy as np
from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc

# G = nx.erdos_renyi_graph(2, 0.5)
# all_colors = [k for k, v in pltc.cnames.items()]
#
# fracs = np.array([])
# labels = ["label1", "label2", "label3", "label4", "label5", "label6", "label7", "label8"]
#
# colors = sample(all_colors, len(fracs))
#
#
# plt.figure(figsize=(10, 10))
# nx.draw_kamada_kawai(G, with_labels=True, node_color=colors, node_size=100, font_size=6, cmap=plt.cm.Oranges)
# plt.legend(labels, loc=(1.05, 0.7))
# # plt.show()
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
#
# import sys, networkx as nx, matplotlib.pyplot as plt
#
# # Create a list of 10 nodes numbered [0, 9]
# nodes = range(10)
# node_sizes = []
# labels = {}
# for n in nodes:
#         node_sizes.append( 100 * n )
#         labels[n] = 100 * n
#
# # Node sizes: [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
#
# # Connect each node to its successor
# edges = [ (i, i+1) for i in range(len(nodes)-1) ]
#
# # Create the graph and draw it with the node labels
# g = nx.Graph()
# g.add_nodes_from(nodes)
# g.add_edges_from(edges)
#
# nx.draw_random(g, node_size = node_sizes, labels=labels, with_labels=True)
# plt.show()
################
import matplotlib.pyplot as plt
# create number for each group to allow use of colormap
from itertools import count
# get unique groups
g = nx.Graph()
for i in range(20):
    if i <20:
        g.add_edge(i,i+1)

groups = set(nx.get_node_attributes(g,'group').values())
mapping = dict(zip(sorted(groups),count()))
nodes = g.nodes()
colors = [mapping[g.node[n]['group']] for n in nodes]

# drawing nodes and edges separately so we can capture collection for colobar
pos = nx.spring_layout(g)
ec = nx.draw_networkx_edges(g, pos, alpha=0.2)
nc = nx.draw_networkx_nodes(g, pos, nodelist=nodes, node_color=colors,
                            with_labels=False, node_size=100, cmap=plt.cm.jet)
plt.colorbar(nc)
plt.axis('off')
plt.show()