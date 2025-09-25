import cv2

# Read the images
face = cv2.imread('./images/donald1.jpg')
clown = cv2.imread('./images/emoji.jpg')


# cv2.imshow('Face Image', face)
# cv2.imshow('Clown Image', clown)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if face is None or clown is None:
    print("Error: One or both images not found.")
else:
    # Resize both images to 2000x1280
    size = (600, 400)
    face_resized = cv2.resize(face, size)
    clown_resized = cv2.resize(clown, size)

    # Superimpose using addWeighted
    blended = cv2.addWeighted(face_resized, 0.7, clown_resized, 0.3, 0)

    cv2.imshow('Superimposed Image', blended)
    cv2.waitKey(0)
    cv2.destroyAllWindows()