import numpy as np
import cv2

# cap = cv2.VideoCapture("http://192.168.1.29:4747/mjpegfeed")
cap = cv2.VideoCapture("http://192.168.1.29:8080/video")
# 640 480

while(True):
	_, img = cap.read()
	# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
	# Display
	cv2.imshow('img', img)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		print('stoped')
		break
	
cap.release()
cv2.destroyAllWindows()