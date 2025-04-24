import cv2
import cvzone
import cvzone.FPS
from cvzone.SelfiSegmentationModule import  SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 50)
segmentor = SelfiSegmentation()
imgBg = cv2.imread("BG/1.jpg")




while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgBg, cutThreshold=0.75)
    


    imgStacked = cvzone.stackImages([img, imgOut],2,1)
    
    cv2.imshow("Image", imgStacked)
    cv2.waitKey(1)