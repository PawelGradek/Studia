import random
import numpy as np
from funkcje_bazowe import TB_function_final , TB_function, swap
from math import e , pow
from mutacje_harmonogramu import end_end_swap, inwersja, swap_nahbar

TASKS_BASE = np.array([[1,1,7],[2,1,5],[3,4,7],[4,1,6],[5,1,5],[6,7,4],[7,2,6],[8,1,7],[9,3,5],[10,3,1],[11,4,1],[12,4,7],[13,2,3],[14,7,6],[15,5,6]])
edgeList = [[1,2],[1,3], [2,4], [2,5], [3,6], [4,7], [4,8], [5,9], [6,9], [7,10], [7,11], [7,12], [8,13], [9,13], [10,15], [11,15], [12,14], [13,14], [14,15]]

# temperatura zmiejsza się liniowo
T0 = 1
Tk = 0.001
N = 100
XX = []
iteracja = 1
T = T0
alfa = (T0 - Tk) / N
while T > Tk:

    if iteracja > 100:
        break

    print(f'------------------------Obecnie {iteracja}-ta iteracja')
    CT = TB_function(TASKS_BASE, edgeList)

    mutacja = random.choice([1,2,3,4,5,6,7,8,9,10])
    if mutacja == 1 or mutacja == 10 :
        TASKS_BASE_S = end_end_swap(TASKS_BASE)
    if mutacja == 2 or mutacja == 9 or mutacja == 6:
        TASKS_BASE_S = inwersja(TASKS_BASE)
    if mutacja == 4:
        TASKS_BASE_S = swap_nahbar(TASKS_BASE)
    else:
        TASKS_BASE_S = swap(TASKS_BASE)

    CT_S = TB_function(TASKS_BASE_S, edgeList)
    print(f'TASKS_BASE_S:\n {TASKS_BASE_S}')
    print(f'T: {T}')
    print(f'CT: {CT} === CT_S: {CT_S}')

    try:
        powToCompare = round(pow(e, (CT - CT_S) / T))
    except OverflowError:
        powToCompare = 0.000000001

    if CT_S < CT:
        print('Zmiana, bo mniejsze')
        TASKS_BASE = TASKS_BASE_S
        XX.append(TASKS_BASE.copy())
    elif powToCompare > random.uniform(0, 1):
        TASKS_BASE = TASKS_BASE_S
        print('Zmiana, bo potega')
    T = T - alfa
    iteracja += 1
    print()

print('\n\n----------SCORES----------------\n')

theShortestTime = []
min_theShortestTime = []
for elem in XX:
    theShortestTime.append(TB_function(elem, edgeList))
    if TB_function(elem, edgeList) == min(theShortestTime):
        # TB_function_final(elem, edgeList)
        # print('==================================================================================')
        min_theShortestTime.append(elem)
print(f'Final CT: {min(theShortestTime)}')
print(f'Ilość list zadań z takim czasem : {len(min_theShortestTime)}')
