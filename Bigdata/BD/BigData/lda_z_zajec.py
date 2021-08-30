import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt

x = pd.read_csv("Train_X_train1.csv", sep=';',names=[i+1 for i in range(561)])
x = StandardScaler().fit_transform(x)
y = pd.read_csv("Train_y_train.csv", names=['action'])
print(x)

lda = LinearDiscriminantAnalysis(n_components=50)
linearAnalysis = lda.fit_transform(x, y)
ldaDF = pd.DataFrame(data=linearAnalysis, columns=[f'component {i}' for i in range(1, 12)]) # zamiast 12 ma być 51
ldaDF = pd.concat([y, ldaDF], axis=1)
print(ldaDF)


visualisation_2d = (1, 2)
tab_2d = []
for i in range(12):
  data = ldaDF[ldaDF['action'] == i + 1]
  tab_2d.append([data[f'component {i}'] for i in visualisation_2d])
fig1 = plt.figure()
ax1 = fig1.add_subplot()
for i in range(12):
  ax1.scatter(tab_2d[i][0], tab_2d[i][1], label=f'{i + 1}')
ax1.set_xlabel(f'Component {visualisation_2d[0]}')
ax1.set_ylabel(f'Component {visualisation_2d[1]}')
ax1.legend()


visualisation_3d = (1, 2, 3)
tab_3d = []
for i in range(12):
  data = ldaDF[ldaDF['action'] == i + 1]
  tab_3d.append([data[f'component {i}'] for i in visualisation_3d])
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
for i in range(12):
  ax2.scatter(tab_3d[i][0], tab_3d[i][1], tab_3d[i][2], label=f'{i + 1}')
ax2.set_xlabel(f'Component {visualisation_3d[0]}')
ax2.set_ylabel(f'Component {visualisation_3d[1]}')
ax2.set_zlabel(f'Component {visualisation_3d[2]}')
ax2.legend()
plt.show()
