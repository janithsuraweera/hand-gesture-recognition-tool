import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

# Initial brightness value
brightness = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count the number of fingers
            finger_count = 0
            landmarks = hand_landmarks.landmark

            # Check for fingers
            if landmarks[mp_hands.HandLandmark.THUMB_TIP].y < landmarks[mp_hands.HandLandmark.THUMB_IP].y:
                finger_count += 1
            if landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                finger_count += 1
            if landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                finger_count += 1
            if landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.RING_FINGER_DIP].y:
                finger_count += 1
            if landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_DIP].y:
                finger_count += 1

            # Adjust brightness based on finger count
            if finger_count == 2:
                brightness += 10  # Increase brightness
            elif finger_count == 5:
                brightness -= 10  # Decrease brightness

            # Clamp brightness value to the range [0, 255]
            brightness = max(0, min(255, brightness))


    # Apply brightness adjustment to the image
    if brightness > 0:
        image = cv2.convertScaleAbs(image, alpha=1, beta=brightness)

    cv2.imshow("Hand Gesture Recognition", image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
