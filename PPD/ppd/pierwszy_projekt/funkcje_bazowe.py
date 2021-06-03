import random
import numpy as np
from itertools import permutations

def check(task, allowedEdges):
    if task > 1:
        for elem in allowedEdges:
            if task in elem:
                return True
        return False
    else:
        return True

def TB_function_final(TASKS_BASE, edgeList):
    resources = 7
    currentTime = 0
    progressList = []
    doneList = []
    orderList = list(TASKS_BASE[:, 0])
    lenOrderList = len(orderList.copy())
    allowedEdges = []
    while (len(doneList) != lenOrderList):
        if currentTime > 100:
            print('-'*100 + ' Minęło za dużo czasu')
            break
        print(f'-------CurrentTime => {currentTime}')
        print(f'len(orderList): {len(orderList)}')
        if len(progressList) > 0:
            print(f'Before progressList: {progressList}')
            for elem in range(len(progressList)):
                progressList[elem][1] -= 1
            for index in range(len(progressList)-1, -1, -1):
                if progressList[index][1] == 0:
                    print(f'Czas minal dla: {progressList[index]}')
                    appendedTask = progressList[index][0]
                    doneList.append(appendedTask)

                    for i in range(appendedTask + 1, len(TASKS_BASE) + 1):
                        if [appendedTask, i] in edgeList:
                            allowedEdges.append([appendedTask, i])

                    resources += progressList[index][2]
                    progressList.pop(index)

        print(f'After progressList: {progressList}')
        if len(orderList) > 0:
            print(f'resources: {resources}')
            for listNumber in orderList:
                if TASKS_BASE[listNumber - 1][2] <= resources and check(listNumber, allowedEdges):
                    print(f'Dodaje: {TASKS_BASE[listNumber - 1]}')
                    resources -= TASKS_BASE[listNumber - 1][2]
                    orderList.remove(listNumber)
                    progressList.append(list(TASKS_BASE[listNumber - 1]))
                    currentTime += 1
                    print(f'progressList: {progressList}\n')
                    break
        currentTime += 1
        print('koniec iteracji\n')
    CT = currentTime+1
    # print(f'Final orderList: {orderList}')
    return CT


def TB_function(TASKS_BASE, edgeList):
    resources = 7
    currentTime = 0
    progressList = []
    doneList = []
    orderList = list(TASKS_BASE[:, 0])
    lenOrderList = len(orderList.copy())
    allowedEdges = []
    while (len(doneList) != lenOrderList):
        if currentTime > 100:
            print('-'*100 + ' Minęło za dużo czasu')
            break
        if len(progressList) > 0:
            for elem in range(len(progressList)):
                progressList[elem][1] -= 1
            for index in range(len(progressList)-1, -1, -1):
                if progressList[index][1] == 0:
                    appendedTask = progressList[index][0]
                    doneList.append(appendedTask)

                    for i in range(appendedTask + 1, len(TASKS_BASE) + 1):
                        if [appendedTask, i] in edgeList:
                            allowedEdges.append([appendedTask, i])

                    resources += progressList[index][2]
                    progressList.pop(index)

        if len(orderList) > 0:
            for listNumber in orderList:
                if TASKS_BASE[listNumber - 1][2] <= resources and check(listNumber, allowedEdges):
                    resources -= TASKS_BASE[listNumber - 1][2]
                    orderList.remove(listNumber)
                    progressList.append(list(TASKS_BASE[listNumber - 1]))
                    currentTime += 1
                    break
        currentTime += 1
    CT = currentTime+1
    return CT

def swap(array):
    i = int(random.uniform(1,len(array)-1))
    j = int(random.uniform(1,len(array)-1))
    if i==j:
        swap(array)
    array[[i, j]] = array[[j, i]]
    return array

def swapTS(array, size, edgeList):
    start = random.randint(0, len(array)-size)
    output = array[start:start+size]
    outputIndex = output[:,0]
    perm = permutations(outputIndex)
    outputDataBase = []
    for permElem in perm:
        partOutputDataBase = []
        for elem in permElem:
            for arrayElem in array:
                if elem == arrayElem[0]:
                    partOutputDataBase.append(arrayElem)
                    break
        outputDataBase.append(np.array(partOutputDataBase))

    ctConcatenates = {}
    for outputElem in outputDataBase:
        concatenate = []
        if array[0:start] is not [] and array[start+size:] is not []:
            concatenate = np.concatenate((array[0:start], outputElem, array[start+size:]), axis=0)
        elif array[0:start] == []:
            concatenate = np.concatenate((concatenate, array[start+size:]), axis=0)
        elif array[start+size:] == []:
            concatenate = np.concatenate((array[0:start], concatenate), axis=0)
        # print(concatenate)
        currentCt = TB_function(concatenate, edgeList)
        ctConcatenates[currentCt] = concatenate

    # print()
    # for dane in ctConcatenates:
    #     print(f'dane: {dane}\nvalue:\n{ctConcatenates[dane]}')
    print(f'To: {TB_function(ctConcatenates[min(ctConcatenates.keys())], edgeList)}')
    return ctConcatenates[min(ctConcatenates.keys())]

# TASKS_BASE = np.array([[1,2,3],[2,3,2],[3,3,3],[4,2,4],[5,3,3],[6,3,4],[7,2,5],[8,1,6]])
# edgeList = [[1,2],[1,3],[1,4],[1,6],[2,4],[2,7],[2,8],[3,5],[3,6],[3,8],[4,6],[5,6],[4,7],[6,7],[7,8]]
TASKS_BASE = np.array([[1,1,7],[2,1,5],[3,4,7],[4,1,6],[5,1,5],[6,7,4],[7,2,6],[8,1,7],[9,3,5],[10,3,1],[11,4,1],[12,4,7],[13,2,3],[14,7,6],[15,5,6]])
edgeList = [[1,2],[1,3], [2,4], [2,5], [3,6], [4,7], [4,8], [5,9], [6,9], [7,10], [7,11], [7,12], [8,13], [9,13], [10,15], [11,15], [12,14], [13,14], [14,15]]
# # print(swapTS(TASKS_BASE, 3, edgeList))
# TB_function(TASKS_BASE, edgeList)

if TASKS_BASE.tolist().copy() not in []:
    print('dupa')


