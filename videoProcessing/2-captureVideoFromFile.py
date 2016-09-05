# @title      :  Capture Video From File
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @description:  Video okuma ve gosterme islemi yapilmasi

# Kutuphaneler
import numpy as np
import cv2

# Nesne yaratilmasi
cap = cv2.VideoCapture('./Assets/test.avi')

# Acilma sorgulamasi
print "Opened? " + str(cap.isOpened())

if cap.isOpened() == False:
    cap.open('./Assets/test.avi')


while(True):
    # yakalama
    ret, frame = cap.read()

    # cap.read() True/False dondurur islem basarili yada degilse
    if cap.read() == False:
        print ("Okuma islemi hatali sonuclandi")
        break

    # yakalandiktan sonra islem yapma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gosterme
    cv2.imshow('frame',gray)

    # Cikis icin Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print "Cikis yapildi"
        break

# Her sey tamamlandiginda kapat
cap.release()
cv2.destroyAllWindows()