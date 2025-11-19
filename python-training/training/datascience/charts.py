import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4]
y = [0, 1.4, 9, 16]
fig, ax = plt.subplots()
ax.plot(x, y, marker="o", label="Data Points")
ax.set_title("Sample Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
plt.show()

x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x**2 + y**3)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z, cmap="viridis", edgecolors="green")
plt.title("3D Surface Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
heatmap = plt.imshow(data, cmap="coolwarm", interpolation="nearest")
plt.title("Heatmap")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar(heatmap)
plt.show()

# use mplot3d to plot a 3D scatter plot with linspace
x = np.linspace(0, 1, 100)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(x, x**2, x**3, c=x, cmap="plasma")
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()

# create a 3d histogram with random data
data = np.random.normal(size=1000)
fig = plt.figure()
ax = plt.axes(projection="3d")
hist, xedges, yedges = np.histogram2d(data, data, bins=30)
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
ax.bar3d(xpos.ravel(), ypos.ravel(), 0, 1, 1, hist.ravel(), zsort="average")
ax.set_title("3D Histogram")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
