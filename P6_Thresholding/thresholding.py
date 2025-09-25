import cv2

# 1. Load image in grayscale
image = cv2.imread('./images/mural.jpg', cv2.IMREAD_GRAYSCALE)

# 2. Callback function for trackbar (does nothing here, needed for OpenCV)
def nothing(x):
    pass

# 3. Create a window
cv2.namedWindow('Binary Threshold Demo')

# 4. Create a trackbar for threshold value
cv2.createTrackbar('Threshold', 'Binary Threshold Demo', 127, 255, nothing)

while True:
    # 5. Get current threshold value from trackbar
    thresh_value = cv2.getTrackbarPos('Threshold', 'Binary Threshold Demo')

    # 6. Apply binary thresholding
    _, binary_thresh = cv2.threshold(image, thresh_value, 255, cv2.THRESH_BINARY)

    # 7. Display result
    cv2.imshow('Binary Threshold Demo', binary_thresh)

    # 8. Break loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
