# Backprop on the Seeds Dataset
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


# Load a CSV file
def load_csv(filename):  # załadowanie zbioru danych
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):  # przekonwertowanie ciągu liczb na liczby zmiennoprzecinkowe
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):  # przekonwertowanie kolumny klasy na waartości całkowite
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    stats = [[min(column), max(column)] for column in zip(*dataset)]
    return stats


# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset,
                      minmax):  # wartości wejściowe różnią się skalą i muszą być znormalizowane do zakresu od 0 do 1. Normalizujemy do zakresu wartości funkcji sigmoidalnej
    for row in dataset:
        for i in range(len(row) - 1):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])



# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]  # ostatni element to bias
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


# Transfer neuron activation
def transfer(activation, Beta):
    return 1.0 / (1.0 + exp(-activation * Beta))


# Forward propagate input to a wagi output
def forward_propagate(network, row, Beta):  # to nad czym pracowałem 29.12.21
    inputs = row  # row to są wejścia
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['wagi'], inputs)
            neuron['output'] = transfer(activation, Beta)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# Calculate the derivative of an neuron output
def transfer_derivative(output, Beta):
    return Beta * output * (1.0 - output)


# Backpropagate error and store in neurons
def backward_propagate_error(network, expected, Beta, x, iteracje= iteracja):  # tu musisz pozmieniać gradienty/ network =[[],[]]
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
                        # do tego momentu jest dobrze w 100%
                        blad_e += (neuron_2['output'] - expected[neuron])**2
                        gradient += (neuron_2['output'] - expected[neuron]) * transfer_derivative(neuron_2['output'],Beta) * neuron_2['wagi'][j]
                    blad_e = 0.5*blad_e
                    blad.append(blad_e)
                    iterac = iteracja[-1]
                    iteracja.append((iterac+1))
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
                    gradient += (neuron_2['output'] - expected[neuron]) * transfer_derivative(neuron_2['output'], Beta) * neuron_2['wagi'][j]
                blad_e = 0.5 * blad_e
                blad.append(blad_e)
                iterac = iteracja[-1]
                iteracja.append((iterac + 1))
                gradient = gradient * transfer_derivative(wagi['output'], Beta) * 1
                gradienty_x_v_bias.append((gradient))
            wszystkie_gradienty['gradienty_x_v_bias'] = gradienty_x_v_bias  # 7 gradientów
            # jeszcze trzeba zrobić dla biasu
            # gradient += (neuron_2['wagi'][j] * neuron_2['delta'])# tu stosujemy gradient- delta
            # gradienty_x_v.append(gradient)
        else:  # tu liczymy dla neuronów ukryte-wyjsciowe/ liczymy to najpierw a potem to co jest u góry
            blad_e1 = 0.0
            for j in range(len(network[1])):
                blad_e1 += (network[1][j]['output'] - expected[j]) ** 2
                for k in network[0]:
                    gradienty_v_y.append(((network[1][j]['output'] - expected[j]) * transfer_derivative(network[1][j]['output'], Beta) * k['output']))  # powinno być expected[j]-neuron['output']
                gradienty_v_y_bias.append(((network[1][j]['output'] - expected[j]) * transfer_derivative(network[1][j]['output'], Beta) * 1))  # tu liczymy  gradient dla biasu

            blad_e1 = 0.5 * blad_e1
            blad.append(blad_e1)
            iterac = iteracja[-1]
            iteracja.append((iterac + 1))



            wszystkie_gradienty['gradienty_v_y'] = gradienty_v_y  # 15 gradientów
            wszystkie_gradienty['gradienty_v_y_bias'] = gradienty_v_y_bias  # 3 gradienty
            # for j in range(len(layer)):
            #     neuron = layer[j]
            #     for k in network[0]:
            #         blad_e += (neuron['output'] - expected[j]) ** 2
            #         gradienty_v_y.append(((neuron['output'] - expected[j]) * transfer_derivative(neuron['output'],Beta) * k['output']))  # powinno być expected[j]-neuron['output']
            #     gradienty_v_y_bias.append(((neuron['output'] - expected[j]) * transfer_derivative(neuron['output'],Beta) * 1))  # tu liczymy  gradient dla biasu


        # for j in range(len(layer)):# te trzy linie kodu mogę usunąć bo już to policzyłem wyżej
        #     neuron = layer[j]
        #     neuron['delta'] = gradienty_x_v[j] * transfer_derivative(neuron['output']) # tu liczymy gradient- delta


# Update wagi wagi with error
def update_weights(network, l_rate):
    for i in range(len(network)):  # network =[  []        []   ] czyli i = [ { }         { }           { }    ...]
        if i != 0:  # najpierw zmieniamy wagi dla wag ukryto-wyjsciowych
            k = -1
            for neuron in network[i]:  # neuron =  {'wagi':[] }
                k = k + 1

                for j in range(len(neuron['wagi'])):

                    if neuron['wagi'][j] != neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_v_y'][j]
                    if neuron['wagi'][j] == neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_v_y_bias'][k]
        if i == 0:
            k = -1
            for neuron in network[i]:  # neuron =  {'wagi':[] }
                k = k + 1
                for j in range(len(neuron['wagi'])):
                    if neuron['wagi'][j] != neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_x_v'][j]
                    if neuron['wagi'][j] == neuron['wagi'][-1]:
                        neuron['wagi'][j] -= l_rate * wszystkie_gradienty['gradienty_x_v_bias'][k]


# Train a wagi for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        # sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row, Beta)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            # sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backward_propagate_error(network, expected, Beta, row)
            update_weights(network, l_rate)
        # print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


# Initialize a wagi
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'wagi': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'wagi': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network



# Make a prediction with a wagi
def predict(network, row):
    outputs = forward_propagate(network, row, Beta)
    return outputs.index(max(outputs))


# Backpropagation Algorithm With Stochastic Gradient Descent
def back_propagation(train, l_rate, n_epoch, n_hidden):
    n_inputs = len(train[0]) - 1  # 7 parametrów wejściowych
    n_outputs = len(set([row[-1] for row in train]))  # 3 wyjścia
    network = initialize_network(n_inputs, n_hidden, n_outputs)
    train_network(network, train, l_rate, n_epoch, n_outputs)
    predictions = list()
    # for row in test:
    #     prediction = predict(network, row)
    #     predictions.append(prediction)
    return (predictions)


# Test Backprop on Seeds dataset
seed(1)
# load and prepare data
filename = 'seeds_dataset'
dataset = load_csv(filename)
for i in range(len(dataset[0]) - 1):
    str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0]) - 1)
# normalize input variables
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)
# evaluate algorithm
n_folds = 1
l_rate = 0.5
n_epoch = 10
n_hidden = 5

# scores = back_propagation(dataset,l_rate, n_epoch, n_hidden)
# print('Scores: %s' % scores)
# scores = evaluate_algorithm(dataset, back_propagation, n_folds, l_rate, n_epoch, n_hidden)
# print('Scores: %s' % scores)
# print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
back_propagation(dataset,l_rate, n_epoch, n_hidden)


del iteracja[0]
plt.plot(iteracja,blad)
plt.show()
