from sklearn.neighbors import KNeighborsClassifier
from operator import itemgetter
import numpy.random as rnd
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 500
K = 10

x1 = 6 * rnd.rand(n) - 3
y1 = 6 * rnd.rand(n) - 3
z1 = 6 * rnd.rand(n) - 3

x2 = rnd.randn(n) + 15
y2 = rnd.randn(n)
z2 = rnd.randn(n)

x3 = rnd.randn(n)
y3 = rnd.randn(n) + 15
z3 = rnd.randn(n)

ax.scatter(x1, y1, z1, c='nie_padly_w_5_loso', marker='^')
ax.scatter(x2, y2, z2, c='r', marker='+')
ax.scatter(x3, y3, z3, c='k', marker='o')
ax.scatter(15, 3, 4, c='g', marker='*')

point = (15, 3, 4)
plt.show()

grupa1 = ['one'] * n
grupa2 = ['two'] * n
grupa3 = ['three'] * n

punkty1 = []
for i in (zip(x1, y1, z1)):
    punkty1.append(i)

punkty2 = []
for i in (zip(x2, y2, z2)):
    punkty2.append(i)

punkty3 = []
for i in (zip(x3, y3, z3)):
    punkty3.append(i)

dystans1 = []
dystans2 = []
dystans3 = []

for i in punkty1:
    dystans1.append(math.pow(i[0] - point[0], 2) + math.pow(i[1] - point[1], 2) + math.pow(i[2] - point[2], 2))

for i in punkty2:
    dystans2.append(math.pow(i[0] - point[0], 2) + math.pow(i[1] - point[1], 2) + math.pow(i[2] - point[2], 2))

for i in punkty3:
    dystans3.append(math.pow(i[0] - point[0], 2) + math.pow(i[1] - point[1], 2) + math.pow(i[2] - point[2], 2))

dystans_od_grupy1 = []
dystans_od_grupy2 = []
dystans_od_grupy_3 = []

for i in (zip(dystans1, grupa1)):
    dystans_od_grupy1.append(i)

for i in (zip(dystans2, grupa2)):
    dystans_od_grupy2.append(i)

for i in (zip(dystans3, grupa3)):
    dystans_od_grupy_3.append(i)

koncowy_dystans = dystans_od_grupy1 + dystans_od_grupy2 + dystans_od_grupy_3
lista_odleglosci = sorted(koncowy_dystans, key=itemgetter(0))

k_sasiadow = lista_odleglosci[:K]

listclass = []
jedynki = 0
dwojki = 0
trojki = 0

for i in k_sasiadow:
    if i[1] == 'one':
        jedynki += 1
    if i[1] == 'two':
        dwojki += 1
    if i[1] == 'three':
        trojki += 1
lista_ilosci_sasiadow_w_grupach = [jedynki, dwojki, trojki]
lista_z_max_iloscia_elem = max(lista_ilosci_sasiadow_w_grupach)
ind_max = lista_ilosci_sasiadow_w_grupach.index(lista_z_max_iloscia_elem)

if ind_max == 0:
    print('nowy element należy do pierwszej klasy')
if ind_max == 1:
    print('nowy element należy do drugiej klasy')
if ind_max == 2:
    print('nowy element należy do trzeciej klasy')


wszystkie_punkty = punkty1 + punkty2 + punkty3
wszystkie_grupy = grupa1 + grupa2 + grupa3

# grupy = class
# punkty = cords

# KNN
classifier = KNeighborsClassifier(n_neighbors=50)
classifier.fit(wszystkie_punkty, wszystkie_grupy)

predicted = classifier.predict([point])
print('KNN: ', predicted)

# SVM
from sklearn import svm
clf = svm.SVC()
clf.fit(wszystkie_punkty, wszystkie_grupy)
print('SVM: ',clf.predict([point]))

# DTC
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(wszystkie_punkty, wszystkie_grupy)
# tree.plot_tree(clf)
print('DTC: ',clf.predict([point]))

# Neural network
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier()
clf = clf.fit(wszystkie_punkty, wszystkie_grupy)
print('NN: ',clf.predict([point]))

#Enseable methods
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier

clf1 = LogisticRegression(multi_class='multinomial', random_state=1)
clf2 = RandomForestClassifier(n_estimators=30)
clf3 = GaussianNB()
clf4 = tree.DecisionTreeClassifier()
clf5 = MLPClassifier()
clf6 = KNeighborsClassifier(n_neighbors=30)
clf7 = svm.SVC()

X = wszystkie_punkty
Y = wszystkie_grupy

clf = VotingClassifier(estimators=[('lr', clf1), ('rfc', clf2), ('gmb',clf3),
                                   ('dtc', clf4),('nn',clf5), ('knn', clf6),('svc', clf7)], voting='hard')

clf = clf.fit(X, Y)
print('EM', clf.predict([point]))