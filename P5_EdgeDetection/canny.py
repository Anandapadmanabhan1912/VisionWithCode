import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("./images/girl.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# Preprocess
blur = cv2.GaussianBlur(gray, (5,5), 1.4)

# Apply Canny
#edges = cv2.Canny(blur, 50, 150)
edges = cv2.Canny(gray, 30, 100)  # More sensitive

# Display
plt.subplot(1,2,1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.subplot(1,2,2), plt.imshow(edges, cmap='gray')
plt.title("Edges (Canny)")
plt.show()
