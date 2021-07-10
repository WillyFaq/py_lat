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

while True:
	success, imgWebcam = cap.read()
	imgWebcam = cv2.rotate(imgWebcam, cv2.ROTATE_90_CLOCKWISE)
	

	# success, abuffer = cv2.imencode('.jpg', imgWebcam)
	# jpg_as_text = base64.b64encode(abuffer)
	

	# print(jpg_as_text)
	imageRGB = cv2.cvtColor(imgWebcam, cv2.COLOR_BGR2RGB)
	im = PIL.Image.fromarray(imageRGB)
	iobuf = io.BytesIO()
	im.save(iobuf, format='png')
	img_data = 'data:image/png;base64,{}'.format((str(base64.b64encode(iobuf.getvalue()), 'utf-8')))

	
	for client in clients:
		print("send!")
		msg = json.dumps({'x': str(img_data)})
		client.sendMessage(str(msg))
	
	cv2.imshow("imgFeatures", imageRGB)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		print('stoped')
		break

cv2.destroyAllWindows()
cap.release()
server.close()