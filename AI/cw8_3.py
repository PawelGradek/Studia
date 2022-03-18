from math import exp
from random import seed
from random import random

# Initialize a wagi
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'wagi':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)] # random()-0.5
	network.append(hidden_layer)
	output_layer = [{'wagi':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a wagi output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['wagi'], inputs) # mnożenie wejść x razy ich wagi
			neuron['output'] = transfer(activation) # dodanie do sieci wyjść które są aktywowane przez funkcje sigmoidalną
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

# Calculate the derivative of an neuron output
def transfer_derivative(output): # pochodna funkcji sigmoidalnej
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		gradienty_lista = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				gradient = 0.0
				for neuron in network[i + 1]:
					gradient += (neuron['wagi'][j] * neuron['delta'])
				gradienty_lista.append(gradient)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				gradienty_lista.append(neuron['output'] - expected[j])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = gradienty_lista[j] * transfer_derivative(neuron['output'])

# Update wagi wagi with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['wagi'][j] -= l_rate * neuron['delta'] * inputs[j]
			neuron['wagi'][-1] -= l_rate * neuron['delta']

# Train a wagi for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

# Test training backprop algorithm
seed(1)
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.5, 20, n_outputs)
for layer in network:
	print(layer)