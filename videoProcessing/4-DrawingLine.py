# @title      :  Drawing Line
# @author     :  Hakan Kaya
# @date       :  03.09.2016
# @description:  Cizgi cizimleri

import numpy as np
import cv2


# Siyah backgroung yaratma
img = np.zeros((512, 512, 3), np.uint8)

# Cizgi yaratma
# Sirasiyla image, (ilk nokta), (son nokta), renk, kalinlik
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Ekrana basma
cv2.imshow("img",img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    print "Cikis yapildi"
    cv2.destroyAllWindows()


