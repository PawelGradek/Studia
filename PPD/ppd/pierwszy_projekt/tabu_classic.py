import random
import numpy as np
from funkcje_bazowe import TB_function_final , TB_function, swap, swapTS

TASKS_BASE = np.array([[1,1,7],[2,1,5],[3,4,7],[4,1,6],[5,1,5],[6,7,4],[7,2,6],[8,1,7],[9,3,5],[10,3,1],[11,4,1],[12,4,7],[13,2,3],[14,7,6],[15,5,6]])
edgeList = [[1,2],[1,3], [2,4], [2,5], [3,6], [4,7], [4,8], [5,9], [6,9], [7,10], [7,11], [7,12], [8,13], [9,13], [10,15], [11,15], [12,14], [13,14], [14,15]]

orderList = list(TASKS_BASE[:,0])

TabuList = []
XX = []
iteracja = 1
T = 0
Tk = 100
while T < Tk:

    print(f'Obecnie {T}-ta iteracja')

    CT = TB_function(TASKS_BASE, edgeList)

    TASKS_BASE_S = swapTS(TASKS_BASE, 3, edgeList)
    # while TASKS_BASE_S in TabuList:
    #     print('--------------------------------------------------------Swapujemy')
    #     TASKS_BASE_S = swapTS(TASKS_BASE, 3, edgeList)

    CT_S = TB_function(TASKS_BASE_S, edgeList)
    print(f'TASKS_BASE_S:\n {TASKS_BASE_S}')
    print(f'CT: {CT} === CT_S: {CT_S}')
    print(TabuList)

    if (TASKS_BASE_S.tolist().copy() not in TabuList):
        print(TASKS_BASE_S.tolist().copy() not in TabuList)

    if CT_S <= CT and (TASKS_BASE_S.tolist().copy() not in TabuList):
    # if (CT_S <= CT) and (TASKS_BASE_S.tolist().copy() not in TabuList):
        XX.append(TASKS_BASE_S.copy())
        # if TASKS_BASE_S.copy() not in TabuList:
        TabuList.append(TASKS_BASE_S.tolist())
        TASKS_BASE = TASKS_BASE_S
    print(f'Tabulist przed popem {TabuList}')
    if len(TabuList) > 3:
        TabuList.remove(TabuList[0])
    print(f'Tabulist po zmianach {TabuList}')
    T += 1
    print()

print('\n\n----------SCORES----------------\n')
theShortestTime = []
min_theShortestTime = []
for elem in XX:
    theShortestTime.append(TB_function(elem, edgeList))
    if TB_function(elem, edgeList) == min(theShortestTime):
        TB_function_final(elem, edgeList)
        print('==================================================================================')
        min_theShortestTime.append(elem)
print(f'Final CT: {min(theShortestTime)}')
print(f'Ilość list zadań z takim czasem : {len(min_theShortestTime)}')