import cv2
import mediapipe as mp
import pyautogui as auto

# MediaPipe initialization
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

## Docs: https://mediapipe.readthedocs.io/en/latest/solutions/hands.html


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def count_fingers(hand_landmarks, hand_label):
    fingers = []

    # Thumb
    if hand_label == "Right":
        if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0]-1].x:
            fingers.append(1)
        else:
            fingers.append(0)
    else:  # Left hand
        if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0]-1].x:
            fingers.append(1)
        else:
            fingers.append(0)

    # Other four fingers
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

print("Show numbers 0–10 using both hands. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    total_fingers = 0

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            label = hand_handedness.classification[0].label  # "Left" or "Right"
            total_fingers += count_fingers(hand_landmarks, label)

    cv2.putText(frame, f"Total Fingers: {total_fingers}", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Two-Hand Finger Counting", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
