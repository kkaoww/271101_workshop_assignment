from cvzone import FPS
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detectors = HandDetector()
fpsReader = FPS()

while True:
    ret, frame = cap.read()
    hands, bboxs = detectors.findHands(frame)
    cv2.putText(frame,"kaow" , (10, 80), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
 
    if hands:
        handsu=hands[0]
        fingersu=detectors.fingersUp(handsu)
        print(fingersu)
        
        if fingersu[0] == 1 :
         cv2.putText(frame,"Thumb" , (50, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 3)

        if fingersu[1] == 1 :
         cv2.putText(frame,"Index" , (180, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 3)

        if fingersu[2] == 1 :
         cv2.putText(frame,"Middle" , (280, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 3)

        if fingersu[3] == 1 :
         cv2.putText(frame,"Ring" , (400, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 3)

        if fingersu[4] == 1 :
         cv2.putText(frame,"Little" , (480, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 3)
 
 
 
    fps, frame = fpsReader.update(frame)

    cv2.imshow("Image", frame)
    
  
    if ord('q') == 0xFF & cv2.waitKey(1):
        break

cap.release()
cv2.destroyAllWindows() 
