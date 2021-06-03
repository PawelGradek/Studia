import random
import numpy as np
from itertools import permutations
import json
import matplotlib.pyplot as plt


def showSettings():
    f = open("C:\\Users\\Lenovo\\Desktop\\settings.txt", "r")
    data = json.load(f)
    return data


def check(task, allowedEdges):
    if task > 1:
        for elem in allowedEdges:
            if task in elem:
                return True
        return False
    else:
        return True


def TB_function_final(TASKS_BASE, edgeList):
    resources = showSettings()['resources']
    currentTime = 0
    progressList = []
    doneList = []
    orderList = list(TASKS_BASE[:, 0])
    lenOrderList = len(orderList.copy())
    allowedEdges = []
    dictTaskAndTime = {}
    listTaskandTime = []
    listTaskandTime2 = []
    lista_z_numerami_zadan = []
    while (len(doneList) != lenOrderList):
        if currentTime > 100:
            print('-' * 100 + ' Minęło za dużo czasu')
            break
        print(f'-------CurrentTime => {currentTime}')
        print(f'len(orderList): {len(orderList)}')
        if len(progressList) > 0:
            print(f'Before progressList: {progressList}')
            for elem in range(len(progressList)):
                progressList[elem][1] -= 1
            for index in range(len(progressList) - 1, -1, -1):
                if progressList[index][1] == 0:
                    print(f'Czas minal dla: {progressList[index]}')
                    appendedTask = progressList[index][0]
                    listTaskandTime.append(currentTime)
                    # print('--------------------------------------------------------------------------------',
                    #       listTaskandTime)
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
                    # dictTaskAndTime[listNumber][0] = currentTime
                    listTaskandTime2.append(currentTime)
                    # print('******' * 10, listTaskandTime2)
                    # dodajemy currentTime na [0]
                    lista_z_numerami_zadan.append(listNumber)
                    progressList.append(list(TASKS_BASE[listNumber - 1]))
                    currentTime += 1
                    print(f'progressList: {progressList}\n')
                    break
        currentTime += 1
        print('koniec iteracji\n')

    listazadan = []
    for i in range(len(listTaskandTime2)):
        listazadan.append([listTaskandTime2[i], listTaskandTime[i]])
    # print(listazadan)
    for j in range(len(listTaskandTime2)):
        dictTaskAndTime[j] = listazadan[j]
    # print('słownik1:', dictTaskAndTime)


    CT = currentTime + 1
    # print(f'Final orderList: {orderList}')
    return CT, listazadan, lista_z_numerami_zadan


taskbase = np.array(
    [[1, 1, 7], [2, 1, 5], [3, 4, 7], [4, 1, 6], [5, 1, 5], [6, 7, 4], [7, 2, 6], [8, 1, 7], [9, 3, 5], [10, 3, 1],
     [11, 4, 1], [12, 4, 7], [13, 2, 3], [14, 7, 6], [15, 5, 6]])
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [4, 7], [4, 8], [5, 9], [6, 9], [7, 10], [7, 11], [7, 12], [8, 13],
         [9, 13], [10, 15], [11, 15], [12, 14], [13, 14], [14, 15]]

TB_function_final(taskbase, edges)


def visualisation(taskbase, edges):
    CT, listazadan, lista_z_numerami_zadan = TB_function_final(taskbase, edges)
    fig, gnt = plt.subplots()

    gnt.set_xlabel('Czas')
    gnt.set_ylabel('Numer zadania')

    gnt.set_yticks([(i + 0.25) for i in range(len(listazadan))])
    gnt.set_yticklabels([f'{i} ' for i in lista_z_numerami_zadan])

    gnt.grid(True)

    for i in range(len(listazadan)):
        gnt.broken_barh([(listazadan[i][0], listazadan[i][1] - listazadan[i][0])], (i, 0.5), facecolors=('tab:orange'))
        gnt.text(x=(listazadan[i][0] + (listazadan[i][1] - listazadan[i][0]) / 2), y=(i + 0.22),
                 s=f"{lista_z_numerami_zadan[i]}", va='center', ha='center', color='black')

    plt.show()

visualisation(taskbase, edges)

def TB_function(TASKS_BASE, edgeList):
    resources = showSettings()['resources']
    currentTime = 0
    progressList = []
    doneList = []
    orderList = list(TASKS_BASE[:, 0])
    lenOrderList = len(orderList.copy())
    allowedEdges = []
    while (len(doneList) != lenOrderList):
        if currentTime > 100:
            print('-' * 100 + ' Minęło za dużo czasu')
            break
        if len(progressList) > 0:
            for elem in range(len(progressList)):
                progressList[elem][1] -= 1
            for index in range(len(progressList) - 1, -1, -1):
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
    CT = currentTime + 1
    return CT


def swap(array):
    i = int(random.uniform(1, len(array) - 1))
    j = int(random.uniform(1, len(array) - 1))
    if i == j:
        swap(array)
    array[[i, j]] = array[[j, i]]
    return array


def swapTS(array, size, edgeList):
    start = random.randint(0, len(array) - size)
    output = array[start:start + size]
    outputIndex = output[:, 0]
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
        if array[0:start] is not [] and array[start + size:] is not []:
            concatenate = np.concatenate((array[0:start], outputElem, array[start + size:]), axis=0)
        elif array[0:start] == []:
            concatenate = np.concatenate((concatenate, array[start + size:]), axis=0)
        elif array[start + size:] == []:
            concatenate = np.concatenate((array[0:start], concatenate), axis=0)
        # print(concatenate)
        currentCt = TB_function(concatenate, edgeList)
        ctConcatenates[currentCt] = concatenate
    print(f'To: {TB_function(ctConcatenates[min(ctConcatenates.keys())], edgeList)}')
    return ctConcatenates[min(ctConcatenates.keys())]


# def swap_nahbar(array):
#     i = int(random.uniform(1,len(array)-3))
#     j = i+1
#     array[[i, j]] = array[[j, i]]
#     return array

def inwersja(array):
    i = int(random.uniform(1, len(array) - 4))
    array[[i, i + 1, i + 2, i + 3]] = array[[i + 3, i + 2, i + 1, i]]
    return array


def end_end_swap(array):
    i = int(random.uniform(1, len(array) - 7))
    j = i + 3
    array[[i, i + 1, i + 2, j, j + 1, j + 2]] = array[[j, j + 1, j + 2, i, i + 1, i + 2]]
    return array


def mutacion(array):
    i = int(random.uniform(1, len(array) - 3))
    j = i + 1
    array[[i, j]] = array[[j, i]]

    i = int(random.uniform(1, len(array) - 4))
    j = i + 3
    array[[i, i + 1, i + 2, j]] = array[[j, i + 2, i + 1, i]]

    return array
