from sklearn.decomposition import PCA
import pandas as pd
import csv
import matplotlib.pyplot as plt

X = pd.read_csv('Train_X_train1.csv', sep=';').values
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

pca_X_df = pd.DataFrame(data=X_pca, columns=['principal components 1', 'principal components 2', 'principal components 3'])


plt.figure(figsize=(6, 6))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Principal Component - 1', fontsize=10)
plt.ylabel('Principal Component - 2', fontsize=10)
plt.title("Principal Component Analysis of Train_X", fontsize=10)
X_pca1 = pca_X_df['principal components 1']
X_pca2 = pca_X_df['principal components 2']
X_pca3 = pca_X_df['principal components 3']

plt.scatter(X_pca1, X_pca2)
plt.show()
