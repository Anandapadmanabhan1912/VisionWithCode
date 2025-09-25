import cv2 as cv

# Capture video from the default camera (0)
cap = cv.VideoCapture(0)
if not cap.isOpened():  
    print("Error: Could not open video.")
    exit()
while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        print("Error: Could not read frame.")
        break
    cv.imshow('Video Frame', frame)  # Display the frame
    if cv.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key
        break   
cap.release()  # Release the capture object
cv.destroyAllWindows()  # Close all OpenCV windows  