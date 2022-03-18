from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
import matplotlib.pyplot as plt

Beta = 0.5

wszystkie_gradienty = {}
iteracja = [0]
blad = []


# załadowanie zbioru danych
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# przekonwertowanie ciągu liczb na liczby zmiennoprzecinkowe
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# przekonwertowanie kolumny klasy na wartości całkowite
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


def dataset_minmax(dataset):
    minmax = list()
    stats = [[min(column), max(column)] for column in zip(*dataset)]
    return stats


# wartości wejściowe różnią się skalą i muszą być znormalizowane do zakresu od 0 do 1. Normalizujemy do zakresu wartości funkcji sigmoidalnej
def normalize_dataset(dataset,minmax):
    for row in dataset:
        for i in range(len(row) - 1):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


def activate(weights, inputs):
    activation = weights[-1]  # ostatni element to bias
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


def transfer(activation, Beta):
    return 1.0 / (1.0 + exp(-activation * Beta))


def forward_propagate(network, row, Beta):
    inputs = row  # row to są wejścia
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['wagi'], inputs)
            neuron['output'] = transfer(activation, Beta)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


def transfer_derivative(output, Beta):
    return Beta * output * (1.0 - output)


def backward_propagate_error(network, expected, Beta, x, iteracje):
    for i in reversed(range(len(network))):  # odwrócenie kolejności, jęsli mamy 2 element w network to mamy range(1,0), najpierw dla elementów neurony ukryte-wyjściowe a potem dla neuronów poczatkowe-ukryte
        layer = network[i]  # []/ network
        gradienty_v_y = list()
        gradienty_x_v = list()
        gradienty_x_v_bias = list()
        gradienty_v_y_bias = list()
        if i != len(network) - 1:  # i != 1 sztuczka żebyśmy pomineli ostatni element network/ to liczymy dla neuronów poczatkowe-ukryte
            for elem in range(len(x)):
                for j in range(len(layer)):
                    wagi = layer[j]
                    gradient = 0.0
                    blad_e = 0.0
                    for neuron in range(len(network[i + 1])):  # kod od pocztku funkcji do tego momentu ma za zadanie przejśc do ostatniego elementu w sieci czyli do neuronów wyjściowych i liczymy gradient dla  wag neuronów ukrytych-wyjsciowych
                        neuron_2 = network[i + 1][neuron]
                        blad_e += (neuron_2['output'] - expected[neuron])**2
                        gradient += (neuron_2['output'] - expected[neuron]) * transfer_derivative(neuron_2['output'],Beta) * neuron_2['wagi'][j]-l_rate*wszystkie_gradienty['gradienty_v_y'][j] # j = 1-5
                    blad_e = 0.5*blad_e
                    blad.append(blad_e)
                    iterac = iteracje[-1]
                    iteracje.append((iterac+1))
                    gradient = gradient * transfer_derivative(wagi['output'], Beta) * x[elem]
                    gradienty_x_v.append((gradient))
            wszystkie_gradienty['gradienty_x_v'] = gradienty_x_v  # 35 gradientów
            for j in range(len(layer)):
                wagi = layer[j]
                gradient = 0.0
                blad_e =0.0
                for neuron in range(len(network[i + 1])):
                    neuron_2 = network[i + 1][neuron]
                    blad_e += (neuron_2['output'] - expected[neuron])**2
                    gradient += (neuron_2['output'] - expected[neuron]) * transfer_derivative(neuron_2['output'], Beta) * neuron_2['wagi'][j]-l_rate*wszystkie_gradienty['gradienty_v_y'][j]
                blad_e = 0.5 * blad_e
                blad.append(blad_e)
                iterac = iteracje[-1]
                iteracje.append((iterac + 1))
                gradient = gradient * transfer_derivative(wagi['output'], Beta) * 1
                gradienty_x_v_bias.append((gradient))
            wszystkie_gradienty['gradienty_x_v_bias'] = gradienty_x_v_bias  # 7 gradientów
        else:  # tu liczymy dla warstwy ukryto-wyjsciowej
            blad_e1 = 0.0
            for j in range(len(network[1])):
                blad_e1 += (network[1][j]['output'] - expected[j]) ** 2
                for k in network[0]:
                    gradienty_v_y.append(((network[1][j]['output'] - expected[j]) * transfer_derivative(network[1][j]['output'], Beta) * k['output']))
                gradienty_v_y_bias.append(((network[1][j]['output'] - expected[j]) * transfer_derivative(network[1][j]['output'], Beta) * 1))  # tu liczymy  gradient dla biasu

            blad_e1 = 0.5 * blad_e1
            blad.append(blad_e1)
            iterac = iteracje[-1]
            iteracje.append((iterac + 1))
            wszystkie_gradienty['gradienty_v_y'] = gradienty_v_y  # 15 gradientów
            wszystkie_gradienty['gradienty_v_y_bias'] = gradienty_v_y_bias  # 3 gradienty


def update_weights(network, l_rate):
    for i in range(len(network)):
        if i != 0:  # najpierw zmieniamy wagi dla wag ukryto-wyjsciowych
            k = -1
            for neuron in network[i]:
                k = k + 1
                for j in range(len(neuron['wagi'])):
                    if neuron['wagi'][j] != neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_v_y'][j]
                    if neuron['wagi'][j] == neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_v_y_bias'][k]
        if i == 0:
            k = -1
            for neuron in network[i]:
                k = k + 1
                for j in range(len(neuron['wagi'])):
                    if neuron['wagi'][j] != neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_x_v'][j]
                    if neuron['wagi'][j] == neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_x_v_bias'][k]


def train_network(network, train, l_rate, n_epoch, n_outputs, iteracje):
    for epoch in range(n_epoch):
        for row in train:
            outputs = forward_propagate(network, row, Beta)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            backward_propagate_error(network, expected, Beta, row, iteracje)
            update_weights(network, l_rate)


def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'wagi': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'wagi': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network


def back_propagation(train, l_rate, n_epoch, n_hidden, iteracje):
    n_inputs = len(train[0]) - 1  # 7 parametrów wejściowych
    n_outputs = len(set([row[-1] for row in train]))  # 3 wyjścia
    network = initialize_network(n_inputs, n_hidden, n_outputs)
    return train_network(network, train, l_rate, n_epoch, n_outputs, iteracje)


seed(1)
filename = 'seeds_dataset'
dataset = load_csv(filename)
for i in range(len(dataset[0]) - 1):
    str_column_to_float(dataset, i)

str_column_to_int(dataset, len(dataset[0]) - 1)

minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)

l_rate = 0.5
n_epoch = 10
n_hidden = 5

back_propagation(dataset, l_rate, n_epoch, n_hidden, iteracja)

del iteracja[0]
plt.plot(iteracja, blad)
plt.show()
