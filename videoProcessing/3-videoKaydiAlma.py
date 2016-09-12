# @title      :  Video Kaydi Alma
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @update     :  11.09.2016
# @description:  Video kaydi yapma ve kaydetme

# Kutuphaneler
import cv2

print """
-----------------------------------------------
 Aygittan goruntu kaydi basladi...
 Not: Cikmak icin ESC'ye (ESCAPE) basiniz.
-----------------------------------------------
"""

# Nesne yaratilmasi
kameram = cv2.VideoCapture(1)

# Codec tanimlamalari ve path tanimlamalari
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./Assets/output.avi', fourcc, 20.0, (640,480))

if not kameram.isOpened():
    print "Hata: Aygitta baglanilamadi."
    kameram.open(0)
# end if

print "Baglanti gerceklesti..."


while True:

    #  Okuma
    ret, frame = kameram.read()


    if ret:
        frame = cv2.flip(frame, 0)

        # Frame'i yaz
        out.write(frame)

        # Goruntuyu ekrana basma
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)

        # Q ile cikis
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # end if
    # end if

    else:
        print "Selam"
        break
    # end else

# Isler bittiginde her seyi sal
kameram.release()
out.release()
cv2.destroyAllWindows()