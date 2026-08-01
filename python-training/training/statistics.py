import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import binom


# plt.hist(
#     data, bins=30, edgecolor="black", density=True, alpha=0.6, label="Data histogram"
# )
# x = np.linspace(min(data), max(data), 1000)
# pdf = stats.norm.pdf(x, loc=loc, scale=scale)
# plt.plot(x, pdf, color="red", linewidth=2, label="Theoritical PDF")
# plt.title("Normal distribution")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.legend()
# plt.grid(True)
# plt.show()

n = 10  # number of trials
p = 0.5  # probability of success
data = np.random.binomial(n=10, p=0.5, size=1000)

plt.hist(
    data,
    bins=np.arange(-0.5, n + 1.5, 1),
    density=True,
    edgecolor="black",
    alpha=0.7,
    label="Sample Data Histogram",
)
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n=n, p=p)
plt.scatter(x, pmf, color="red", label="Theoritical PMF")
plt.vlines(x, 0, pmf, colors="red", linestyles="dashed")
plt.title("Binomial Distribution(n=10,p=0.5)")
plt.xlabel("number of success")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.show()
