import cv2
import numpy as np

# Load image
image = cv2.imread("./images/balls.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for blue color in HSV
# The following values are a broader range for a wider spectrum of 'blue'
# You can adjust these values for more specific shades
lower_blue = np.array([0, 102, 0]) 
upper_blue = np.array([179, 255, 255])

# Create a mask for the blue color
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask to the original image to get the blue parts
result = cv2.bitwise_and(image, image, mask=mask)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Mask (Blue Parts)", mask)
cv2.imshow("Segmented Result", result)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()