from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
import matplotlib.pyplot as plt
from random import shuffle
import json

# {"liczba_iteracji":  [],  "wartosci_bledu_w_poszczegolnych_iteracjach":  [], "koncowe_wartosci_wag":  [],  "wyniki_dzialania_dla_zbioru_testujacego":  []}

file_1 = open('wyniki_symulacji', "r")
data = json.load(file_1)
file_1.close()

file_2 = open('zbior_testujacy', "r")
data_2 = json.load(file_2)
file_2.close()

file_3 = open('zbior_uczacy', "r")
data_3 = json.load(file_3)
dataset = data_3["zbior_uczacy"]
# dataset = json.load(file_3)
file_3.close()

# from Pakiety.zbiory import zbior_uczacy
# dataset = zbior_uczacy

all_weights = {
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

perceptrons = {
    'v1': [],
    'v2': [],
    'v3': [],
    'v4': [],
    'v5': [],

    'y1': [],
    'y2': [],
    'y3': []
}
all_gradients = {}
e ={
    'error': []
}


# # załadowanie zbioru danych
# def load_file_csv(filename):
#     dataset = list()
#     with open(filename, 'r') as file:
#         csv_reader = reader(file)
#         for row in csv_reader: # row = ['15.26', '14.84', '0.871', '5.763', '3.312', '2.221', '5.22', '1']
#             if not row:
#                 continue
#             dataset.append(row)
#     return dataset

def activate(weights, inputs):
    activation = 0
    for i in range(len(weights)):
        activation += weights[i] * inputs[i]
    return activation


def sigmoid(activation, beta):
    return 1.0 / (1.0 + exp(-activation * beta))


def forward_propagate(all_weights, row, beta):
    inputs = row  # row to są wejścia
    bias = [1]
    perceptrons['v1'] = activate(all_weights['w1'], inputs[:-1]) # ostatni element to [0,1,0]
    perceptrons['v1'] += activate(all_weights['w10'], bias)
    perceptrons['v1'] = sigmoid(perceptrons['v1'], beta)

    perceptrons['v2'] = activate(all_weights['w2'], inputs[:-1])
    perceptrons['v2'] += activate(all_weights['w20'], bias)
    perceptrons['v2'] = sigmoid(perceptrons['v2'], beta)

    perceptrons['v3'] = activate(all_weights['w3'], inputs[:-1])
    perceptrons['v3'] += activate(all_weights['w30'], bias)
    perceptrons['v3'] = sigmoid(perceptrons['v3'], beta)

    perceptrons['v4'] = activate(all_weights['w4'], inputs[:-1])
    perceptrons['v4'] += activate(all_weights['w40'], bias)
    perceptrons['v4'] = sigmoid(perceptrons['v4'], beta)

    perceptrons['v5'] = activate(all_weights['w5'], inputs[:-1])
    perceptrons['v5'] += activate(all_weights['w50'], bias)
    perceptrons['v5'] = sigmoid(perceptrons['v5'], beta)

    perceptrons['y1'] = activate(all_weights['w6'], [perceptrons['v1'], perceptrons['v2'], perceptrons['v3'], perceptrons['v4'], perceptrons['v5']])
    perceptrons['y1'] += activate(all_weights['w60'], bias)
    perceptrons['y1'] = sigmoid(perceptrons['y1'], beta)

    perceptrons['y2'] = activate(all_weights['w7'],[perceptrons['v1'], perceptrons['v2'], perceptrons['v3'], perceptrons['v4'], perceptrons['v5']])
    perceptrons['y2'] += activate(all_weights['w70'], bias)
    perceptrons['y2'] = sigmoid(perceptrons['y2'], beta)

    perceptrons['y3'] = activate(all_weights['w8'],[perceptrons['v1'], perceptrons['v2'], perceptrons['v3'], perceptrons['v4'], perceptrons['v5']])
    perceptrons['y3'] += activate(all_weights['w80'], bias)
    perceptrons['y3'] = sigmoid(perceptrons['y3'], beta)

    return [perceptrons['y1'], perceptrons['y2'], perceptrons['y3']]


def sigmoid_derivative(output, beta):
    return beta * output * (1.0 - output)


def backward_propagate(expected, beta, x, e, iteracje):
    l_rate = 0.7
    # liczenie gradientów dla warstwy ukryto-wyjsciowej
    iteracje.append((iteracje[-1] + 1))
    print('it: ', iteracje[-1])
    data["liczba_iteracji"] = iteracje[-1]
    e1 = 0.0
    outputs = [perceptrons['y1'], perceptrons['y2'], perceptrons['y3']]
    hiden_neurons = [perceptrons['v1'], perceptrons['v2'], perceptrons['v3'], perceptrons['v4'], perceptrons['v5']]
    for j in range(len(outputs)):
        e1 += (expected[j]-outputs[j]) ** 2
        g = []
        gb = []
        for k in hiden_neurons:
            g.append(-(expected[j]-outputs[j])*sigmoid_derivative(outputs[j], beta) * k)
        gb.append(-(expected[j]-outputs[j])*sigmoid_derivative(outputs[j], beta) * 1)
        all_gradients[f'g{j+6}'] = g
        all_gradients[f'g{j*10+60}'] = gb
    e1 = 0.5 * e1
    e['error'].append(e1)
    data["wartosci_bledu_w_poszczegolnych_iteracjach"].append(e1)


    # aktualizacja wag ukryto-wyjsciowych

    # dla warstwy wejsciowo- ukrytej
    weights_updat = [all_weights['w6'], all_weights['w7'], all_weights['w8']]
    weights_updat_bias = [all_weights['w60'], all_weights['w70'], all_weights['w80']]

    gradients = [all_gradients['g6'], all_gradients['g7'], all_gradients['g8']]
    gradients_bias =[all_gradients['g60'], all_gradients['g70'], all_gradients['g80']]

    # aktualizacja wag ukryto-wyjsciowych
    for i in range(len(weights_updat)):
        for j in range(len(weights_updat[i])):
            weights_updat[i][j] = weights_updat[i][j] - l_rate * gradients[i][j]


    # aktualizacja wag bias ukryto-wyjsciowych
    for i in range(len(weights_updat_bias)):
        for j in range(len(weights_updat_bias[i])):
            weights_updat_bias[i][j] = weights_updat_bias[i][j] - l_rate * gradients_bias[i][j]


    # liczenie gradientów dla warstwy wejsciowo-ukrytej
    for i in range(len(hiden_neurons)): # 5
        g_2 = []
        gb_2 = []
        for j in range(len(x)): # 7
            gradient = 0
            for m in range(len(outputs)): # 3
                gradient += -(expected[m]-outputs[m])*sigmoid_derivative(outputs[m], beta) * weights_updat[m][i]
            gradient = gradient*sigmoid_derivative(hiden_neurons[i], beta)*x[j]
            gradient_b = gradient*sigmoid_derivative(hiden_neurons[i], beta)*1 # gradienty bias
            g_2.append(gradient)
            gb_2.append(gradient_b) # gradienty bias
        all_gradients[f'g{i + 1}'] = g_2  #  będzie g1 -g5 takie że g1 =[   weights_hiden1_x1      weights_hiden1_x2    ...        ] 1-7
        all_gradients[f'g{i * 10 + 10}'] = gb_2  # gradienty bias


    # aktualizacja wag wejsciowo-ukrytych
    weights_updat_xv = [all_weights['w1'], all_weights['w2'], all_weights['w3'], all_weights['w4'], all_weights['w5']]
    weights_updat_bias_xv = [all_weights['w10'], all_weights['w20'], all_weights['w30'], all_weights['w40'], all_weights['w50']]

    gradients_xv = [all_gradients['g1'], all_gradients['g2'], all_gradients['g3'], all_gradients['g4'], all_gradients['g5']]
    gradients_bias_xv = [all_gradients['g10'], all_gradients['g20'], all_gradients['g30'], all_gradients['g40'], all_gradients['g50']]

    # aktualizacja wag wejsciowo-ukrytych
    for i in range(len(weights_updat_xv)):
        for j in range(len(weights_updat_xv[i])):
            weights_updat_xv[i][j] = weights_updat_xv[i][j] - l_rate * gradients_xv[i][j]

    # aktualizacja wag wejsciowo-ukrytych bias
    for i in range(len(weights_updat_bias_xv)):
        for j in range(len(weights_updat_bias_xv[i])):
            weights_updat_bias_xv[i][j] = weights_updat_bias_xv[i][j] - l_rate * gradients_bias_xv[i][j]

'''def update_weight(all_weights, l_rate):
    # aktualizacja wag ukryto-wyjsciowych

    # dla warstwy wejsciowo- ukrytej
    weights_updat = [all_weights['w6'], all_weights['w7'], all_weights['w8']]
    weights_updat_bias = [all_weights['w60'], all_weights['w70'], all_weights['w80']]

    gradients = [all_gradients['g6'], all_gradients['g7'], all_gradients['g8']]
    gradients_bias = [all_gradients['g60'], all_gradients['g70'], all_gradients['g80']]

    # aktualizacja wag ukryto-wyjsciowych
    for i in range(len(weights_updat)):
        for j in range(len(weights_updat[i])):
            weights_updat[i][j] = weights_updat[i][j] - l_rate * gradients[i][j]

    # aktualizacja wag bias ukryto-wyjsciowych
    for i in range(len(weights_updat_bias)):
        for j in range(len(weights_updat_bias[i])):
            weights_updat_bias[i][j] = weights_updat_bias[i][j] - l_rate * gradients_bias[i][j]

    # aktualizacja wag wejsciowo-ukrytych
    weights_updat_xv = [all_weights['w1'], all_weights['w2'], all_weights['w3'], all_weights['w4'], all_weights['w5']]
    weights_updat_bias_xv = [all_weights['w10'], all_weights['w20'], all_weights['w30'], all_weights['w40'], all_weights['w50']]

    gradients_xv = [all_gradients['g1'], all_gradients['g2'], all_gradients['g3'], all_gradients['g4'], all_gradients['g5']]
    gradients_bias_xv = [all_gradients['g10'], all_gradients['g20'], all_gradients['g30'], all_gradients['g40'], all_gradients['g50']]

    # aktualizacja wag wejsciowo-ukrytych
    for i in range(len(weights_updat_xv)):
        for j in range(len(weights_updat_xv[i])):
            weights_updat_xv[i][j] = weights_updat_xv[i][j] - l_rate * gradients_xv[i][j]

    # aktualizacja wag wejsciowo-ukrytych bias
    for i in range(len(weights_updat_bias_xv)):
        for j in range(len(weights_updat_bias_xv[i])):
            weights_updat_bias_xv[i][j] = weights_updat_bias_xv[i][j] - l_rate * gradients_bias_xv[i][j]'''


# trzeba zrobić warunek stopu
def train_network(train, l_rate, beta, e):
    iteracje = [0]
    flag = True
    while flag:
        list_outputs = []
        list_expected = []
        for row in train:
            outputs = forward_propagate(all_weights, row, beta)
            # print('outputs: ', outputs)
            max_out = outputs.index(max(outputs))
            # print('max_out: ',max_out)
            outputs_2 = [0, 0, 0]
            outputs_2[max_out] = 1
            print('outputs_2: ', outputs_2)

            list_outputs.append(outputs_2)
            # print('lista wyjść:', list_outputs)
            # index_max_output = predict(all_weights, row, beta)
            # list_outputs.append(index_max_output)

            # index_max_expected = expected.index(max(expected))
            # list_expected.append(index_max_expected)
            expected = row[-1]
            print('expected: ', expected)
            list_expected.append(expected)
            # print('lista wyjść oczekiwanych:', list_expected)
            backward_propagate(expected, beta, row[:-1], e, iteracje)# expected, beta, l_rate, x, e, iteracje
            # update_weight(all_weights, l_rate)
            #if len(list_outputs) == len(dataset) or len(list_outputs) > len(dataset):
            scores = 0
            if len(list_outputs) >= len(dataset):
                for i in range(len(list_outputs[-168:])):
                    if list_outputs[-168+i] == list_expected[-168+i]:
                        scores += 1
                        if scores > 152:
                            print('tu jest ta iteracja', iteracje[-1])
                            data["koncowe_wartosci_wag"] = all_weights
                            flag = False
                            break



# seed(1)
l_rate = 0.5
beta = 0.5
# {"liczba_iteracji":  [],  "wartosci_bledu_w_poszczegolnych_iteracjach":  [], "koncowe_wartosci_wag":  [],  "wyniki_dzialania_dla_zbioru_testujacego":  []}
train_network(dataset, l_rate, beta, e) # (train, l_rate, beta, e)

g = open("wyniki_symulacji", "w")
json.dump(data, g)
g.close()