import numpy as np
import cv2

# cap = cv2.VideoCapture("http://192.168.1.29:4747/mjpegfeed")
# cap = cv2.VideoCapture("http://192.168.1.29:8080/video")
cap = cv2.VideoCapture("rtsp://192.168.1.29:8080/h264_pcm.sdp")
# 640 480


def main():
	i = 0
	j = 0
	th = 15
	sti = (0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0)
	while(True):
		_, img = cap.read()
		img1 = cv2.resize(img, (200,267))
		
		
		# stackImages[0] = img
		# Display

		if j<=th:
			lis = list(sti)
			lis[i] = img1
			sti = tuple(lis)
		else:
			lis = list(sti)
			lis[15] = lis[14]
			lis[14] = lis[13]
			lis[13] = lis[12]
			lis[12] = lis[11]
			lis[11] = lis[10]
			lis[10] = lis[9]
			lis[9] = lis[8]
			lis[8] = lis[7]
			lis[7] = lis[6]
			lis[6] = lis[5]
			lis[5] = lis[4]
			lis[4] = lis[3]
			lis[3] = lis[2]
			lis[2] = lis[1]
			lis[1] = lis[0]
			lis[0] = img1
			sti = tuple(lis)
			# lis[i] = img1

			imgStacked = stackImages((
										[sti[9], sti[10], sti[11], sti[12], sti[13], sti[14], sti[15]],
										[sti[8], sti[7], sti[6], sti[5], sti[4], sti[3], sti[2]],
										[sti[1], sti[0], sti[-15], sti[-14], sti[-13], sti[-12], sti[-11]]
										# [sti[7], sti[6], sti[5], sti[4]],
										# [sti[3], sti[2], sti[1], sti[0]]
									),0.5)
			cv2.imshow('img', imgStacked)
		i+=1
		j+=1
		if i>th:
			i=0
		if cv2.waitKey(10) & 0xFF == ord('q'):
			print('stoped')
			break
	# print(stackImages)


def stackImages(imgArray,scale,lables=[]):
	sizeW= imgArray[0][0].shape[1]
	sizeH = imgArray[0][0].shape[0]
	rows = len(imgArray)
	cols = len(imgArray[0])
	rowsAvailable = isinstance(imgArray[0], list)
	if rowsAvailable:
		for x in range ( 0, rows):
			for y in range(0, cols):
				imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW,sizeH), None, scale, scale)
				if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
		imageBlank = np.zeros((sizeH, sizeW, 3), np.uint8)
		hor = [imageBlank]*rows
		hor_con = [imageBlank]*rows
		for x in range(0, rows):
			hor[x] = np.hstack(imgArray[x])
			hor_con[x] = np.concatenate(imgArray[x])
		ver = np.vstack(hor)
		ver_con = np.concatenate(hor)
	else:
		for x in range(0, rows):
			imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
			if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
		hor= np.hstack(imgArray)
		hor_con= np.concatenate(imgArray)
		ver = hor
	if len(lables) != 0:
		eachImgWidth= int(ver.shape[1] / cols)
		eachImgHeight = int(ver.shape[0] / rows)
		print(eachImgHeight)
		for d in range(0, rows):
			for c in range (0,cols):
				cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
				cv2.putText(ver,lables[d],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
	return ver


if __name__ == '__main__':
	main()

cap.release()
cv2.destroyAllWindows()