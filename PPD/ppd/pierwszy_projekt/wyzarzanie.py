import random
import numpy as np
from funkcje_bazowe_old import TB_function_final , TB_function, swap
from math import e , pow
TASKS_BASE = np.array([[1,2,3],[2,3,2],[3,3,3],[4,2,4],[5,3,3],[6,3,4],[7,2,5],[8,1,6]])
orderList = list(TASKS_BASE[:,0])

T0 = 1
Tk = 0.001
N = 5000
XX = []
iteracja = 1
T = T0
while T > Tk:

    print(f'Obecnie {iteracja}-ta iteracja')
    CT = TB_function(TASKS_BASE)

    TASKS_BASE_S = swap(TASKS_BASE)

    CT_S = TB_function(TASKS_BASE_S)
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
    elif powToCompare > random.uniform(0, 0.5):
        TASKS_BASE = TASKS_BASE_S
        print('Zmiana, bo potega')
    alfa = (T0 - Tk) / (N * T0 * Tk)
    T = T / (1 + alfa + T)
    iteracja += 1
    print()

print('\n\n----------SCORES----------------\n')
theShortestTime = []
for elem in XX:
    theShortestTime.append(TB_function(elem))
    if TB_function(elem) == min(theShortestTime):
        TB_function_final(elem)
        print('==================================================================================')
print(f'Final CT: {min(theShortestTime)}')



