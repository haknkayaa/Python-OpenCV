# Kutuphaneler
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Dosya okuma
img = cv2.imread("./Assets/opencv.png")

#
kernel = np.ones((15, 15), np.float32) / 255

#
dst = cv2.filter2D(img, -1, kernel)

# Blurlama
blur = cv2.blur(img, (5, 5))


# Ciktilari ekrana basma
plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(dst), plt.title('Puruzleri kaldirma')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(blur), plt.title('Blurlama')
plt.xticks([]), plt.yticks([])
plt.show()

