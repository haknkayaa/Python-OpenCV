import cv2
import numpy as np

kameram = cv2.VideoCapture(0)

if kameram == False:
    print "Hata: Aygit baslatilamadi. :("
    kameram.open(0)
# end if

while True:
    _, frame = kameram.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    min_red = np.array([150, 150, 50])
    max_red = np.array([180, 255, 150])

    maskelenmis = cv2.inRange(hsv, min_red, max_red)
    sonuc = cv2.bitwise_and(frame, frame, mask=maskelenmis)

    kernel = np.ones((15, 15), np.float32) / 255

    blur = cv2.filter2D(sonuc, -1, kernel)

    gaussianBlur = cv2.GaussianBlur(sonuc , (15,15), 0)

    medianBlur = cv2.medianBlur(sonuc, 15)

    bilateral = cv2.bilateralFilter(sonuc, 15, 75, 75)

    cv2.imshow("orjinal goruntu", frame)
    cv2.imshow("sonuc", sonuc)
    cv2.imshow("blur", blur)
    cv2.imshow("gaussionBlur", gaussianBlur)
    cv2.imshow("medianBlur", medianBlur)


    if cv2.waitKey(1) & 0xFF == 27:
        print "Cikis yapildi."
        break
    # end if

# end while

cv2.destroyAllWindows()
kameram.release()
