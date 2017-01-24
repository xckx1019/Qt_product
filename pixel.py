import numpy as np
import matplotlib.pyplot as plt

X = 10 * np.random.rand(8, 8)
print X
fig, ax = plt.subplots()
ax.imshow(X, interpolation='nearest')

numrows, numcols = X.shape


def format_coord(x, y):
    col = int(x)
    row = int(y)
    if col >= 0 and col < numcols and row >= 0 and row < numrows:
        z = int(X[row, col])
        return 'x=%1.4f, y=%1.4f, z=%1.4f' % (x, y, z)
    else:
        return 'x=%1.4f, y=%1.4f' % (x, y)

#ax.format_coord = format_coord
plt.show()