# Import Modules 
from datetime import date, datetime
from modules import helper as help
import time
import cv2
import numpy as np
import math
from cvzone.HandTrackingModule import HandDetector  
import cvzone

# Global Variabels
playername = help.Starting()

ESC_BUTTON = 27
cap = cv2.VideoCapture(0)
videowidth = 1280
videoheight = 720

cap.set(3,videowidth)
cap.set(4,videoheight)

detector = HandDetector(detectionCon=0.8,maxHands=1)
mask = False
index = 0
center = [help.GeneratRandom(videowidth), help.GeneratRandom(videoheight)]
score = 0
gameover = False
repeat = None
color = (255,0,255)
counter = 0
MAXSCORE = 5
font = cv2.FONT_HERSHEY_SIMPLEX
StartTime = time.time()
GameTime = 20
# scores = []
while True:
    sucess, img = cap.read()
    hands = detector.findHands(img,draw=False)
    if (time.time() - StartTime < GameTime):
        if hands and not gameover:
            x1, y1, z1 = hands[0]["lmList"][5]
            x2, y2, z2 = hands[0]["lmList"][17]
            x, y, w, h = hands[0]["bbox"]
            distance = int(math.sqrt((x1-x2)**2 + (y1-y2)**2))
            distance_CM = help.GetDistanceCM(distance)

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),5)
            cvzone.putTextRect(img,f"{distance_CM} cm",(x+7,y-7))                    
            if distance_CM < 40 and x < center[0] < x+w and y < center[1] < y+h:
                    counter = 1
            if counter:
                color = (0,255,0)
                counter+=1
                if counter == 3:
                    score +=1
                    color=(255,0,255)
                    center = (help.GeneratRandom(videowidth),help.GeneratRandom(videoheight))
                    counter = 0
            else:
                color=(255,0,255)

        img = cv2.circle(img,center ,20,color,-1)
        img = cv2.circle(img,center,5,(255,255,255),-1)
        img = cv2.circle(img,center,21,(0,0,0),2)
        img = cv2.circle(img,center,15,(255,255,255),2)              
        timenow = GameTime - int(time.time() - StartTime)   
        cvzone.putTextRect(img,f"Time: {timenow}",(1000,75)) 
        cvzone.putTextRect(img,f"Score: {score}",(20,75))
    else:
        gameover = True
        cvzone.putTextRect(img,"Game Over",(500,300),4)  
        cvzone.putTextRect(img,f"Score: {score}",(580,370),3)  
        cvzone.putTextRect(img,f"To repeat game press 'r'",(400,450))  
        cvzone.putTextRect(img,f"To exit game press 'ESC'",(400,520))  

    cv2.imshow("Camera",img)
    key = cv2.waitKey(1)
    if key & 0xFF == ESC_BUTTON:
        help.StorePlayer(playername, score)
        break
    if key & 0xFF == ord('s'):
        cv2.imwrite(f"screen {index}.png",img)
        index+=1
    if key & 0xFF == ord('r'):
        help.StorePlayer(playername, score)
        score = 0
        gameover = False
        playername = help.Starting()
        StartTime = time.time()

cv2.destroyAllWindows()
help.GetMaxScore()