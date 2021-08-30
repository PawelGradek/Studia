from operator import itemgetter

import numpy.random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt, ceil
import math
from sklearn.neighbors import KNeighborsClassifier

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


wszystkie_punkty = []
wszystkie_grupy = []

wszystkie_punkty = punkty1 + punkty2 + punkty3
wszystkie_grupy = grupa1 + grupa2 + grupa3


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

from sklearn import cross_validation
clf = svm.SVC(kernel='linear', C=1)
scores = cross_validation.cross_val_score(clf, X, y, cv=10)

print( "Wyniki dla każdego podzbioru: ")
print( scores)

predicted = cross_validation.cross_val_predict(clf, X, y, cv=10)
print( "Średnia sprawność klasyfikatora")
print(metrics.accuracy_score(iris.target, predicted))
