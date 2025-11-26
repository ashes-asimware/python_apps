from scipy.cluster.vq import kmeans, whiten, vq
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.optimize import curve_fit

# call loadtxt from scipy to load the diabetes dataset
dataset = np.loadtxt("data\\diabetes-train.csv", delimiter=",")
dataset = dataset[:, 0:8]  # Exclude the last column (labels)
dataset = whiten(dataset)
centroids, mean_dist = kmeans(dataset, 2)
clusters, dist = vq(dataset, centroids)
plt.scatter(dataset[:, 0], dataset[:, 1], c=clusters)
nondiabetic = dataset[clusters == 0]
diabetic = dataset[clusters == 1]
# plt.pie([len(nondiabetic), len(diabetic)], labels=["Non-Diabetic", "Diabetic"])
# plt.show()

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4.3, 7.2, 18.6, 53.5])


# create lamda function to calculate exponential
def exp_func(a, b, x):
    return a * np.exp(b * x)


# use curve_fit to fit the exponential function to the data
params, covariance = curve_fit(exp_func, x, y, p0=(1, 0.5))
# generate x values for the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
# generate y values using the fitted parameters
y_fit = exp_func(params[0], params[1], x_fit)
# plot the original data and the fitted curve
plt.scatter(x, y, label="Data Points")
plt.plot(x_fit, y_fit, label="Fitted Curve")
plt.legend()
plt.show()
