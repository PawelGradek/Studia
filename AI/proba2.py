from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)


dane_treningowe = np.array(
    [
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]])
x= dane_treningowe.T[0]
y = x.T
print(y)
# d(n)
d = np.array(
    [
        [0],
        [1],
        [1],
        [0]])


class MLP:


    def __init__(self, dane_treningowe, d, gamma=0.1, num_epok=3, num_wejsc=3, num_ukrytych=2, num_wyjsc=1, Beta=0.5):
        self.dane_treningowe = dane_treningowe
        self.d = d
        self.gamma = gamma
        self.num_epok = num_epok
        self.Beta = Beta

        self.wagi_x_v1 = np.random.uniform(-0.5,0.5,size=(num_wejsc, num_ukrytych))
        self.wagi_x_v2 = np.random.uniform(-0.5,0.5,size=(num_wejsc, num_ukrytych))
        self.wagi_v_y = np.random.uniform(-0.5,0.5,size=(num_ukrytych+1, num_wyjsc))

        # self.bias_x_v = np.random.uniform(-0.5,0.5,size=(1, num_ukrytych))
        # self.bias_v_y = np.random.uniform(-0.5,0.5,size=(1, num_wyjsc))
        # tu jest funkcja błędu e z sumą
        self.e = []

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-self.Beta * x))

    def pochodna_sigmoid(self, x):
        return self.Beta * x * (1 - x)

    def pierwszy_etap(self, zbior_X):
        # ;) problem rozwiązany dobrze tylko w v1 i v2 muszą być różne wagi
        v1 = self.sigmoid(x=(self.dane_treningowe @ self.wagi_x_v1))
        v2 = self.sigmoid(x=(self.dane_treningowe @ self.wagi_x_v2))


        y = self.sigmoid(x=(v1*self.wagi_v_y[0][0]+v2*self.wagi_v_y[1][0]+1*self.wagi_v_y[2][0]))
        print('v1', y)
        # liczymy błąd kwadratowy d(n) - y
        epsilon = (self.d - y)
        self.e.append(0.5 *sum(epsilon ** 2))
        print('błąd kwadratowy:', epsilon)
        print('suma błędu kwadratowego:', self.e)
        return  v1, v2, y, epsilon, self.e

    def aktualizowanie_wag(self):
        v1, v2, y, epsilon, e = self.pierwszy_etap(dane_treningowe)

        # dla warstwy wyjściowej
        gradient_y_v1 = -epsilon*self.pochodna_sigmoid(y)*v1
        gradient_y_v2 = -epsilon*self.pochodna_sigmoid(y)*v2
        gradient_y_bias = -epsilon*self.pochodna_sigmoid(y)*1
        print('Blad w gradiencie',gradient_y_v1 )

        # nowe wagi
        # dla wag od v do y
        print('Nasz Blad gradient ',gradient_y_v1)
        print('Nasz Blad wagi ',self.wagi_v_y[0][0])
        print('Nasz Bla epsilon',epsilon)
        print('Nasz Blad pochodna sigmoidy',self.pochodna_sigmoid(y)*v1)
        self.wagi_v_y[0][0] = self.wagi_v_y[0][0] - self.gamma * gradient_y_v1
        self.wagi_v_y[1][0] = self.wagi_v_y[1][0] - self.gamma * gradient_y_v2
        self.wagi_v_y[2][0] = self.wagi_v_y[2][0] - self.gamma * gradient_y_bias

        # dla warstwy ukrytej
        gradient_v1_x1 = -epsilon*self.pochodna_sigmoid(y)*self.wagi_v_y[0][0] *self.pochodna_sigmoid(v1)*self.dane_treningowe.T[0]
        gradient_v1_x2 = -epsilon*self.pochodna_sigmoid(y)* self.wagi_v_y[0][0] *self.pochodna_sigmoid(v1)*self.dane_treningowe.T[1]


        gradient_v2_x1 = -epsilon * self.pochodna_sigmoid(y) * self.wagi_v_y[1][0] * self.pochodna_sigmoid(v2) * self.dane_treningowe.T[0]
        gradient_v2_x2 = -epsilon * self.pochodna_sigmoid(y) * self.wagi_v_y[1][0] * self.pochodna_sigmoid(v2) * self.dane_treningowe.T[1]

        gradient_v1_x0 = -epsilon * self.pochodna_sigmoid(y) * self.wagi_v_y[2][0] * self.pochodna_sigmoid(v1) * 1
        gradient_v2_x0 = -epsilon * self.pochodna_sigmoid(y) * self.wagi_v_y[2][0] * self.pochodna_sigmoid(v2) * 1


        # nowe wagi
        # dla wag x do v1
        self.wagi_x_v1[0][0] = self.wagi_x_v1[0][0]- self.gamma*gradient_v1_x1
        self.wagi_x_v1[0][1] = self.wagi_x_v1[0][1]- self.gamma*gradient_v1_x1

        self.wagi_x_v1[1][0] = self.wagi_x_v1[1][0]- self.gamma*gradient_v1_x2
        self.wagi_x_v1[1][1] = self.wagi_x_v1[1][1]- self.gamma*gradient_v1_x2

        self.wagi_x_v1[2][0] = self.wagi_x_v1[1][1]- self.gamma*gradient_v1_x0
        self.wagi_x_v1[2][1] = self.wagi_x_v1[1][1]- self.gamma*gradient_v1_x0

        # dla wag x do v2
        self.wagi_x_v2[0][0] = self.wagi_x_v2[0][0] - self.gamma * gradient_v2_x1
        self.wagi_x_v2[0][1] = self.wagi_x_v2[0][1] - self.gamma * gradient_v2_x1

        self.wagi_x_v2[1][0] = self.wagi_x_v2[1][0] - self.gamma * gradient_v2_x2
        self.wagi_x_v2[1][1] = self.wagi_x_v2[1][1] - self.gamma * gradient_v2_x2

        self.wagi_x_v2[2][0] = self.wagi_x_v2[1][1] - self.gamma * gradient_v2_x0
        self.wagi_x_v2[2][1] = self.wagi_x_v2[1][1] - self.gamma * gradient_v2_x0



    def trenuj(self):
        for _ in range(self.num_epok):
            self.pierwszy_etap(self.dane_treningowe)
            self.aktualizowanie_wag()

'''
2. Wykonać badania ekspertymentalne, których celem jest:
a) ocena wpływu współczynnika kształtu funkcji aktywacji "beta",
b) ocena wpływu współczynnika uczenia "gamma"
na przebieg procesu uczenia.
3. Wyniki przedstawić na wykresach pokazujących:
a) Przebieg błędu uczenia e(n) dla 3 różnych wartości "beta" i ustalonego "gamma",
b) Przebieg błędu uczenia e(n) dla 3 różnych wartości "gamma" i ustalonego "beta".
4. Sformułować wnioski
'''

mlp = MLP(dane_treningowe, d, 0.2, 3)
mlp.trenuj()