import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hand_state = 0
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,

                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                five_landmark = hand_landmarks.landmark[5]
                x5 = five_landmark.x
                y5 = five_landmark.y
                # print("x =", x5, ", y =", y5,)
                seven_landmark = hand_landmarks.landmark[8]
                x8 = seven_landmark.x
                y8 = seven_landmark.y
                # print("x =", x7, ", y =", y7,)
                closex = x8 - x5
                closey = y8 - y5
                seventeen_landmark = hand_landmarks.landmark[17]
                x17 = seventeen_landmark.x
                y17 = seventeen_landmark.y
                # print("x =", x5, ", y =", y5,)
                twenty_landmark = hand_landmarks.landmark[20]
                x20 = twenty_landmark.x
                y20 = twenty_landmark.y
                # print("x =", x7, ", y =", y7,)
                closex1 = x8 - x5
                closex2 = x17 - x20
                closey1 = y8 - y5
                closey2 = y20 - y17
                if closey1 >= 0.01 and closey2 >= 0.01:
                    print('close')
                    hand_state == 0

                else:
                    print('open')
                    hand_state == 1
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()