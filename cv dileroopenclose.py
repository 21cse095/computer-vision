import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("C:\\Users\\Lenovo\\Desktop\\chessboard.png", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

dilated_image = cv2.dilate(image, kernel, iterations=1)

eroded_image = cv2.erode(image, kernel, iterations=1)

closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


titles = ['Original', 'Dilation', 'Erosion', 'Closing', 'Opening']
images = [image, dilated_image, eroded_image, closing_image, opening_image]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
