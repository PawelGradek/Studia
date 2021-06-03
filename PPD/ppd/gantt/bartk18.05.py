import numpy as np
import json
from funkcje_bazowe_mutacja import TB_function_final , TB_function, swapTS,inwersja, mutacion

def showSettings():
    f = open("D:\\Python\\projekty\\PPD_Projekt_2\\settings.txt", "r")
    data = json.load(f)
    return data

def results(result, score):
    g = open("D:\\Python\\projekty\\PPD_Projekt_2\\results.txt", "w")
    raport = f'Stan algorytmu: {result}.\n' \
             f'Najlepszy wynik: {score}.\n' \
             f'Ile surowcow: {showSettings()["resources"]}.\n' \
             f'Dodatkowa optymalizacja: {showSettings()["additOpt"]}.\n' \
             f'TASKS_BASE: {showSettings()["taskBase"]}.\n' \
             f'edgeList: {showSettings()["edgeList"]}.\n'
    # json.dump(raport, g)
    g.write(raport)
    g.close()

TASKS_BASE = np.array(showSettings()['taskBase'])
edgeList = showSettings()['edgeList']

XX = []
iteracja = 1
finished = True

while iteracja < 100:
    print(f'------------------------Obecnie {iteracja}-ta iteracja')

    #mutacja rozwiązania
    TASKS_BASE_S = mutacion(TASKS_BASE.copy())

    CT_S = TB_function(TASKS_BASE_S, edgeList)
    CT = TB_function(TASKS_BASE, edgeList)
    print(f'TASKS_BASE_S:\n {TASKS_BASE_S}')
    print(f'CT: {CT} === CT_S: {CT_S}')

    if CT_S < CT:
        XX.append(TASKS_BASE_S)
        TASKS_BASE = TASKS_BASE_S.copy()
        print('Zmiana, bo mniejsze')

        if showSettings()['additOpt'] == 'True':

            TB_S_S = swapTS(TASKS_BASE_S.copy(),3 ,edgeList)
            CT_S_S = TB_function(TB_S_S, edgeList)
            print(f'---------------------------------------------CT_S: {CT_S} === CT_S_S: {CT_S_S}')
            if CT_S_S < CT_S:
                TASKS_BASE = TB_S_S.copy()
                XX.append(TB_S_S)
                print('---------------------------, jeszcze mniejsze rozwiązanie po optymalizacji lokalnej')
                TASKS_BASE = inwersja(TASKS_BASE_S.copy())
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
try:
    minCt = min(theShortestTime)
    print(f'Final CT: {minCt}')
    print(f'Ilość list zadań z takim czasem : {len(min_theShortestTime)}')
    results('success', minCt)
except ValueError:
    minCt = None
    print(f'Final CT: {minCt}')
    print('Nie znaleziono lepszego rozwiązania')
    results('failure', minCt)