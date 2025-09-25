import cv2
import numpy as np

def warp_perspective(img_path, src_matrix, dst_matrix, output_size):
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError("Image not found or path is incorrect.")

    # Compute perspective transform matrix
    M = cv2.getPerspectiveTransform(np.float32(src_matrix), np.float32(dst_matrix))
    warped = cv2.warpPerspective(img, M, output_size)
    return warped

if __name__ == "__main__":
    # Example: 4 points in source and destination
    src_pts = [[90, 478], [135, 650], [917, 337], [956, 529]]
    dst_pts = [[0, 0], [0, 150], [800, 25], [875, 150]]

    # Sort both src_pts and dst_pts in top-left to bottom-right fashion
    src_pts = sorted(src_pts, key=lambda x: (x[1], x[0]))
    dst_pts = sorted(dst_pts, key=lambda x: (x[1], x[0]))
    

    output_size = (900, 150)

    result = warp_perspective("binary_output.jpg", src_pts, dst_pts, output_size)
    #result = cv2.flip(result, 0) 
    result = cv2.flip(result, 1)
    cv2.imshow("Warped Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("warped_output.jpg", result)