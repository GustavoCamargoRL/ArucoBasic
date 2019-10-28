import cv2
import cv2.aruco as aruco
import numpy as np

cap = cv2.VideoCapture(1)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
parameters =  aruco.DetectorParameters_create()
markerMoves = []
markerMovesR = []
markerMovesG = []
markerMovesB = []
color = (0,0,0)
command = 'stop'

while(True):

    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if ids is not None and ids[0] == 2:
        centerX = (corners[0][0][0] + corners[0][0][2])/2
        centerY = (corners[0][0][0] + corners[0][0][3])/2
        action = cv2.waitKey(1) & 0xFF
        print((corners[0][0][0] + corners[0][0][2]))
        if action == ord('r'):
            color = (0,0,255)
        if action == ord('b'):
            color = (255,0,0)
        if action == ord('g'):
            color = (0,255,0)
        if action == ord('d'):
            command = 'draw'
        if action == ord('s'):
            command = 'stop'
        if action == ord('c'):
            markerMoves = []
        if command == 'draw':
            if len(markerMoves) == 0:
                markerMoves.append((centerX,centerY))
            else:
                if (centerX + markerMoves[len(markerMoves) - 1][0]).any():
                    markerMoves.append((centerX,centerY))
            for i in range(len(markerMoves)):
                if i == 0:
                    continue
                else:
                    if markerMoves[i-1] is None or markerMoves[i] is None:
                        continue
                    #print(markerMoves[i],markerMoves[i][0][1],markerMoves[i][1][1],centerX,centerY)
                    cv2.line(frame,(markerMoves[i-1][0][0],markerMoves[i-1][0][1]),(markerMoves[i][0][0],markerMoves[i][0][1]),color,3,cv2.LINE_AA,0)
        elif command == 'stop':
            for i in range(len(markerMoves)):
                if i == 0:
                    continue
                else:
                    if markerMoves[i-1] is None or markerMoves[i] is None:
                        continue
                    #print(markerMoves[i],markerMoves[i][0][1],markerMoves[i][1][1],centerX,centerY)
                    cv2.line(frame,(markerMoves[i-1][0][0],markerMoves[i-1][0][1]),(markerMoves[i][0][0],markerMoves[i][0][1]),color,3,cv2.LINE_AA,0)




    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)


    cv2.imshow('frame',frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

