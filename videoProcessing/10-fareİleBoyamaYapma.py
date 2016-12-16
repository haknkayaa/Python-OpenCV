# @title      :  Goruntu Aygitindan Goruntu Alma
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @update     :  11.09.2016 by Hakan Kaya
# @description:  Video okuma ve gosterme islemi yapilmasi


# Kutuphaneler
import cv2
import numpy as np

print """
-----------------------------------------------
 Kameradan goruntu aktarilma basladi...
 Not: Cikmak icin ESC'ye (ESCAPE) basiniz.
-----------------------------------------------
"""

# 1. aygittan goruntu almak icin tanimlama
kameram = cv2.VideoCapture(0)

print "Yukleme basarili..."


def draw_circle(event, x, y, flags, param):


    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(gray, (x, y), 100, (255, 0, 0), -1)


while True:

    # Yakalama
    ret, orjinalGoruntu = kameram.read()

    # Grilestirme islemi
    gray = cv2.cvtColor(orjinalGoruntu, cv2.COLOR_BGR2GRAY)

    # Gosterme
    cv2.namedWindow("Grilesmis Goruntu", cv2.WINDOW_NORMAL)
    cv2.imshow('Grilesmis Goruntu', gray)

    cv2.setMouseCallback('Grilesmis Goruntu', draw_circle)

    # Cikis icin ESC
    if cv2.waitKey(1) & 0xFF == 27:
        print "Cikis yapildi"
        break
        # end if
# end while


# Her sey tamamlandiginda kapat
kameram.release()
cv2.destroyAllWindows()
