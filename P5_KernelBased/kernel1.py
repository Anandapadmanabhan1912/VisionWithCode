import cv2
import numpy as np

def apply_custom_kernel(image, kernel):
    """
    Apply a custom convolution kernel to an image.
    """
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

# Load image
image = cv2.imread("./images/donald1.jpg")
image = cv2.resize(image, (600, 400))
cv2.imshow("Original", image)

# Example 3x3 kernels 
kernels = {
    "identity": np.array([[0,0,0],[0,1,0],[0,0,0]], dtype=np.float32),
    "sharpen": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], dtype=np.float32),
    "box_blur": np.ones((3,3), dtype=np.float32) / 9,
    "edge_detect": np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], dtype=np.float32),
    "emboss": np.array([[-2,-1,0],[-1,1,1],[0,1,2]], dtype=np.float32)
}


                   
for name, k in kernels.items():
    result = apply_custom_kernel(image, k)
    cv2.imshow(f"{name}", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


