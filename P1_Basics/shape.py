import cv2
import numpy as np

# Read an image
image = cv2.imread("./images/donald.jpg")

# Print pixel values (just a small region, since printing all is too big)
print("Top-left corner pixel [B, G, R]:", image[0, 0])  
print("Pixel at (50, 100):", image[50, 100])  

# Print shape of the image
# Format: (height, width, channels)
print("Image shape:", image.shape)

# Print color space (default in OpenCV is BGR)
print("Color space: BGR (Blue, Green, Red)")
