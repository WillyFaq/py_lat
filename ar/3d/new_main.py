import cv2
import numpy as np
import math
from objloader_simple import *
from object_module import *

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("http://192.168.1.38:4747/mjpegfeed")
# imgTarget = cv2.imread('TargetImage.jpg')
imgTarget = cv2.imread('qh.jpg')
imgTarget2 = cv2.imread('qh.jpg',0)
#imgTarget = cv2.imread('SS12.png')
myVid = cv2.VideoCapture('lol.mp4')
obj = OBJ('fox/fox.obj', swapyz=True)
obj = three_d_object('fox/fox.obj', 'fox/texture.png')
# camera_parameters = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]])
camera_parameters = np.array([[1019.37187, 0, 618.709848], [0, 1024.2138, 327.280578], [0, 0, 1]])

detection = False
frameCounter = 0

success, imgVideo = myVid.read()
hT, wT, cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo, (wT, hT))

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)
#imgTarget = cv2.drawKeypoints(imgTarget, kp1, None)
#imgWebcam = cv2.imread('webcam.jpg')


def render(img, obj, projection, model, color=False):
    """
    Render a loaded obj model into the current video frame
    """
    vertices = obj.vertices
    scale_matrix = np.eye(3) * 3
    h, w = model.shape

    for face in obj.faces:
        face_vertices = face[0]
        points = np.array([vertices[vertex - 1] for vertex in face_vertices])
        points = np.dot(points, scale_matrix)
        # render model in the middle of the reference surface. To do so,
        # model points must be displaced
        points = np.array([[p[0] + w / 2, p[1] + h / 2, p[2]] for p in points])
        dst = cv2.perspectiveTransform(points.reshape(-1, 1, 3), projection)
        imgpts = np.int32(dst)
        # if color is False:
        #     cv2.fillConvexPoly(img, imgpts, (0, 255, 0))
        # else:
        #     color = hex_to_rgb(face[-1])
        #     color = color[::-1]  # reverse
        #     cv2.fillConvexPoly(img, imgpts, color)

        if color is False:
            cv2.fillConvexPoly(img, imgpts, (50, 50, 50))
        else:
            cv2.fillConvexPoly(img, imgpts, face[-1])

    return img

def projection_matrix(camera_parameters, homography):
    """
    From the camera calibration matrix and the estimated homography
    compute the 3D projection matrix
    """
    # Compute rotation along the x and y axis as well as the translation
    homography = homography * (-1)
    rot_and_transl = np.dot(np.linalg.inv(camera_parameters), homography)
    col_1 = rot_and_transl[:, 0]
    col_2 = rot_and_transl[:, 1]
    col_3 = rot_and_transl[:, 2]
    # normalise vectors
    l = math.sqrt(np.linalg.norm(col_1, 2) * np.linalg.norm(col_2, 2))
    rot_1 = col_1 / l
    rot_2 = col_2 / l
    translation = col_3 / l
    # compute the orthonormal basis
    c = rot_1 + rot_2
    p = np.cross(rot_1, rot_2)
    d = np.cross(c, p)
    rot_1 = np.dot(c / np.linalg.norm(c, 2) + d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
    rot_2 = np.dot(c / np.linalg.norm(c, 2) - d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
    rot_3 = np.cross(rot_1, rot_2)
    # finally, compute the 3D projection matrix from the model to the current frame
    projection = np.stack((rot_1, rot_2, rot_3, translation)).T
    return np.dot(camera_parameters, projection)

def hex_to_rgb(hex_color):
    """
    Helper function to convert hex strings to RGB
    """
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))

while True:
	success, imgWebcam = cap.read()
	imgWebcam = cv2.rotate(imgWebcam, cv2.ROTATE_90_CLOCKWISE)
	imgAug = imgWebcam.copy()
	kp2, des2 = orb.detectAndCompute(imgWebcam, None)

	# if detection == False:
	# 	myVid.set(cv2.CAP_PROP_POS_FRAMES,0)
	# 	frameCounter = 0
	# else:
	# 	if frameCounter == myVid.get(cv2.CAP_PROP_FRAME_COUNT):
	# 		myVid.set(cv2.CAP_PROP_POS_FRAMES, 0)
	# 		frameCounter = 0
	# 	success, imgVideo = myVid.read()
	# 	imgVideo = cv2.resize(imgVideo, (wT, hT))


	bf = cv2.BFMatcher()
	matches = set()
	if len(kp2) > 1:
		matches = bf.knnMatch(des1,des2,k=2)

		good = []
		for m,n in matches:
			if m.distance < 0.75 *n.distance:
				good.append(m)
		print(len(good))
		imgFeatures = cv2.drawMatches(imgTarget,kp1,imgWebcam,kp2,good,None,flags=2)

		if len(good) > 20:
			detection = True
			srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
			dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
			matrix, mask = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5)
			# print(matrix)
			if matrix is not None:
				# pts = np.float32([[0,0],[0,hT],[wT,hT],[wT,0]]).reshape(-1,1,2)
				# dst = cv2.perspectiveTransform(pts,matrix)
				# img2 = cv2.polylines(imgWebcam,[np.int32(dst)],True,(255,0,255),3)
				
				# imgWarp = cv2.warpPerspective(imgVideo,matrix, (imgWebcam.shape[1],imgWebcam.shape[0]))
				# maskNew = np.zeros((imgWebcam.shape[0],imgWebcam.shape[1]),np.uint8)
				# cv2.fillPoly(maskNew,[np.int32(dst)],(255,255,255))
				# maskInv = cv2.bitwise_not(maskNew)
				# imgAug = cv2.bitwise_and(imgAug,imgAug,mask = maskInv)
				# imgAug = cv2.bitwise_or(imgWarp,imgAug)
				projection = projection_matrix(camera_parameters, matrix)
				# print(projection)
				imgAug = render(imgWebcam, obj, projection, imgTarget2, True)
				

 
	cv2.imshow("imgFeatures", imgAug)
	#cv2.imshow("imgTarget", imgTarget)
	#cv2.imshow("imgWebcam", imgWebcam)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		print('stoped')
		break

# cv2.destroyAllWindows()
# cap.release()