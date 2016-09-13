# Kutuphaneler
import cv2
from matplotlib import pyplot as plt

# Materyal
img = cv2.imread('./Assets/gradient.jpg', 0)

# threshhold                kaynak,esik,max,donusum tipi
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# Baslislar
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

# Icerikler
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# Ekrana bastirma
for i in xrange(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# end for

plt.show()
