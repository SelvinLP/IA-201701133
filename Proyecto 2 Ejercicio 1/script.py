import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

resultArray = np.array([[8,2],[9,7],[2,12], 
                        [9,1],[10,7],[3,14],
                        [8,1],[1,13]])

r_kmeans = KMeans(n_clusters=3)
r_kmeans.fit(resultArray)

# Imprimir log
print(r_kmeans.cluster_centers_)

# Codigo para mostrar la grafica final
plt.scatter(X[:,0],X[:,1] , c =r_kmeans.labels_ , cmap='rainbow')
plt.show()