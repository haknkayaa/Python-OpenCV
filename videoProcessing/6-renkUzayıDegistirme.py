# Title        : Renk Uzaylari
# @author      : Hakan Kaya
# @date        : 10.09.2016
# @description : BGR, HSV gibi renk uzaylari ustunde
#                oynama
"""
BGR: (Blue Green Red)
----------------------------------
Mavi, yesil, kirmizi. RGB'nin ters kodlanisi.
Ana renklerinin 0-255 arasindeki
degerlerinden olusur.

HSV: (Hue Saturation Value)
----------------------------------
Renk ozu, doygunluk, parlaklik olarak tanimlanir.
0-360 derece cevrince renkler dizilmistir.
Ancak OpenCV de bu deger araligi 0-180'dir.
"""

import cv2

print "Cikmak icin ESC'ye basin..."

# Aygitta baglanma
kameram = cv2.VideoCapture(0)


while kameram.isOpened():

    # Frame okuma islemi
    ret , orjinal = kameram.read()

    # BGR'den HSV'ye donusum
    hsv_donusum = cv2.cvtColor(orjinal, cv2.COLOR_BGR2HSV)

    # Goruntuleri ekrana basma
    cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)  # Pencere boyutunu duzenleme
    cv2.imshow("HSV", hsv_donusum)             # Pencereye aktarilacak icerik

    cv2.namedWindow("BGR", cv2.WINDOW_NORMAL)  # Pencere boyutunu duzenleme
    cv2.imshow("BGR",orjinal)                  # Pencereye aktarilacak icerik


    if cv2.waitKey(5) & 0xFF == 27:            # ESC'ye basinca
        break                                  # While'dan cikma
    # end if
# end while

# Yiktim gectim buralari
cv2.destroyAllWindows()