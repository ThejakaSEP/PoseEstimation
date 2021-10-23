#Example of how to use the Created Class
import cv2
import time
import PoseModule as pm


cap = cv2.VideoCapture('PoseVideos/Video1.mp4')
previousTime = 0

detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.getPosition(img)
    print(lmList)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(img, str(int(fps)), (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    cv2.waitKey(1)