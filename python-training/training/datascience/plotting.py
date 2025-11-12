# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.stats as stats
# from scipy.stats import binom
# import pandas as pd


# def plot_binomial_distribution(n, p):
#     # Define the range of x values (number of successes)
#     x = np.arange(0, n + 1)

#     # Calculate the binomial probability mass function (PMF)
#     pmf = binom.pmf(x, n, p)

#     # Create the plot
#     plt.figure(figsize=(10, 6))
#     plt.bar(x, pmf, color="skyblue", alpha=0.7)
#     plt.title(f"Binomial Distribution (n={n}, p={p})")
#     plt.xlabel("Number of Successes")
#     plt.ylabel("Probability")
#     plt.xticks(x)
#     plt.grid(axis="y")

#     # Show the plot
#     plt.show()


# # Example usage
# n = 10  # number of trials
# p = 0.5  # probability of success
# plot_binomial_distribution(n, p)
# To run the example, simply call the function with desired n and p values.
