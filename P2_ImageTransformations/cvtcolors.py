import cv2
import numpy as np

def convert_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or unable to read.")

    # Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to GBR (swap channels: BGR -> GBR)
    gbr = img.copy()
    temp = gbr[:, :, 0].copy()  # Save Blue
    gbr[:, :, 0] = gbr[:, :, 1] # G → B
    gbr[:, :, 1] = temp         # B → G  # Swap B and G channels

    return gray, rgb, gbr

# Example usage:
if __name__ == "__main__":
    image_path = "./images/donald1.jpg"  # Change to your image path
    gray, rgb, gbr = convert_image(image_path)
    cv2.imwrite("output_gray.jpg", gray)
    cv2.imwrite("output_rgb.jpg", cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))  # Save as BGR for OpenCV
    cv2.imwrite("output_gbr.jpg", gbr)