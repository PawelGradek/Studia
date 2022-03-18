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
    def __init__(self, dane_treningowe, d, gamma=0.9, num_wejsc=2, num_ukrytych=2, num_wyjsc=1, Beta=0.9):
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
    def pr(self):
        print('self.wagi_x_v',self.wagi_x_v)
        print('self.wagi_v_y',self.wagi_v_y)
        print('self.wagi_bias_x_v',self.wagi_bias_x_v)
        print('self.wagi_bias_v_y',self.wagi_bias_v_y)
        print('$$'*20)
        print('self.wagi_x_v', self.wagi_x_v)
        print('self.wagi_v_y', self.wagi_v_y)
        print('self.wagi_bias_x_v', self.wagi_bias_x_v)
        print('self.wagi_bias_v_y', self.wagi_bias_v_y)


sn = SN(dane_treningowe, d, 0.2)
#sn.pr()
num_wejsc=2
num_ukrytych=3
x = np.random.uniform(-0.5,0.5,size=(num_wejsc, num_ukrytych))
print(x)
