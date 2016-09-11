# @title      :  Dosyadan Goruntu Alma
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @update     :  11.09.2016
# @description:  Video okuma ve gosterme islemi yapilmasi

# Kutuphaneler
import numpy as np
import cv2

print """
-----------------------------------------------
 Dosyadan goruntu aktarilma basladi...
 Not: Cikmak icin ESC'ye (ESCAPE) basiniz.
-----------------------------------------------
"""

# Nesne yaratilmasi
medyam = cv2.VideoCapture('./Assets/video1.mp4')


if medyam.isOpened() == False:
    print "Hata: Medya acilamadi."
    medyam.open('./Assets/video1.mp4')


while(True):

    # yakalama
    ret, frame = medyam.read()

    # cap.read() True/False dondurur islem basarili yada degilse
    if medyam.read() == False:
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
medyam.release()
cv2.destroyAllWindows()