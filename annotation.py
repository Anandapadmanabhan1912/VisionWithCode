import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype="uint8")
cv2.line(canvas, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(canvas, (384, 0), (510, 128), (0, 255, 0), 3)

cv2.putText(canvas, "Hello, OpenCV!", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
