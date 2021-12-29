import os
f = os.listdir()
print(f)
for elem in os.listdir():
    print(elem)

f = [elem.split('.')[0] for elem in os.listdir()]
print(f)

from collections import Counter
h = Counter('acaacbwa')
print(h)

with open('zaj3','r') as plik:
    linia = plik.readline()#.rstrip()
    #for linia in plik:
        #print(linia.replace(',',':'))
        #print(linia.join(''))
        #print(tuple(linia.strip().replace('(','').replace(')','').split(',')))
    lista_polaczona = [tuple(linia.strip().replace('(','').replace(')','').split(',')) for linia in plik]
    print(lista_polaczona)
print('To jest lista polaczona:',lista_polaczona)
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from(lista_polaczona)
G.nodes(data=True)
nx.draw_spring(G,with_labels=True)

#plt.show()
lista = ['ab','cd','cuba','cde','cd','cde']
p = set(lista) # tak jak lista tylko każdy element jest unikalny
print(p)
slo = {}

# zadanie domowe [ w1: lista polaczona....

f = lista_polaczona[0][0][1]
print(f)

slo1 = {}
for (wA,wB) in lista_polaczona:
    if wA in slo1:
        slo1[wA].append(wB)
    else:
        slo1[wA] = [wB]
print(slo1)



