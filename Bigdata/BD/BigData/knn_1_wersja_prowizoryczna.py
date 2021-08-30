import numpy.random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt, ceil

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

n = 500

x1 = 6 * rnd.rand(n) - 3
y1 = 6 * rnd.rand(n) - 3
z1 = 6 * rnd.rand(n) - 3

x2 = rnd.randn(n) + 15
y2 = rnd.randn(n)
z2 = rnd.randn(n)

x3 = rnd.randn(n)
y3 = rnd.randn(n) + 15
z3 = rnd.randn(n)

ax.scatter(x1,y1,z1, c='nie_padly_w_5_loso', marker = '^')
ax.scatter(x2,y2,z2, c='r', marker = '+')
ax.scatter(x3,y3,z3, c='k', marker = 'o')

#plt.show()

def odleglosc(e1, e2):
    suma_kwadratow = 0
    for a, b in zip(e1, e2):
        suma_kwadratow += ((a - b) ** 2)
    return sqrt(suma_kwadratow)

print(odleglosc([10, 5], [7, 6]))

def ustal_k(n, c):
    k = ceil(sqrt(n))
    while k <= c:
        k += 1
    return k

z = (70, 9)

print(f"ustal_{z} = ", ustal_k(70, 9))

grupa = {
    'A' : [(10, 5), (7, 6)],
    'B' : [(2, 5), (5, 3)]
}
odl = []

nowy = (8, 5)

ilosc_elementow = 0

for gr, elems in grupa.items():
    for elem in elems:
        ilosc_elementow += 1
        odl.append((gr, odleglosc(nowy, elem)))

k = ustal_k(ilosc_elementow, len(grupa))
print("k = ", k)

odl.sort()
k_najblizszych = odl[:k]
print(k_najblizszych)

wyst = {}
for element in k_najblizszych:
    naj_grupa = element[0]
    if naj_grupa in wyst.keys():
        wyst[naj_grupa] += 1
    else:
        wyst[naj_grupa] = 1
print(wyst)

klasyfikacja = max(wyst, key=wyst.get)
print("Nowy element należy do grupy ", klasyfikacja)

print("Wejscie: ", grupa, " i ", nowy)



def klasyfikacja_knn(sklasyfikowane, nowy):
    odl = []

    ilosc_elementow = 0

    for gr, elems in sklasyfikowane.items():
        for elem in elems:
            ilosc_elementow += 1
            odl.append((gr, odleglosc(nowy, elem)))

    k = ustal_k(ilosc_elementow, len(sklasyfikowane))

    odl.sort()
    k_najblizszych = odl[:k]

    wyst = {}
    for element in k_najblizszych:
        naj_grupa = element[0]
        if naj_grupa in wyst.keys():
            wyst[naj_grupa] += 1
        else:
            wyst[naj_grupa] = 1

    sklasyfikowane[max(wyst, key=wyst.get)].append(nowy)
    return sklasyfikowane


print("Wyjscie: ", klasyfikacja_knn(grupa.copy(), nowy))
