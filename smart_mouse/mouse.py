import cv2
import autopy
import time
import numpy as np
import modulesuport as htm

# Camera and frame settings
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7

# Previous and current locations for smoothening
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Capture video from webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Initialize hand detector
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    # Read frame from webcam
    success, img = cap.read()
    if not success:
            break

    # Find hand and landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip

        # Check which fingers are up
        fingers = detector.fingersUp()

        # Draw a rectangle for the interaction area
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (0, 255, 0), 2)  # Green rectangle

        # Moving mode: Only index finger is up
        if fingers[1] == 1 and fingers[2] == 0:
            # Convert coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # Smoothen values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)  # Red circle for moving mode
            plocX, plocY = clocX, clocY

        # Clicking mode: Both index and middle fingers are up
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 39:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (255, 255, 0), cv2.FILLED)  # Yellow circle for clicking mode
                autopy.mouse.click()

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 3)  # Cyan text for FPS

    # Display the image
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
