import cv2

# Variables to store cropping coordinates
cropping = False
x_start, y_start, x_end, y_end = -1, -1, -1, -1

def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, cropping, image, clone

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start = x, y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            img_copy = clone.copy()
            cv2.rectangle(img_copy, (x_start, y_start), (x, y), (0,255,0), 2)
            cv2.imshow("Image", img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        cropping = False
        cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0,255,0), 2)
        cv2.imshow("Image", image)
        # Crop and save
        if x_start != x_end and y_start != y_end:
            roi = clone[min(y_start, y_end):max(y_start, y_end), min(x_start, x_end):max(x_start, x_end)]
            cv2.imwrite("./images/cropped_image.jpg", roi)
            print("Cropped image saved as cropped_image.jpg")

# Read image
image = cv2.imread("./images/donald.jpg")  # Change filename as needed
clone = image.copy()

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_crop)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()