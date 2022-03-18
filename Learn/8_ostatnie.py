from random import random
from math import exp
import json
import matplotlib.pyplot as plt


file_1 = open('simulation_results', "r")
data = json.load(file_1)
file_1.close()

file_2 = open('simulation_results2', "r")
data2 = json.load(file_2)
file_2.close()

file_3 = open('train_set', "r")
data_3 = json.load(file_3)
train_dataset = data_3["train_set"]
file_3.close()

w = {
    'w1': [random()-0.5 for _ in range(7)],
    'w2': [random()-0.5 for _ in range(7)],
    'w3': [random()-0.5 for _ in range(7)],
    'w4': [random()-0.5 for _ in range(7)],
    'w5': [random()-0.5 for _ in range(7)],

    'w6': [random()-0.5 for _ in range(5)],
    'w7': [random()-0.5 for _ in range(5)],
    'w8': [random()-0.5 for _ in range(5)],


    'w10': [random()-0.5],
    'w20': [random()-0.5],
    'w30': [random()-0.5],
    'w40': [random()-0.5],
    'w50': [random()-0.5],

    'w60': [random()-0.5],
    'w70': [random()-0.5],
    'w80': [random()-0.5]
}

v = {
    'v1': [],
    'v2': [],
    'v3': [],
    'v4': [],
    'v5': []
}

y = {
    'y1': [],
    'y2': [],
    'y3': []
}
all_gradients = {}

error = {
    'error': []
}


def activate(weights, inputs):
    s = 0
    for i in range(len(weights)):
        s += weights[i] * inputs[i]
    return s


def sigmoid(s, beta):
    return 1.0 / (1.0 + exp(-s * beta))


def forward_propagate(all_weights, row, beta):
    x = row
    b = [1]
    v['v1'] = activate(all_weights['w1'], x[:-1])
    v['v1'] += activate(all_weights['w10'], b)
    v['v1'] = sigmoid(v['v1'], beta)

    v['v2'] = activate(all_weights['w2'], x[:-1])
    v['v2'] += activate(all_weights['w20'], b)
    v['v2'] = sigmoid(v['v2'], beta)

    v['v3'] = activate(all_weights['w3'], x[:-1])
    v['v3'] += activate(all_weights['w30'], b)
    v['v3'] = sigmoid(v['v3'], beta)

    v['v4'] = activate(all_weights['w4'], x[:-1])
    v['v4'] += activate(all_weights['w40'], b)
    v['v4'] = sigmoid(v['v4'], beta)

    v['v5'] = activate(all_weights['w5'], x[:-1])
    v['v5'] += activate(all_weights['w50'], b)
    v['v5'] = sigmoid(v['v5'], beta)

    y['y1'] = activate(all_weights['w6'], [v['v1'], v['v2'], v['v3'],v['v4'], v['v5']])
    y['y1'] += activate(all_weights['w60'], b)
    y['y1'] = sigmoid(y['y1'], beta)

    y['y2'] = activate(all_weights['w7'],[v['v1'], v['v2'], v['v3'], v['v4'], v['v5']])
    y['y2'] += activate(all_weights['w70'], b)
    y['y2'] = sigmoid(y['y2'], beta)

    y['y3'] = activate(all_weights['w8'],[v['v1'], v['v2'], v['v3'], v['v4'], v['v5']])
    y['y3'] += activate(all_weights['w80'], b)
    y['y3'] = sigmoid(y['y3'], beta)

    y_ = [y['y1'], y['y2'], y['y3']]
    v_ = [v['v1'],v['v2'],v['v3'],v['v4'],v['v5']]
    return v_, y_


def sigmoid_derivative(f_s, beta):
    return beta * f_s * (1.0 - f_s)


def backward_propagate(d, beta, x, error, iterations,v,y):
    # liczenie gradientów dla warstwy ukryto-wyjsciowej
    iterations.append((iterations[-1] + 1))
    data["liczba_iteracji"] = iterations[-1]
    e = 0.0
    for j in range(len(y)):
        e += (d[j]-y[j]) ** 2
        gradient_vy_list = []
        gradient_vy_bias = []
        for k in v:
            gradient_vy_list.append(-(d[j]-y[j])*sigmoid_derivative(y[j], beta) * k)
        gradient_vy_bias.append(-(d[j]-y[j])*sigmoid_derivative(y[j], beta) * 1)
        all_gradients[f'g{j+6}'] = gradient_vy_list
        all_gradients[f'g{j*10+60}'] = gradient_vy_bias
    e = 0.5 * e
    e = round(e,4)

    error['error'].append(e)
    data["wartosc_bledu_w_poszczegolnych_iteracjach"] = error['error']

    # wagi warstwy ukryto-wyjsciowej
    weights_v_y = [w['w6'], w['w7'], w['w8']]

    # liczenie gradientów dla warstwy wejsciowo-ukrytej
    for i in range(len(v)):
        gradient_xv_list = []
        gradient_xv_bias_list = []
        for j in range(len(x)):
            gradient_xv = 0
            for m in range(len(y)):
                gradient_xv += -(d[m]-y[m])*sigmoid_derivative(y[m], beta) * weights_v_y[m][i]
            gradient_xv = gradient_xv*sigmoid_derivative(v[i], beta)*x[j]
            gradient_xv_bias = gradient_xv*sigmoid_derivative(v[i], beta)*1
            gradient_xv_list.append(gradient_xv)
            gradient_xv_bias_list.append(gradient_xv_bias)
        all_gradients[f'g{i + 1}'] = gradient_xv_list
        all_gradients[f'g{i * 10 + 10}'] = gradient_xv_bias_list


def update_weight(all_weights, gamma, all_gradients):
    # listy do aktualizacji wag wejsciowo-ukrytych
    weights_updat_vy = [all_weights['w6'], all_weights['w7'], all_weights['w8']]
    weights_updat_bias_vy = [all_weights['w60'], all_weights['w70'], all_weights['w80']]

    gradients_vy = [all_gradients['g6'], all_gradients['g7'], all_gradients['g8']]
    gradients_bias_vy = [all_gradients['g60'], all_gradients['g70'], all_gradients['g80']]

    # aktualizacja wag ukryto-wyjsciowych
    for i in range(len(weights_updat_vy)):
        for j in range(len(weights_updat_vy[i])):
            weights_updat_vy[i][j] = weights_updat_vy[i][j] - gamma * gradients_vy[i][j]
            weights_updat_vy[i][j] = round(weights_updat_vy[i][j],4)

    # aktualizacja wag ukryto-wyjsciowych bias
    for i in range(len(weights_updat_bias_vy)):
        for j in range(len(weights_updat_bias_vy[i])):
            weights_updat_bias_vy[i][j] = weights_updat_bias_vy[i][j] - gamma * gradients_bias_vy[i][j]
            weights_updat_bias_vy[i][j] = round(weights_updat_bias_vy[i][j], 4)

    # listy do aktualizacji wag wejsciowo-ukrytych
    weights_updat_xv = [all_weights['w1'], all_weights['w2'], all_weights['w3'], all_weights['w4'], all_weights['w5']]
    weights_updat_bias_xv = [all_weights['w10'], all_weights['w20'], all_weights['w30'], all_weights['w40'], all_weights['w50']]

    gradients_xv = [all_gradients['g1'], all_gradients['g2'], all_gradients['g3'], all_gradients['g4'], all_gradients['g5']]
    gradients_bias_xv = [all_gradients['g10'], all_gradients['g20'], all_gradients['g30'], all_gradients['g40'], all_gradients['g50']]

    # aktualizacja wag wejsciowo-ukrytych
    for i in range(len(weights_updat_xv)):
        for j in range(len(weights_updat_xv[i])):
            weights_updat_xv[i][j] = weights_updat_xv[i][j] - gamma * gradients_xv[i][j]
            weights_updat_xv[i][j] = round(weights_updat_xv[i][j],4)

    # aktualizacja wag wejsciowo-ukrytych bias
    for i in range(len(weights_updat_bias_xv)):
        for j in range(len(weights_updat_bias_xv[i])):
            weights_updat_bias_xv[i][j] = weights_updat_bias_xv[i][j] - gamma * gradients_bias_xv[i][j]
            weights_updat_bias_xv[i][j] = round(weights_updat_bias_xv[i][j],4)

def train_network(train, gamma, beta, e, iterations, number_epochs, value_of_difference,y,v):
    flag = True
    list_of_error_in_epoch = []
    while flag:
        list_outputs = []
        list_expected = []
        for row in train:
            v, y = forward_propagate(w, row, beta)
            max_out = y.index(max(y))
            y_2 = [0, 0, 0]
            y_2[max_out] = 1
            list_outputs.append(y_2)

            d = row[-1]
            list_expected.append(d)
            backward_propagate(d, beta, row[:-1], e, iterations, v,y)
            update_weight(w, gamma, all_gradients)
        print(f'Current epoch {int(iterations[-1] / 168)}')
        # Warunek stopu jest tak skonstruowany że jeżeli w ciągu ostatnich 'number_epochs' cykli liczba blednych rozpoznań nie rózni się o 'value_of_difference'
        scores_of_error = 0
        if len(list_outputs) >= len(train_dataset):
            for i in range(len(list_outputs[-168:])):
                if list_outputs[-168 + i] != list_expected[-168 + i]:
                    scores_of_error += 1
        print('scores_of_error', scores_of_error)
        list_of_error_in_epoch.append(scores_of_error)
        # if len(list_of_error_in_epoch) >= number_epochs+1:
        #     minimum = min(list_of_error_in_epoch)
        #     maximum = max(list_of_error_in_epoch)
        #     if maximum - minimum < value_of_difference:
        #         data2["koncowe_wartosci_wag"] = w
        #         flag = False
        #         break
        #     else:
        #         del list_of_error_in_epoch[0]
        significant_change = [0]
        if len(list_of_error_in_epoch) >= number_epochs+1:
            for i in range(len(list_of_error_in_epoch[:-1])):
                if abs(list_of_error_in_epoch[i] - list_of_error_in_epoch[i+1]) > value_of_difference:
                    significant_change.append(1)
            if sum(significant_change) == 0:
                data["koncowe_wartosci_wag"] = w
                flag = False
                break
            else:
                del list_of_error_in_epoch[0]

            # differences_of_errors_between_epochs = []
            # for j in range(len(list_of_error_in_epoch[:-1])):
            #     difference = list_of_error_in_epoch[j + 1] - list_of_error_in_epoch[j]
            #     differences_of_errors_between_epochs.append(difference)
            # list_of_scores_differences = []
            # for dif in differences_of_errors_between_epochs:
            #     if abs(dif) < value_of_difference:
            #         list_of_scores_differences.append(1)
            #     else:
            #         list_of_scores_differences.append(0)
            # if sum(list_of_scores_differences) == number_epochs:
            #     # print('this iteration is here', iterations[-1])
            #     data["final_values_of_weights"] = all_weights
            #     flag = False
            #     break
            # else:
            #     del list_of_error_in_epoch[0]


        # error_in_epoch = 0
        # for i in e['error'][-168:]:
        #     error_in_epoch += i
        # sum_of_error_in_epoch.append(error_in_epoch)
        # if len(sum_of_error_in_epoch) >= number_epochs+1:
        #     differences_of_errors_between_epochs = []
        #     for j in range(len(sum_of_error_in_epoch[:-2])):
        #         difference = sum_of_error_in_epoch[j+1] - sum_of_error_in_epoch[j]
        #         differences_of_errors_between_epochs.append(difference)
        #     list_of_scores_differences = []
        #     for dif in differences_of_errors_between_epochs:
        #         if abs(dif) < value_of_difference:
        #             list_of_scores_differences.append(1)
        #         else:
        #             list_of_scores_differences.append(0)
        #     if sum(list_of_scores_differences) == number_epochs:
        #         # print('this iteration is here', iterations[-1])
        #         data["final_values_of_weights"] = all_weights
        #         flag = False
        #         break


iterations = [0]
gamma = 0.7  # 0.7
beta = 0.5  # 0.5
number_epochs = 10
value_of_difference = 4  # 6

result = {
    'scores': []
}

def testing_neural_network(all_weights, row, beta, s, i):
    d = row[-1]
    v, y = forward_propagate(all_weights, row, beta)
    max_out = y.index(max(y))
    y_2 = [0, 0, 0]
    y_2[max_out] = 1
    # print('Oczekiwana wartość klasy:', d)
    # print('Wyjście sieci neuronowej: ', y_2)
    if y_2 == [1,0,0]:
        y_3 = 'Kama'
    elif y_2 == [0,1,0]:
        y_3 = 'Rosa'
    elif y_2 == [0,0,1]:
        y_3 = 'Canadian'
    if d == [1,0,0]:
        d_3 = 'Kama'
    elif d == [0,1,0]:
        d_3 = 'Rosa'
    elif d == [0,0,1]:
        d_3 = 'Canadian'
    print('Oczekiwane wyjście:', d_3)
    print('Wyjście sieci neuronowej: ', y_3)

    # result['scores'].append({'number of package': i+1, 'expected output': expected_3, 'neural network output': outputs_3})

    if y_2 == d:
        result['scores'].append(1)
        # result['scores'].append([f'Sklasyfikowano poprawnie {y_3}'])
        s.append(s[-1]+1)
        print('--->Sklasyfikowano poprawnie')
    else:
        result['scores'].append(0)
        # result['scores'].append([f'Sklasyfikowano nie poprawnie oczekiwano:{d_3} . Wyjście sieci neuronowej {y_3}'])
        print('--->Sklasyfikowano nie poprawne')


answer = str(input('Czy chcesz trenować [train] czy testować [test] sieć neuronową: '))
if answer =='train':
    train_network(train_dataset, gamma, beta, error, iterations, number_epochs, value_of_difference,y,v)
    iterations_for_plot = iterations[1:]
    plt.figure(figsize=(10, 6))
    plt.plot(iterations_for_plot, error['error'])
    plt.grid(True)
    plt.xlabel("Liczba iteracji")
    plt.ylabel("Wartość błędu e")
    plt.title(f"Wrtość błędu dla poszczególnych iteracji \n dla Beta = {beta} i Gamma = {gamma}")
    plt.savefig("wykres.jpg", dpi=164)
    plt.show()

if answer == 'test':
    answer1 = input('Na jakim zbiorze chcesz testować: zbiór testowy - [1], zbiór uczący - [2]: ')
    test_dataset = []
    if answer1 == '1':
        file_4 = open('test_set', "r")
        data_4 = json.load(file_4)
        test_dataset = data_4["test_set"]
        file_4.close()

    if answer1 == '2':
        file_5 = open('train_set', "r")
        data_5 = json.load(file_5)
        test_dataset = data_5["train_set"]
        file_5.close()

    score=[0]

    for i in range(len(test_dataset)):
        print('Numer zestawu: ', i+1)
        testing_neural_network(data["koncowe_wartosci_wag"], test_dataset[i], beta, score, i)
    print('Liczba poprawnie sklasyfikowanych zestawów: ',score[-1])

    data2["wyniki_dzialania_dla_zbioru_na_ktorym_testowalismy"] = result['scores']
    data2["Liczba_poprawnie_sklasyfikowanych_zestawow"] = score[-1]

if answer != 'test' and answer != 'train':
    print('Zła odpowiedź')
    print(answer)


g = open("simulation_results", "w")
json.dump(data, g)
g.close()


g2 = open("simulation_results2", "w")
json.dump(data2, g2)
g2.close()
