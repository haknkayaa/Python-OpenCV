# @title      :  Capture Video From Camera
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @description:  Capture video from camera device

# Kütüphaneler
import numpy as np
import cv2

# Aygıt adı tanımalaması
cap = cv2.VideoCapture(1)

while(True):
    # yakalama
    ret, frame = cap.read()

    # yakalandıktan sonra işlem yapma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gösterme
    cv2.imshow('frame',gray)

    #Çıkış için Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şey tamamlandığında kapat
cap.release()
cv2.destroyAllWindows()