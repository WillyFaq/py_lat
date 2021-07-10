import cv2
import numpy as np

imgTarget = cv2.imread('TargetImage.jpg')
imgWebcam = cv2.imread('webcam.jpg')
# imgTarget = cv2.imread('SS12.png')
# imgWebcam = cv2.imread('wc2.jpg')
#cap = cv2.VideoCapture("http://192.168.1.8:4747/mjpegfeed")
#cap = cv2.VideoCapture(0)
#success, imgWebcam = cap.read()

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget,None)
kp2, des2 = orb.detectAndCompute(imgWebcam, None)

imgTarget = cv2.drawKeypoints(imgTarget,kp1,None)
imgWebcam = cv2.drawKeypoints(imgWebcam,kp2,None)

bf = cv2.BFMatcher()
matches = set()
if len(kp2) > 1:
    matches = bf.knnMatch(des1,des2,k=2)

#matches = bf.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.75 *n.distance:
        good.append(m)
print(("Matches : {}").format(len(good)))
imgFeatures = cv2.drawMatches(imgTarget,kp1,imgWebcam,kp2,good,None,flags=2)
#if len(good) > 20:
    
cv2.imshow('ImgTarget',imgTarget)
cv2.imshow('imgWebcam',imgWebcam)
cv2.imshow('imgFeatures',imgFeatures)

cv2.waitKey(0)