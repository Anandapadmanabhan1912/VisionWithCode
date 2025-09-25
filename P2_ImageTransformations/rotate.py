import cv2

# Load the image
image = cv2.imread('./images/donald1.jpg')  # Replace 'input.jpg' with your image path

prerotate = cv2.resize(image, (400, 200))


cv2.imshow('Original Image', prerotate)
# Rotate the image by 90 degrees clockwise
rotated = cv2.rotate(prerotate, cv2.ROTATE_90_CLOCKWISE)


# Display the rotated image
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()