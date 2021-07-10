import cv2
import numpy as np
import threading
import json
import base64
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import PIL.Image
import io

server = None
clients = []


class SimpleWSServer(WebSocket):
	def handleConnected(self):
		clients.append(self)

	def handleClose(self):
		clients.remove(self)


def run_server():
	global server
	server = SimpleWebSocketServer('', 9000, SimpleWSServer,
								   selectInterval=(1000.0 / 15) / 1000)
	server.serveforever()


t = threading.Thread(target=run_server)
t.start()

cap = cv2.VideoCapture("http://192.168.1.25:4747/mjpegfeed")
imgTarget = cv2.imread('qh.jpg')
myVid = cv2.VideoCapture('../lol.mp4')

detection = False
frameCounter = 0

success, imgVideo = myVid.read()
hT, wT, cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo, (wT, hT))

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)

while True:
	success, imgWebcam = cap.read()
	imgWebcam = cv2.rotate(imgWebcam, cv2.ROTATE_90_CLOCKWISE)
	imgAug = imgWebcam.copy()
	kp2, des2 = orb.detectAndCompute(imgWebcam, None)
	#imgWebcam = cv2.drawKeypoints(imgWebcam, kp2, None)

	if detection == False:
		myVid.set(cv2.CAP_PROP_POS_FRAMES,0)
		frameCounter = 0
	else:
		if frameCounter == myVid.get(cv2.CAP_PROP_FRAME_COUNT):
			myVid.set(cv2.CAP_PROP_POS_FRAMES, 0)
			frameCounter = 0
		success, imgVideo = myVid.read()
		imgVideo = cv2.resize(imgVideo, (wT, hT))


	bf = cv2.BFMatcher()
	matches = set()
	if len(kp2) > 1:
		matches = bf.knnMatch(des1,des2,k=2)

		good = []
		for m,n in matches:
			if m.distance < 0.75 *n.distance:
				good.append(m)
		imgFeatures = cv2.drawMatches(imgTarget,kp1,imgWebcam,kp2,good,None,flags=2)

		if len(good) > 20:
			detection = True
			srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
			dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
			matrix, mask = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5)
			if matrix is not None:
				pts = np.float32([[0,0],[0,hT],[wT,hT],[wT,0]]).reshape(-1,1,2)
				dst = cv2.perspectiveTransform(pts,matrix)
				img2 = cv2.polylines(imgWebcam,[np.int32(dst)],True,(255,0,255),3)
				
				for client in clients:
					imageRGB = cv2.cvtColor(imgWebcam, cv2.COLOR_BGR2RGB)
					im = PIL.Image.fromarray(imageRGB)
					iobuf = io.BytesIO()
					im.save(iobuf, format='png')
					img_data = 'data:image/png;base64,{}'.format((str(base64.b64encode(iobuf.getvalue()), 'utf-8')))
					x = int(dst[0][0][0])
					y = int(dst[0][0][1])
					radius = int(dst[3][0][0] / 2)
					msg = json.dumps({'x':x, 'y':y, 'radius':radius ,'src': str(img_data)})
					client.sendMessage(str(msg))
					# msg = json.dumps({'x': x / w, 'y': y / h, 'radius': radius / w})


				print(dst[0][0])
				print(dst[0][0][0]) # x
				print(dst[0][0][1]) # y
				print(" ======================\n\n ")

				print(dst[3][0])
				print(dst[3][0][0]) # w
				print(dst[3][0][1])
				print(" ======================\n\n ")
				imgWarp = cv2.warpPerspective(imgVideo, matrix, (imgWebcam.shape[1],imgWebcam.shape[0]))
				# maskNew = np.zeros((imgWebcam.shape[0],imgWebcam.shape[1]),np.uint8)
				# cv2.fillPoly(maskNew,[np.int32(dst)],(255,255,255))
				# maskInv = cv2.bitwise_not(maskNew)
				# imgAug = cv2.bitwise_and(imgAug,imgAug,mask = maskInv)
				# imgAug = cv2.bitwise_or(imgWarp,imgAug)
				cv2.imshow("imgWarp", imgWarp)
	
	cv2.imshow("imgFeatures", imgAug)
	#cv2.imshow("imgTarget", imgTarget)
	#cv2.imshow("imgWebcam", imgWebcam)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		print('stoped')
		break

cv2.destroyAllWindows()
cap.release()
server.close()