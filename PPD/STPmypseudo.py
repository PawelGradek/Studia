import pulp

# definiujemy TSP
miasta = 6 #całkowita liczba miast

# definiujemy macierz odległości od poszczególnych miast
dystans = [[0, 25, 67, 70, 15, 20],
           [25, 0, 30, 35, 40, 45],
           [67, 30, 0, 50, 55, 60],
           [70, 35, 50, 0, 65, 67],
           [15, 40, 55, 65, 0, 10],
           [20, 45, 60, 67, 10, 0]]


# zdefiniowanie problemu, nazwa problemu, minimalizujemy czy maksymalizujemy
problem = pulp.LpProblem('TSP', pulp.LpMinimize)

# ustawiamy zmienne Ta funkcja tworzy słownik z określonymi skojarzonymi parametrami.LpVariable,
# (i, j) - Lista ciągów kluczy do słownika zmiennych LP oraz główna część samej nazwy zmiennej
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(miasta) for j in range(miasta)), lowBound=0, upBound=1, cat='Binary')

# musimy śledzić kolejność w trasie, aby wyeliminować możliwość podtorów
u = pulp.LpVariable.dicts('u', (i for i in range(miasta)), lowBound=1, upBound=miasta, cat='Integer')

# ustawiamy funkcję celu,
# Oblicz sumę z listy wyrażeń liniowych
problem += pulp.lpSum(dystans[i][j] * x[i, j] for i in range(miasta) for j in range(miasta))

# ustawiamy ograniczenia
for i in range(miasta):
    problem += x[i, i] == 0# odległość z miasta A do miasta A musi być równa 0

for i in range(miasta):
    problem += pulp.lpSum(x[i, j] for j in range(miasta)) == 1
    problem += pulp.lpSum(x[j, i] for j in range(miasta)) == 1

# eliminujemy podtory
for i in range(miasta):
    for j in range(miasta):
        if i != j and (i != 0 and j != 0):
            problem += u[i] - u[j] <= miasta * (1 - x[i, j]) - 1

# rozwiązanie problemu
status = problem.solve()

# stan wyjścia, wartość funkcji celu
status, pulp.LpStatus[status], pulp.value(problem.objective)

#Użyj LpVariable (), aby utworzyć nowe zmienne. Aby utworzyć zmienną 0 <= x <= 3:
#x = LpVariable("x", 0, 3)
#Użyj LpProblem (), aby stworzyć nowe problemy. Utwórz „myProblem”:
#prob = LpProblem("myProblem", LpMinimize)
#Połącz zmienne, aby utworzyć wyrażenia i ograniczenia, a następnie dodaj je do problemu:
#prob += x + y <= 2
#Aby rozwiązać za pomocą domyślnego dołączonego solwera:
#status = prob.solve()


