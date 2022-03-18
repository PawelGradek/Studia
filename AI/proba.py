from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np



train_data = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]])

# d(n)
target_xor = np.array(
    [
        [0],
        [1],
        [1],
        [0]])


class MLP:


    def __init__(self, train_data, target, lr=0.1, num_epochs=3, num_input=2, num_hidden=2, num_output=1):
        self.train_data = train_data
        self.target = target
        self.lr = lr
        self.num_epochs = num_epochs

        self.weights_01 = np.random.uniform(size=(num_input, num_hidden))
        self.weights_12 = np.random.uniform(size=(num_hidden, num_output))

        self.b01 = np.random.uniform(size=(1, num_hidden))
        self.b12 = np.random.uniform(size=(1, num_output))
        # tu jest funkcja błędu epsilon z sumą
        self.losses = []

    def update_weights(self):

        # Calculate the squared error
        loss = 0.5 * (self.target - self.output_final) ** 2
        print('Błąd kwadratowy:',loss) # mamy 4 błędy
        self.losses.append(np.sum(loss))
        print('epsilon suma błedu kwadratowego',self.losses)

        error_term = (self.target - self.output_final)

        # the gradient for the hidden layer wagi
        grad01 = self.train_data.T @ (
                    ((error_term * self._delsigmoid(self.output_final)) * self.weights_12.T) * self._delsigmoid(
                self.hidden_out))
        print("grad01: ", grad01)
        print('Rozmiar grad01',grad01.shape)
        print('Tu jest hidden!!!',self.hidden_out)
        # the gradient for the output layer wagi
        grad12 = self.hidden_out.T @ (error_term * self._delsigmoid(self.output_final))

        print("grad12: ", grad12)
        print('Rozmiar grad12',grad12.shape)

        # updating the wagi by the learning rate times their gradient
        self.weights_01 += self.lr * grad01
        self.weights_12 += self.lr * grad12

        # update the biases the same way
        self.b01 += np.sum(
            self.lr * ((error_term * self._delsigmoid(self.output_final)) * self.weights_12.T) * self._delsigmoid(
                self.hidden_out), axis=0)
        self.b12 += np.sum(self.lr * error_term * self._delsigmoid(self.output_final), axis=0)

    def _sigmoid(self, x):
        """
        The sigmoid activation function.
        """
        return 1 / (1 + np.exp(-x))

    def _delsigmoid(self, x):
        """
        The first derivative of the sigmoid function wrt x
        """
        return x * (1 - x)

    def forward(self, batch):
        """
        A single forward pass through the network.
        Implementation of wX + b
        """

        self.hidden_ = np.dot(batch, self.weights_01) + self.b01
        self.hidden_out = self._sigmoid(self.hidden_)

        self.output_ = np.dot(self.hidden_out, self.weights_12) + self.b12
        self.output_final = self._sigmoid(self.output_)

        return self.output_final

    def classify(self, datapoint):
        """
        Return the class to which a datapoint belongs based on
        the perceptron's output for that point.
        """
        datapoint = np.transpose(datapoint)
        if self.forward(datapoint) >= 0.5:
            return 1

        return 0



    def train(self):
        """
        Train an MLP. Runs through the data num_epochs number of times.
        A forward pass is done first, followed by a backward pass (backpropagation)
        where the networks parameter's are updated.
        """
        for _ in range(self.num_epochs):
            self.forward(self.train_data)
            self.update_weights()

mlp = MLP(train_data, target_xor, 0.2, 3)
mlp.train()