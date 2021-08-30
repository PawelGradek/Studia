

l1 = [5,10,11,13,14,21,28,31,35,37,41,42,52,54,61,63,64,67,68,79]
l2 = [1,2,15,19,20,22,25,31,34,35,37,39,43,51,58,59,61,69,73,75]
l3 = [2,4,6,8,12,18,22,23,26,31,34,35,36,40,46,47,54,63,70,80]
l4 = [1,4,7,15,16,22,33,35,37,38,45,50,51,56,64,67,70,74,75,79]
l5 = [5,6,11,12,21,27,32,43,44,45,46,48,52,59,62,65,68,76,78,80]



l16 = [l1,l2,l3,l4,l5]
l16koncowa = []
for i in l16:
    for j in i:
        if j not in l16koncowa:
            l16koncowa.append(j)

print(l16koncowa)

l0 = []
for i in range(1,81):
    l0.append(i)
print(l0)

for i in l1:
    l0.remove(i)
for j in l2:
    if j in l0:
        l0.remove(j)
print(len(l0))
print(l0)

for i in l0:
    if i not in l16koncowa:
        l0.remove(i)

print(len(l0))
print(l0)


