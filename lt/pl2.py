import itertools as it
import random

l1 = [5,10,11,13,14,21,28,31,35,37,41,42,52,54,61,63,64,67,68,79]
l2 = [1,2,15,19,20,22,25,31,34,35,37,39,43,51,58,59,61,69,73,75]

l0 = []
for i in range(1,81):
    l0.append(i)
print(l0)

ll = [l1,l2]
lnowa = []
for i in ll:
    for j in i:
        if j not in lnowa:
            lnowa.append(j)
print(len(lnowa))
print(lnowa)


print(random.choice(lnowa))
# result = it.permutations(lnowa[:-20], r=8)
# print(list(result))

kombinacje = []
for i in range(7):
    pass