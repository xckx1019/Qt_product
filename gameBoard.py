import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw rectangle(not filled)
cv2.rectangle(img,(15,20),(70,50),(0,255,0),3)

# Draw filled rectangle
cv2.rectangle(img,(115,120),(170,150),(255,0,0),-1)

#Display the image
cv2.imshow("img",img)

cv2.waitKey(0)