from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(42)


dane_treningowe = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]])

# d(n)
d = np.array(
    [
        [0],
        [1],
        [1],
        [0]])


class SN:
    def __init__(self, dane_treningowe, d, gamma=0.9, num_wejsc=2, num_ukrytych=2, num_wyjsc=1, Beta=0.9, bias=1):
        self.dane_treningowe = dane_treningowe
        self.d = d
        self.gamma = gamma
        self.Beta = Beta

        self.wagi_x_v = np.random.uniform(-0.5,0.5,size=(num_wejsc, num_ukrytych))
        self.wagi_v_y = np.random.uniform(-0.5,0.5,size=(num_ukrytych, num_wyjsc))

        self.wagi_bias_x_v = np.random.uniform(-0.5,0.5,size=(1, num_ukrytych))
        self.wagi_bias_v_y = np.random.uniform(-0.5,0.5,size=(1, num_wyjsc))
        # tu jest funkcja błędu e z sumą błąd kwadratowy
        self.e = []
        self.bias = bias


    def sigmoid(self, s):
        return 1 / (1 + np.exp(-self.Beta * s))

    def pochodna_sigmoid(self, s):
        return self.Beta * s * (1 - s)

    def funkcja_bledu(self):
        e = 0
        for i in self.d:
            for j in self.y:

                e = e + (i[0] - j[0])**2
        e = 0.5*e
        return e

    def aktualizowanie_wag(self):
        gradient_warstwy_ukrytej = self.dane_treningowe.T @ (((epsilon * self.pochodna_sigmoid(self.y)) * self.wagi_v_y.T) * self.pochodna_sigmoid(self.v))
        print("gradient warstwy ukrytej: ", gradient_warstwy_ukrytej)


        gradient_wyjscia = self.v.T @ (epsilon * self.pochodna_sigmoid(self.y))

        print("gradient wyjsia: ", gradient_wyjscia)



        self.wagi_x_v += self.gamma * gradient_warstwy_ukrytej
        self.wagi_v_y += self.gamma * gradient_wyjscia


        self.wagi_bias_x_v += np.sum(self.gamma * ((epsilon * self.pochodna_sigmoid(self.y)) * self.wagi_v_y.T) * self.pochodna_sigmoid(self.v), axis=0)
        self.wagi_bias_v_y += np.sum(self.gamma * epsilon * self.pochodna_sigmoid(self.y), axis=0)


    def pierwszy_etap(self, zbior_x):
        # x-wejscia [0.  0.]
        # v - warttwa ukryyta [[0.  0.],[0.  0.]]
        # y - wyjścia
        # va - x pomnożone przez wagi
        v = []
        v1 = 0
        for i in len(zbior_x):# 2
            for j in len(self.wagi_x_v):#2 elementy 2 elementowe
                if i == j:
                    v1 = v1 + zbior_x[i] * self.wagi_v_y[j][0]
        v1 = v1 + self.bias*self.wagi_bias_x_v[0][0]
        v1 = self.sigmoid(v1)
        v.append(v1)

        v2 = 0
        for i in len(zbior_x):  # 2
            for j in len(self.wagi_x_v):  # 2 elementy 2 elementowe
                if i == j:
                    v2 = v2 + zbior_x[i] * self.wagi_v_y[j][1]
        v2 = v2 + self.bias * self.wagi_bias_x_v[0][1]
        v2 = self.sigmoid(v2)
        v.append(v2)

        y = 0
        for i in len(v):
            for j in len(self.wagi_v_y):
                if i == j:
                    y = y + v[i]*self.wagi_v_y[j]
        y = y + self.bias*self.wagi_bias_v_y[0][0]
        y = self.sigmoid(y)





        self.v_0 = np.dot(zbior_x, self.wagi_x_v) + self.wagi_bias_x_v
        self.v = self.sigmoid(self.v_0)

        self.y_0 = np.dot(self.v, self.wagi_v_y) + self.wagi_bias_v_y
        self.y = self.sigmoid(self.y_0)

        return self.y


    def trenuj(self, num_epok):
        self.epoka =1
        flag = True

        while flag:
            self.pierwszy_etap(self.dane_treningowe)
            self.aktualizowanie_wag()

            num_epok= num_epok-1

            self.y_sklasyfikowane = []
            print('tu jest klasyfikacja', self.y_sklasyfikowane)
            if float(self.y[0][0]) > 0.5:
                self.y_sklasyfikowane.append(1)
            else:
                self.y_sklasyfikowane.append(0)
            if float(self.y[1][0]) > 0.5:
                self.y_sklasyfikowane.append(1)
            else:
                self.y_sklasyfikowane.append(0)
            if float(self.y[2][0]) > 0.5:
                self.y_sklasyfikowane.append(1)
            else:
                self.y_sklasyfikowane.append(0)
            if float(self.y[3][0]) > 0.5:
                self.y_sklasyfikowane.append(1)
            else:
                self.y_sklasyfikowane.append(0)

            if self.y_sklasyfikowane[0] == 0 and self.y_sklasyfikowane[1] == 1 and self.y_sklasyfikowane[2] == 1 and self.y_sklasyfikowane[3] == 0 :
                print('Koniec iteracji nastąpił warunek stopu')
            else:
                # num_epok = num_epok + 1
                self.epoka = self.epoka+1
            if num_epok > 0:
                flag = True
            else:
                flag = False


    def wykresy(self):
        losses = np.zeros((self.epoka, 1))
        for i in range(self.epoka):
            losses[i, 0] = self.cost
        # Evaluating the performance
        plt.figure()
        plt.plot(losses)
        plt.xlabel("Epoka")
        plt.ylabel("Wartość funkcji błędu")
        plt.show()


sn = SN(dane_treningowe, d, 0.2)
sn.trenuj(num_epok=1000)
sn.wykresy()