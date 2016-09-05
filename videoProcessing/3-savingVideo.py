# @title      :  Saving a Video
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @description:  Saving a capture video from camera

import numpy as np
import cv2

# Nesne yaratilmasi
cap = cv2.VideoCapture(1)

# Codec tanimlamalari ve path tanimlamalari
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./Assets/output.avi',fourcc, 20.0, (640,480))

print "Is Opened? " + str(cap.isOpened())

if cap.isOpened() == False:
    cap.open(1)
    print "Opened"


while(True):

    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame,0)

        # Frame'i yaz
        out.write(frame)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Isler bittiginde her seyi sal
cap.release()
out.release()
cv2.destroyAllWindows()