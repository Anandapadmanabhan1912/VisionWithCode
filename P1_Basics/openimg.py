import cv2

# Read the image (replace 'face.jpg' with your image filename)
image = cv2.imread('./images/donald.jpg')

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()