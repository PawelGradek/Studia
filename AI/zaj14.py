network = [[{'wagi': [0.9087377006253031, 0.5823594352860809, 0.03143984616958351, 0.10564217819589117, 0.6692112498008741, 0.21757197949975704, 0.11736293435352407, 0.4142394782437794], 'output': 0.9999985386379222}, {'wagi': [0.47667026682505576, 0.42748596255031535, 0.12074895763499827, 0.614044614746305, 0.02313877858224256, 0.5961122095760389, 0.08272433746297803, 0.8588058113428132], 'output': 0.9999535231415456}, {'wagi': [0.6998304846463939, 0.4998166426432127, 0.2972888933006296, 0.020381513763316095, 0.828405041341631, 0.2377295574353161, 0.7244379828955804, 0.951625368595201], 'output': 0.9999982201469491}, {'wagi': [0.6170700429875376, 0.41369638836433276, 0.0008309814596797471, 0.5873425862447117, 0.01249211430753927, 0.771195742665081, 0.23639399906397607, 0.10302667086864381], 'output': 0.9999835679868253}, {'wagi': [0.21451863056111575, 0.04820631076027804, 0.8604945323136874, 0.4389269310823436, 0.7329798431895064, 0.03127237601803201, 0.026899934868901076, 0.06170637711925908], 'output': 0.9931971389740972}], [{'wagi': [0.33512791664631736, 0.35322485613336707, 0.34089866854747797, 0.6440047074264649, 0.00615114658507232, 0.20738123764867067], 'output': 0.7197777198512899}, {'wagi': [0.5935217979725639, 0.19020750833991074, 0.11239063074769562, 0.8670645193831847, 0.6938339938681721, 0.34568083563614616], 'output': 0.802021589026915}, {'wagi': [0.21484689653870193, 0.08153839073590863, 0.6516010807894344, 0.19859531613372627, 0.35549495431811184, 0.7002918812709494], 'output': 0.7502546353219479}]]
wszystkie_gradienty = {}
'''def update_weights(network):
    for i in range(len(network)): # network =[  []        []   ] czyli i = [ { }         { }           { }    ...]
        print('to jest i ',network[i])
        if i != 9: # najpierw zmieniamy wagi dla wag ukryto-wyjsciowych
            for neuron in network[i]:  #neuron =  {'wagi':[] }
                print('to jest neuron ',neuron)
                for j in neuron['wagi']:
                    print(len(neuron['wagi']))
                    print('to jest j ',j)
                    for l in range(len(neuron['wagi'])):
                        print('tu jest znalezione', l)
                    #if neuron[j] != neuron[-1]:
update_weights(network)'''

def transfer_derivative(output,Beta=0.5):
    return Beta * output * (1.0 - output)

def backward_propagate_error(network, expected, Beta,x): # tu musisz pozmieniać gradienty/ network =[[],[]]
    for i in reversed(range(len(network))): # odwrócenie kolejności, jęsli mamy 2 element w network to mamy range(1,0), najpierw dla elementów neurony ukryte-wyjściowe a potem dla neuronów poczatkowe-ukryte
        layer = network[i] # []/ network
        gradienty_v_y = list()
        gradienty_x_v = list()
        gradienty_x_v_bias = list()
        gradienty_v_y_bias = list()
        if i != len(network) - 1: # i != 1 sztuczka żebyśmy pomineli ostatni element network/ to liczymy dla neuronów poczatkowe-ukryte
            for elem in range(len(x)):
                for j in range(len(layer)):
                    wagi = layer[j]
                    gradient = 0.0
                    for neuron in range(len(network[i + 1])): # kod od pocztku funkcji do tego momentu ma za zadanie przejśc do ostatniego elementu w sieci czyli do neuronów wyjściowych i liczymy gradient dla  wag neuronów ukrytych-wyjsciowych
                        neuron_2 = network[i+1][neuron]
                        # do tego momentu jest dobrze w 100%
                        gradient += (neuron_2['output'] - expected[neuron])*transfer_derivative(neuron_2['output'],Beta)*neuron_2['wagi'][j]
                    gradient = gradient*transfer_derivative(wagi['output'],Beta)*x[elem]
                    gradienty_x_v.append(gradient)
            print(gradienty_x_v)
            wszystkie_gradienty['gradienty_x_v'] = gradienty_x_v  # 35 gradientów

            for j in range(len(layer)):
                wagi = layer[j]
                gradient = 0.0
                for neuron in range(len(network[i + 1])):
                    neuron_2 = network[i + 1][neuron]
                    gradient += (neuron_2['output'] - expected[neuron]) * transfer_derivative(neuron_2['output'],Beta) * neuron_2['wagi'][j]
                gradient = gradient * transfer_derivative(wagi['output'], Beta) * 1
                gradienty_x_v_bias.append(gradient)
            print(gradienty_x_v_bias)
            wszystkie_gradienty['gradienty_x_v_bias'] = gradienty_x_v_bias  # 7 gradientów
            #print(gradienty_x_v_bias)
                # jeszcze trzeba zrobić dla biasu
                        #gradient += (neuron_2['wagi'][j] * neuron_2['delta'])# tu stosujemy gradient- delta
                    #gradienty_x_v.append(gradient)

        else: # tu liczymy dla neuronów ukryte-wyjsciowe/ liczymy to najpierw a potem to co jest u góry
            for j in range(len(layer)):
                neuron = layer[j]
                for k in network[0]:
                    gradienty_v_y.append((neuron['output'] - expected[j])*transfer_derivative(neuron['output'],Beta)*k['output']) # powinno być expected[j]-neuron['output']

                gradienty_v_y_bias.append((neuron['output'] - expected[j])*transfer_derivative(neuron['output'],Beta)*1) # tu liczymy  gradient dla biasu
            wszystkie_gradienty['gradienty_v_y'] = gradienty_v_y # 15 gradientów
            wszystkie_gradienty['gradienty_v_y_bias'] = gradienty_v_y_bias  # 3 gradienty


backward_propagate_error(network, [0,1,0], 0.5,[15.26,14.84,0.871,5.763,3.312,2.221,5.22])
#print(network['gradienty_v_y'])
print(wszystkie_gradienty)

l1= [1,2,3]
l2=[4,5]
k=[l1,l2]
s =sum(k,[])
print(s)

'''
# to nie musi być !!!!!!!!!!!!
# Split a dataset into k folds k krotna walidacja krzyżowa
def cross_validation_split(dataset, n_folds):
    dataset_split = [list(dataset)]
    print('datasetsplit',dataset_split)
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
    dataset_lista = cross_validation_split(dataset, n_folds) # [[dataset]] zwykle [  [f1]  [f2]  [f3] [f4] [f5]     ]
    scores = list()
    for fold in dataset_lista: # [f1]
        train_set = list(dataset_lista)# [[[dataset]]] zwykle  [[  [f1]  [f2]  [f3] [f4] [f5]     ]]
        #train_set.remove(fold) [[    [f2]  [f3] [f4] [f5]     ]]
        #train_set = sum(train_set, []) [ f2,f3,f4,f5]
        test_set = list()
        for row in fold: #[]
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores'''
