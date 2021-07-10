import cv2
import time
import math
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

# capture = cv2.VideoCapture(0)

capture = cv2.VideoCapture("http://192.168.1.16:4747/mjpegfeed")
# print capture.get(cv2.CAP_PROP_FPS)

t = 100
w = 640.0

last = 0
while True:
    ret, image = capture.read()
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    img_height, img_width, depth = image.shape
    scale = w / img_width
    h = img_height * scale

    imgs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equ = cv2.equalizeHist(imgs)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(imgs)
    imgb = cv2.GaussianBlur(cl1, (5, 5), 0)

    circles = cv2.HoughCircles (imgb, cv2.HOUGH_GRADIENT, 1, 200,
                param1 = 80,
                param2 = 50,
                minRadius = 30,
                maxRadius = 60)

    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im = PIL.Image.fromarray(imageRGB)
    iobuf = io.BytesIO()
    im.save(iobuf, format='png')
    img_data = 'data:image/png;base64,{}'.format((str(base64.b64encode(iobuf.getvalue()), 'utf-8')))
    for client in clients:
        msg = json.dumps({'x':'a','src': str(img_data)})
        client.sendMessage(str(msg))

    if circles is not None:
        circle = circles[0][0]
        x, y, radius = int(circle[0]), int(circle[1]), int(circle[2])
        print(x, y, radius)

        cv2.circle(image, (x, y), radius, (0, 0, 255), 1)
        cv2.circle(image, (x, y), 1, (0, 0, 255), 1)

        for client in clients:
            client.sendMessage(str(json.dumps({'x': x / w, 'y': y / h, 'radius': radius / w, 'src': str(img_data)})))
    


    cv2.imshow('Image with detected circle', image)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

server.close()