import cv2
import numpy as np

cap = cv2.VideoCapture("http://192.168.1.22:4747/mjpegfeed")
imgTarget = cv2.imread('../qh.jpg')

while True:
	success, imgWebcam = cap.read()
	imgWebcam = cv2.rotate(imgWebcam, cv2.ROTATE_90_CLOCKWISE)
	hT, wT, cT = imgWebcam.shape
	new_size = imgWebcam.size
	imgTarget = cv2.resize(imgTarget, (wT, hT))
	imgAug = imgTarget.copy()

	x = 54
	y = 43
	w = 369
	h = 542
	imgWebcam = cv2.resize(imgWebcam, (w,h))

	imgTarget = cv2.rectangle(imgTarget, (x, y),  
                                       (x + w, y + h),  
                                       (255, 0, 0), 2) 
	xx = x+4
	yy = y+4
	ww = w-8
	hh = h-8
	dst = np.array([[xx,yy],[xx, yy+hh],[xx+ww,yy+hh],[xx+ww, yy]],np.int32)
	pts = np.float32(dst).reshape(-1,1,2)
	img2 = cv2.polylines(imgTarget,[np.int32(pts)],True,(255,0,255),1)

	color = [101, 52, 152] # 'cause purple!

	# border widths; I set them all to 150
	# top, bottom, left, right = [150]*4
	top = y
	bottom = hT - (y+h)
	left = x
	right = wT - (x + w) 
	imgwb = cv2.copyMakeBorder(imgWebcam, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)


	maskNew = np.zeros((imgTarget.shape[0],imgTarget.shape[1]),np.uint8)
	cv2.fillPoly(maskNew,[np.int32(dst)],(255,255,255))
	maskInv = cv2.bitwise_not(maskNew)
	imgAug = cv2.bitwise_and(imgAug,imgAug,mask = maskInv)
	imgAug = cv2.bitwise_or(imgwb,imgAug)

	cv2.imshow("img2", imgAug)
	cv2.imshow("imgTarget", imgWebcam)
	# cv2.imshow("result", result)
	# cv2.imshow("img2", imgAug)
	#cv2.imshow("imgTarget", imgTarget)
	#cv2.imshow("imgWebcam", imgWebcam)
	# cv2.waitKey(0)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		print('stoped')
		break

cv2.destroyAllWindows()
cap.release()