# Backprop on the Seeds Dataset
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp

# inicjacja wag poczatkowych
w1 = random() - 0.5
w2 = random() - 0.5
w3 = random() - 0.5
w4 = random() - 0.5
w5 = random() - 0.5
w6 = random() - 0.5
w7 = random() - 0.5
print(w1)
lista_wag_x_v = [w1, w2, w3, w4, w5, w6, w7]
print(lista_wag_x_v)
# inicjacja wag od neuronów ukrytych do neuronów wyjściowych/ bedzie 5 neuronów ukrytych
w8 = random() - 0.5
w9 = random() - 0.5
w11 = random() - 0.5
w12 = random() - 0.5
w13 = random() - 0.5
lista_wag_v_y = [w8, w9, w11, w12, w13]
# inicjacja wag bias poczatkowych
w10 = random() - 0.5
w20 = random() - 0.5
w30 = random() - 0.5
w40 = random() - 0.5
w50 = random() - 0.5
lista_wag_bias_x_v = [w10, w20, w30, w40, w50]
# inicjacja wag bias od neuronów ukrytych do neuronów wyjściowych
w60 = random() - 0.5
w70 = random() - 0.5
w80 = random() - 0.5
lista_wag_bias_v_y = [w60, w70, w80]
bias = 1
Beta=0.5


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


'''
# to nie musi być !!!!!!!!!!!!
# Split a dataset into k folds k krotna walidacja krzyżowa
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split


# Calculate accuracy percentage
def accuracy_metric(actual, predicted): # funkcja do obliczenia dokładności przewidywań
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args): # ocena algorytmu za pomocą walidacji krzyżowej
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores'''


# Calculate neuron activation for an input
def activate(wagi, wagi_bias, inputs, bias):
    activation = 0
    for i in range(len(wagi)):
        activation += wagi[i] * inputs[i]
    for i in range(len(wagi_bias)):
        activation += wagi_bias[i] * bias
    return activation


# Transfer neuron activation
def transfer(activation,Beta):
    return 1.0 / (1.0 + exp(-activation*Beta))


# Forward propagate input to a wagi output
def forward_propagate(wagi,wagi_bias, row, bias):  # to nad czym pracowałem 29.12.21
    inputs = row  # row to są wejścia
    new_inputs = []
    activation = activate(wagi, wagi_bias, inputs, bias)
    output = transfer(activation, Beta)
    new_inputs.append(output)
    inputs = new_inputs
    return inputs


# Calculate the derivative of an neuron output
def transfer_derivative(output,Beta):
    return Beta * output * (1.0 - output)


# Backpropagate error and store in neurons
def backward_propagate_error(wagi_x_v, wagi_bias_x_v, wagi_v_y, wagi_bias_v_y, network, expected):  # tu musisz pozmieniać gradienty
    # for i in range(wagi_v_y):
    #     gradient = -(expected[i]-)
    for i in reversed(range(len(network))):  # odwrócenie kolejności, jęsli mamy 3 layers in wagi to mamy range(2,0)
        layer = network[i]
        errors = list()
        if i != len(network) - 1:  # i != 0 sztuczka żebyśmy pomineli ostatni element za 3 lini kodu
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[
                    i + 1]:  # kod od pocztku funkcji do tego momentu ma za zadanie przejśc do ostatniego elementu w sieci czyli do neuronów wyjściowych
                    error += (neuron['wagi'][j] * neuron['delta'])  # tu stosujemy gradient- delta
                errors.append(error)
        else:  # tu liczymy dla ostatniego layer
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(neuron['output'] - expected[j])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'], Beta)  # tu liczymy gradient- delta


# Update wagi wagi with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]  # bez biasu
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]  # ustawiamy output dla warstwy ukrytej
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['wagi'][j] -= l_rate * neuron['delta'] * inputs[j]
            neuron['wagi'][-1] -= l_rate * neuron['delta']


# Train a wagi for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        # sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            # sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        # print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


# Initialize a wagi
def initialize_network(n_inputs,n_hidden,n_outputs):
    network = list()
    hidden_layer = [{'wagi': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    #hidden_layer = [{'wagi': wagi_x_v} ]
    network.append(hidden_layer)
    output_layer = [{'wagi': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    #output_layer = [{'wagi': wagi_v_y} ]
    network.append(output_layer)
    return network
print(initialize_network(7,5,3))


# Make a prediction with a wagi
def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))


# Backpropagation Algorithm With Stochastic Gradient Descent
def back_propagation(train, test, l_rate, n_epoch, n_hidden,wagi_x_v,wagi_v_y):
    n_inputs = len(train[0]) - 1  # 7 parametrów wejściowych
    n_outputs = len(set([row[-1] for row in train]))  # 3 wyjścia
    network = initialize_network(wagi_x_v,wagi_v_y)
    train_network(network, train, l_rate, n_epoch, n_outputs)
    predictions = list()
    for row in test:
        prediction = predict(network, row)
        predictions.append(prediction)
    return (predictions)


'''# Test Backprop on Seeds dataset
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
n_folds = 5
l_rate = 0.3
n_epoch = 500
n_hidden = 5
scores = evaluate_algorithm(dataset, back_propagation, n_folds, l_rate, n_epoch, n_hidden)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))'''
