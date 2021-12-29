s1={'k1': 1, 'k2': 2}
s2={'k3': 3, 'k4': 4}

for i in s2.keys():
    for j in s2.values():
        s1[i] = j
# print(s1)

for klucz, wartosc in s2.items():
    s1[klucz] = wartosc
# print(s1)

s1.update(s2)
print(s1)

import pandas as pd

plik = open('cytaty.txt', 'w')
plik.write('Polacy wyssali\n'
           '.....\n'
           'matki.')
plik.close()

with open('cytaty.txt','r') as plik:
    print(plik.readlines())

plik = open('cytaty.txt','r')
zawartosc = plik.readlines()
plik.close()
print(zawartosc)

t = zawartosc[0]
print(t.strip())

with open('cytaty.txt','r') as plik:
    print(plik.readline())
    print(plik.readline())
    print(plik.readline())

l = []
for i in range(10):
    l.append(i)
print(l)

l = [i for i in range(10)]
print(l)

k = [j**2 for j in range(10)]
print(k)


g = [chr(e) for e in [48,72,65]]
print(g)

m = [ord(znak) for znak in 'ABCDE']
print(m)

n = [znak for znak in 'ABCDE']
print(n)

w = 'A-B-C-D'.split('-')
print(w)

v = ':'.join('ABCDE')
print(v)

o = [znak.lower() for znak in 'ABCDE']
print(o)

o = [znak.lower() for znak in 'ABCDE' if znak != 'D']
print(o)

with open('cytaty.txt','r') as plik:
    print(plik.readlines())

o = [linia.strip() for linia in open('cytaty.txt','r')]
print(o)

import os
l = os.listdir()# listą składaną wrzucić do pliku
print(l)

for i, elem in enumerate(l):
    print(f'{i+1}:{elem}')

print(list(enumerate(l)))
print(list(range(4)))
print(list(zip(['a','b','c'],[1,2,3])))
# powyżej to generatory lub funkcje leniwe

p = [linia.strip() for linia in open('cytaty.txt','w') if linia.endswith('.txt')]
print(p)

f = os.listdir()
print(f)