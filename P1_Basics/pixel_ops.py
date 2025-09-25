import cv2
import numpy as np

# Read the image
image = cv2.imread('./images/donald.jpg')

if image is None:
    print("Error: Image not found.")
else:
    # Access and print the value of a pixel at (100, 100)
    pixel = image[100, 100]
    print(f"Pixel value at (100, 100): {pixel}")

    # Change the pixel at (100, 100) to pure red (BGR format)
    image[100, 100] = [0, 0, 255]

    # Manipulate the blue channel: set all blue values to 0
    image[:, :, 0] = 0

    # Manipulate the green channel: increase green intensity by 50 (clip at 255)
    image[:, :, 1] = np.clip(image[:, :, 1] + 50, 0, 255)

    cv2.imshow('Manipulated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()