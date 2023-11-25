import cv2
import numpy as np
from matplotlib import pyplot as plt
def subtract_images(image1_path, image2_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    if img1.shape != img2.shape:
       img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    img_diff = cv2.subtract(img1, img2)
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title('Image 1')
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.title('Image 2')
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(img_diff, cv2.COLOR_BGR2RGB))
    plt.title('Difference of Images')
    plt.show()
image1_path = "C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot_20221116_214803.png"
image2_path = "C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot_20221116_214743.png"
subtract_images(image1_path, image2_path)
