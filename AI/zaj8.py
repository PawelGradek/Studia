"""
Moduł do implementacji algorytmu
uczenia gradientu stochastycznego dla sieci neuronowej ze sprzężeniem do przodu.
Gradienty są obliczane przy użyciu propagacji wstecznej.
"""

#### Libraries
# Standard library
import random

# Third-party libraries
import numpy as np

class Network(object):

    def __init__(self, sizes):
        """Lista ``rozmiary`` zawiera liczbę neuronów w
        odpowiednich warstwach sieci. Na przykład, jeśli lista
        byłaby [2, 3, 1], byłaby to sieć trójwarstwowa, przy czym
        pierwsza warstwa zawierająca 2 neurony, druga warstwa 3 neurony
        i trzecia warstwa neurony 1. Błędy i wagi dla
        sieci są inicjowane losowo, przy użyciu
        rozkładu
Gaussa ze średnią 0 i wariancją 1. Należy zauważyć, że         zakłada się,
że pierwsza warstwa jest warstwę wejściową i zgodnie z konwencją nie         będziemy ustawiać żadnych odchyleń dla tych neuronów, ponieważ odchylenia są
        używane
        tylko przy obliczaniu wyników z późniejszych warstw."""
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.ones(y, 1) for y in sizes[1:]]
        self.weights = [np.random.uniform(-0.5, 0.5, size=((y, x) for x, y in zip(sizes[:-1], sizes[1:])))]

    def feedforward(self, a):
        """Zwróć wyjście sieci, jeśli ``a`` jest wejściem."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
    # stochastic gradient descent
    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        ''' trenuj  sieć neuronowa przy użyciu mini-partią stochastyczny
        gradientu opadanie` training_data`` jest lista krotki.
        `` (x, y) `` reprezentujących wejścia treningowe i pożądane
        wyjścia. Inne
        nieopcjonalne
parametry nie wymagają wyjaśnień. Jeśli podano ``dane_testowe``,         sieć zostanie oceniona na podstawie danych testowych po każdej
        epoce i wydrukowany zostanie częściowy postęp. Jest to przydatne w przypadku
        śledzenie postępów, ale znacznie spowalnia działanie.'''
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test))
            else:
                print( "Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):
        """Zaktualizuj wagi i obciążenia sieci, stosując
        gradient gradientu przy użyciu wstecznej propagacji do pojedynczej minipartii.
        ``mini_batch`` to lista krotek ``(x, y)``, a ``eta``
        to szybkość uczenia się."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        """Zwróć krotkę ``(nabla_b, nabla_w)`` reprezentującą
        gradient dla funkcji kosztu C_x. ``nabla_b`` i
        ``nabla_w`` są listy warstwa po warstwie numpy tablic, podobne
        do ``self.biases`` i ``self.wagi``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Zauważ, że zmienna l w poniższej pętli jest używana
         # l = 1 oznacza ostatnią warstwę neuronów, l = 2 to
        # przedostatnia warstwa i tak dalej. Jest to zmiana numeracji
        #schematu  # w książce, użyta tutaj, aby wykorzystać fakt,
        # że Python może używać indeksów ujemnych na listach.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Powrót liczba wejść testowych, dla których neuronowych
        . Sieć wysyła poprawny wynik Należy zauważyć, że
        zakłada się, że wyjście sieci
        neuronowej jest indeksem tego         neuronu w ostatniej warstwie, który ma najwyższą aktywację."""
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Return wektor pochodnych cząstkowych \partial C_x /
        \partial a dla aktywacji wyjścia."""
        return (output_activations-y)

#### Miscellaneous functions
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """pochodna of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

x = ([0,1],1),([1,0],1)
net = Network([2,1])
net.SGD(x, 30, 10, 3.0, test_data=None)