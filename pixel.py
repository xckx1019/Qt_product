import cv2
import numpy as np

# Parameters
jpg_offset_row = 3
jpg_offset_col = 6

step = 10
out_size = 300

line_color = (0, 255, 255)
center_color = (0, 0, 255)

# Initialize white background
grid = np.ones((step*8+9, step*8+9, 3), np.uint8)*255

# Create the grid
for idx in range(9):
    ctr = (step+1)*idx
    grid[:, ctr] = 0
    grid[ctr, :] = 0

for col in range(8):
        left_x = (step + 1) * col + 1
        right_x = (step + 1) * (col + 1) - 1
        top_y = (step + 1) * jpg_offset_row + 1
        bottom_y = (step + 1) * (jpg_offset_row + 1) - 1

        corners = np.asarray(
        [(left_x, top_y),
         (right_x, top_y),
         (right_x, bottom_y),
         (left_x, bottom_y)]
        )

        cv2.fillConvexPoly(grid, corners, line_color)

for row in range(8):
        left_x = (step + 1) * jpg_offset_col + 1
        right_x = (step + 1) * (jpg_offset_col + 1) - 1
        top_y = (step + 1) * row + 1
        bottom_y = (step + 1) * (row + 1) - 1

        corners = np.asarray(
                [(left_x, top_y),
                (right_x, top_y),
                (right_x, bottom_y),
                (left_x, bottom_y)]
        )


        cv2.fillConvexPoly(grid, corners, line_color)

left_x2 = (step + 1) * jpg_offset_col + 1
right_x2 = (step + 1) * (jpg_offset_col + 1) - 1
top_y2 = (step + 1) * jpg_offset_row + 1
bottom_y2 = (step + 1) * (jpg_offset_row + 1) - 1
corners2 = np.asarray(
        [(left_x2, top_y2),
         (right_x2, top_y2),
         (right_x2, bottom_y2),
         (left_x2, bottom_y2)]
    )

cv2.fillConvexPoly(grid, corners2, center_color)
grid = cv2.resize(grid, (out_size, out_size), interpolation=cv2.INTER_NEAREST)


cv2.imshow('test', grid)
cv2.waitKey(-1)