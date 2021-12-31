import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pred.csv",sep=",")
X=df['C'].values


lista_x=[]
for y in range(1,31):
    lista_x.append(y)


reg = LinearRegression().fit(lista_x,np.array([X]))
#print(reg)
#reg.predict(np.array([[3, 5]]))
print(lista_x)
print(X)