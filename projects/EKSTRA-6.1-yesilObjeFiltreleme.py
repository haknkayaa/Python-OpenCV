# @title      :  Goruntu Aygitindan Goruntu Alma
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @update     :  11.09.2016 by Hakan Kaya
# @description:  Video okuma ve gosterme islemi yapilmasi


# kutuphaneler
import cv2
import numpy as np

                                                                # Medya nesnesi
cap = cv2.VideoCapture(0)

while True:                                                     # Sonsuz Dongu

    _, frame = cap.read()                                       # Frame okumasi

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                # Uzay renk donusumu BGR > HSV

    minDeger = np.array([50, 50, 50])                           # Minimum renk degeri
    maxDeger = np.array([70, 255, 255])                         # Maksimum renk degeri

    mask = cv2.inRange(hsv, minDeger, maxDeger)                 # Maskeleme islemlerinin uygulanmasi

    res = cv2.bitwise_and(frame, frame, mask=mask)              # Son hali

    cv2.namedWindow('orjinal goruntu', cv2.WINDOW_NORMAL)       # Pencere boyutunun ayarlanabilir olmasi icin
    cv2.imshow('orjinal goruntu', frame, )                      # Pencereye aktarilacak materyal

    cv2.namedWindow('maskelenmis', cv2.WINDOW_NORMAL)           # Pencere boyutunun ayarlanabilir olmasi icin
    cv2.imshow('maskelenmis', mask)                             # Pencereye aktarilacak materyal

    cv2.namedWindow('sonuc', cv2.WINDOW_NORMAL)                 # Pencere boyutunun ayarlanabilir olmasi icin
    cv2.imshow('sonuc', res)                                    # Pencereye aktarilacak materyal

    if cv2.waitKey(5) & 0xFF == 27:                             # ESC'ye basinca fonksiyonun cikmasi icin
        break
    # end if

cv2.destroyAllWindows()                                         # Acilan pencereleri kapatma
cap.realese()
