import cv2
import cv2.aruco as aruco
import numpy as np

cap = cv2.VideoCapture(0)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
parameters =  aruco.DetectorParameters_create()


while(True):

    ret, frame = cap.read()


    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)


    cv2.imshow('frame',frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

