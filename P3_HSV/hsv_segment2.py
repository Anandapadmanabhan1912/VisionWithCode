import cv2
import numpy as np

# Load image
image = cv2.imread("./images/balls.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define HSV range
lower_blue = np.array([0, 102, 0])
upper_blue = np.array([179, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# --- Noise removal & enclosing operations ---
# Define kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Remove small noise (Opening = Erosion + Dilation)
mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Fill small holes inside the object (Closing = Dilation + Erosion)
mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel, iterations=2)

# Optional: Ensure we keep largest connected segments (remove stray blobs)
contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask_final = np.zeros_like(mask_clean)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:  # adjust threshold based on object size
        cv2.drawContours(mask_final, [cnt], -1, 255, thickness=cv2.FILLED)

# Apply mask on original image
result = cv2.bitwise_and(image, image, mask=mask_final)

# Show results
cv2.imshow("Original", image)
cv2.imshow("Mask - Raw", mask)
cv2.imshow("Mask - Clean", mask_final)
cv2.imshow("Segmented (Blue Parts)", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
