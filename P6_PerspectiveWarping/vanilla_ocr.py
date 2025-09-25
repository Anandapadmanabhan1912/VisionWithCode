import pytesseract
from PIL import Image
import os.path as path

# Path to your image file
#image_path = './images/numberplate.jpg'
image_path = 'warped_output.jpg'
image_path = path.join(path.dirname('images'), image_path)
image_path = path.abspath(image_path)

# Open the image
image = Image.open(image_path)

# Extract text using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted text: ", text)














# import cv2
# import pytesseract
# import numpy as np

# # Load image
# img = cv2.imread("warped_output.jpg", cv2.IMREAD_GRAYSCALE)

# # Threshold (adaptive works better here)
# thresh = cv2.adaptiveThreshold(img, 255,
#                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                cv2.THRESH_BINARY, 41, 11)

# # Morph close to reduce background pattern
# kernel = np.ones((3,3), np.uint8)
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# # Optional: dilate slightly to thicken text
# dilated = cv2.dilate(morph, kernel, iterations=1)

# # OCR
# custom_config = r'--oem 3 --psm 6'
# text = pytesseract.image_to_string(dilated, config=custom_config)

# print(text)
