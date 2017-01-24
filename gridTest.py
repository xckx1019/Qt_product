import matplotlib.pyplot as plt
import numpy as np

nrows, ncols = 8, 8
image = np.zeros((nrows, ncols))

# Set every other cell to a random number (this would be your data)
image[3, 4] = 1.0

# Reshape things into a 8x8 grid.
#image = image.reshape((nrows, ncols))

row_labels = range(nrows)
col_labels = range(ncols)
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.grid(True)
plt.show()