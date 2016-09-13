"""
Kirmizi rengin BGR kodu: 0,0,255 dir.
"""

import cv2
import numpy as np

renkBGR = []


def renkSorgu(girilenDeger):
    if girilenDeger == [0, 0, 255]:
        print "Kirmizi renk secildi"
        hsvHesapla(girilenDeger)
    # end if

    elif girilenDeger == [0, 255, 0]:
        print "Yesil renk secildi"
        hsvHesapla(girilenDeger)
    # end elif

    elif girilenDeger == [255, 0, 0]:
        print "Mavi renk secildi"
        hsvHesapla(girilenDeger)
    # end elif

    else:
        print "Hata: Kayitlanmamis renk secildi..."
    # end else


# end renkSorgu

def hsvHesapla(BGRkodu):

    renk = np.uint8([[BGRkodu]])
    hsv_renkDegeri = cv2.cvtColor(renk, cv2.COLOR_BGR2HSV)

    print hsv_renkDegeri

    print hsv_renkDegeri[[[0]]].append("99")

# end hsvHesapla

def main():
    kameram = cv2.VideoCapture(0)

    if not kameram.isOpened():
        print "Hata: Aygit acilamadi"
        kameram.open()
    # endif

    print "Sirasiyle 3 indisi giriniz..."

    for i in range(0, 3):
        indis = int(raw_input("indis > "))
        renkBGR.append(indis)
    # end for

    print "Renk kodunuz :", renkBGR
    print "Islem onaylandi...\n"

    renkSorgu(renkBGR)

    while True:
        # Saniye saniye frame alma
        ret, orjinal = kameram.read()

        hsvRenk = cv2.cvtColor(orjinal, cv2.COLOR_BGR2HSV)

    cv2.destroyAllWindows()


# end main func


if __name__ == "__main__":
    main()
