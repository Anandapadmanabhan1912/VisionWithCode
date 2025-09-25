import cv2
import numpy as np

def posterize(image, levels=4):
    """
    Posterize image by reducing number of intensity levels per channel.
    levels = number of color bins (e.g., 2, 4, 8, 16).
    """
    # Ensure levels are valid
    levels = max(2, min(levels, 256))
   

    # Quantization step size
    step = 256 // levels

    # Quantize each pixel
    posterized = (image // step) * step + step // 2

    return posterized

# Load image
image = cv2.imread("./images/donald1.jpg")
image = cv2.resize(image, (600, 400))
# Apply posterization (try different levels: 2, 4, 8, etc.)
posterized_img = posterize(image, levels=9)

# Show results
cv2.imshow("Original", image)
cv2.imshow("Posterized", posterized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
