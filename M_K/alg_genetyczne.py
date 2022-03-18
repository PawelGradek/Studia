import random
import matplotlib.pyplot as plt

# generowanie populacji
def create_initial_populations(r, k):
    S = []
    for i in range(k):
        list_to_s = []
        for j in range(r):
            list_to_choice = [0, 1]
            choice = random.choice(list_to_choice)
            list_to_s.append(choice)
        S.append(list_to_s)

    return S

# funkcja celu
def objective_function(c, c_star):
    value_function = []
    error = 0
    for i in range(len(c)):
        if c[i] == c_star[i]:
            value_function.append(4)
        if c[i] != c_star[i]:
            value_function.append(1)
            error += 1
    finall_value = sum(value_function)

    return finall_value, error


# generowanie listy wartosci funkcji celu dla poszczegolnych osobnikow
def generate_values_of_fuc(s_lista, k, c_star):
    list_of_the_values_objective_function = []
    list_of_error_in_iteration = []
    for i in range(k):
        finall_value, error = objective_function(s_lista[i], c_star)
        list_of_the_values_objective_function.append(finall_value)
        list_of_error_in_iteration.append(error)

    return list_of_the_values_objective_function, sum(list_of_error_in_iteration)

# selekcja
# funkcja pomocnicza do selekcji
def fun_to_selection(f_n_list, f_n):
    divider = 0
    for i in range(len(f_n_list)):
        divider += f_n_list[i]
    p_n = f_n / divider
    return p_n


def selection(p_n, f_n_list, k, S, iteration):
    for i in range(len(f_n_list)):
        x1 = fun_to_selection(f_n_list, f_n_list[i])
        if i == 0:
            p_n.append([0, x1])
        if i in range(1,k):
            x2 = p_n[-1][-1]
            x3 = x2 + fun_to_selection(f_n_list, f_n_list[i])
            if i == k-1:
                x3 = int(round(x2 + fun_to_selection(f_n_list, f_n_list[i]), 1))

            p_n.append([x2, x3])

    d = []
    for i in range(k):

        d_ = random.random()
        d.append(d_)
    S_p = []
    for i in range(len(d)):
        for j in range(len(p_n)):
            if p_n[j][0] <= d[i] < p_n[j][1]:
                S_p.append(S[j])
    print(f"S'({iteration})", S_p)
    return S_p


# krzyżowanie
def genetic_crossing(pc, k, S, iteration):
    S_pp = []

    for i in range(int(k/2)):
        d = random.random()
        lista_S = S.copy()
        x = random.choice(lista_S)
        lista_S.remove(x)
        y = random.choice(lista_S)
        if d <= pc:

            crossing_point = random.randint(1, r-1)
            x_nowe = []
            y_nowe = []

            for elem in range(len(x[:crossing_point])):
                x_nowe.append(y[elem])
                y_nowe.append(x[elem])
            for elem in x[crossing_point:]:
                x_nowe.append(elem)
            for elem in y[crossing_point:]:
                y_nowe.append(elem)

            S_pp.append(x_nowe)
            S_pp.append(y_nowe)
        else:
            S_pp.append(x)
            S_pp.append(y)

    print(f'osobniki po krzyzowaniu S"({iteration})', S_pp)
    return S_pp


#mutacje
def genetic_mutations(populacja, pm, iteration):
    S_nowe = []
    for i in range(len(populacja)):
        populacjai = []
        for j in range(len(populacja[i])):

            populacja_ij = 2
            d = random.random()
            if d <= pm:
                if populacja[i][j] == 1:
                    populacja_ij = 0
                if populacja[i][j] == 0:
                    populacja_ij = 1
            if d > pm:
                populacja_ij = populacja[i][j]
            populacjai.append(populacja_ij)
        S_nowe.append(populacjai)
    S_pp = S_nowe
    print(f'osobniki po mutacjii S"({iteration})',  S_pp)
    return S_pp


def genetic_algorithm(k, c_star, S, iteration):
    print(f'S({iteration}) ', S)
    f_n_list, error = generate_values_of_fuc(S, k, c_star)
    print(f'Ocena osobników: S({iteration}) ', f_n_list)
    p_n = []
    S_p = selection(p_n, f_n_list, k, S, iteration)
    f_n_list_S_p, error = generate_values_of_fuc(S_p, k, c_star)
    print(f"Ocena osobników S'({iteration})",f_n_list_S_p)

    S_pp = genetic_crossing(pc, k, S_p, iteration)
    S_pp = genetic_mutations(S_pp, pm, iteration)
    f_n_list_S_pp, error = generate_values_of_fuc(S_pp, k, c_star)
    print(f'Ocena osobników S"({iteration})', f_n_list_S_pp)
    return S_pp


c_star = [1, 0, 0, 1, 1, 0, 0, 1]
r = 8
k = 10
epsilon = 4
pc = 0.8 # parametr zwany prawdopodobieństwem krzyżowania
pm = 0.05 # prawdopodobienstwo mutacjii
iterations = [0]
number_of_iterations = 10
# c_star = []
# print('Wprowadz wartości [0] , [1] lub [2]-obojetne dla kolejnych genow c*: ')
# for i in range(r):
#     x = int(input(f'c*({i+1}): '))
#     c_star.append(x)
S = create_initial_populations(r, k)


def run_alg(epsilon, k, c_star, S, iterations, number_of_iterations):
    flag = True
    list_of_error = []
    list_of_error2 = []
    list_of_average = []
    iteration = iterations[-1]
    iterations.append(iteration)
    print('Iteracja numer:', iteration)
    S_pp = genetic_algorithm(k, c_star, S, iteration)
    rate_population, error = generate_values_of_fuc(S_pp, k, c_star)
    list_of_average.append(sum(rate_population) / k) # liczymy średnią ocen całeł populacji
    list_of_error.append(error)
    list_of_error2.append(error)
    while flag:
        iteration += 1
        iterations.append(iteration)
        print('Iteracja numer:', iteration)
        S_pp = genetic_algorithm(k, c_star, S_pp, iteration)
        rate_population, error = generate_values_of_fuc(S_pp, k, c_star)
        list_of_average.append(sum(rate_population) / k)
        list_of_scores = []
        list_of_error.append(error)
        list_of_error2.append(error)

        if len(list_of_error) == number_of_iterations:
            for i in range(len(list_of_error[:-1])):
                if abs(list_of_error[i]-list_of_error[i+1]) >= epsilon:
                    list_of_scores.append(1)
            if sum(list_of_scores) == 0:
                # iteration += 1
                # iterations.append(iteration)
                print('STOP')
                print(f'S({iteration+1})', S_pp)
                # rate_population, error = generate_values_of_fuc(S_pp, k, c_star)
                # list_of_average.append(sum(rate_population) / k)
                # list_of_error.append(error)
                # list_of_error2.append(error)
                flag = False
                print('lista bledów:',list_of_error)

                print('c star', c_star)
            else:
                del list_of_error[0]
    return iterations, list_of_error2



iterations, error = run_alg(epsilon, k, c_star, S, iterations, number_of_iterations)
iterations_for_plot = iterations[1:]
plt.figure(figsize=(10, 6))
plt.plot(iterations_for_plot, error)
plt.grid(True)
plt.xlabel("Liczba iteracji")
plt.ylabel("Liczba przeciwnych wartości genów do genów c* w całej populacji")
plt.title(f"Liczba przeciwnych wartość do c* w populacjach w kolejnych iteracjach")
plt.show()