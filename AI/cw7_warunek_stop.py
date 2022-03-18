import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x, Beta=0.5):
    return 1 / (1 + np.exp(-Beta * x))

def pochodna_sigmoid(x, Beta=0.05):
    return Beta * x * (1 - x)


def inicjalizacja_parametrow( num_wejsc=2, num_ukrytych=2, num_wyjsc=1,gamma=0.9,):


    wagi_x_v = np.random.uniform(-0.5, 0.5, size=(num_ukrytych,num_wejsc))
    wagi_v_y = np.random.uniform(-0.5, 0.5, size=(num_wyjsc,num_ukrytych))

    wagi_bias_x_v = np.random.uniform(-0.5, 0.5, size=(num_ukrytych,1))
    wagi_bias_v_y = np.random.uniform(-0.5, 0.5, size=(num_wyjsc,1))

    parametry = {"W1": wagi_x_v, "b1": wagi_bias_x_v,
                  "W2": wagi_v_y, "b2": wagi_bias_v_y}
    return parametry



def pierwszy_etap(X, Y, parametry):
    m = X.shape[1]
    wagi_x_v = parametry["W1"]
    wagi_v_y = parametry["W2"]
    wagi_bias_x_v = parametry["b1"]
    wagi_bias_v_y = parametry["b2"]

    Z1 = np.dot(wagi_x_v, X) + wagi_bias_x_v
    A1 = sigmoid(Z1)
    Z2 = np.dot(wagi_v_y, A1) + wagi_bias_v_y
    A2 = sigmoid(Z2)

    pamiec = (Z1, A1, wagi_x_v, wagi_bias_x_v, Z2, A2, wagi_v_y, wagi_bias_v_y)
    e_0 = np.multiply(np.log(A2), Y) + np.multiply(np.log(1 - A2), (1 - Y))
    e = -np.sum(e_0) / m
    return e, pamiec, A2



def propagacja_wsteczna(X, Y, pamiec):
    m = X.shape[1]
    (Z1, A1, wagi_x_v, wagi_bias_x_v, Z2, A2, wagi_v_y, wagi_bias_v_y) = pamiec

    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T) / m
    db2 = np.sum(dZ2, axis=1, keepdims=True)

    dA1 = np.dot(wagi_v_y.T, dZ2)
    dZ1 = np.multiply(dA1, pochodna_sigmoid(A1))
    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m

    gradienty = {"dZ2": dZ2, "dW2": dW2, "db2": db2,
                 "dZ1": dZ1, "dW1": dW1, "db1": db1}
    return gradienty



def aktualizacja_parametrow(parametry, gradient, gamma):
    parametry["W1"] = parametry["W1"] - gamma * gradient["dW1"]
    parametry["W2"] = parametry["W2"] - gamma * gradient["dW2"]
    parametry["b1"] = parametry["b1"] - gamma * gradient["db1"]
    parametry["b2"] = parametry["b2"] - gamma * gradient["db2"]
    return parametry


X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
Y = np.array([[0, 1, 1, 0]])


# definiowanie parametrów modelu
num_ukrytych = 2
num_wejsc = X.shape[0]
num_wyjsc = Y.shape[0]
parametry = inicjalizacja_parametrow(num_wejsc, num_ukrytych, num_wyjsc)
epoch = 2000
gamma = 0.01
e = np.zeros((epoch, 1))

for i in range(epoch):
     e[i, 0], pamiec, A2 = pierwszy_etap(X, Y, parametry)
     gradienty = propagacja_wsteczna(X, Y, pamiec)
     parametry = aktualizacja_parametrow(parametry, gradienty, gamma)
epoka=1

def trenuj(epoka):
    epoka =1
    flag = True

    while flag:
        e[epoka, 0], pamiec, A2 = pierwszy_etap(X, Y, parametry)

        epoka = epoka-1

        y_sklasyfikowane = []
        print('tu jest klasyfikacja', y_sklasyfikowane)
        if float(A2[0][0]) > 0.5:
            y_sklasyfikowane.append(1)
        else:
            y_sklasyfikowane.append(0)
        if float(A2[1][0]) > 0.5:
            y_sklasyfikowane.append(1)
        else:
            y_sklasyfikowane.append(0)
        if float(A2[2][0]) > 0.5:
            y_sklasyfikowane.append(1)
        else:
            y_sklasyfikowane.append(0)
        if float(A2[3][0]) > 0.5:
            y_sklasyfikowane.append(1)
        else:
            y_sklasyfikowane.append(0)

        if y_sklasyfikowane[0] == 0 and y_sklasyfikowane[1] == 1 and y_sklasyfikowane[2] == 1 and y_sklasyfikowane[3] == 0 :
            print('Koniec iteracji nastąpił warunek stopu')
        else:
            # num_epok = num_epok + 1
            epoka = epoka+1
        if epoka > 0:
            flag = True
        else:
            flag = False




plt.figure()
plt.plot(e)
plt.xlabel("EPOCHS")
plt.ylabel("Loss value")
plt.show()


X = np.array([[1, 1, 0, 0], [0, 1, 0, 1]])
cost, _, A2 = pierwszy_etap(X, Y, parametry)
print(A2)
prediction = (A2 > 0.5) * 1.0

print(prediction)