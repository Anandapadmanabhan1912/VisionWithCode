import cv2
import numpy as np

# Load an image
img = cv2.imread("./images/numberplate.jpg")

# Get image dimensions
rows, cols = img.shape[:2]

# Define rotation matrix (rotate 45 degrees around center)
M = cv2.getRotationMatrix2D((cols/2, rows/2), -45, 1)  # (center, angle, scale)

# Apply affine transform
rotated = cv2.warpAffine(img, M, (cols, rows))

# Show results
cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
