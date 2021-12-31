import numpy as np
X = np.array([[10.5,1,400.5,True],[9.8,5,405.8,False],[11.2,20,410.9,False],
[9.2,60,425.4,False],[9.1,90,450.1,True],[10.8,120,500.5,True],[11.5,180,575.7,False],
[11.2,220,456.5,True],[10.3,340,320.1,True],[9.7,410,221.9,False]])
Y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[100,0,100,False]]))