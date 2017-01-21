import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1977)
x, y, z = np.random.random((3, 10))

# Bin the data onto a 10x10 grid
# Have to reverse x & y due to row-first indexing
zi, yi, xi = np.histogram2d(y, x, bins=(8, 8), weights=z, normed=False)
zi = np.ma.masked_equal(zi, 0)

fig, ax = plt.subplots()
ax.pcolormesh(xi, yi, zi, edgecolors='black')
scat = ax.scatter(x, y, c=z, s=200)
fig.colorbar(scat)
ax.margins(0.05)

plt.show()