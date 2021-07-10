# import packages
import cv2
import numpy as np
import math

print("OpenCV:", cv2.__version__)
cap = cv2.VideoCapture("http://192.168.1.16:4747/mjpegfeed")
while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img = cv2.flip(img, 1)
    #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow('Img', img)
    cv2.rectangle(img, (400,400), (100,100), (0,0,255),0)
    crop_img = img[100:400, 100:400]

    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    # grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', grey)

    value = (15, 15)
    blurred = cv2.GaussianBlur(grey, value, 0)
    cv2.imshow('blurred', blurred)

    _, thresh1 = cv2.threshold(blurred, 127, 255,
                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    cv2.imshow('Thresholded', thresh1)

    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
        cv2.CHAIN_APPROX_NONE)

    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

    hull = cv2.convexHull(cnt)

    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

    hull = cv2.convexHull(cnt, returnPoints=False)

    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]

        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0,255,0], -1)
        
        cv2.line(crop_img,start, end, [255,0,0], 2)
        
    if count_defects == 1:
        cv2.putText(img,"Aku Sayang Ayah", (40, 50), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 255))
    elif count_defects == 2:
        str = "Sayang Adik Kakak"
        cv2.putText(img, str, (30, 50), cv2.FONT_ITALIC, 2, (100, 255, 255))
    elif count_defects == 3:
        cv2.putText(img,"1, 2, 3", (50, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 100, 255))
    elif count_defects == 4:
        cv2.putText(img,"Sayang Semuanya", (5, 60), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0))
    else:
        cv2.putText(img,"Aku Sayang Ibu", (60, 50),\
                    cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 255))

    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)
    

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('Done')
        break

cap.release()
cv2.destroyAllWindows()