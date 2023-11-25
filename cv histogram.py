import cv2
import numpy as np
from matplotlib import pyplot as plt
def histogram_equalization(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_equalized = cv2.equalizeHist(img)
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(img_equalized, cmap='gray')
    plt.title('Equalized Image')
    plt.show()
input_image_path ="C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot 2023-09-03 212640.png" 
histogram_equalization(input_image_path)
