from sklearn.decomposition import PCA
import pandas as pd
# import csv
import matplotlib.pyplot as plt

X = pd.read_csv('Train_X_train1.csv', sep=';').values
pca = PCA(n_components=20)
X_pca = pca.fit_transform(X)
principalDf = pd.DataFrame(data=X_pca, columns=[f'principal component {i}'for i in range(1, 21)])
print(principalDf)

# 2D

components_to_2d_visualization = (1, 2)
data_2d = []
for i in range(1, 12):
    # dane = ldaDF[ldaDF[f'principal component {i}'] == i+1]
    data_2d.append(principalDf[f'principal component {i}']) #for i in components_to_2d_visualization]
fig1 = plt.figure()
ax1 = fig1.add_subplot()
for i in range(12):
    ax1.scatter(data_2d[3], data_2d[1], label=f'{i+1}') #

ax1.set_xlabel(f'Principal component 1')
ax1.set_ylabel(f'Principal component 2')
ax1.legend()
plt.show()

# 3D
'''
components_to_3d_visualization = (1, 3, 2)
tab_3d = []
for i in range(12):
    dane = ldaDF#[ldaDF['test label'] == i+1]
    tab_3d.append([dane[f'pricipal component {i}'] for i in components_to_3d_visualization])
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
for i in range(12):
    ax2.scatter(tab_3d[i][0], tab_3d[i][1], tab_3d[i][2], label=f'{i+1}')
ax2.set_xlabel(f'Principal component{components_to_3d_visualization[0]}')
ax2.set_ylabel(f'Principal component{components_to_3d_visualization[1]}')
ax2.set_zlabel(f'Principal component{components_to_3d_visualization[2]}')
ax2.legend()'''