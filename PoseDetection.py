import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('PoseVideos/Video1.mp4')
previousTime = 0
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    # print(results.pose_landmarks)#Getting the points of the image / x,y,z and Visibility values

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)

    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

    cv2.putText(img,str(int(fps)),(70,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image",img)

    cv2.waitKey(1)

