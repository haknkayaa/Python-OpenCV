# @title      :  Capture Video From Camera
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @description:  Capture video from camera device

# Kutuphaneler
import numpy as np
import cv2

# Aygit adi tanimalamasi
cap = cv2.VideoCapture(1)

while(True):
    # yakalama
    ret, frame = cap.read()

    # cap.read() True/False dondurur islem basarili yada degilse
    if cap.read() == False:
        print ("Okuma islemi hatali sonuclandi")

    # yakalandiktan sonra islem yapma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gosterme
    cv2.imshow('frame',gray)

    # Cikis icin Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her sey tamamlandiginda kapat
cap.release()
cv2.destroyAllWindows()