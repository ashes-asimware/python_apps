import numpy as np

# Normal distribution
mu, sigma = 0, 0.1  # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
print("Normal Distribution Sample:")
print(s[:10])  # Print first 10 samples
# Binomial distribution
n, p = 10, 0.5  # number of trials, probability of
s = np.random.binomial(n, p, 1000)
print("Binomial Distribution Sample:")
print(s[:10])  # Print first 10 samples
# Poisson distribution
lam = 5.0  # rate (lambda)
s = np.random.poisson(lam, 1000)
print("Poisson Distribution Sample:")
print(s[:10])  # Print first 10 samples

