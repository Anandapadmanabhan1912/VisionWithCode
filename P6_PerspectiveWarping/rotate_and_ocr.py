import cv2
import numpy as np
import pytesseract

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -angle, 1.0)  # negative for clockwise
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    rotated = rotate_image(image, 45)
    gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    return binary

def extract_text(binary_image):
    text = pytesseract.image_to_string(binary_image)
    return text

if __name__ == "__main__":
    image_path = "./images/numberplate.jpg"  # Change to your image path
    binary_image = preprocess_image(image_path)
    text = extract_text(binary_image)
    cv2.imshow("Binary Image", binary_image)
    cv2.imwrite("binary_output.jpg", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Extracted Text:\n", text)