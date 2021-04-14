import pulp
import time

# Lista krotek z wartościa i waga (objetosc) przedmiotow
przedmioty = [(11, 4), (16, 5), (8, 3), (30, 12), (15, 5), (26, 10), (53, 18)]

# liczba przedmiotów
iloscprzedmiotow = len(przedmioty)

# maksymalna pojemności plecaka
pojemnoscplecaka = 24


# Zmienne decyzyjne
#t = pulp.LpVariable.dicts('przedmiot', range(iloscprzedmiotow), cat='Binary')# to jest pierwszy podpunkt binarny



x = pulp.LpVariable.dicts('przedmiot', range(iloscprzedmiotow),lowBound = 0, cat = 'Real') # to jest podpunkt 2a



#t = pulp.LpVariable.dicts('przedmiot', range(iloscprzedmiotow),lowBound = 0,upBound = 3,  cat = 'Integer') # to jest podpunkt 3b


# Inicjujemy problem i określamy typ
problem = pulp.LpProblem("Problem_plecakowy", pulp.LpMaximize)

# dodajemy funkcje celu
problem += pulp.lpSum([x[i] * (przedmioty[i])[0] for i in range(iloscprzedmiotow)]), "Objective: Maximize profit"

# Ograniczenie wydajności: suma wag musi być mniejsza niż pojemność plecaka
problem += pulp.lpSum([x[i] * (przedmioty[i])[1] for i in range(iloscprzedmiotow)]) <= pojemnoscplecaka, "Constraint: Max capacity"

print(problem.constraints)

# rozwiazujemy problem optymalizacji
start_time = time.time()
problem.solve()
print("Rozwiazane w  czasie %s sekund." % (time.time() - start_time))

# Czy problem został rozwiązany w sposób optymalny?
print("Status:", pulp.LpStatus[problem.status])

# Kazda ze zmiennych jest wypisywana z rozwiązaną optymalną wartością
for v in problem.variables():
    print(v.name, "=", v.varValue)

# Wyswietlenie zoptymalizowanej wartości funkcji celu
print("Całkowity zysk = ", pulp.value(problem.objective))


# Wyswietlenie przedmiotow ktorych uzylismy
used_cap = 0.0
print("Uzyte przedmioty:")
for i in range(iloscprzedmiotow):
    if x[i].value() >= 1:
        print(i, przedmioty[i])
        used_cap += przedmioty[i][1]
print("Zysk: %d " % (pulp.value(problem.objective)))
