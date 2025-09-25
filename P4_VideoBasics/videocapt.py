import cv2
import os

# Create output directory if it doesn't exist
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

# Open the default camera (0 is usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Get the default video frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of the frames in the video stream
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height of the frames in the video stream

# Define the codec and create VideoWriter object
# Arguments:
#   'mp4v' - FourCC code for mp4 format
#   20.0   - Frames per second
#   (frame_width, frame_height) - Size of the video frames
out = cv2.VideoWriter(
    os.path.join(output_dir, 'output.mp4'),
    cv2.VideoWriter_fourcc(*'mp4v'),
    20.0,
    (frame_width, frame_height)
)

while True:
    ret, frame = cap.read()  # ret: True if frame is read correctly, frame: the captured frame
    if not ret:
        break

    out.write(frame)  # Write the frame to the output file

    cv2.imshow('Video Feed', frame)  # Display the frame

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()