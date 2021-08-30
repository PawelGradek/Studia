import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

x = pd.read_csv("Train_X_train1.csv", sep=';',names=[i+1 for i in range(561)])
x = StandardScaler().fit_transform(x)
y = pd.read_csv("Train_y_train.csv", names=['test label'])
print(x)

pca = PCA(n_components=50)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = [f'principal component {i}' for i in range(1,51)])
principalDf = pd.concat([y,principalDf],axis=1)
print(principalDf)

exp_var = pca.explained_variance_ratio_
import matplotlib.pyplot as plt
#%matplotlib inline
x = [i for i in range(50)]
plt.bar(x,exp_var)


components_to_2d_visualisation=(1,2)
data_2d = []
for i in range(12):
  data = principalDf[principalDf['test label'] == i+1]
  data_2d.append([data[f'principal component {i}'] for i in components_to_2d_visualisation])
fig1 = plt.figure()
ax1 = fig1.add_subplot()
for i in range(12):
  ax1.scatter(data_2d[i][0],data_2d[i][1], label=f'comp {i+1}')
ax1.set_xlabel(f'Principal component {components_to_2d_visualisation[0]}')
ax1.set_ylabel(f'Principal component {components_to_2d_visualisation[1]}')
ax1.legend()

components_to_3d_visualisation=(1,2,3)
data_3d = []
for i in range(12):
  data = principalDf[principalDf['test label'] == i+1]
  data_3d.append([data[f'principal component {i}'] for i in components_to_3d_visualisation])
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
for i in range(12):
  ax2.scatter(data_3d[i][0],data_3d[i][1],data_3d[i][2], label=f'{i+1}')
ax2.set_xlabel(f'Principal component {components_to_3d_visualisation[0]}')
ax2.set_ylabel(f'Principal component {components_to_3d_visualisation[1]}')
ax2.set_zlabel(f'Principal component {components_to_3d_visualisation[2]}')
ax2.view_init(30,60)
ax2.legend()
plt.show()


