import matplotlib.pyplot as plt
import numpy as np

# Make a 9x9 grid...
nrows, ncols = 8,8
image = np.zeros(nrows*ncols)

# Set every other cell to a random number (this would be your data)
image[::2] = np.random.random(32)

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols))

row_labels = range(nrows)
col_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()