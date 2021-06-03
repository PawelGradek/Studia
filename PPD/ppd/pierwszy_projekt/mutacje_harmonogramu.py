import random

# zmieniają się sąsiednie zadania
# potencjalnie można stosować cały czas
def swap_nahbar(array):
    i = int(random.uniform(1,len(array)-2))
    j = i+1
    array[[i, j]] = array[[j, i]]
    return array

# zamiana inwersyjna, im zadania są dalej od siebie tym większą drogę pokonają podczas zamiany
# można wrzucać nas do dużo gorszych rozwiązań
# bardzo agresywne przekształcenie
def inwersja(array):
    i = int(random.uniform(1,len(array)-3))
    j = i+3
    array[[i, i+1, i+2, j]] = array[[j, i+2, i+1, i]]
    return array

# zamiana ze sobą wycinków tablicy zadań
# bardzo agresywne przekształcenie
def end_end_swap(array):
    i = int(random.uniform(1,len(array)-6))
    j = i+3
    array[[i, i+1, i+2, j, j+1, j+2]] = array[[j, j+1, j+2, i, i+1, i+2]]
    return array