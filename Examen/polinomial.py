
from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# data 
x = np.asarray([0,1,2,3,4,5,6,7,8,9])[:,np.newaxis]
y = np.asarray([1,5,20,60,90,120,180,220,340,410])[:,np.newaxis]
plt.scatter(x,y)

# regression transform
poly_degree =2
polynomial_features = PolynomialFeatures(degree = poly_degree)
x_transform = polynomial_features.fit_transform(x)

# fit the model
model = LinearRegression().fit(x_transform, y)
y_new = model.predict(x_transform)

# calculate rmse and r2
rmse = np.sqrt(mean_squared_error(y, y_new))
r2 = r2_score(y, y_new)
print('RMSE: ', rmse)
print('R2: ', r2)
print('v: ', r2)

# prediction
x_new_min = 0.0
x_new_max = 50.0

x_new = np.linspace(x_new_min, x_new_max, 50)
x_new = x_new[:,np.newaxis]

x_new_transform = polynomial_features.fit_transform(x_new)
y_new = model.predict(x_new_transform)

# plot the prediction
plt.plot(x_new, y_new, color='coral', linewidth=3)
plt.grid()
plt.xlim(x_new_min,x_new_max)
plt.ylim(0,10000)
title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(rmse,2), round(r2,2))
plt.title("Prediction of Infection of Covid-19 in Guatemala\n " + title, fontsize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.show()