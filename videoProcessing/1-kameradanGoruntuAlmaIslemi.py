# @title      :  Capture Video From Camera
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @update     :  11.09.2016 by Hakan Kaya
# @description:  Video okuma ve gosterme islemi yapilmasi


# Kutuphaneler
import numpy as np
import cv2

print """
-----------------------------------------------
 Kameradan goruntu aktarilma basladi...
 Not: Cikmak icin ESC'ye (ESCAPE) basiniz.
-----------------------------------------------
"""

# 0. aygittan goruntu almak icin tanimlama
kameram = cv2.VideoCapture(1)

# Acilma sorgulamasi
if kameram.isOpened() == False:
    print ("Hata: Secili aygittan goruntu alinamadi.")       # Ekrana hata bastirma
    kameram.open(0)                                   # Bir daha dene yada farkli aygit dene

print "Yukleme basarili..."

while(True):
    # yakalama
    ret, orjinalGoruntu = kameram.read()

    # cap.read() True/False dondurur islem basarili yada degilse
    if kameram.read() == False:
        print ("Okuma islemi hatali sonuclandi...")
        break

    # yakalandiktan sonra islem yapm
    gray = cv2.cvtColor(orjinalGoruntu, cv2.COLOR_BGR2GRAY)

    # Gosterme
    cv2.namedWindow("Grilesmis Goruntu", cv2.WINDOW_NORMAL)
    cv2.imshow('Grilesmis Goruntu',gray)

    # Cikis icin Q
    if cv2.waitKey(1) & 0xFF == 27:
        print "Cikis yapildi"
        break

# Her sey tamamlandiginda kapat
cap.release()
cv2.destroyAllWindows()