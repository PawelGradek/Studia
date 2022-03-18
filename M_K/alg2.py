import random
import numpy as np

# generowanie nowej populacji
def create_initial_populations(r, k):
    S_0 = []
    for i in range(k):
        list_to_s_0 = []
        for j in range(r):
            list_to_choice = [0, 1]
            choice = random.choice(list_to_choice)
            list_to_s_0.append(choice)
        S_0.append(list_to_s_0)

    return S_0

# funkcja celu
def objective_function(c, c_star):
    value_function = []
    for i in range(len(c)):
        if c[i] == c_star[i]:
            value_function.append(4)
        if c[i] != c_star[i]:
            value_function.append(1)
    finall_value = sum(value_function)
    return finall_value


# generowanie listy wartosci funkcji celu dla poszczegolnych osobnikow
def generate_values_of_fuc(s_0_lista, k, c_star):
    list_of_the_values_objective_function = []
    for i in range(k):
        list_of_the_values_objective_function.append(objective_function(s_0_lista[i], c_star))
    return list_of_the_values_objective_function

# selekcja
# funkcja pomocnicza do selekcji
def fun_to_selection(f_n_list, f_n_i, k):
    divider = 0
    for i in range(len(f_n_list)):
        divider += f_n_list[i]
    p_n = f_n_i / divider
    return p_n


def selection(p_c, f_n_list, k, S):
    for i in range(len(f_n_list)):
        x1 = fun_to_selection(f_n_list, f_n_list[i], k)
        if i == 0:
            p_c.append([0, x1])
        else:
            x2 = p_c[-1][-1]
            if i == k-1:
                x3 = int(round(x2 + fun_to_selection(f_n_list, f_n_list[i], k),1))
            else:
                x3 = x2 + fun_to_selection(f_n_list, f_n_list[i], k)
            p_c.append([x2,x3])
    # print('p(c) ', p_c)
    d = []
    for i in range(k):
        maximum = 1
        minimum = 0
        ra = random.random() * (maximum - minimum) + minimum
        d.append(ra)
    # print('d ', d)
    S_prim = []
    for i in range(len(d)):
        for j in range(len(p_c)):
            if p_c[j][0] < d[i] < p_c[j][1]:
                S_prim.append(S[j])
    print("S'", S_prim)
    return S_prim


# krzyżowanie
def genetic_crossing(pc, k, S):
    S_pp = []

    for i in range(int(k/2)):
        maximum = 1
        minimum = 0
        d = random.random() * (maximum - minimum) + minimum
        lista_S = S.copy()
        x = random.choice(lista_S)
        lista_S.remove(x)
        y = random.choice(lista_S)
        if d <= pc: # to osobniki są poddawane krzyżowaniu

            crossing_point = random.randint(1, r-1) # tyle ile wynosi punkt krzyżowania tyle zmieniamy genów w chromosomie, zmieniając od początku
            for elem in range(len(x[:crossing_point])):
                z1 = x[elem]
                z2 = y[elem]
                x[elem] = z2
                y[elem] = z1
            S_pp.append(x)
            S_pp.append(y)
        else:
            S_pp.append(x)
            S_pp.append(y)

    print('osobniki po krzyzowaniu S"', S_pp)
    return S_pp


#mutacje
def genetic_mutations(S_pp, pm):
    for i in range(len(S_pp)):
        for j in range(len(S_pp[i])):
            maximum = 1
            minimum = 0
            d = random.random() * (maximum - minimum) + minimum
            if d <= pm:
                if S_pp[i][j] == 1:
                    S_pp[i][j] = 0
                else:
                    S_pp[i][j] = 1
    print('osbniki po mutacjii',S_pp)
    return S_pp

c_star = [1, 0, 0, 0, 0, 0, 0, 1]
r = 8
k = 10
epsilon = 1
pc = 0.4 # parametr zwany prawdopodobieństwem krzyżowania
pm = 0.06 # prawdopodobienstwo mutacjii
iteration = 0
number_of_iterations = 10
# c_star = []
# print('Wprowadz wartości [0] , [1] lub [2]-obojetne dla kolejnych genow c*: ')
# for i in range(r):
#     x = int(input(f'c*({i+1}): '))
#     c_star.append(x)

def genetic_algorithm(epsilon, r, k, c_star, S, iteration, number_of_iterations):
    print('Iteracja numer:', iteration)
    print(f'S({iteration})', S)
    iteration += 1
    list_of_the_values_objective_function = generate_values_of_fuc(S, k, c_star)
    min_value = min(list_of_the_values_objective_function)
    max_value = max(list_of_the_values_objective_function)
    if max_value - min_value <= epsilon:
        print('Ocena ostatniej populacji: ', list_of_the_values_objective_function)
        print('STOP')
        # print(list_of_the_values_objective_function)
        print('c star', c_star)
    else:
        f_n_list = generate_values_of_fuc(S, k, c_star)
        print('Ocena osbników:  ', f_n_list)
        p_c = []
        S_p = selection(p_c, f_n_list, k, S)
        f_n_list_S_prim = generate_values_of_fuc(S_p, k, c_star)
        print('Ocena osobnikow prim',f_n_list_S_prim)

        S_pp = genetic_crossing(pc, k, S_p)
        S_pp = genetic_mutations(S_pp, pm)
        genetic_algorithm(epsilon, r, k, c_star, S_pp, iteration, number_of_iterations)

S = create_initial_populations(r, k)
genetic_algorithm(epsilon, r, k, c_star, S, iteration, number_of_iterations)
