import cv2
import numpy as np

# Load an image
img = cv2.imread("./images/numberplate.jpg")

# Get image dimensions
rows, cols = img.shape[:2]


# Define an affine transform matrix manually
# Example: rotation + translation
theta = np.radians(30)
cos_t, sin_t = np.cos(theta), np.sin(theta)

# Rotation + translation
M = np.float32([[cos_t, -sin_t, 50],   # shift x by 50
                [sin_t,  cos_t, 30]])  # shift y by 30

transformed = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Affine Rotation + Translation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
