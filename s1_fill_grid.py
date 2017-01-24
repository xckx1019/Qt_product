import cv2
import numpy as np

def fill_square(grid,step,col,row,color):
    # Determine the corners
    left_x = (step + 1) * (col) + 1
    right_x = (step + 1) * (col + 1) - 1
    top_y = (step + 1) * (row) + 1
    bottom_y = (step + 1) * (row + 1) - 1

    corners = np.asarray(
        [(left_x, top_y),
         (right_x, top_y),
         (right_x, bottom_y),
         (left_x, bottom_y)]
    )

    # Fill in the central point
    cv2.fillConvexPoly(grid, corners, color)

    return grid


# Parameters
jpg_offset_row = 3
jpg_offset_col = 6

step = 10
out_size = 400

line_color = (0,255,255)
center_color = (0,0,255)

# Initialize white background
grid = np.ones((step*8+9,step*8+9,3),np.uint8)*255

# Create the grid
for idx in range(9):
    ctr = (step+1)*(idx)
    grid[:,ctr] = 0
    grid[ctr,:] = 0

# Fill line and column
for col in range(8):
    grid = fill_square(grid,step,col,jpg_offset_row,line_color)
for row in range(8):
    grid = fill_square(grid,step,jpg_offset_col,row,line_color)

# Fill the center
grid = fill_square(grid,step,jpg_offset_col,jpg_offset_row,center_color)

grid = cv2.resize(grid,(out_size,out_size),interpolation=cv2.INTER_NEAREST)

cv2.imshow('test', grid)
cv2.waitKey(-1)